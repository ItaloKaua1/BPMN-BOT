import pandas as pd

from llama_index.core import Document


# =========================
# FUNÇÃO AUXILIAR
# =========================

def criar_documentos_csv(caminho_csv, nome_dataset):

    df = pd.read_csv(caminho_csv)

    documentos = []

    for _, row in df.iterrows():

        texto = ""

        for coluna in df.columns:

            valor = row[coluna]

            texto += f"{coluna}: {valor}\n"

        doc = Document(
            text=texto,
            metadata={
                "dataset": nome_dataset
            }
        )

        documentos.append(doc)

    return documentos


# =========================
# CARREGAR DATASETS
# =========================

datasets = [
    "categories",
    "classifications",
    "constructs",
    "publications",
    "text_fields",
    "users"
]

todos_documentos = []

for dataset in datasets:

    caminho = f"datasets/{dataset}.csv"

    docs = criar_documentos_csv(
        caminho,
        dataset
    )

    todos_documentos.extend(docs)

    print(f"{dataset}: {len(docs)} documentos carregados")


print("\nTOTAL DE DOCUMENTOS:")
print(len(todos_documentos))

def carregar_documentos_csv():
    datasets = [
        "categories",
        "classifications",
        "constructs",
        "publications",
        "text_fields",
        "users"
    ]

    todos_documentos = []

    for dataset in datasets:
        caminho = f"datasets/{dataset}.csv"

        docs = criar_documentos_csv(
            caminho,
            dataset
        )

        todos_documentos.extend(docs)

    return todos_documentos