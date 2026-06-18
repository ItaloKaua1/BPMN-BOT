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

    if "como criar" in pergunta_lower and "extensão bpmn" in pergunta_lower:
        return """
Para criar uma extensão BPMN, comece verificando se ela é realmente necessária.

1. Analise a necessidade da extensão
    Verifique o domínio, os conceitos que precisam ser representados e se o BPMN padrão já atende ao problema.

2. Descreva os conceitos da extensão
    Liste os conceitos novos, veja se algum construto BPMN pode ser reutilizado e defina a relação entre os conceitos da extensão e o BPMN.

3. Desenvolva a extensão
    Defina metamodelo, regras de validação, sintaxe concreta, análise de consistência e, se necessário, suporte ferramental.

4. Valide e avalie a extensão
    Aplique a extensão em um cenário, consulte especialistas, corrija problemas e registre evidências de avaliação.

5. Publique a extensão
    Registre a extensão no catálogo, busque endosso quando necessário e disponibilize a especificação.

Primeiro passo agora:
responda qual domínio ou área de aplicação você quer modelar e quais conceitos o BPMN padrão não consegue representar.

Artefato inicial:
Extension specification [Analysed].
""".strip()

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