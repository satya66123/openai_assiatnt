import streamlit as st
import requests
from PyPDF2 import PdfReader

st.set_page_config(page_title="PDF Chatbot", layout="wide")

if "api_key_valid" not in st.session_state:
    st.session_state.api_key_valid = False

if not st.session_state.api_key_valid:
    st.title("🔐 Enter your OpenAI API Key")
    api_key_input = st.text_input("OpenAI API Key", type="password")
    if st.button("Validate Key"):
        try:
            headers = {"Authorization": f"Bearer {api_key_input}"}
            resp = requests.get("https://api.openai.com/v1/models", headers=headers)
            if resp.status_code == 200:
                st.session_state.api_key = api_key_input
                st.session_state.api_key_valid = True
                st.success("✅ Key validated successfully!")
                st.rerun()
            else:
                st.error("❌ Invalid or expired API key.")
        except Exception as e:
            st.error(f"Connection error: {e}")
    st.stop()

api_key = st.session_state.api_key
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

st.header("📄 PDF Chatbot")
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_file:
    reader = PdfReader(uploaded_file)
    content = "".join([page.extract_text() for page in reader.pages])
    question = st.text_input("Ask a question about this PDF:")
    if st.button("Ask"):
        data = {"model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": f"PDF content:\n{content[:8000]}"},
                    {"role": "user", "content": question}
                ]}
        resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        if resp.status_code == 200:
            st.success(resp.json()["choices"][0]["message"]["content"])
        else:
            st.error(f"API Error: {resp.status_code}\n{resp.text}")
