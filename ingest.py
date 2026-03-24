from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

print("Starting ingestion...")

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# read pdf
reader = PdfReader("data/test.pdf")

text = ""
for page in reader.pages:
    text += page.extract_text()

print("PDF loaded")

# split into chunks
chunk_size = 500
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

print("Chunks:", len(chunks))

# create embeddings
embeddings = model.encode(chunks)

# create vector index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# save vector database
faiss.write_index(index, "vector_store.index")

# save chunks
np.save("chunks.npy", chunks)

print("Vector database created successfully")