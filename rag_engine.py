from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import requests

model = SentenceTransformer("all-MiniLM-L6-v2")

def ask_question(question, history=[]):
    if not os.path.exists("db/vector_store.index") or not os.path.exists("db/chunks.npy"):
        return "❌ No PDF processed yet. Please upload a PDF first."

    index = faiss.read_index("db/vector_store.index")
    chunks = np.load("db/chunks.npy", allow_pickle=True)

    query_embedding = model.encode([question])
    distances, indices = index.search(np.array(query_embedding), k=3)

    threshold = 1.5
    if distances[0][0] > threshold:
        return "❌ This information is not found in the uploaded PDF."

    results = [chunks[i] for i in indices[0] if i < len(chunks)]
    context = "\n\n".join(results)

    history_text = ""
    for msg in history[-4:]:
        history_text += f"{msg['role'].capitalize()}: {msg['content']}\n"

    prompt = f"""You are a helpful assistant. Answer in 1-2 sentences only using the context below.

Context: {context}

{history_text}
User: {question}
Assistant:"""

    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral:latest",
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]