from rag_code.load_documents import load_documents
from rag_code.split_documents import split_documents
from rag_code.vector_store import build_vector_store, load_vector_store
from rag_code.rag_pipeline import query_rag

def main():
    print("📄 Loading documents...")
    docs = load_documents()

    print(f"✅ Loaded {len(docs)} documents. Splitting into chunks...")
    chunks = split_documents(docs, chunk_size=500, chunk_overlap=50)

    print(f"✅ {len(chunks)} chunks created. Building or loading vector store...")
    
    # Build vector store for the first time
    vector_db = build_vector_store(chunks, model_name="all-MiniLM-L6-v2")

    # Or use this to load an existing one:
    # vector_db = load_vector_store("all-MiniLM-L6-v2")

    print("🤖 RAG System Ready. Ask a question (type 'exit' to quit):\n")
    while True:
        query = input("🔎 Your question: ")
        if query.lower() == "exit":
            print("👋 Exiting. Bye!")
            break

        answer = query_rag(vector_db, query)
        print("\n💬 Answer:")
        print(answer)
        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    main()
