import re
from pathlib import Path

from llama_index.core import (
    SimpleDirectoryReader,
    Settings,
    VectorStoreIndex,
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

from preparedata import carregar_documentos_csv

from catalog_query import (
    autores_mais_frequentes,
    buscar_publicacoes_por_termo,
    contar_publicacoes_por_ano,
    listar_publicacoes_por_ano,
    listar_publicacoes_por_tipo,
    listar_dominios_e_areas
)

ROOT_DIR = Path(__file__).resolve().parents[1]


Settings.llm = Ollama(
    model="qwen2.5:3b",
    request_timeout=180,
)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)


def carregar_documentos_diretorio(caminho, nome_base):
    if not caminho.exists():
        print(f"Aviso: diretorio nao encontrado: {caminho}")
        return []

    arquivos = [arquivo for arquivo in caminho.rglob("*") if arquivo.is_file()]

    if not arquivos:
        print(f"Aviso: nenhum arquivo encontrado em: {caminho}")
        return []

    documentos = SimpleDirectoryReader(
        str(caminho),
        recursive=True,
    ).load_data()

    for documento in documentos:
        documento.metadata["base"] = nome_base

    return documentos


def carregar_catalogo():
    documentos = carregar_documentos_csv()

    # Complementa o catalogo estruturado com documentos longos, quando existirem.
    documentos.extend(
        carregar_documentos_diretorio(ROOT_DIR / "docs" / "catalog", "catalogo")
    )

    return documentos


def carregar_processo():
    documentos = carregar_documentos_diretorio(
        ROOT_DIR / "docs" / "process",
        "processo",
    )

    # Carrega documentos do metamodelo, se existirem.
    documentos.extend(
        carregar_documentos_diretorio(ROOT_DIR / "docs" / "metamodel", "metamodelo")
    )

    return documentos


print("Carregando catalogo...")
catalog_documents = carregar_catalogo()

print("Carregando documentos do processo...")
process_documents = carregar_processo()

all_documents = catalog_documents + process_documents

print(f"Documentos do catalogo: {len(catalog_documents)}")
print(f"Documentos do processo: {len(process_documents)}")
print(f"Documentos totais: {len(all_documents)}")


print("Criando indice do catalogo...")
catalog_index = VectorStoreIndex.from_documents(catalog_documents)

print("Criando indice do processo...")
process_index = VectorStoreIndex.from_documents(process_documents)

catalog_engine = catalog_index.as_query_engine(similarity_top_k=4)
process_engine = process_index.as_query_engine(similarity_top_k=6)

estado_conversa = {
    "fluxo_ativo": None,
    "etapa_atual": None,
    "dominio": None,
    "conceitos": [],
}


def contem_alguma(pergunta, palavras):
    pergunta_lower = pergunta.lower()
    return any(palavra in pergunta_lower for palavra in palavras)


def escolher_engine(pergunta):
    pergunta_lower = pergunta.lower()

    if "desenvolver" in pergunta_lower or "develop" in pergunta_lower:
        return process_engine, "processo"

    if "recomenda" in pergunta_lower or "comunidade bpmn" in pergunta_lower:
        return process_engine, "processo"

    if "especialista" in pergunta_lower or "expert" in pergunta_lower:
        return process_engine, "processo"

    palavras_processo = [
        "como criar",
        "como desenvolver",
        "como validar",
        "etapas",
        "processo",
        "checklist",
        "consistencia",
        "consistência",
        "conflitos",
        "sintaxe concreta",
        "metamodelo",
        "guidelines",
        "diretrizes",
        "regras",
        "modelagem",
        "validacao",
        "validação",
        "consultar especialistas",
        "especialistas",
        "experts",
        "recomendações",
        "recomendacoes",
        "comunidade bpmn",
        "community",
        "abstract syntax",
        "concrete syntax",
        "sintaxe abstrata",
        "sintaxe abstrata",
        "ferramenta",
        "tool",
        "publicar",
        "publicise",
        "avaliar",
        "evaluate",
        "validar",
        "validate",
    ]

    palavras_catalogo = [
        "catalogo",
        "catálogo",
        "dataset",
        "publicacao",
        "publicação",
        "publicacoes",
        "publicações",
        "artigo",
        "artigos",
        "autor",
        "autores",
        "ano",
        "dominio",
        "domínio",
        "area de aplicacao",
        "área de aplicação",
        "areas de aplicacao",
        "áreas de aplicação",
        "extensoes existentes",
        "extensões existentes",
        "extensao existente",
        "extensão existente",
        "slr",
    ]

    pergunta_processo = contem_alguma(pergunta, palavras_processo)
    pergunta_catalogo = contem_alguma(pergunta, palavras_catalogo)

    if pergunta_processo:
        return process_engine, "processo"

    if pergunta_catalogo:
        return catalog_engine, "catalogo"

    return process_engine, "processo"

