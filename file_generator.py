import streamlit as st
import tempfile

st.set_page_config(page_title="File Generator", layout="wide")

st.header("📂 File Generator (txt/docx/pdf)")
content = st.text_area("Enter text content:")
file_type = st.selectbox("Select output format:", ["txt", "pdf", "docx"])

if st.button("Generate File"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp:
        tmp.write(content.encode("utf-8"))
        st.download_button("Download File", tmp.name, file_name=f"output.{file_type}")
