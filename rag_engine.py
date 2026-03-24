import warnings
warnings.filterwarnings("ignore")

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import ollama

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# load vector database
index = faiss.read_index("vector_store.index")

# load stored text chunks
chunks = np.load("chunks.npy", allow_pickle=True)


def ask_question(question):

    question_embedding = model.encode([question])

    D, I = index.search(np.array(question_embedding), k=3)

    context = ""
    threshold = 1.2

    for dist, idx in zip(D[0], I[0]):
        if dist < threshold:
            context += chunks[idx] + "\n"

    if context.strip() == "":
        return "I could not find the answer in the document."

    prompt = f"""
You are a document assistant.

Answer the question ONLY using the information provided in the context.

If the answer is NOT present in the context, reply with:
"I could not find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]