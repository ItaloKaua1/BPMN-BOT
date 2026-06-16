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
    model="qwen2.5:7b",
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

print("Criando indice combinado...")
combined_index = VectorStoreIndex.from_documents(all_documents)


catalog_engine = catalog_index.as_query_engine(similarity_top_k=4)
process_engine = process_index.as_query_engine(similarity_top_k=4)
combined_engine = combined_index.as_query_engine(similarity_top_k=6)


def contem_alguma(pergunta, palavras):
    pergunta_lower = pergunta.lower()
    return any(palavra in pergunta_lower for palavra in palavras)


def escolher_engine(pergunta):
    pergunta_lower = pergunta.lower()

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

    if pergunta_processo and pergunta_catalogo:
        return combined_engine, "catalogo + processo"

    if pergunta_processo:
        return process_engine, "processo"

    if pergunta_catalogo:
        return catalog_engine, "catalogo"

    return combined_engine, "catalogo + processo"


def criar_prompt(pergunta, tipo_base):
    return f"""
Voce e o BPMN-BOT, um assistente especializado em extensoes BPMN.

Base consultada: {tipo_base}.

Voce conhece duas frentes complementares:
1. O catalogo de extensoes BPMN, vindo dos datasets e de documentos em docs/catalog.
2. O processo de criacao de extensoes BPMN, vindo de docs/process e docs/metamodel.

Use somente as fontes recuperadas.

Quando a pergunta for sobre criacao, validacao, checklist, metamodelo,
sintaxe concreta, consistencia ou conflitos, responda em passos.

Quando a pergunta for sobre catalogo, publicacoes, dominios, autores,
areas de aplicacao ou extensoes existentes, responda comparando os registros
recuperados e citando a origem.

Se as fontes recuperadas nao forem suficientes, diga que a base nao contem
informacao suficiente.

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