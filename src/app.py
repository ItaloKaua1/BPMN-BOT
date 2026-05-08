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
    similarity_top_k=5
)

print("\nBPMN-BOT iniciado!")
print("Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Pergunta: ")

    if pergunta.lower() == "sair":
        break

    resposta = query_engine.query(pergunta)

    print("\nResposta:")
    print(resposta.response)

    print("\nFontes recuperadas:")

    for i, node in enumerate(resposta.source_nodes, start=1):
        dataset = node.metadata.get(
            "dataset",
            "dataset desconhecido"
        )

        print(f"\nFonte {i}: {dataset}")
        print(node.text[:500])
        print("---")

    print("\n")