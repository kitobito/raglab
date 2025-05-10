from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings

def build_vector_store(chunks, model_name="all-MiniLM-L6-v2"):
    embeddings = SentenceTransformerEmbeddings(model_name=model_name)
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(f"vectorstore_{model_name}")
    return db

def load_vector_store(model_name="all-MiniLM-L6-v2"):
    embeddings = SentenceTransformerEmbeddings(model_name=model_name)
    return FAISS.load_local(f"vectorstore_{model_name}", embeddings)
