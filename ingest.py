from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from PyPDF2 import PdfReader
import os
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

model = SentenceTransformer("all-MiniLM-L6-v2")

def process_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    # ✅ Sentence-aware chunking
    sentences = nltk.sent_tokenize(text)

    # ✅ Chunk overlap - each chunk shares 2 sentences with the next
    chunks = []
    i = 0
    current_chunk = ""

    while i < len(sentences):
        current_chunk = ""
        j = i
        while j < len(sentences) and len(current_chunk) + len(sentences[j]) <= 500:
            current_chunk += " " + sentences[j]
            j += 1
        if current_chunk:
            chunks.append(current_chunk.strip())
        # Move forward but overlap by 2 sentences
        i = max(i + 1, j - 2)

    print("Chunks:", len(chunks))

    embeddings = model.encode(chunks)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    os.makedirs("db", exist_ok=True)
    faiss.write_index(index, "db/vector_store.index")
    np.save("db/chunks.npy", chunks)

    print("✅ Vector DB created with smart chunking + overlap")