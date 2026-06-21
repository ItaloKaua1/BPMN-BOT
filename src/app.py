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
        "registrar dificuldades encontradas",
        "identificar limitações da bpmn",
        "identificar conceitos que bpmn não representa",
    ],
    "02_describe_extension_concepts.md": [
        "conceitos minha extensão deve introduzir",
        "quais conceitos minha extensão",
        "definir um conceito da extensão", "definir conceito da extensão",
        "reutilizar construtos de extensões", "reutilizar construtos existentes",
        "integrar novos conceitos à bpmn", "relacionar conceitos da extensão",
        "equivalências entre conceitos", "especializado ou criado do zero",
        "documentar conceitos reutilizados",
        "caracterizar estruturalmente uma extensão",
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
        "registrar resultados de avaliação",
        "extensão está pronta para validação",
        "extensão está pronta para avaliação",
        "extension specification validated",
        "extension specification evaluated",
        "gerar a extension specification",
    ],
    "06_consult_experts.md": [
        "consultar especialistas em extensões bpmn",
        "consultar especialista bpmn",
        "quem são os especialistas em extensões bpmn",
        "quando devo consultar especialistas bpmn",
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
        "quais pesquisadores podem ser consultados",
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

    # docs/process (inclui docs/process/artifacts/ recursivamente)
    documentos.extend(
        carregar_documentos_diretorio(ROOT_DIR / "docs" / "process", "processo")
    )

    # docs/metamodel
    documentos.extend(
        carregar_documentos_diretorio(ROOT_DIR / "docs" / "metamodel", "metamodelo")
    )

    # docs/guidelines (opcional)
    documentos.extend(
        carregar_documentos_diretorio(ROOT_DIR / "docs" / "guidelines", "guideline")
    )

    # Arquivos individuais de suporte ao RAG
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


def escolher_engine(pergunta):
    if contem_alguma(pergunta, PALAVRAS_CATALOGO):
        return catalog_engine, "catalogo"
    return knowledge_engine, "conhecimento"


# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

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
        if "01_analyse_need_for_extension.md" in documentos_alvo:
            bloco_especializado = """
            A pergunta refere-se ao subprocesso 1 - Analyse the Need for Extension.

            Responda apenas com base nas atividades deste subprocesso.

            Priorize:
            - estudo do domínio ou área de aplicação
            - identificação dos conceitos a serem introduzidos
            - verificação de adequação do BPMN padrão (BPMN conformity checklist)
            - modelagem de exemplo com BPMN padrão e observações de modelagem
            - busca por extensões BPMN relacionadas no catálogo
            - consulta a especialistas em domínio ou BPMN, quando necessário
            - geração da Extension Specification [Analysed]

            Não descreva etapas de descrição de conceitos, desenvolvimento de metamodelo,
            suporte ferramental, validação, avaliação ou publicação.

            A resposta deve seguir exatamente esta estrutura:

            1. Estudar/Revisar o Domínio ou Área de Aplicação
            Explique que o Extender deve identificar o propósito da extensão, a área de aplicação, aspectos práticos e referências relevantes.

            2. Identificar os Conceitos a Serem Introduzidos
            Explique que o Extender deve listar os conceitos que a extensão introduzirá no BPMN, descrevendo nome, definição, fonte e relevância de cada um.

            3. Verificar se o BPMN Padrão Atende os Requisitos
            Explique que o Extender deve usar o BPMN conformity checklist para avaliar se a notação BPMN é adequada e se a sintaxe padrão já modela a necessidade.

            4. Modelar um Exemplo com BPMN Padrão
            Explique que o Extender deve criar um modelo BPMN de exemplo com os conceitos identificados e registrar as observações de modelagem.

            5. Buscar Extensões BPMN Relacionadas
            Explique que o Extender deve pesquisar o Catálogo de Extensões BPMN para verificar se alguma extensão existente já atende a necessidade.

            6. Gerar a Extension Specification [Analysed]
            Explique que, se o BPMN padrão for insuficiente e nenhuma extensão existente satisfizer a necessidade, o Extender deve gerar a especificação analisada com toda a evidência coletada.

            Artefatos/resultados esperados:
            - Lista de referências e pesquisadores consultados
            - Lista de conceitos a serem introduzidos
            - BPMN conformity checklist
            - Observações de modelagem
            - Lista de extensões BPMN relacionadas à proposta
            - Extension specification [Analysed]
            - Decisão: existe necessidade da extensão
            """
        elif "02_describe_extension_concepts.md" in documentos_alvo:
            bloco_especializado = """
            A pergunta refere-se ao subprocesso 2 - Describe Concepts of the BPMN Extension.

            Responda apenas com base nas atividades deste subprocesso.

            Priorize:
            - busca e seleção de construtos BPMN reutilizáveis
            - descrição dos conceitos da extensão (nome, definição, propósito, relação com BPMN)
            - análise de como integrar os construtos da extensão com o BPMN
            - análise de equivalência entre construtos propostos e construtos BPMN existentes
            - consulta a especialistas em extensões BPMN, quando necessário
            - geração da Extension Specification [Concepts Described]

            Não descreva etapas de análise da necessidade, desenvolvimento de metamodelo,
            sintaxe concreta, suporte ferramental, validação, avaliação ou publicação.

            A resposta deve seguir exatamente esta estrutura:

            1. Buscar e Selecionar Construtos a Serem Reutilizados
            Explique que o Extender deve identificar construtos BPMN ou de extensões existentes que possam ser reutilizados, registrando nome, fonte, motivo de reutilização e limitações.

            2. Descrever os Conceitos da Extensão
            Explique que cada conceito deve ser descrito com nome, definição, propósito, relação com BPMN, classificação (novo, reutilizado ou adaptado) e exemplos de uso.

            3. Analisar como Integrar os Construtos da Extensão com o BPMN
            Explique que o Extender deve mapear cada conceito ao construto BPMN que ele estende, especializa ou complementa, identificando o tipo de relação (estrutural, semântica, notacional) e possíveis conflitos.

            4. Analisar a Equivalência entre os Construtos
            Explique que o Extender deve verificar se algum construto proposto é equivalente a construtos BPMN ou de extensões existentes, preferindo reutilização quando possível.

            5. Gerar a Extension Specification [Concepts Described]
            Explique que o Extender deve consolidar construtos reutilizados, conceitos introduzidos, relações com BPMN e caracterização conceitual e estrutural na especificação com conceitos descritos.

            Artefatos/resultados esperados:
            - Lista de construtos a serem reutilizados
            - Lista de conceitos a serem introduzidos [com descrição dos conceitos]
            - Lista de relações entre construtos da extensão e construtos BPMN
            - Caracterização conceitual e estrutural
            - Extension specification [Concepts described]
            - Decisão: extensão BPMN conceitualizada
            """
        elif "03_develop_bpmn_extension.md" in documentos_alvo:
            bloco_especializado = """
            A pergunta refere-se ao subprocesso 3 - Develop BPMN Extension.

            Responda apenas com base nas atividades deste subprocesso.

            Priorize:
            - definição do metamodelo da extensão (elementos, atributos, relacionamentos, cardinalidades)
            - definição de regras de validação não representáveis no metamodelo
            - definição da sintaxe concreta (representação visual de cada construto)
            - verificação de completude, consistência e conflitos (checklist)
            - decisão sobre suporte ferramental
            - geração da Extension Specification [Developed]

            Não descreva etapas de análise da necessidade, descrição de conceitos,
            implementação da ferramenta de modelagem, validação, avaliação ou publicação.

            A resposta deve seguir exatamente esta estrutura:

            1. Definir o Metamodelo da Extensão
            Explique que o Extender deve mapear cada conceito descrito para um elemento do metamodelo BPMN, especificando atributos, relacionamentos, cardinalidades, restrições e, quando aplicável, o esquema XML.

            2. Definir Regras de Validação
            Explique que restrições que não podem ser representadas diretamente no metamodelo devem ser expressas como regras de validação explícitas, com identificador, condição, severidade e justificativa.

            3. Definir a Sintaxe Concreta
            Explique que cada construto da extensão deve ter uma representação visual definida (marcador, ícone, forma, cor, rótulo ou relacionamento), compatível com a notação BPMN.

            4. Verificar Completude, Consistência e Conflitos
            Explique que o Extender deve aplicar o checklist de verificação para garantir que todos os conceitos estão representados no metamodelo, que a sintaxe concreta está alinhada e que não há conflitos com o BPMN padrão.

            5. Decidir sobre Suporte Ferramental
            Explique que o Extender deve decidir se a extensão será suportada por uma ferramenta de modelagem e registrar a decisão, mesmo que seja negativa.

            6. Gerar a Extension Specification [Developed]
            Explique que o Extender deve consolidar metamodelo, regras de validação, sintaxe concreta, resultado do checklist e decisão sobre ferramenta na especificação desenvolvida.

            Artefatos/resultados esperados:
            - Metamodelo da extensão
            - Regras de validação da extensão
            - Lista de representações de sintaxe concreta
            - Checklist de verificação de problemas
            - Decisão sobre suporte ferramental
            - Extension specification [Developed]
            - Decisão: extensão BPMN desenvolvida
            """
        elif "04_support_extension_with_tool.md" in documentos_alvo:
            bloco_especializado = """
            A pergunta é sobre o subprocesso 3.5 Support the Extension With a Modelling Tool.

            Responda somente sobre suporte ferramental.
            Nao inclua etapas de validação, avaliação, publicação, endorsement ou catálogo.
            Nao inclua análise de domínio nem descrição de conceitos, exceto se forem necessários como entrada já existente.

            A resposta deve seguir exatamente esta estrutura:

            1. Decidir a estratégia de ferramenta
            Explique que o Extender deve decidir se vai usar uma ferramenta existente ou criar uma nova.

            2. Adicionar construtos a uma ferramenta existente
            Explique que, se não houver intenção de criar uma nova ferramenta, os construtos devem ser adicionados/configurados na ferramenta existente.

            3. Implementar uma nova ferramenta, se necessário
            Explique que, se uma ferramenta dedicada for necessária, ela deve suportar metamodelo, sintaxe concreta, criação/edição de construtos, validação, persistência, importação/exportação e integração com BPMN.

            4. Testar a ferramenta
            Explique que a ferramenta deve ser testada verificando criação de construtos, renderização da sintaxe concreta, edição de propriedades, regras de validação, salvamento/carregamento e compatibilidade BPMN.

            5. Corrigir problemas
            Explique que problemas identificados devem ser corrigidos e a ferramenta deve ser testada novamente.

            6. Disponibilizar a ferramenta
            Explique que, quando não houver correções pendentes, a ferramenta deve ser disponibilizada aos usuários.

            Artefatos/resultados esperados:
            - Modelling tool for the extension
            - Tool test results
            - Corrected modelling tool
            - Extension available
            - Extension applied
            """
        elif "05_validate_and_evaluate_extension.md" in documentos_alvo:
            bloco_especializado = """
            A pergunta refere-se ao subprocesso 4 - Validate and Evaluate the BPMN Extension.

            Responda apenas com base nas atividades deste subprocesso.

            Priorize:
            - uso prático da extensão em cenários de modelagem realistas
            - aplicação de correções identificadas durante o uso
            - revisão por especialistas em extensões BPMN e, quando aplicável, especialistas no domínio
            - aplicação de correções sugeridas por especialistas
            - avaliação formal da extensão (experimento controlado, estudo de caso ou survey)
            - aplicação de melhorias identificadas na avaliação
            - geração da Extension Specification [Validated/Evaluated]

            Não descreva etapas de análise da necessidade, descrição de conceitos, desenvolvimento,
            suporte ferramental, registro no catálogo, endosso ou publicação.

            A resposta deve seguir exatamente esta estrutura:

            1. Usar a Extensão BPMN para Modelar um Sistema
            Explique que o Extender deve aplicar a extensão em cenários de modelagem realistas, documentando decisões de modelagem, limitações identificadas e oportunidades de melhoria.

            2. Aplicar Correções do Uso Prático
            Explique que correções identificadas durante o uso devem ser aplicadas na especificação antes de prosseguir para a revisão por especialistas.

            3. Consultar Especialistas
            Explique que a extensão deve ser submetida à revisão de especialistas em extensões BPMN e, quando relevante, especialistas no domínio, coletando recomendações, correções e sugestões.

            4. Aplicar Correções dos Especialistas
            Explique que o Extender deve incorporar o feedback recebido, verificando que as modificações não introduzem inconsistências, incompletude ou conflitos.

            5. Avaliar a Extensão BPMN (opcional)
            Explique que a extensão pode ser avaliada formalmente por meio de experimento controlado, estudo de caso ou survey, registrando método, participantes, resultados e melhorias identificadas.

            6. Gerar a Extension Specification [Validated/Evaluated]
            Explique que o Extender deve consolidar exemplos de uso, feedback de especialistas, resultados da avaliação e melhorias aplicadas na especificação validada/avaliada.

            Artefatos/resultados esperados:
            - Exemplos de uso
            - Resultados da revisão por especialistas
            - Resultados da avaliação
            - Melhorias identificadas e aplicadas
            - Extension specification [Validated/Evaluated]
            - Decisão: extensão BPMN avaliada
            """
        elif "06_consult_experts.md" in documentos_alvo:
            bloco_especializado = """
            A pergunta refere-se ao subprocesso 4.3 - Consult Experts.

            Responda apenas com base nas atividades deste subprocesso.

            Priorize:
            - identificação do tipo de especialista necessário (BPMN ou domínio)
            - preparação do material a ser enviado aos especialistas
            - coleta e organização do feedback recebido
            - registro de recomendações, correções e impacto em cada construto

            Não descreva etapas de desenvolvimento do metamodelo, sintaxe concreta ou regras de validação,
            uso prático para modelagem, avaliação formal, publicação, catálogo ou endosso.

            A resposta deve seguir exatamente esta estrutura:

            1. Consultar Especialistas em Extensões BPMN
            Explique que o Extender deve identificar especialistas em extensões BPMN e enviar a especificação desenvolvida, modelos de exemplo, problemas identificados e questões específicas.

            2. Consultar Especialistas no Domínio/Área de Aplicação
            Explique que este passo é executado apenas quando a extensão está relacionada a um domínio específico (como segurança, saúde, IoT, robótica), coletando conceitos ausentes, inconsistências terminológicas e observações práticas.

            3. Especialistas em BPMN Analisam a Extensão
            Explique que os especialistas devem analisar definições de construtos, integração com BPMN, sintaxe concreta, metamodelo e regras de validação, produzindo feedback de especialistas BPMN.

            4. Especialistas no Domínio Analisam a Extensão
            Explique que os especialistas devem analisar correção de domínio, completude conceitual e aplicabilidade prática, produzindo feedback de especialistas no domínio.

            5. Receber e Registrar o Feedback
            Explique que o Extender deve registrar cada recomendação com especialista, recomendação, construto impactado e ação tomada, tanto para feedback BPMN quanto para feedback de domínio.

            Artefatos/resultados esperados:
            - Feedback de especialistas em BPMN
            - Feedback de especialistas no domínio
            - Registros de consulta a especialistas
            - Lista de recomendações
            - Correções e melhorias identificadas
            - Extensão BPMN validada por especialistas
            """
        elif "07_publicise_bpmn_extension.md" in documentos_alvo:
            bloco_especializado = """
            A pergunta refere-se ao subprocesso 6 - Publicise the BPMN Extension.

            Responda apenas com base nas atividades deste subprocesso.

            Priorize:
            - registro da extensão no Catálogo de Extensões BPMN
            - endosso da extensão (interno ou externo)
            - publicação da extensão com todos os artefatos necessários

            Não descreva etapas de análise da necessidade, descrição de conceitos, desenvolvimento,
            suporte ferramental, validação ou avaliação (já concluídas neste ponto).

            A resposta deve seguir exatamente esta estrutura:

            1. Adicionar a Extensão ao Catálogo
            Explique que o Extender deve registrar a extensão no Catálogo de Extensões BPMN com nome, versão, autores, propósito, área de aplicação, resumo dos conceitos, sintaxe concreta, status de validação/avaliação e informações de suporte ferramental.

            2. Endossar a Extensão BPMN (endosso interno)
            Explique que, se um especialista em extensões BPMN faz parte da equipe Extender, o endosso pode ser realizado internamente, verificando se a extensão está bem definida, compatível com BPMN e com artefatos de publicação prontos.

            3. Notificar Especialistas Externos (quando necessário)
            Explique que, se não houver especialista em extensões BPMN na equipe, especialistas externos devem ser notificados com a especificação validada/avaliada, entrada no catálogo e solicitação de endosso.

            4. Receber Decisão de Endosso
            Explique que especialistas externos analisam a extensão e decidem se ela está bem definida, gerando os resultados possíveis: extensão BPMN endossada ou extensão BPMN não endossada.

            5. Publicar a Extensão BPMN
            Explique que, após o endosso e o registro no catálogo, o Extender deve disponibilizar a especificação, entrada no catálogo, exemplos, metamodelo, regras de validação, sintaxe concreta, informações de suporte ferramental e notas de versão.

            Artefatos/resultados esperados:
            - Entrada no catálogo para a extensão BPMN
            - Notificação de nova extensão (quando especialistas externos são consultados)
            - Extensão BPMN endossada ou não endossada
            - Pacote de publicação ou localização de acesso público
            - Extensão BPMN publicada
            """
    return f"""Voce e o BPMN-BOT, um assistente especializado em extensoes BPMN.

Base consultada: {tipo_base}.
{bloco_documentos}
Instrucoes:
- Use somente as fontes recuperadas.
- Responda em portugues.
- Nao mostre raciocinio interno nem cite nomes de arquivos.
- Se houver documento alvo, nao use informações de outros subprocessos para completar a resposta.
- Responda diretamente ao usuario, como um assistente orientando uma pessoa.
- Nao comece dizendo "o usuario esta no arquivo X".
- Quando citar artefatos, use exatamente os nomes encontrados nas fontes.
- Não renomeie artefatos.
- Não crie artefatos equivalentes.
- Não adicione resultados de subprocessos diferentes.

Escopo da resposta:
- Se a pergunta for sobre uma etapa específica, uma decisão, um artefato ou um termo, responda somente essa parte.
- Apresente o fluxo completo do subprocesso apenas quando a pergunta pedir explicitamente o processo inteiro.

Se a pergunta for sobre "como fazer" algo no processo:
- Comece com uma frase direta resumindo o que deve ser feito.
- Apresente os passos em ordem numerada.
- Para cada passo, descreva o objetivo brevemente.
- Informe quais artefatos sao produzidos ou utilizados em cada passo.
- Quando houver uma decisao importante, explique os criterios para tomar essa decisao.
- Termine indicando o proximo passo ou o artefato esperado ao final.
{bloco_especializado}
Se a pergunta for sobre catalogo:
- Responda somente com base nos registros recuperados.
- Nao invente publicacoes, autores ou dominios.

Se as fontes recuperadas nao forem suficientes, diga:
"A base atual nao contem informacao suficiente para confirmar isso."

Pergunta do usuario:
{pergunta}""".strip()


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
        termo = pergunta_lower.split("relacionadas a", 1)[1].replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)

    if "relacionados a" in pergunta_lower:
        termo = pergunta_lower.split("relacionados a", 1)[1].replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)

    if "sobre" in pergunta_lower and "public" in pergunta_lower:
        termo = pergunta_lower.split("sobre", 1)[1].replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)

    if "domínios" in pergunta_lower or "dominios" in pergunta_lower:
        return listar_dominios_e_areas()

    if "áreas de aplicação" in pergunta_lower or "areas de aplicacao" in pergunta_lower:
        return listar_dominios_e_areas()

    if "existe" in pergunta_lower and "extensão" in pergunta_lower and "para" in pergunta_lower:
        termo = pergunta_lower.split("para", 1)[1].replace("?", "").replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)

    if "existe" in pergunta_lower and "extensao" in pergunta_lower and "para" in pergunta_lower:
        termo = pergunta_lower.split("para", 1)[1].replace("?", "").replace(".", "").strip()
        return buscar_publicacoes_por_termo(termo)

    return None


