import re
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
MAPA_DOCUMENTOS = {
    "01_analyse_need_for_extension.md": [
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
    ],
    "02_describe_extension_concepts.md": [
        "conceitos minha extensão deve introduzir",
        "quais conceitos minha extensão",
        "definir um conceito da extensão", "definir conceito da extensão",
        "reutilizar construtos de extensões", "reutilizar construtos existentes",
        "integrar novos conceitos à bpmn", "relacionar conceitos da extensão",
        "equivalências entre conceitos", "especializado ou criado do zero",
        "identificar equivalências",
    ],
    "03_develop_bpmn_extension.md": [
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
    "04_support_extension_with_tool.md": [
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
    "05_validate_and_evaluate_extension.md": [
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
    "06_consult_experts.md": [
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
    "07_publicise_bpmn_extension.md": [
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

print(f"Documentos do catalogo: {len(catalog_documents)}")
print(f"Documentos do conhecimento: {len(knowledge_documents)}")

print("Criando indice do catalogo...")
catalog_index = VectorStoreIndex.from_documents(catalog_documents)

print("Criando indice do conhecimento...")
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

def identificar_documentos_alvo(pergunta):
    pergunta_lower = pergunta.lower()
    alvos = []
    for nome_doc, palavras_chave in MAPA_DOCUMENTOS.items():
        for kw in palavras_chave:
            if kw in pergunta_lower:
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
        engine_alvo = VectorStoreIndex.from_documents(docs_alvo).as_query_engine(
            similarity_top_k=6
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
    "01_analyse_need_for_extension.md": "prompt_01_analyse_need.txt",
    "02_describe_extension_concepts.md": "prompt_02_describe_concepts.txt",
    "03_develop_bpmn_extension.md": "prompt_03_develop_extension.txt",
    "04_support_extension_with_tool.md": "prompt_04_support_tool.txt",
    "05_validate_and_evaluate_extension.md": "prompt_05_validate_evaluate.txt",
    "06_consult_experts.md": "prompt_06_consult_experts.txt",
    "07_publicise_bpmn_extension.md": "prompt_07_publicise_extension.txt",
}


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
            "Priorize trechos desses documentos se eles aparecerem entre as fontes recuperadas.\n"
        )

    bloco_especializado = ""
    if documentos_alvo:
        for documento in documentos_alvo:
            nome_prompt = PROMPTS_ESPECIALIZADOS.get(documento)
            if nome_prompt:
                bloco_especializado = carregar_prompt(nome_prompt)
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


def _detectar_intencao_criar(pergunta_lower):
    return (
        ("como criar" in pergunta_lower and "extensão bpmn" in pergunta_lower)
        or ("como criar" in pergunta_lower and "extensao bpmn" in pergunta_lower)
        or ("quero criar" in pergunta_lower and "extensão bpmn" in pergunta_lower)
        or ("quero criar" in pergunta_lower and "extensao bpmn" in pergunta_lower)
        or "criar extensão bpmn" in pergunta_lower
        or "criar extensao bpmn" in pergunta_lower
    )


def tentar_responder_fluxo_guiado(pergunta):
    global estado_conversa
    pergunta_lower = pergunta.lower()

    intencao_criar = _detectar_intencao_criar(pergunta_lower)

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


def tentar_responder_catalogo_estruturado(pergunta):
    pergunta_lower = pergunta.lower()

    if "autores" in pergunta_lower and ("mais" in pergunta_lower or "frequentes" in pergunta_lower):
        return autores_mais_frequentes()

    if "por ano" in pergunta_lower or "quantas publicações" in pergunta_lower:
        return contar_publicacoes_por_ano()

    resultado_ano = _buscar_por_ano_catalogo(pergunta_lower)
    if resultado_ano:
        return resultado_ano

    if "journal" in pergunta_lower:
        return listar_publicacoes_por_tipo("journal")

    if "conference" in pergunta_lower or "conferência" in pergunta_lower:
        return listar_publicacoes_por_tipo("conference")

    resultado_relacao = _buscar_por_relacao_catalogo(pergunta_lower)
    if resultado_relacao:
        return resultado_relacao

    if "sobre" in pergunta_lower and "public" in pergunta_lower:
        termo = pergunta_lower.split("sobre", 1)[1].replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)

    if contem_alguma(pergunta_lower, ["domínios", "dominios", "áreas de aplicação", "areas de aplicacao"]):
        return listar_dominios_e_areas()

    return _buscar_extensao_catalogo(pergunta_lower)


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

# ---------------------------------------------------------------------------
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

    documentos_alvo = identificar_documentos_alvo(pergunta)

    if not documentos_alvo:
        resposta_estruturada = tentar_responder_catalogo_estruturado(pergunta)
        if resposta_estruturada:
            print(LABEL_RESPOSTA)
            print(resposta_estruturada)
            print("\nFonte: consulta estruturada com pandas nos CSVs do catálogo\n")
            continue

    resposta_fluxo = tentar_responder_fluxo_guiado(pergunta)
    if resposta_fluxo:
        print(LABEL_RESPOSTA)
        print(resposta_fluxo)
        print("\nFonte: fluxo guiado de criação de extensão BPMN\n")
        continue

    engine, tipo_base = escolher_engine(pergunta, documentos_alvo)

    print(f"\nBase escolhida: {tipo_base}")
    if documentos_alvo:
        print(f"Documentos alvo: {', '.join(documentos_alvo)}")

    pergunta_expandida = _expandir_pergunta(pergunta, documentos_alvo)
    prompt = criar_prompt(pergunta_expandida, tipo_base, documentos_alvo)

    if documentos_alvo and tipo_base == "conhecimento":
        resposta = _executar_query(prompt, documentos_alvo, knowledge_engine)
    else:
        resposta = engine.query(prompt)

    print(LABEL_RESPOSTA)
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