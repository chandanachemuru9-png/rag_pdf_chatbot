import streamlit as st
import requests

st.title("PDF RAG Chatbot")

question = st.text_input("Ask a question")

if question:

    response = requests.get(
        "http://127.0.0.1:8000/ask",
        params={"q": question}
    )

    answer = response.json()["answer"]

    st.write(answer)