# ---------------------------------------------------------------------------
# Teste de recuperação RAG
# ---------------------------------------------------------------------------

def testar_perguntas_rag(modo_verbose=False):
    caminho = ROOT_DIR / "docs" / "rag_test_questions.md"
    if not caminho.exists():
        print("Arquivo rag_test_questions.md não encontrado.")
        return

    conteudo = caminho.read_text(encoding="utf-8")

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

    print(f"\n{'='*80}")
    print(f"RELATÓRIO DE TESTE RAG — {len(pares)} perguntas")
    print(f"{'='*80}\n")

    ok = 0
    falha = 0

    for pergunta, esperado in pares:
        documentos_alvo = identificar_documentos_alvo(pergunta)
        pergunta_expandida = _expandir_pergunta(pergunta, documentos_alvo)
        prompt = criar_prompt(pergunta_expandida, "conhecimento", documentos_alvo)

        resposta = _executar_query(prompt, documentos_alvo, knowledge_engine)

        fontes = [
            node.metadata.get("file_name", "")
            for node in resposta.source_nodes
            if node.metadata.get("file_name")
        ]

        encontrado = any(
            esperado in f or f.endswith(esperado)
            for f in fontes
        )

        if encontrado:
            ok += 1
            status = "OK   "
        else:
            falha += 1
            status = "FALHA"

        print(f"[{status}] {pergunta[:60]}")
        print(f"         Esperado:    {esperado}")
        print(f"         Recuperados: {', '.join(fontes[:5]) or 'nenhum'}")
        if modo_verbose and documentos_alvo:
            print(f"         Alvo RAG:    {', '.join(documentos_alvo)}")
        print()

    print(f"{'='*80}")
    print(f"Resultado: {ok} OK / {falha} FALHA de {len(pares)} perguntas")
    if pares:
        print(f"Taxa de acerto: {ok / len(pares) * 100:.1f}%")
    print(f"{'='*80}\n")


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

    documentos_alvo = identificar_documentos_alvo(pergunta)
    engine, tipo_base = escolher_engine(pergunta)

    print(f"\nBase escolhida: {tipo_base}")
    if documentos_alvo:
        print(f"Documentos alvo: {', '.join(documentos_alvo)}")

    pergunta_expandida = _expandir_pergunta(pergunta, documentos_alvo)
    prompt = criar_prompt(pergunta_expandida, tipo_base, documentos_alvo)

    if documentos_alvo and tipo_base == "conhecimento":
        resposta = _executar_query(prompt, documentos_alvo, knowledge_engine)
    else:
        resposta = engine.query(prompt)

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