def criar_prompt(pergunta, tipo_base):
    return f"""
Voce e o BPMN-BOT, um assistente especializado em extensoes BPMN.

Base consultada: {tipo_base}.

Use somente as fontes recuperadas.
Responda em portugues.
Nao mostre raciocinio interno.
Nao diga "o usuario esta no arquivo X" como primeira resposta.
Nao escreva como se estivesse analisando os documentos.
Responda como um assistente orientando uma pessoa.

Se a pergunta for sobre processo:
- Comece com uma resposta direta.
- Depois apresente os passos recomendados.
- Para cada passo, diga brevemente o objetivo.
- Informe os principais artefatos produzidos.
- Termine dizendo qual e o proximo passo.
- Cite o nome do subprocesso somente quando for util.

Se a pergunta for sobre catalogo:
- Responda somente com base nos registros recuperados.
- Nao invente publicacoes, autores ou dominios.

Se as fontes recuperadas nao forem suficientes, diga:
"A base atual nao contem informacao suficiente para confirmar isso."

Pergunta do usuario:
{pergunta}
"""

print("\nBPMN-BOT iniciado!")
print("Digite 'sair' para encerrar.\n")

def extrair_dominio(pergunta):
    pergunta_lower = pergunta.lower().strip()
    padroes = [
        r"é na área de (.+)",
        r"é para (.+)",
        r"na área de (.+)",
        r"área de (.+)",
        r"domínio de (.+)",
        r"dominio de (.+)",
        r"para (.+)",
    ]
    for padrao in padroes:
        match = re.search(padrao, pergunta_lower)
        if match:
            return match.group(1).strip().rstrip(".,?")
    return pergunta.strip().rstrip(".,?")


def tentar_responder_fluxo_guiado(pergunta):
    global estado_conversa
    pergunta_lower = pergunta.lower()

    intencao_criar = (
        ("como criar" in pergunta_lower and "extensão bpmn" in pergunta_lower)
        or ("como criar" in pergunta_lower and "extensao bpmn" in pergunta_lower)
        or ("quero criar" in pergunta_lower and "extensão bpmn" in pergunta_lower)
        or ("quero criar" in pergunta_lower and "extensao bpmn" in pergunta_lower)
        or "criar extensão bpmn" in pergunta_lower
        or "criar extensao bpmn" in pergunta_lower
    )

    if intencao_criar:
        estado_conversa["fluxo_ativo"] = "criacao_extensao"
        estado_conversa["etapa_atual"] = "informar_dominio"
        estado_conversa["dominio"] = None
        estado_conversa["conceitos"] = []
        return "Qual é o domínio ou área de aplicação da extensão que você deseja criar?"

    if estado_conversa["fluxo_ativo"] == "criacao_extensao":

        if estado_conversa["etapa_atual"] == "informar_dominio":
            dominio = extrair_dominio(pergunta)
            estado_conversa["dominio"] = dominio

            resultado_catalogo = buscar_publicacoes_por_termo(dominio)
            tem_resultado = resultado_catalogo and "nenhuma publicação encontrada" not in resultado_catalogo.lower()

            if tem_resultado:
                resposta = (
                    f"Domínio registrado: {dominio}\n\n"
                    f"Encontrei extensões relacionadas no catálogo:\n\n"
                    f"{resultado_catalogo}\n\n"
                    "O processo BPMN recomenda verificar se alguma extensão existente já atende "
                    "à sua necessidade antes de criar uma nova. Avalie se alguma das extensões "
                    "acima pode ser reutilizada ou adaptada.\n\n"
                    "---\n\n"
                    "Quais conceitos desse domínio o BPMN padrão não consegue representar adequadamente?"
                )
            else:
                resposta = (
                    f"Domínio registrado: {dominio}\n\n"
                    "Não foram encontradas extensões relacionadas a esse domínio no catálogo. "
                    "Isso sugere que sua extensão pode ser uma contribuição inédita para a comunidade.\n\n"
                    "---\n\n"
                    "Quais conceitos desse domínio o BPMN padrão não consegue representar adequadamente?"
                )

            estado_conversa["etapa_atual"] = "identificar_conceitos"
            return resposta

        if estado_conversa["etapa_atual"] == "identificar_conceitos":
            conceitos = [c.strip() for c in re.split(r"[,;]", pergunta) if c.strip()]
            estado_conversa["conceitos"] = conceitos
            estado_conversa["etapa_atual"] = "descrever_conceitos"

            lista = "\n".join(f"- {c}" for c in conceitos)
            return (
                f"Conceitos registrados para o domínio '{estado_conversa['dominio']}':\n\n"
                f"{lista}\n\n"
                "Agora vamos verificar se algum construto BPMN existente pode ser reutilizado "
                "para representar esses conceitos, ou se novos elementos precisam ser criados.\n\n"
                "Para cada conceito, você consegue informar:\n"
                "1. O que ele representa no seu domínio?\n"
                "2. Por que o BPMN padrão não consegue representá-lo?"
            )

    return None


