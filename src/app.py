import re
import textwrap
import unicodedata
from pathlib import Path

from llama_index.core import (
    SimpleDirectoryReader,
    Settings,
    VectorStoreIndex,
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

from preparedata import (
    carregar_documentos_csv,
    carregar_documentos_markdown,
)

from catalog_query import (
    autores_mais_frequentes,
    buscar_publicacoes_por_termo,
    buscar_extensoes_catalogo_por_termo,
    buscar_extensoes_por_dominio_ou_area,
    contar_publicacoes_por_ano,
    listar_publicacoes_por_ano,
    listar_publicacoes_por_tipo,
    listar_dominios_e_areas,
)

ROOT_DIR = Path(__file__).resolve().parents[1]

Settings.llm = Ollama(
    model="qwen2.5:3b",
    request_timeout=180,
)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

# ---------------------------------------------------------------------------
# Mapa de roteamento: keywords -> documento processual esperado
# ---------------------------------------------------------------------------
_DOC_01 = "01_analyse_need_for_extension.md"
_DOC_02 = "02_describe_extension_concepts.md"
_DOC_03 = "03_develop_bpmn_extension.md"
_DOC_04 = "04_support_extension_with_tool.md"
_DOC_05 = "05_validate_and_evaluate_extension.md"
_DOC_06 = "06_consult_experts.md"
_DOC_07 = "07_publicise_bpmn_extension.md"

MAPA_DOCUMENTOS = {
    _DOC_01: [
        "bpmn é adequado", "bpmn adequado para meu domínio",
        "limitações da bpmn", "limitacoes da bpmn",
        "justificar a criação de uma extensão", "justificar criacao",
        "verificar se já existe uma extensão", "verificar se ja existe",
        "usar o catálogo de extensões", "usar o catalogo de extensoes",
        "quando extensão não é necessária", "quando extensao nao e necessaria",
        "analisar necessidade", "analyse need",
        "extensão semelhante", "extensao semelhante",
        "modelar usando apenas bpmn padrão",
        "identificar limitações da bpmn",
        "identificar conceitos que bpmn não representa",
        "preencher o bpmn conformity checklist",
        "bpmn conformity checklist",
        "preciso criar uma extensão bpmn",
        "preciso criar uma extensao bpmn",
        "realmente preciso criar uma extensão bpmn",
        "realmente preciso criar uma extensao bpmn",
        "como identificar se preciso criar",
        "como saber se preciso criar",
        "como decidir se devo criar uma extensão bpmn",
        "como decidir se devo criar uma extensao bpmn",
        "quando devo criar uma extensão bpmn",
        "quando devo criar uma extensao bpmn",
        "quando criar uma extensão bpmn",
        "quando criar uma extensao bpmn",
        "como avaliar a necessidade de uma extensão bpmn",
        "como avaliar a necessidade de uma extensao bpmn",
        "como identificar a necessidade de uma extensão bpmn",
        "como identificar a necessidade de uma extensao bpmn",
        "existe necessidade de criar uma extensão",
        "existe necessidade de criar uma extensao",
        "devo estender o bpmn",
        "bpmn padrão é suficiente",
        "bpmn padrao e suficiente",
        "minha necessidade já é atendida pelo bpmn",
        "minha necessidade ja e atendida pelo bpmn",
        "quando uma extensão bpmn não é necessária",
        "quando uma extensao bpmn nao e necessaria",
    ],
    _DOC_02: [
        "conceitos minha extensão deve introduzir",
        "quais conceitos minha extensão",
        "definir um conceito da extensão", "definir conceito da extensão",
        "reutilizar construtos de extensões", "reutilizar construtos existentes",
        "integrar novos conceitos à bpmn", "relacionar conceitos da extensão",
        "equivalências entre conceitos", "especializado ou criado do zero",
        "identificar equivalências",
        "como descrever corretamente os conceitos",
        "descrever corretamente os conceitos",
        "descrever conceitos de uma extensão bpmn",
        "descrever conceitos de uma extensao bpmn",
        "como descrever conceitos da extensão",
        "como descrever conceitos da extensao",
        "describe concepts",
        "describe extension concepts",
        "conceitos de uma extensão bpmn",
        "conceitos de uma extensao bpmn",
        "conceitos da extensão bpmn",
        "conceitos da extensao bpmn",
        "conceitualizar extensão bpmn",
        "conceitualizar extensao bpmn",
        "extension specification concepts described",
        "extension specification [concepts described]",
    ],
    _DOC_03: [
        "definir o metamodelo", "definir metamodelo de uma extensão",
        "criar regras de validação", "regras de validacao para uma extensão",
        "definir a sintaxe concreta", "sintaxe concreta da extensão",
        "verificar completude de uma extensão",
        "verificar consistência de uma extensão",
        "identificar conflitos com bpmn",
        "restrições que não cabem no metamodelo",
        "xml compatível com omg", "xml compativel com omg",
        "como desenvolver uma extensão bpmn", "como desenvolver extensão bpmn",
        "como desenvolver extensao bpmn",
        "relacionar o metamodelo com bpmn",
        "representação xml",
    ],
    _DOC_04: [
        "ferramenta de modelagem para apoiar",
        "criar uma ferramenta de modelagem",
        "preciso desenvolver uma ferramenta nova",
        "ferramenta nova para minha extensão",
        "bpmn.io", "meta4model", "camunda", "bizagi",
        "reutilizar bpmn.io", "usar meta4model-bpmn",
        "adicionar novos construtos em uma ferramenta",
        "testar uma ferramenta de modelagem bpmn",
        "problemas devem ser corrigidos antes de liberar",
        "disponibilizar uma ferramenta para os usuários",
        "extension available", "extension applied",
        "adaptar uma ferramenta ou criar uma nova",
        "escolher entre adaptar uma ferramenta",
        "suporte de ferramenta", "tool support",
        "implementar a extensão em ferramenta",
        "posso reutilizar bpmn.io",
        "posso usar meta4model",
        "adapto uma ferramenta existente",
        "crio uma nova ferramenta de modelagem",
        "adaptar ferramenta existente",
        "criar nova ferramenta de modelagem",
        "decidir se adapto uma ferramenta existente",
        "decidir se crio uma nova ferramenta",
        "usuários não conseguiriam aplicar a extensão",
        "usuarios nao conseguiriam aplicar a extensao",
        "aplicar a extensão apenas lendo a especificação",
        "aplicar a extensao apenas lendo a especificacao",
    ],
    _DOC_05: [
        "como validar uma extensão bpmn",
        "como avaliar uma extensão bpmn",
        "aplicar uma extensão bpmn em um caso real",
        "usar a extensão bpmn para modelar",
        "identificar melhorias durante o uso",
        "limitações durante a modelagem",
        "registrar correções identificadas durante",
        "decidir se a extensão deve ser formalmente avaliada",
        "métodos podem ser usados para avaliar",
        "quando devo executar um experimento",
        "quando devo executar um estudo de caso",
        "quando devo executar um survey",
        "extensão está pronta para validação",
        "extensão está pronta para avaliação",
        "pronta para validação",
        "pronta para avaliação",
        "pronta para validacao",
        "pronta para avaliacao",
        "ready for validation",
        "ready for evaluation",
        "gerar a extension specification",
        "difference between validation and evaluation",
        "diferença entre validação e avaliação",
        "diferenca entre validacao e avaliacao",
        "validação e avaliação",
        "validacao e avaliacao",
    ],
    _DOC_06: [
        "consultar especialistas em extensões bpmn",
        "consultar especialista bpmn",
        "quando devo consultar especialistas bpmn",
        "quando devo consultar especialistas",
        "quando devo consultar especialistas do domínio",
        "selecionar especialistas para revisão",
        "informações devem ser enviadas aos especialistas",
        "solicitar feedback sobre uma extensão",
        "especialistas bpmn devem analisar",
        "especialistas do domínio devem analisar",
        "registrar feedback recebido dos especialistas",
        "documentar recomendações dos especialistas",
        "opiniões conflitantes de especialistas",
        "especialista não responder",
        "distinguir feedback bpmn de feedback do domínio",
        "construtos impactados por uma recomendação",
        "extensão foi validada por especialistas",
        "como consultar especialistas",
        "consultar especialistas",
        "consulta a especialistas",
        "feedback de especialistas",
        "recomendações dos especialistas",
        "recomendacoes dos especialistas",
    ],
    _DOC_07: [
        "como publicar uma extensão bpmn",
        "registrar uma extensão bpmn no catálogo",
        "quais informações devem ser incluídas no catálogo",
        "preparar uma extensão bpmn para publicação",
        "como obter endorsement", "endorsement para uma extensão",
        "quem pode endossar uma extensão bpmn",
        "especialistas externos devem ser notificados",
        "enviado para especialistas durante o endorsement",
        "extensão bpmn é bem definida",
        "critérios são usados para endorsement",
        "extensão não é endossada",
        "publicada sem endorsement",
        "status de publicação da extensão",
        "disponibilizar artefatos para a comunidade bpmn",
        "tornar uma extensão bpmn descoberta",
        "conformidade com as diretrizes omg",
        "pacote de publicação",
        "suporte ferramental no catálogo",
        "pronta para publicação",
        "pronta para publicacao",
        "extensão pronta para publicação",
        "extensao pronta para publicacao",
        "como sei se minha extensão está pronta para publicação",
        "como sei se minha extensao esta pronta para publicacao",
        "quando minha extensão pode ser publicada",
        "quando minha extensao pode ser publicada",
        "antes de publicar a extensão",
        "antes de publicar a extensao",
        "condições para publicação",
        "condicoes para publicacao",
        "requisitos para publicar",
        "pronto para publicar",
        "pronta para publicar",
    ],
    "artifact_modelling_and_observations.md": [
        "registrar dificuldades encontradas durante a modelagem",
        "registrar dificuldades encontradas",
        "dificuldades encontradas durante a modelagem",
        "observações de modelagem",
        "observacoes de modelagem",
        "modelling observations",
        "modelling difficulties",
        "dificuldades de modelagem",
    ],
    "artifact_extension_specification_concepts_described.md": [
        "documentar conceitos reutilizados",
        "conceitos reutilizados",
        "caracterizar estruturalmente uma extensão",
        "caracterização estrutural",
        "caracterizacao estrutural",
        "estruturalmente uma extensão bpmn",
        "conceptual characterization",
        "specification concepts described",
    ],
    "artifact_concrete_syntax_representations.md": [
        "representar graficamente novos construtos",
        "representação gráfica de construtos",
        "sintaxe concreta representações",
        "ícone para construto", "marcador visual para extensão",
    ],
    "artifact_checklist_completeness_consistency_conflicts.md": [
        "preencher o checklist de completude",
        "checklist de completude consistência conflitos",
        "checklist completude consistência",
        "como verificar completude de uma extensão",
        "como verificar consistência de uma extensão",
        "como identificar conflitos com bpmn",
    ],
    "list_of_bpmn_extension_experts.md": [
        "quem são os especialistas em extensões bpmn",
        "quem sao os especialistas em extensoes bpmn",
        "especialistas em extensões bpmn",
        "pesquisadores bpmn",
        "quais pesquisadores podem ser consultados",
        "bpmn extension experts",
        "lista de especialistas bpmn",
        "lista de pesquisadores bpmn",
    ],
    "artifact_extension_specification_developed.md": [
        "extension specification developed",
        "especificação developed",
        "especificacao developed",
    ],
    "artifact_extension_specification_validated_evaluated.md": [
        "extension specification validated",
        "extension specification evaluated",
        "registrar resultados de avaliação",
        "documentar melhorias identificadas durante a avaliação",
    ],
}

PALAVRAS_CATALOGO = [
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
    "area de aplicacao",
    "área de aplicação",
    "extensoes existentes",
    "extensões existentes",
    "extensao existente",
    "extensão existente",
    "slr",
]


# ---------------------------------------------------------------------------
# Carregamento de documentos
# ---------------------------------------------------------------------------

def _enriquecer_metadados(documentos, nome_base_padrao):
    for doc in documentos:
        file_name = doc.metadata.get("file_name", "")

        if "artifact_" in file_name:
            doc.metadata["base"] = "artefato"
            doc.metadata["artifact_id"] = file_name.replace(".md", "")
        elif "guidelines_" in file_name:
            doc.metadata["base"] = "guideline"
        elif "knowledge_map" in file_name:
            doc.metadata["base"] = "mapa"
        elif "rag_test" in file_name:
            doc.metadata["base"] = "teste"
        else:
            match = re.match(r"^(\d{2})_", file_name)
            if match:
                doc.metadata["base"] = "processo"
                doc.metadata["process_id"] = match.group(1)
            else:
                doc.metadata["base"] = nome_base_padrao

    return documentos


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

    _enriquecer_metadados(documentos, nome_base)
    return documentos


def carregar_arquivos_individuais(caminhos, nome_base):
    existentes = [str(c) for c in caminhos if Path(c).exists()]
    if not existentes:
        return []
    documentos = SimpleDirectoryReader(input_files=existentes).load_data()
    _enriquecer_metadados(documentos, nome_base)
    return documentos


def carregar_catalogo():
    documentos = carregar_documentos_csv()
    documentos.extend(
        carregar_documentos_diretorio(ROOT_DIR / "docs" / "catalog", "catalogo")
    )
    return documentos


def carregar_conhecimento():
    documentos = []

    documentos.extend(carregar_documentos_markdown())

    documentos.extend(
        carregar_arquivos_individuais(
            [
                ROOT_DIR / "docs" / "knowledge_map.md",
            ],
            "mapa",
        )
    )

    return documentos


print("Carregando catalogo...")
catalog_documents = carregar_catalogo()

print("Carregando documentos do conhecimento...")
knowledge_documents = carregar_conhecimento()

DOCUMENTOS_POR_NOME = {}
for _doc in knowledge_documents:
    _fn = _doc.metadata.get("file_name", "")
    if _fn:
        DOCUMENTOS_POR_NOME.setdefault(_fn, []).append(_doc)

print("Documentos por nome:")
for nome in sorted(DOCUMENTOS_POR_NOME):
    print("-", nome)

print(f"Documentos do catálogo: {len(catalog_documents)}")
print(f"Documentos do conhecimento: {len(knowledge_documents)}")

print("Criando índice do catálogo...")
catalog_index = VectorStoreIndex.from_documents(catalog_documents)

print("Criando índice do conhecimento...")
knowledge_index = VectorStoreIndex.from_documents(knowledge_documents)

catalog_engine = catalog_index.as_query_engine(similarity_top_k=4)
knowledge_engine = knowledge_index.as_query_engine(similarity_top_k=8)

estado_conversa = {
    "fluxo_ativo": None,
    "etapa_atual": None,
    "dominio": None,
    "conceitos": [],
}


# ---------------------------------------------------------------------------
# Roteamento
# ---------------------------------------------------------------------------

def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def contem_termo(p, termos):
    return any(t in p for t in termos)


def eh_consulta_catalogo(pergunta):
    p = normalizar_texto(pergunta)

    termos_catalogo = [
        "catalogo",
        "catalogo de extensoes",
        "catalogo de extensoes bpmn",
        "publicacao",
        "publicacoes",
        "artigo",
        "artigos",
        "autor",
        "autores",
        "por ano",
        "tipo journal",
        "journal",
        "conference",
        "conferencia",
        "dominio",
        "dominios",
        "area de aplicacao",
        "areas de aplicacao",
        "extensoes existentes",
        "extensao existente",
        "extensoes relacionadas",
        "extensao relacionada",
        "relacionadas a",
        "relacionados a",
        "existem extensoes",
        "liste extensoes",
        "listar extensoes",
        "publicacoes relacionadas",
        "slr",
    ]

    return any(t in p for t in termos_catalogo)


def rotear_artefato(pergunta):
    p = normalizar_texto(pergunta)

    if contem_termo(p, [
        "verificar completude",
        "como verificar completude",
        "verificar completude de uma extensao",
        "verificar consistencia",
        "como verificar consistencia",
        "verificar consistencia de uma extensao",
        "identificar conflitos com bpmn",
        "como identificar conflitos com bpmn",
        "checklist de completude",
        "checklist completude consistencia conflitos",
        "checklist de verificacao",
    ]):
        return ["artifact_checklist_completeness_consistency_conflicts.md"]

    if contem_termo(p, [
        "extension specification analysed",
        "extension specification analyzed",
        "specification analysed",
        "specification analyzed",
        "especificacao analisada",
        "especificação analisada",
    ]):
        return [
            "artifact_extension_specification_analysed.md",
            _DOC_01,
            _DOC_02,
        ]

    if contem_termo(p, [
        "extension specification concepts described",
        "concepts described",
        "conceitos descritos",
        "especificacao concepts described",
        "especificação concepts described",
    ]):
        return [
            "artifact_extension_specification_concepts_described.md",
            _DOC_02,
        ]

    if contem_termo(p, [
        "extension specification developed",
        "specification developed",
        "especificacao developed",
        "especificação developed",
        "especificacao desenvolvida",
        "especificação desenvolvida",
    ]):
        return [
            "artifact_extension_specification_developed.md",
            _DOC_03,
        ]

    if contem_termo(p, [
        "registrar resultados de avaliacao",
        "como registrar resultados de avaliacao",
        "documentar melhorias identificadas durante a avaliacao",
        "como documentar melhorias identificadas durante a avaliacao",
    ]):
        return ["artifact_extension_specification_validated_evaluated.md"]

    if contem_termo(p, [
        "extension specification validated evaluated",
        "extension specification validated/evaluated",
        "validated evaluated",
        "validated/evaluated",
        "especificacao validated evaluated",
        "especificação validated evaluated",
        "especificacao validada avaliada",
        "especificação validada avaliada",
    ]):
        if p.startswith("como gerar") or "como gerar a extension specification" in p:
            return []

        return [
            "artifact_extension_specification_validated_evaluated.md",
            _DOC_05,
        ]

    if contem_termo(p, [
        "modelling tool for the extension",
        "modeling tool for the extension",
        "ferramenta de modelagem da extensao",
        "ferramenta de modelagem da extensão",
        "modelling tool",
        "modeling tool",
    ]):
        return ["artifact_modelling_and_observations.md"]

    if contem_termo(p, [
        "list of bpmn extension experts",
        "lista de especialistas em extensoes bpmn",
        "lista de especialistas em extensões bpmn",
        "especialistas em extensoes bpmn",
        "especialistas em extensões bpmn",
    ]):
        return [
            "list_of_bpmn_extension_experts.md",
            _DOC_06,
        ]

    if contem_termo(p, [
        "bpmn extension catalog entry",
        "extension catalog entry",
        "catalog entry",
        "entrada no catalogo de extensoes bpmn",
        "entrada no catalogo de extensao bpmn",
        "entrada da extensao no catalogo",
        "entrada da extensao no catalogo de extensoes bpmn",
    ]):
        return [_DOC_07]

    return []

def rotear_subprocesso(pergunta):
    p = normalizar_texto(pergunta)

    if contem_termo(p, [
        "especialistas externos devem ser notificados",
        "quando especialistas externos devem ser notificados",
        "enviado para especialistas durante o endorsement",
        "enviadas para especialistas durante o endorsement",
        "o que deve ser enviado para especialistas durante o endorsement",
        "especialistas durante o endorsement",
        "notificar especialistas externos",
        "endorsement",
        "endosso",
    ]):
        return [_DOC_07]

    # 03 vem antes do 02: perguntas sobre metamodelo/sintaxe podem conter
    # "conceitos", mas pertencem ao desenvolvimento, não à descrição.
    if contem_termo(p, [
        "metamodelo",
        "sintaxe concreta",
        "xml",
        "esquema xml",
        "cardinalidade",
        "cardinalidades",
        "atributo",
        "atributos",
        "relacionamento",
        "relacionamentos",
        "restricao",
        "restricoes",
        "regra de validacao",
        "regras de validacao",
        "completude",
        "consistencia",
        "conflito",
        "conflitos",
        "checklist de verificacao",
    ]):
        return [_DOC_03]

    if contem_termo(p, [
        "descrever conceito",
        "descrever conceitos",
        "descrever corretamente os conceitos",
        "conceitos de uma extensao",
        "conceitos da extensao",
        "conceitos introduzidos",
        "conceito introduzido",
        "construtos reutilizados",
        "construto reutilizado",
        "reutilizar construtos",
        "integrar construtos",
        "integrar conceitos",
        "relacionar conceitos",
        "relacao entre conceitos",
        "relacao entre construtos",
        "equivalencia",
        "equivalente",
        "conceitualizar",
        "concepts described",
        "describe concepts",
        "describe extension concepts",
    ]):
        return [_DOC_02]

    if contem_termo(p, [
        "necessidade",
        "preciso criar",
        "devo criar",
        "quando criar",
        "quando devo criar",
        "bpmn padrao",
        "bpmn e adequado",
        "adequado para meu dominio",
        "atende meu dominio",
        "limitacao da bpmn",
        "limitacoes da bpmn",
        "conformity checklist",
        "catalogo de extensoes",
        "extensao relacionada",
        "extensoes relacionadas",
        "bpmn nao e suficiente",
        "bpmn e suficiente",
    ]):
        return [_DOC_01]

    if "suporte ferramental" in p and "catalogo" in p:
        return [_DOC_07]

    if contem_termo(p, [
        "ferramenta",
        "ferramental",
        "suporte ferramental",
        "tool",
        "modelling tool",
        "bpmn.io",
        "camunda",
        "bizagi",
        "meta4model",
        "extension available",
        "extension applied",
        "adaptar ferramenta",
        "criar ferramenta",
        "implementar ferramenta",
    ]):
        return [_DOC_04]

    if contem_termo(p, [
        "validar",
        "validacao",
        "avaliar",
        "avaliacao",
        "experimento",
        "estudo de caso",
        "survey",
        "uso pratico",
        "modelar um sistema",
        "aplicar a extensao",
        "resultados da avaliacao",
        "validated",
        "evaluated",
    ]):
        return [_DOC_05]

    if contem_termo(p, [
        "especialista",
        "especialistas",
        "consultar especialistas",
        "feedback",
        "recomendacao",
        "recomendacoes",
        "revisao por especialistas",
        "especialistas bpmn",
        "especialistas do dominio",
    ]):
        return [_DOC_06]

    if contem_termo(p, [
        "publicar",
        "publicacao",
        "publicise",
        "catalogo",
        "entrada no catalogo",
        "endorsement",
        "endosso",
        "endossar",
        "notificar especialistas externos",
        "pacote de publicacao",
        "disponibilizar para a comunidade",
    ]):
        return [_DOC_07]

    return []

def identificar_documentos_alvo(pergunta):
    artefatos = rotear_artefato(pergunta)
    if artefatos:
        return artefatos

    documentos = rotear_subprocesso(pergunta)
    if documentos:
        return documentos

    pergunta_normalizada = normalizar_texto(pergunta)

    alvos = []
    for nome_doc, palavras_chave in MAPA_DOCUMENTOS.items():
        for kw in palavras_chave:
            if normalizar_texto(kw) in pergunta_normalizada:
                alvos.append(nome_doc)
                break

    return alvos


def _expandir_pergunta(pergunta, documentos_alvo):
    if not documentos_alvo:
        return pergunta
    lista = ", ".join(documentos_alvo)
    return f"Documento esperado: {lista}\nPergunta: {pergunta}"


def contem_alguma(pergunta, palavras):
    pergunta_lower = pergunta.lower()
    return any(palavra in pergunta_lower for palavra in palavras)


def buscar_documentos_por_nome(nomes_alvo):
    resultado = []
    for nome in nomes_alvo:
        resultado.extend(DOCUMENTOS_POR_NOME.get(nome, []))
    return resultado


def _executar_query(prompt, documentos_alvo, engine_padrao):
    docs_alvo = buscar_documentos_por_nome(documentos_alvo)
    if docs_alvo:
        top_k = max(4, len(documentos_alvo) * 2)
        engine_alvo = VectorStoreIndex.from_documents(docs_alvo).as_query_engine(
            similarity_top_k=top_k
        )
        return engine_alvo.query(prompt)
    return engine_padrao.query(prompt)


def eh_contexto_de_processo(pergunta):
    pergunta_lower = pergunta.lower()
    expressoes = [
        "minha extensão",
        "minha extensao",
        "publicar a extensão",
        "publicar a extensao",
        "pronta para publicação",
        "pronta para publicacao",
        "pronta para publicar",
        "pronto para publicar",
        "quando minha extensão",
        "quando minha extensao",
        "antes de publicar",
    ]
    return any(e in pergunta_lower for e in expressoes)


def escolher_engine(pergunta, documentos_alvo=None):
    if documentos_alvo:
        return knowledge_engine, "conhecimento"
    if contem_alguma(pergunta, PALAVRAS_CATALOGO) and not eh_contexto_de_processo(pergunta):
        return catalog_engine, "catalogo"
    return knowledge_engine, "conhecimento"


# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

PROMPTS_ESPECIALIZADOS = {
    "artifact_extension_specification_analysed.md": "prompt_artifact_extension_specification_analysed.txt",
    "list_of_bpmn_extension_experts.md": "prompt_artifact_bpmn_extension_experts.txt",
    _DOC_01: "prompt_01_analyse_need.txt",
    _DOC_02: "prompt_02_describe_concepts.txt",
    _DOC_03: "prompt_03_develop_extension.txt",
    _DOC_04: "prompt_04_support_tool.txt",
    _DOC_05: "prompt_05_validate_evaluate.txt",
    _DOC_06: "prompt_06_consult_experts.txt",
    _DOC_07: "prompt_07_publicise_extension.txt",
}

_ARTEFATOS_CONHECIDOS = {
    "artifact_extension_specification_analysed.md",
    "artifact_extension_specification_concepts_described.md",
    "artifact_extension_specification_developed.md",
    "artifact_extension_specification_validated_evaluated.md",
    "artifact_modelling_and_observations.md",
    "artifact_concrete_syntax_representations.md",
    "artifact_checklist_completeness_consistency_conflicts.md",
    "list_of_bpmn_extension_experts.md",
}

_BLOCO_INSTRUCAO_ARTEFATO = """
--------------------------------------------------
INSTRUCOES PARA PERGUNTAS SOBRE ARTEFATOS
--------------------------------------------------

Responda tratando o item como artefato do processo BPMN Extension.
Nao exponha nomes internos de arquivos no corpo da resposta.
Nao cite caminhos de arquivo, nomes de arquivo ou identificadores internos.
Explique a finalidade, o conteudo esperado e o uso do artefato no processo.
Quando a pergunta for "O que deve conter...", liste as secoes e campos que compoem o artefato.
Quando a pergunta for "Para que serve...", explique a finalidade do artefato no processo.
"""


def carregar_prompt(nome_arquivo):
    caminho = ROOT_DIR / "prompts" / nome_arquivo
    if not caminho.exists():
        return ""
    return caminho.read_text(encoding="utf-8")


def criar_prompt(pergunta, tipo_base, documentos_alvo=None):
    bloco_documentos = ""
    if documentos_alvo:
        lista = ", ".join(documentos_alvo)
        bloco_documentos = (
            f"\nDocumentos esperados para esta pergunta: {lista}\n"
            "Use esses documentos como contexto principal da resposta. Quando houver um artefato e subprocessos relacionados, explique o artefato com base nesses documentos, sem dizer que a base é insuficiente se houver elementos listados neles.\n"
        )

    eh_artefato = bool(
        documentos_alvo and any(d in _ARTEFATOS_CONHECIDOS for d in documentos_alvo)
    )

    bloco_especializado = _BLOCO_INSTRUCAO_ARTEFATO if eh_artefato else ""
    if documentos_alvo:
        for documento in documentos_alvo:
            nome_prompt = PROMPTS_ESPECIALIZADOS.get(documento)
            if nome_prompt:
                conteudo = carregar_prompt(nome_prompt)
                bloco_especializado = (bloco_especializado + "\n" + conteudo).strip()
                break

    base_prompt = carregar_prompt("base_prompt.txt")

    return base_prompt.format(
        tipo_base=tipo_base,
        bloco_documentos=bloco_documentos,
        bloco_especializado=bloco_especializado,
        pergunta=pergunta,
    ).strip()


# ---------------------------------------------------------------------------
# Logica conversacional
# ---------------------------------------------------------------------------

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


_PREFIXOS_CONSULTA = (
    "como ",
    "o que ",
    "o que é",
    "qual ",
    "quais ",
    "quando ",
    "por que ",
    "porque ",
    "explique ",
    "explica ",
    "descreva ",
    "descreve ",
    "defina ",
    "define ",
    "me explique ",
    "pode explicar ",
)


def _eh_pergunta_consulta(pergunta):
    p = normalizar_texto(pergunta).strip()
    return p.startswith(_PREFIXOS_CONSULTA)


def _detectar_intencao_criar(pergunta_lower):
    p = normalizar_texto(pergunta_lower)
    return (
        ("quero criar" in p and ("extensao bpmn" in p or "uma extensao" in p))
        or ("vamos criar" in p and ("extensao bpmn" in p or "uma extensao" in p))
        or ("me ajude a desenvolver" in p and ("extensao" in p or "extensão" in p))
        or "iniciar desenvolvimento de extensao" in p
        or "quero comecar uma nova extensao" in p
        or "quero comecar uma extensao" in p
    )


def tentar_responder_fluxo_guiado(pergunta):
    global estado_conversa
    pergunta_lower = pergunta.lower()

    if estado_conversa["fluxo_ativo"] is None:
        if _eh_pergunta_consulta(pergunta):
            return None
        if not _detectar_intencao_criar(pergunta_lower):
            return None
        estado_conversa["fluxo_ativo"] = "criacao_extensao"
        estado_conversa["etapa_atual"] = "informar_dominio"
        estado_conversa["dominio"] = None
        estado_conversa["conceitos"] = []
        return "Qual é o domínio ou área de aplicação da extensão que você deseja criar?"

    if estado_conversa["fluxo_ativo"] == "criacao_extensao":

        if estado_conversa["etapa_atual"] == "informar_dominio":
            dominio = extrair_dominio(pergunta)
            estado_conversa["dominio"] = dominio

            resultado_catalogo = buscar_extensoes_por_dominio_ou_area(dominio)
            tem_resultado = resultado_catalogo and "não encontrei" not in resultado_catalogo.lower()

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


def _buscar_por_ano_catalogo(pergunta_lower):
    for ano in ["2019", "2020", "2021", "2022", "2023", "2024", "2025"]:
        if ano in pergunta_lower and "public" in pergunta_lower:
            return listar_publicacoes_por_ano(ano)
    return None


def _buscar_por_relacao_catalogo(pergunta_lower):
    if "relacionadas a" in pergunta_lower:
        termo = pergunta_lower.split("relacionadas a", 1)[1].replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)
    if "relacionados a" in pergunta_lower:
        termo = pergunta_lower.split("relacionados a", 1)[1].replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)
    return None


