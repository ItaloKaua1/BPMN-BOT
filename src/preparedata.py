from pathlib import Path

import pandas as pd
from llama_index.core import Document


ROOT_DIR = Path(__file__).resolve().parents[1]
DATASETS_DIR = ROOT_DIR / "datasets"


def valor_seguro(row, coluna):
    if coluna not in row:
        return ""

    valor = row[coluna]

    if pd.isna(valor):
        return ""

    return str(valor).strip()


def criar_texto_semantico(row, nome_dataset):
    if nome_dataset == "SLR-DATA":
        titulo = valor_seguro(row, "TITLE")

        atributos = valor_seguro(
            row,
            "What are the basic attributes of each extension (such as authors, year of publication and type of publication)?",
        )

        tipo = valor_seguro(
            row,
            "{RQ1:} Is the extension proposed for a specific domain, Application Areas or improvement of the language itself?",
        )

        dominio = valor_seguro(
            row,
            "{RQ1.1:} What are the specific domains targeted by the BPMN extensions?",
        )

        area = valor_seguro(
            row,
            "{RQ1.2:} What are the Application Areas targeted by the BPMN extensions?",
        )

        texto = f"""
TITLE: {titulo}

Esta publicação apresenta uma extensão BPMN registrada na revisão sistemática.
Título original: {titulo}.
Atributos bibliográficos: {atributos}.
Tipo de contribuição da extensão: {tipo}.
Domínio específico da extensão: {dominio}.
Área de aplicação da extensão: {area}.

Palavras-chave preservadas para recuperação semântica:
{titulo}
{tipo}
{dominio}
{area}
BPMN extension
BPMN extensions
Business Process Model and Notation
""".strip()

        return texto

    if nome_dataset == "publications":
        titulo = valor_seguro(row, "title")
        ano = valor_seguro(row, "year")
        autores = valor_seguro(row, "authors")
        veiculo = valor_seguro(row, "journal")
        tipo = valor_seguro(row, "type")
        url = valor_seguro(row, "url")

        texto = f"""
TITLE: {titulo}

Esta publicação está registrada no catálogo de extensões BPMN.
Título original: {titulo}.
Ano: {ano}.
Autores: {autores}.
Veículo de publicação: {veiculo}.
Tipo de publicação: {tipo}.
URL: {url}.

Palavras-chave preservadas para recuperação semântica:
{titulo}
{autores}
{veiculo}
BPMN extension
BPMN extensions
Business Process Model and Notation
""".strip()

        return texto

    campos = []

    for coluna in row.index:
        valor = valor_seguro(row, coluna)

        if valor:
            campos.append(f"{coluna}: {valor}")

    return f"""
Dataset: {nome_dataset}

Registro estruturado do catálogo de extensões BPMN.

""" + "\n".join(campos)


def criar_documentos_csv(caminho_csv, nome_dataset):
    df = pd.read_csv(caminho_csv)

    documentos = []

    for _, row in df.iterrows():
        texto = criar_texto_semantico(row, nome_dataset)

        doc = Document(
            text=texto,
            metadata={
                "dataset": nome_dataset,
                "source": str(caminho_csv),}
        )

        documentos.append(doc)

    return documentos


def carregar_documentos_csv():
    datasets = [
        "categories",
        "classifications",
        "constructs",
        "publications",
        "text_fields",
        "users",
        "SLR-DATA",
    ]

    todos_documentos = []

    for dataset in datasets:
        caminho = DATASETS_DIR / f"{dataset}.csv"

        if not caminho.exists():
            print(f"Aviso: dataset nao encontrado: {caminho}")
            continue

        docs = criar_documentos_csv(caminho, dataset)

        todos_documentos.extend(docs)

        print(f"{dataset}: {len(docs)} documentos carregados")

    print("\nTOTAL DE DOCUMENTOS:")
    print(len(todos_documentos))

    return todos_documentos
