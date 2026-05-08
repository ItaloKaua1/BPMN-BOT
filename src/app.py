from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings

from llama_index.llms.ollama import Ollama

from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# Configuração do modelo local
Settings.llm = Ollama(model="qwen2.5:1.5b", request_timeout=120)

# Configuração de embeddings
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Carrega documentos da pasta docs
documents = SimpleDirectoryReader("docs").load_data()

# Cria índice vetorial
index = VectorStoreIndex.from_documents(documents)

# Cria mecanismo de busca
query_engine = index.as_query_engine(
    similarity_top_k=5
)

print("BPMN-BOT iniciado!")
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

        arquivo = node.metadata.get(
            "file_name",
            "arquivo desconhecido"
        )

        pagina = node.metadata.get(
            "page_label",
            "página desconhecida"
        )

        print(f"\nFonte {i}: {arquivo} - página {pagina}")
        print(node.text[:500])
        print("---")

    print("\n")