def _buscar_extensao_catalogo(pergunta_lower):
    tem_existe = re.search(r"\bexiste\b", pergunta_lower)
    tem_extensao = "extensão" in pergunta_lower or "extensao" in pergunta_lower
    if tem_existe and tem_extensao and "para" in pergunta_lower:
        termo = pergunta_lower.split("para", 1)[1].replace("?", "").replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)
    return None


def extrair_termo_catalogo(pergunta):
    p = pergunta.lower()

    padroes = [
        r"relacionadas? (?:à|a|ao|com) (.+)",
        r"relacionados? (?:à|a|ao|com) (.+)",
        r"extens[oõ]es bpmn para (.+)",
        r"extens[oõ]es para (.+)",
        r"publicac[oõ]es relacionadas? (?:a|à|ao) (.+)",
        r"publicações relacionadas? (?:a|à|ao) (.+)",
        r"sobre (.+)",
        r"para (.+)",
    ]

    lixo = [
        "no catálogo de extensões bpmn",
        "no catalogo de extensoes bpmn",
        "no catálogo",
        "no catalogo",
    ]

    for padrao in padroes:
        match = re.search(padrao, p)
        if match:
            termo = match.group(1)
            termo = termo.replace("?", "").replace(".", "").strip()
            for l in lixo:
                termo = termo.replace(l, "").strip()
            if termo:
                return termo

    return None


