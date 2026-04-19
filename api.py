from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any
from rag_engine import ask_question

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str
    history: List[Any] = []

@app.post("/ask")
def ask(request: AskRequest):
    answer = ask_question(request.question, request.history)
    return {"answer": answer}