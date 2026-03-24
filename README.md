# 📄 RAG PDF Chatbot

## 🚀 Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot that answers questions strictly from a PDF document.

It uses FAISS for vector search and a local LLM (Mistral via Ollama) for generating answers.

---

## 🧠 Features
- Ask questions from PDF
- Answers only from document content
- Semantic search using FAISS
- Local LLM (Ollama)
- FastAPI backend
- Streamlit UI

---

## 🛠 Tech Stack
- Python
- Sentence Transformers
- FAISS
- Ollama (Mistral)
- FastAPI
- Streamlit

---

## ⚙️ Setup Instructions

### 1. Clone repository
git clone https://github.com/chandanachemuru9-png/rag_pdf_chatbot.git

cd rag_pdf_chatbot

---

### 2. Install dependencies
pip install -r requirements.txt

---

### 3. Run ingestion
python ingest.py

---

### 4. Start backend API
uvicorn api:app --reload

---

### 5. Run UI
streamlit run ui.py

---

## 📌 How it works
1. Extract text from PDF  
2. Split into chunks  
3. Convert to embeddings  
4. Store in FAISS index  
5. Retrieve relevant chunks  
6. Generate answer using LLM  

---

## ⚠️ Important
If answer is not in PDF → chatbot will say:
"I could not find the answer in the document."

---

## 📷 Demo
(Add screenshot here later)

---

## 💡 Future Improvements
- Better chunking strategy
- Add PDF upload feature
- Improve retrieval accuracy
- Deploy online