def tentar_responder_catalogo_estruturado(pergunta):
    pergunta_norm = normalizar_texto(pergunta)

    if "autores" in pergunta_norm and ("frequentes" in pergunta_norm or "mais" in pergunta_norm):
        return autores_mais_frequentes()

    if "por ano" in pergunta_norm or "quantas publicacoes" in pergunta_norm:
        return contar_publicacoes_por_ano()

    resultado_ano = _buscar_por_ano_catalogo(pergunta.lower())
    if resultado_ano:
        return resultado_ano

    if "journal" in pergunta_norm:
        return listar_publicacoes_por_tipo("journal")

    if "conference" in pergunta_norm or "conferencia" in pergunta_norm:
        return listar_publicacoes_por_tipo("conference")

    if "dominio" in pergunta_norm or "dominios" in pergunta_norm or "area de aplicacao" in pergunta_norm or "areas de aplicacao" in pergunta_norm:
        return listar_dominios_e_areas()

    # Consulta estruturada por domínio/área (campos controlados do SLR-DATA)
    # Deve vir antes de qualquer busca textual ampla para evitar falsos positivos.
    termo = extrair_termo_catalogo(pergunta)
    if termo and (
        "extensao" in pergunta_norm
        or "extensoes" in pergunta_norm
        or "relacionada" in pergunta_norm
        or "relacionadas" in pergunta_norm
        or "relacionado" in pergunta_norm
        or "relacionados" in pergunta_norm
        or "para" in pergunta_norm
    ):
        return buscar_extensoes_por_dominio_ou_area(termo)

    # Fallback textual (mantido para consultas de publicações sem menção a extensões)
    resultado_relacao = _buscar_por_relacao_catalogo(pergunta.lower())
    if resultado_relacao:
        return resultado_relacao

    resultado_extensao = _buscar_extensao_catalogo(pergunta.lower())
    if resultado_extensao:
        return resultado_extensao

    if termo:
        return buscar_extensoes_catalogo_por_termo(termo)

    return None


