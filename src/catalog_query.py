import re
import unicodedata
from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
DATASETS_DIR = ROOT_DIR / "datasets"

_SEM_TITULO = "sem título"
_SEM_AUTORES = "autores não informados"

_DOMINIO_COL = "{RQ1.1:} What are the specific domains targeted by the BPMN extensions?"
_AREA_COL = "{RQ1.2:} What are the Application Areas targeted by the BPMN extensions?"

_ALIASES = {
    "ia": ["ia", "ai", "artificial intelligence", "machine learning"],
    "ai": ["ia", "ai", "artificial intelligence", "machine learning"],
    "inteligencia artificial": ["ia", "ai", "artificial intelligence", "machine learning"],
    "seguranca": ["security", "cyber security", "cybersecurity", "seguranca"],
    "security": ["security", "cyber security", "cybersecurity"],
    "iot": ["iot", "internet of things"],
    "saude": ["healthcare", "health", "saude"],
    "robotica": ["robotics", "robotica"],
}


def normalizar_catalogo(texto):
    texto = str(texto).lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def aliases_termo_catalogo(termo):
    return _ALIASES.get(normalizar_catalogo(termo), [normalizar_catalogo(termo)])


def valor_controlado_corresponde(valor, aliases):
    valor_norm = normalizar_catalogo(valor)
    if not valor_norm:
        return False
    partes = re.split(r"[,;/|]", valor_norm)
    partes = [p.strip() for p in partes if p.strip()]
    for parte in partes:
        for alias in aliases:
            alias_norm = normalizar_catalogo(alias)
            if parte == alias_norm:
                return True
            if alias_norm in parte.split():
                return True
    return False


def contem_termo_seguro(serie, termo):
    termo_norm = normalizar_catalogo(termo)
    if len(termo_norm) <= 3:
        padrao = rf"\b{re.escape(termo_norm)}\b"
        return serie.fillna("").astype(str).apply(
            lambda x: bool(re.search(padrao, normalizar_catalogo(x)))
        )
    return serie.fillna("").astype(str).apply(
        lambda x: termo_norm in normalizar_catalogo(x)
    )


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
        titulo = row.get("title", _SEM_TITULO)
        autores = row.get("authors", _SEM_AUTORES)
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

    linhas = ["Autores mais frequentes no catálogo:"]

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
        titulo = row.get("title", _SEM_TITULO)
        ano = row.get("year", "ano não informado")
        autores = row.get("authors", _SEM_AUTORES)

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
        titulo = row.get("title", _SEM_TITULO)
        ano = row.get("year", "ano não informado")
        autores = row.get("authors", _SEM_AUTORES)
        tipo = row.get("type", "tipo não informado")

        linhas.append(f"- {titulo} ({ano}) | {autores} | {tipo}")

    return "\n".join(linhas)

def listar_dominios_e_areas():
    df = carregar_csv("SLR-DATA")

    linhas = []

    if _DOMINIO_COL in df.columns:
        dominios = df[_DOMINIO_COL].dropna().astype(str).value_counts()
        linhas.append("Domínios específicos encontrados no catálogo:")
        for dominio, total in dominios.items():
            linhas.append(f"- {dominio}: {total}")

    if _AREA_COL in df.columns:
        areas = df[_AREA_COL].dropna().astype(str).value_counts()
        linhas.append("\nÁreas de aplicação encontradas no catálogo:")
        for area, total in areas.items():
            linhas.append(f"- {area}: {total}")

    return "\n".join(linhas)


def buscar_extensoes_por_dominio_ou_area(termo):
    df = carregar_csv("SLR-DATA")

    if df.empty:
        return "Não encontrei o dataset SLR-DATA."

    if _DOMINIO_COL not in df.columns and _AREA_COL not in df.columns:
        return "Não encontrei as colunas de domínio ou área de aplicação no dataset SLR-DATA."

    aliases = aliases_termo_catalogo(termo)
    resultados = []

    for _, row in df.iterrows():
        dominio = row.get(_DOMINIO_COL, "")
        area = row.get(_AREA_COL, "")

        if valor_controlado_corresponde(dominio, aliases) or valor_controlado_corresponde(area, aliases):
            titulo = row.get("TITLE", _SEM_TITULO)
            dominio_str = "" if pd.isna(dominio) else str(dominio).strip()
            area_str = "" if pd.isna(area) else str(area).strip()
            classificacao = dominio_str or area_str or "não informado"
            resultados.append(f"- {titulo} | Domínio ou Área: {classificacao}")

    if not resultados:
        return f"Não encontrei extensões classificadas no catálogo para '{termo}'."

    vistos = set()
    unicos = []
    for item in resultados:
        if item not in vistos:
            vistos.add(item)
            unicos.append(item)

    return f"Extensões classificadas no catálogo para '{termo}':\n" + "\n".join(unicos)


def buscar_extensoes_catalogo_por_termo(termo):
    resultados = []

    pub = carregar_csv("publications")
    if not pub.empty:
        colunas_pub = [c for c in ["title", "authors", "journal", "type", "year"] if c in pub.columns]
        if colunas_pub:
            mascara = False
            for coluna in colunas_pub:
                mascara = mascara | contem_termo_seguro(pub[coluna], termo)
            for _, row in pub[mascara].iterrows():
                titulo = row.get("title", _SEM_TITULO)
                ano = row.get("year", "ano não informado")
                autores = row.get("authors", _SEM_AUTORES)
                tipo = row.get("type", "tipo não informado")
                resultados.append(f"- {titulo} ({ano}) | {autores} | {tipo}")

    slr = carregar_csv("SLR-DATA")
    if not slr.empty:
        colunas_textuais = slr.select_dtypes(include=["object"]).columns
        mascara = False
        for coluna in colunas_textuais:
            mascara = mascara | contem_termo_seguro(slr[coluna], termo)
        for _, row in slr[mascara].iterrows():
            titulo = row.get("TITLE", _SEM_TITULO)
            resultados.append(f"- {titulo}")

    if not resultados:
        return f"Não encontrei extensões ou publicações relacionadas a '{termo}'."

    vistos = set()
    unicos = []
    for item in resultados:
        if item not in vistos:
            vistos.add(item)
            unicos.append(item)

    return f"Extensões/publicações relacionadas a '{termo}':\n" + "\n".join(unicos)