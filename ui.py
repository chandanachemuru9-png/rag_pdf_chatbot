import streamlit as st
import requests
import os
from ingest import process_pdf

# Page config
st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stChatMessage { border-radius: 12px; margin-bottom: 8px; }
    .upload-section {
        background: #1e2130;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
        border: 1px solid #2e3250;
    }
    h1 { color: #4CAF50 !important; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("## 📄 PDF RAG Chatbot")
st.markdown("*Upload a PDF and ask questions about it*")
st.divider()

# Upload section
with st.container():
    uploaded_file = st.file_uploader("📎 Upload your PDF", type="pdf")

    if uploaded_file is not None:
        file_path = os.path.join("data", uploaded_file.name)
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        col1, col2 = st.columns(2)
        with col1:
            st.success("✅ Uploaded")
        with col2:
            with st.spinner("Processing..."):
                process_pdf(file_path)
            st.success("✅ Processed")

st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
question = st.chat_input("💬 Ask a question about your PDF...")

if question:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Get answer
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                res = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={
                        "question": question,
                        "history": st.session_state.messages[:-1]
                    },
                    timeout=120
                )
                answer = res.json()["answer"]
            except Exception as e:
                answer = "❌ Backend not running. Start FastAPI first."

        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

# Clear chat button
if st.session_state.messages:
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()