# ---------------------------------------------------------------------------
# Teste de recuperação RAG
# ---------------------------------------------------------------------------

def _parsear_pares_de_teste(conteudo):
    pares = []
    for linha in conteudo.splitlines():
        linha = linha.strip()
        if not linha.startswith("|") or "Pergunta" in linha or linha.startswith("| -"):
            continue
        partes = [p.strip() for p in linha.split("|") if p.strip()]
        if len(partes) >= 2:
            pergunta, esperado = partes[0], partes[1]
            if pergunta and esperado:
                pares.append((pergunta, esperado))
    return pares


def _avaliar_par_de_teste(pergunta, esperado, modo_verbose):
    documentos_alvo = identificar_documentos_alvo(pergunta)
    pergunta_expandida = _expandir_pergunta(pergunta, documentos_alvo)
    prompt = criar_prompt(pergunta_expandida, "conhecimento", documentos_alvo)
    resposta = _executar_query(prompt, documentos_alvo, knowledge_engine)

    fontes = [
        node.metadata.get("file_name", "")
        for node in resposta.source_nodes
        if node.metadata.get("file_name")
    ]

    encontrado = any(esperado in f or f.endswith(esperado) for f in fontes)
    status = "OK   " if encontrado else "FALHA"

    print(f"[{status}] {pergunta[:60]}")
    print(f"         Esperado:    {esperado}")
    print(f"         Recuperados: {', '.join(fontes[:5]) or 'nenhum'}")
    if modo_verbose and documentos_alvo:
        print(f"         Alvo RAG:    {', '.join(documentos_alvo)}")
    print()

    return encontrado


