# 📄 PDF RAG Chatbot

A conversational AI chatbot that lets you upload any PDF and ask questions about it. Built using Retrieval-Augmented Generation (RAG) with a fully local LLM — no API key required!

---

## 🚀 Features

- 📤 Upload any PDF file
- 🔍 Smart sentence-aware chunking with overlap for better context retrieval
- 🧠 Local LLM (Mistral via Ollama) — runs completely offline
- 💬 Multi-turn chat with conversation history
- ❌ Detects when a question is not related to the PDF
- 🎨 Clean chat-style UI built with Streamlit

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Embeddings | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Vector Store | FAISS |
| LLM | Mistral (via Ollama) |
| PDF Parsing | PyPDF2 |
| Chunking | NLTK (sentence-aware) |

---

## 📁 Project Structure

```
RAG_PDF_PROJECT/
├── api.py            # FastAPI backend
├── ui.py             # Streamlit frontend
├── rag_engine.py     # RAG logic (retrieval + LLM)
├── ingest.py         # PDF processing & vector DB creation
├── requirements.txt  # Python dependencies
├── data/             # Uploaded PDFs
└── db/               # FAISS vector store
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/chandanachemuru9-png/rag_pdf_chatbot.git
cd rag_pdf_chatbot
```

### 2. Create a virtual environment
```bash
python -m venv rag_env
rag_env\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Ollama & pull Mistral
- Download Ollama from [ollama.com](https://ollama.com)
```bash
ollama pull mistral
```

---

## ▶️ Running the App

Open **3 terminals** and run:

**Terminal 1 — Ollama:**
```bash
ollama serve
```

**Terminal 2 — FastAPI backend:**
```bash
uvicorn api:app --reload --port 8000
```

**Terminal 3 — Streamlit UI:**
```bash
streamlit run ui.py
```

Then open your browser at `http://localhost:8501`

---

## 💡 How It Works

1. User uploads a PDF
2. PDF is parsed and split into sentence-aware chunks with overlap
3. Chunks are embedded using Sentence Transformers and stored in FAISS
4. When a question is asked, the most relevant chunks are retrieved
5. Retrieved context + chat history is sent to Mistral LLM
6. Mistral generates a precise, context-based answer

---

## 👩‍💻 Developer

**Chandana** — B.Tech CSE (AI & ML), Sri Venkateswara College of Engineering, Tirupati
