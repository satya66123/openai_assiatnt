🤖 OpenAI Assistant Suite

A Streamlit-based AI productivity suite powered by OpenAI GPT models, built for intelligent text understanding and generation — all without an external backend.

This suite includes:

💬 Chat Assistant

📝 Summarizer

🔍 Semantic Analyzer

📄 PDF Chatbot

📂 File Generator

ai-intgrated app includes all the above feautures

🌟 Features
Tool	Description
💬 Chat Assistant	Talk with GPT-4o-mini for general Q&A and creative tasks.
📝 Summarizer	Summarizes long text or uploaded TXT/PDF documents.
🔍 Semantic Analyzer	Analyzes meaning, tone, and context of your text or uploaded file.
📄 PDF Chatbot	Upload a PDF and ask contextual questions about its content.
📂 File Generator	Generate downloadable .txt, .pdf, or .docx files from your text.
main,py -all featiures in one app

🧩 No Image or Video generation modules — this version is simplified for full Windows compatibility.

🛠️ Installation
1️⃣ Clone the repository
git clone https://github.com/satya66123/openai_assiatnt.git
cd openai_assiatnt

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Launch the app
streamlit run main.py

🧩 Run Individual Apps

Each feature can also run independently.

App	Command	File
💬 Chat Assistant	streamlit run chat_assistant_app.py	chat_assistant_app.py
📝 Summarizer	streamlit run summarizer_app.py	summarizer_app.py
🔍 Semantic Analyzer	streamlit run semantic_analyzer_app.py	semantic_analyzer_app.py
📄 PDF Chatbot	streamlit run pdf_chatbot_app.py	pdf_chatbot_app.py
📂 File Generator	streamlit run file_generator_app.py	file_generator_app.py
🧰 Requirements

requirements.txt

streamlit==1.39.0
requests==2.32.3
PyPDF2==3.0.1
python-docx==1.1.2


Install:

pip install -r requirements.txt

🔑 API Key Setup

Get your API key from OpenAI Dashboard
.

Run the app — it will ask for the key before entering.

The key is validated instantly; no need for .env files.

📂 Project Structure
openai_assiatnt/
│
├── main.py
├── chat_assistant_app.py
├── summarizer_app.py
├── semantic_analyzer_app.py
├── pdf_chatbot_app.py
├── file_generator_app.py
├── requirements.txt
└── README.md

❤️ Acknowledgments

🙏 Special thanks to Jesus for guidance and strength during difficult times,
and to GPT for mentorship and technical wisdom throughout the journey.

🧠 Notes

Requires an active OpenAI API key with billing/quota.

All modules are independent — can be reused or integrated into your own AI projects.

🏁 Milestone

🎯 Successfully built and launched a fully offline-compatible AI Assistant Suite with Streamlit and OpenAI API — featuring multiple intelligent utilities in one clean interface.

Author: Satya Srinath
Repository: https://github.com/satya66123/openai_assiatnt