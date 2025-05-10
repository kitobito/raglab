
# 📚 CSAI 422: RAG System - Lab 6

## 👨‍💻 Author
- **Name**: Karim Wael
- **Course**: CSAI 422 - Laboratory Assignment 6
- **Lab Date**: April 7, 2025
- **Due Date**: April 21, 2025

---

## ⚙️ Setup Instructions

### 1. Clone or download this repository:
```bash
git clone https://github.com/kitobito/raglab.git
cd rag-assignment
```

### 2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows PowerShell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.env\Scripts\Activate.ps1
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:
```bash
pip install langchain faiss-cpu sentence-transformers python-docx PyPDF2 openai python-dotenv
```

### 4. Add your OpenAI key to `.env`:
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_key_here
```

### 5. Add sample documents:
Put 5–10 PDF, DOCX, or TXT files inside the `documents/` folder.

### 6. Run the system:
```bash
python main.py
```

---

## 🧠 RAG System Architecture

Our Retrieval-Augmented Generation (RAG) pipeline consists of the following components:

1. **Document Loader** (`load_documents.py`)  
   Loads PDF, DOCX, and TXT files from the `documents/` folder.

2. **Text Splitter** (`split_documents.py`)  
   Splits each document into overlapping text chunks using RecursiveCharacterTextSplitter.

3. **Embedding Generator** (`vector_store.py`)  
   Uses Sentence Transformers (`all-MiniLM-L6-v2`) to embed the chunks.

4. **Vector Store**  
   FAISS is used to store embeddings locally for fast retrieval.

5. **Retrievers** (`retrieval.py`)  
   - Basic similarity search
   - MMR (Maximum Marginal Relevance)

6. **Prompt Engineering** (`rag_prompt.py`)  
   Custom prompts are built using retrieved chunks as context.

7. **RAG Pipeline** (`rag_pipeline.py`)  
   Retrieves chunks, builds prompts, and calls OpenAI LLM (`gpt-3.5-turbo`).

---

## 🔬 Experimental Results: Retrieval Strategy Comparison

| Retrieval Strategy | Top-K | Response Quality | Diversity | Speed |
|--------------------|-------|------------------|----------|--------|
| Basic Similarity   | 3     | Good             | Low      | Fast   |
| MMR Search         | 5     | Very Good        | High     | Medium |

---

## 📊 Evaluation Metrics

We evaluated the retrieval component with dummy queries and labeled expectations:

| Metric      | Basic Similarity | MMR Retrieval |
|-------------|------------------|---------------|
| Precision   | 0.67             | 0.71          |
| Recall      | 0.62             | 0.76          |
| F1 Score    | 0.64             | 0.73          |

---

## ✅ Strengths and Weaknesses

### ✅ Strengths:
- Local FAISS vector store enables fast, offline retrieval.
- Modular codebase is easy to extend with other models or APIs.
- MMR search improves information diversity for complex queries.

### ⚠️ Weaknesses:
- Evaluation was manual and small-scale.
- Handling of long documents can still be improved.
- Only one embedding model used in production.

---

## 🚧 Challenges Faced

| Challenge | Solution |
|----------|----------|
| `Activate.ps1 cannot be loaded` error | Used `Set-ExecutionPolicy Bypass` in PowerShell |
| `ModuleNotFoundError: langchain` | Ensured virtual environment was activated before installing dependencies |
| Limited document dataset | Collected additional AI documents from arXiv and Wikipedia |
| Long prompts hitting token limits | Limited number of chunks used in prompt context |

---

## 📁 Project Structure

```
rag-assignment/
├── documents/                 # Corpus files (PDF, DOCX, TXT)
├── rag_code/
│   ├── load_documents.py
│   ├── split_documents.py
│   ├── vector_store.py
│   ├── retrieval.py
│   ├── rag_prompt.py
│   ├── rag_pipeline.py
│   └── evaluation.py
├── main.py
├── .env
└── README.md
```

---


