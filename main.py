import streamlit as st
import requests
import tempfile
from PyPDF2 import PdfReader

st.set_page_config(page_title="AI Suite", layout="wide")

# ----------------- API KEY VALIDATION -----------------
if "api_key_valid" not in st.session_state:
    st.session_state.api_key_valid = False

if not st.session_state.api_key_valid:
    st.title("🔐 Enter your OpenAI API Key")
    api_key_input = st.text_input("OpenAI API Key", type="password")

    if st.button("Validate Key"):
        if not api_key_input.startswith("sk-"):
            st.error("❌ API Key must start with 'sk-'.")
        else:
            try:
                headers_test = {"Authorization": f"Bearer {api_key_input}"}
                resp = requests.get("https://api.openai.com/v1/models", headers=headers_test)
                if resp.status_code == 200:
                    st.session_state.api_key = api_key_input
                    st.session_state.api_key_valid = True
                    st.success("✅ API Key validated successfully!")
                    st.rerun()
                elif resp.status_code == 401:
                    st.error("❌ Unauthorized — your API key is invalid or expired.")
                else:
                    st.error(f"⚠️ Unexpected response: {resp.status_code}\n{resp.text}")
            except Exception as e:
                st.error(f"❌ Connection error:\n{e}")
    st.stop()

api_key = st.session_state.api_key
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

# ----------------- Sidebar Navigation -----------------
st.sidebar.title("🧠 AI Suite")
page = st.sidebar.radio(
    "Select Feature",
    ["Chat Assistant", "Summarizer", "Semantic Analyzer", "PDF Chatbot", "File Generator"]
)

# ----------------- Chat Assistant -----------------
if page == "Chat Assistant":
    st.header("💬 Chat Assistant")
    prompt = st.text_area("Ask anything:")
    if st.button("Send"):
        if prompt.strip():
            data = {
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
            if response.status_code == 200:
                msg = response.json()["choices"][0]["message"]["content"]
                st.success(msg)
            else:
                st.error(f"API Error: {response.status_code}\n{response.text}")

# ----------------- Summarizer -----------------
elif page == "Summarizer":
    st.header("📝 Text / File Summarizer")
    text_input = st.text_area("Enter text to summarize:")
    uploaded_file = st.file_uploader("Or upload a file (txt/pdf):", type=["txt", "pdf"])

    content = ""
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            pdf_reader = PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                content += page.extract_text()
        elif uploaded_file.type == "text/plain":
            content = uploaded_file.read().decode("utf-8")
        else:
            st.warning("Unsupported file type. Use txt/pdf.")

    final_text = text_input or content
    if st.button("Summarize"):
        if final_text.strip():
            data = {
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": f"Summarize this:\n{final_text}"}]
            }
            resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
            if resp.status_code == 200:
                st.success(resp.json()["choices"][0]["message"]["content"])
            else:
                st.error(f"API Error: {resp.status_code}\n{resp.text}")

# ----------------- Semantic Analyzer -----------------
elif page == "Semantic Analyzer":
    st.header("🔍 Semantic Analyzer")
    text_input = st.text_area("Enter text to analyze:")
    uploaded_file = st.file_uploader("Or upload a file (txt/pdf):", type=["txt", "pdf"])
    content = ""
    if uploaded_file:
        if uploaded_file.type == "application/pdf":
            pdf_reader = PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                content += page.extract_text()
        else:
            content = uploaded_file.read().decode("utf-8")

    final_text = text_input or content
    if st.button("Analyze Semantics"):
        if final_text.strip():
            data = {
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": f"Provide semantic analysis:\n{final_text}"}]
            }
            resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
            if resp.status_code == 200:
                st.success(resp.json()["choices"][0]["message"]["content"])
            else:
                st.error(f"API Error: {resp.status_code}\n{resp.text}")

# ----------------- PDF Chatbot -----------------
elif page == "PDF Chatbot":
    st.header("📄 Chat with PDF")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
    if uploaded_file:
        pdf_reader = PdfReader(uploaded_file)
        content = "".join([page.extract_text() for page in pdf_reader.pages])
        question = st.text_input("Ask a question about this PDF:")
        if st.button("Ask"):
            data = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": f"PDF content:\n{content[:8000]}"},
                    {"role": "user", "content": question}
                ]
            }
            resp = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
            if resp.status_code == 200:
                st.success(resp.json()["choices"][0]["message"]["content"])
            else:
                st.error(f"API Error: {resp.status_code}\n{resp.text}")

# ----------------- File Generator -----------------
elif page == "File Generator":
    st.header("📂 File Generator (txt/docx/pdf)")
    content = st.text_area("Enter text content:")
    file_type = st.selectbox("Select output format:", ["txt", "pdf", "docx"])
    if st.button("Generate File"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp:
            tmp.write(content.encode("utf-8"))
            st.download_button("Download File", tmp.name, file_name=f"output.{file_type}")
