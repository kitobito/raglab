import os
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

def load_documents(path="./documents"):
    all_docs = []
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(full_path)
        elif filename.endswith(".docx"):
            loader = Docx2txtLoader(full_path)
        elif filename.endswith(".txt"):
            loader = TextLoader(full_path)
        else:
            print(f"Unsupported file type: {filename}")
            continue
        all_docs.extend(loader.load())
    return all_docs