def testar_perguntas_rag(modo_verbose=False):
    caminho = ROOT_DIR / "docs" / "rag_test_questions.md"
    if not caminho.exists():
        print("Arquivo rag_test_questions.md não encontrado.")
        return

    pares = _parsear_pares_de_teste(caminho.read_text(encoding="utf-8"))

    print(f"\n{'='*80}")
    print(f"RELATÓRIO DE TESTE RAG — {len(pares)} perguntas")
    print(f"{'='*80}\n")

    ok = sum(1 for p, e in pares if _avaliar_par_de_teste(p, e, modo_verbose))
    falha = len(pares) - ok

    print(f"{'='*80}")
    print(f"Resultado: {ok} OK / {falha} FALHA de {len(pares)} perguntas")
    if pares:
        print(f"Taxa de acerto: {ok / len(pares) * 100:.1f}%")
    print(f"{'='*80}\n")


LABEL_RESPOSTA = "\nResposta:"

def limpar_resposta(texto):
    texto = str(texto)

    substituicoes = {
        "documento esperado": "subprocesso correspondente",
        "Documento esperado": "Subprocesso correspondente",

        "restreções": "restrições",
        "Restreções": "Restrições",

        "na metamodelo": "no metamodelo",
        "da metamodelo": "do metamodelo",
        "das metamodelo": "dos metamodelos",

        "Explica o relacionamento": "Explique o relacionamento",
        "Prove referências": "Forneça referências",
        "Prove evidências": "Forneça evidências",

        "avaliados pelo equivalência": "avaliados quanto à equivalência",
        "avaliado pelo equivalência": "avaliado quanto à equivalência",

        "análise analítica": "análise realizada",
        "conforme a orientação fornecida": "conforme o subprocesso correspondente",

        "O subprocesso correspondente contém": "O artefato deve conter",
        "subprocesso correspondente": "artefato correspondente",

        "escenário": "cenário",
        "Até final deste artefato": "Ao final deste artefato",

        "constructos": "construtos",
        "Constructos": "Construtos",

        "reglas": "regras",
        "Reglas": "Regras",

        "notação concisa": "notação concreta",
        "notacao concisa": "notação concreta",

        "novas, reutilizadas ou adaptadas conceitos": "conceitos novos, reutilizados ou adaptados",

        "deve contém": "deve conter",
        "Deve contém": "Deve conter",

        "dominio": "domínio",
        "Dominio": "Domínio",

        "o sintaxe concreta": "a sintaxe concreta",
        "do sintaxe concreta": "da sintaxe concreta",
        "validação do sintaxe concreta": "validação da sintaxe concreta",
        "O documento list_of_bpmn_extension_experts.md fornece": "A lista de especialistas em extensões BPMN fornece",
        "documento list_of_bpmn_extension_experts.md": "artefato List of BPMN Extension Experts",
    }

    for errado, certo in substituicoes.items():
        texto = texto.replace(errado, certo)

    return texto

