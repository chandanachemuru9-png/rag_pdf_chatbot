from fastapi import FastAPI
from rag_engine import ask_question

app = FastAPI()

@app.get("/ask")
def ask(q: str):
    answer = ask_question(q)
    return {"question": q, "answer": answer}