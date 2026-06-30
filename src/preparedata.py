import re
from pathlib import Path

import pandas as pd
from llama_index.core import Document


ROOT_DIR = Path(__file__).resolve().parents[1]
DATASETS_DIR = ROOT_DIR / "datasets"
DOCS_DIR = ROOT_DIR / "docs" / "process"


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


def quebrar_markdown_em_secoes(conteudo):
    secoes = []
    secao_atual_titulo = None
    secao_atual_linhas = []

    for linha in conteudo.splitlines():
        match = re.match(r'^(#{1,3})\s+(.+)', linha)
        if match:
            if secao_atual_titulo is not None:
                secoes.append((secao_atual_titulo, "\n".join(secao_atual_linhas).strip()))
            secao_atual_titulo = match.group(2).strip()
            secao_atual_linhas = []
        elif secao_atual_titulo is not None:
            secao_atual_linhas.append(linha)

    if secao_atual_titulo is not None:
        secoes.append((secao_atual_titulo, "\n".join(secao_atual_linhas).strip()))

    return secoes


def _extrair_keywords(titulo_secao, conteudo_secao):
    palavras = re.sub(r'[^\w\s]', ' ', titulo_secao.lower()).split()
    keywords = [p for p in palavras if len(p) > 3]

    bold = re.findall(r'\*\*([^*]+)\*\*', conteudo_secao)
    keywords.extend(b.lower() for b in bold)

    seen = set()
    result = []
    for k in keywords:
        if k not in seen:
            seen.add(k)
            result.append(k)
    return result


def criar_documento_semantico_markdown(nome_arquivo, titulo_secao, process_name, conteudo_secao, document_type, source):
    keywords = _extrair_keywords(titulo_secao, conteudo_secao)

    texto = f"""FILE: {nome_arquivo}

SECTION: {titulo_secao}

PROCESS: {process_name}

CONTENT:
{conteudo_secao}

KEYWORDS:
{chr(10).join(keywords)}""".strip()

    return Document(
        text=texto,
        metadata={
            "file_name": nome_arquivo,
            "section_title": titulo_secao,
            "document_type": document_type,
            "source": source,
        },
    )


def carregar_documentos_markdown():
    diretorios = [
        (DOCS_DIR, "process"),
        (DOCS_DIR / "artifacts", "artifact"),
    ]

    todos_documentos = []

    for diretorio, document_type in diretorios:
        if not diretorio.exists():
            print(f"Aviso: diretório não encontrado: {diretorio}")
            continue

        _ARQUIVOS_TESTE = {"rag_test_questions.md", "catalog_test_questions.md"}
        for caminho in sorted(diretorio.glob("*.md")):
            if caminho.name in _ARQUIVOS_TESTE:
                continue
            conteudo = caminho.read_text(encoding="utf-8")
            nome_arquivo = caminho.name

            secoes = quebrar_markdown_em_secoes(conteudo)

            if not secoes:
                continue

            process_name = secoes[0][0]

            docs = []
            for titulo_secao, conteudo_secao in secoes:
                if not conteudo_secao.strip():
                    continue

                doc = criar_documento_semantico_markdown(
                    nome_arquivo=nome_arquivo,
                    titulo_secao=titulo_secao,
                    process_name=process_name,
                    conteudo_secao=conteudo_secao,
                    document_type=document_type,
                    source=str(caminho),
                )
                docs.append(doc)

            todos_documentos.extend(docs)
            print(f"{nome_arquivo}: {len(docs)} seções carregadas")

    print(f"\nTOTAL DE DOCUMENTOS MARKDOWN: {len(todos_documentos)}")
    return todos_documentos


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