# ---------------------------------------------------------------------------
def imprimir_formatado(texto, largura=100):
    for bloco in str(texto).splitlines():
        bloco = bloco.strip()
        if not bloco:
            print()
            continue
        if bloco.startswith(("-", "*")) or re.match(r"^\d+\.", bloco):
            print(textwrap.fill(bloco, width=largura, subsequent_indent="   "))
        else:
            print(textwrap.fill(bloco, width=largura))


# Loop principal
# ---------------------------------------------------------------------------

print("\nBPMN-BOT iniciado!")
print("Digite 'sair' para encerrar.")
print("Digite 'testar' para executar o teste de recuperação RAG.")
print("Digite 'testar -v' para o modo verbose do teste.\n")

while True:
    pergunta = input("Pergunta: ").strip()

    if not pergunta:
        continue

    if pergunta.lower() == "sair":
        break

    if pergunta.lower() in ("testar", "testar -v"):
        testar_perguntas_rag(modo_verbose="-v" in pergunta.lower())
        continue

    if eh_consulta_catalogo(pergunta):
        resposta_estruturada = tentar_responder_catalogo_estruturado(pergunta)
        if resposta_estruturada:
            print(LABEL_RESPOSTA)
            imprimir_formatado(limpar_resposta(resposta_estruturada))
            print("\nFonte: consulta estruturada com pandas nos CSVs do catálogo\n")
            continue

    documentos_alvo = identificar_documentos_alvo(pergunta)

    if not documentos_alvo:
        resposta_estruturada = tentar_responder_catalogo_estruturado(pergunta)
        if resposta_estruturada:
            print(LABEL_RESPOSTA)
            imprimir_formatado(limpar_resposta(resposta_estruturada))
            print("\nFonte: consulta estruturada com pandas nos CSVs do catálogo\n")
            continue

    if not documentos_alvo:
        resposta_fluxo = tentar_responder_fluxo_guiado(pergunta)
        if resposta_fluxo:
            print(LABEL_RESPOSTA)
            imprimir_formatado(resposta_fluxo)
            print("\nFonte: fluxo guiado de criação de extensão BPMN\n")
            continue

    engine, tipo_base = escolher_engine(pergunta, documentos_alvo)

    pergunta_expandida = _expandir_pergunta(pergunta, documentos_alvo)
    prompt = criar_prompt(pergunta_expandida, tipo_base, documentos_alvo)

    if documentos_alvo and tipo_base == "conhecimento":
        resposta = _executar_query(prompt, documentos_alvo, knowledge_engine)
    else:
        resposta = engine.query(prompt)

    print(LABEL_RESPOSTA)
    resposta_limpa = limpar_resposta(resposta.response)
    imprimir_formatado(resposta_limpa)

    fontes = []
    for node in resposta.source_nodes:
        origem = (
            node.metadata.get("file_name")
            or node.metadata.get("dataset")
            or node.metadata.get("base")
        )
        if origem and origem not in fontes:
            fontes.append(origem)

    if fontes:
        print(f"\nFontes: {', '.join(fontes)}")

    print("\n")