def tentar_responder_catalogo_estruturado(pergunta):
    pergunta_lower = pergunta.lower()

    if "autores" in pergunta_lower and (
        "mais" in pergunta_lower or "frequentes" in pergunta_lower
    ):
        return autores_mais_frequentes()

    if "por ano" in pergunta_lower or "quantas publicações" in pergunta_lower:
        return contar_publicacoes_por_ano()

    for ano in ["2019", "2020", "2021", "2022", "2023", "2024", "2025"]:
        if ano in pergunta_lower and "public" in pergunta_lower:
            return listar_publicacoes_por_ano(ano)

    if "journal" in pergunta_lower:
        return listar_publicacoes_por_tipo("journal")

    if "conference" in pergunta_lower or "conferência" in pergunta_lower:
        return listar_publicacoes_por_tipo("conference")

    if "relacionadas a" in pergunta_lower:
        termo = pergunta_lower.split("relacionadas a", 1)[1]
        termo = termo.replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)

    if "relacionados a" in pergunta_lower:
        termo = pergunta_lower.split("relacionados a", 1)[1]
        termo = termo.replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)

    if "sobre" in pergunta_lower and "public" in pergunta_lower:
        termo = pergunta_lower.split("sobre", 1)[1]
        termo = termo.replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)
    
    if "domínios" in pergunta_lower or "dominios" in pergunta_lower:
        return listar_dominios_e_areas()

    if "áreas de aplicação" in pergunta_lower or "areas de aplicacao" in pergunta_lower:
        return listar_dominios_e_areas()
    
    if "existe" in pergunta_lower and "extensão" in pergunta_lower and "para" in pergunta_lower:
        termo = pergunta_lower.split("para", 1)[1]
        termo = termo.replace("?", "").replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)

    if "existe" in pergunta_lower and "extensao" in pergunta_lower and "para" in pergunta_lower:
        termo = pergunta_lower.split("para", 1)[1]
        termo = termo.replace("?", "").replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)

    return None

def tentar_responder_processo_guiado(pergunta):
    pergunta_lower = pergunta.lower()

    if "como desenvolver" in pergunta_lower and "extensão bpmn" in pergunta_lower:
        return """
Para desenvolver uma extensão BPMN, você deve partir de uma extensão já conceitualizada.

1. Defina o metamodelo
    Indique quais elementos, atributos, relações e restrições representam os conceitos da extensão.

2. Defina regras de validação
    Crie regras para restrições que não podem ser representadas apenas no metamodelo.

3. Defina a sintaxe concreta
    Escolha como os conceitos aparecerão nos diagramas: marcador, ícone, cor, rótulo, artefato ou novo elemento visual.

4. Verifique completude, consistência e conflitos
    Confirme se cada conceito tem representação, se a sintaxe concreta corresponde ao metamodelo e se não há conflito com BPMN.

5. Decida se precisa de suporte em ferramenta
    Se a extensão precisar ser usada na prática, implemente ou configure uma ferramenta de modelagem.

Resultado esperado:
Extension specification [Developed].
""".strip()

    return None

while True:
    pergunta = input("Pergunta: ")

    if pergunta.lower() == "sair":
        break

    resposta_estruturada = tentar_responder_catalogo_estruturado(pergunta)

    if resposta_estruturada:
        print("\nResposta:")
        print(resposta_estruturada)
        print("\nFonte: consulta estruturada com pandas nos CSVs do catálogo\n")
        continue

    resposta_fluxo = tentar_responder_fluxo_guiado(pergunta)

    if resposta_fluxo:
        print("\nResposta:")
        print(resposta_fluxo)
        print("\nFonte: fluxo guiado de criação de extensão BPMN\n")
        continue

    resposta_processo_guiado = tentar_responder_processo_guiado(pergunta)

    if resposta_processo_guiado:
        print("\nResposta:")
        print(resposta_processo_guiado)
        print("\nFonte: fluxo guiado do processo BPMN\n")
        continue

    engine, tipo_base = escolher_engine(pergunta)
    print(f"\nBase escolhida: {tipo_base}")

    resposta = engine.query(criar_prompt(pergunta, tipo_base))

    print("\nResposta:")
    print(resposta.response)

    print("\nFontes recuperadas:")

    for i, node in enumerate(resposta.source_nodes, start=1):
        file_name = node.metadata.get("file_name")
        dataset = node.metadata.get("dataset")
        base = node.metadata.get("base")
        origem = file_name or dataset or base or "fonte desconhecida"

        print(f"\nFonte {i}: {origem}")
        print(node.text[:300])
        print("---")

    print("\n")