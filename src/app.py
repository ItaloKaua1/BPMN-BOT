from llama_index.core import VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from preparedata import carregar_documentos_csv

Settings.llm = Ollama(
    model="qwen2.5:1.5b",
    request_timeout=120
)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Carregando documentos dos CSVs...")
documents = carregar_documentos_csv()

print(f"Total de documentos carregados: {len(documents)}")

print("Criando índice vetorial...")
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(
    similarity_top_k=3
)

print("\nBPMN-BOT iniciado!")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Pergunta: ")

    if pergunta.lower() == "sair":
        break

    prompt = f"""
        Você é o BPMN-BOT, um assistente especializado em extensões BPMN.

        Use SOMENTE as fontes recuperadas da base de conhecimento.

        Regras obrigatórias:
        1. Não invente relações entre publicações.
        2. Não diga que uma publicação trata de segurança, processos sensíveis, privacidade ou risco se isso não estiver explicitamente no título, domínio, área de aplicação ou descrição recuperada.
        3. Se houver uma publicação claramente relacionada, cite o título dela.
        4. Se houver apenas indícios, diga que são apenas indícios.
        5. Se as fontes recuperadas não forem suficientes, diga que a base atual não permite confirmar.
        6. Responda em português.
        7. Seja objetivo.
        8. Nunca invente nomes de extensões BPMN.
        9. Nunca crie publicações inexistentes.
        10. Se não tiver certeza, diga explicitamente que não há evidência suficiente.

        Pergunta do usuário:
        {pergunta}
        """

    resposta = query_engine.query(prompt)

    print("\nResposta:")
    print(resposta.response)

    print("\nFontes recuperadas:")

    for i, node in enumerate(resposta.source_nodes, start=1):
        dataset = node.metadata.get(
            "dataset",
            "dataset desconhecido"
        )

        print(f"\nFonte {i}: {dataset}")
        print(node.text[:300])
        print("---")

    print("\n")