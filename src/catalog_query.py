from pathlib import Path
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
DATASETS_DIR = ROOT_DIR / "datasets"


def carregar_csv(nome):
    caminho = DATASETS_DIR / f"{nome}.csv"

    if not caminho.exists():
        return pd.DataFrame()

    return pd.read_csv(caminho)


def listar_publicacoes_por_ano(ano):
    df = carregar_csv("publications")

    if df.empty or "year" not in df.columns:
        return "Não encontrei o dataset de publicações ou a coluna year."

    resultado = df[df["year"].astype(str) == str(ano)]

    if resultado.empty:
        return f"Não encontrei publicações do ano {ano}."

    linhas = []

    for _, row in resultado.iterrows():
        titulo = row.get("title", "sem título")
        autores = row.get("authors", "autores não informados")
        tipo = row.get("type", "tipo não informado")

        linhas.append(f"- {titulo} | {autores} | {tipo}")

    return "\n".join(linhas)


def contar_publicacoes_por_ano():
    df = carregar_csv("publications")

    if df.empty or "year" not in df.columns:
        return "Não encontrei o dataset de publicações ou a coluna year."

    contagem = (
        df["year"]
        .dropna()
        .astype(str)
        .value_counts()
        .sort_index()
    )

    linhas = ["Publicações por ano:"]

    for ano, total in contagem.items():
        linhas.append(f"- {ano}: {total}")

    return "\n".join(linhas)


def autores_mais_frequentes(top_n=10):
    df = carregar_csv("publications")

    if df.empty or "authors" not in df.columns:
        return "Não encontrei o dataset de publicações ou a coluna authors."

    autores = []

    for valor in df["authors"].dropna():
        partes = str(valor).replace(" and ", ",").split(",")

        for autor in partes:
            autor = autor.strip()

            if autor:
                autores.append(autor)

    contagem = pd.Series(autores).value_counts().head(top_n)

    linhas = [f"Autores mais frequentes no catálogo:"]

    for autor, total in contagem.items():
        linhas.append(f"- {autor}: {total}")

    return "\n".join(linhas)


def listar_publicacoes_por_tipo(tipo_busca):
    df = carregar_csv("publications")

    if df.empty or "type" not in df.columns:
        return "Não encontrei o dataset de publicações ou a coluna type."

    resultado = df[
        df["type"]
        .fillna("")
        .astype(str)
        .str.lower()
        .str.contains(tipo_busca.lower())
    ]

    if resultado.empty:
        return f"Não encontrei publicações do tipo {tipo_busca}."

    linhas = [f"Publicações do tipo {tipo_busca}:"]

    for _, row in resultado.iterrows():
        titulo = row.get("title", "sem título")
        ano = row.get("year", "ano não informado")
        autores = row.get("authors", "autores não informados")

        linhas.append(f"- {titulo} ({ano}) | {autores}")

    return "\n".join(linhas)


def buscar_publicacoes_por_termo(termo):
    df = carregar_csv("publications")

    if df.empty:
        return "Não encontrei o dataset de publicações."

    colunas_busca = ["title", "authors", "journal", "type", "year"]
    colunas_existentes = [c for c in colunas_busca if c in df.columns]

    if not colunas_existentes:
        return "Não encontrei colunas buscáveis no dataset de publicações."

    mascara = False

    for coluna in colunas_existentes:
        mascara = mascara | df[coluna].fillna("").astype(str).str.lower().str.contains(
            termo.lower()
        )

    resultado = df[mascara]

    if resultado.empty:
        return f"Não encontrei publicações relacionadas a '{termo}'."

    linhas = [f"Publicações relacionadas a '{termo}':"]

    for _, row in resultado.iterrows():
        titulo = row.get("title", "sem título")
        ano = row.get("year", "ano não informado")
        autores = row.get("authors", "autores não informados")
        tipo = row.get("type", "tipo não informado")

        linhas.append(f"- {titulo} ({ano}) | {autores} | {tipo}")

    return "\n".join(linhas)