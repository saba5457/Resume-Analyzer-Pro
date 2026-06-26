# 📄 Resume Analyzer Pro

An AI-powered resume analysis web application built with Flask + LangChain + Groq API.

## ✨ Features
- Upload PDF resume and get instant analysis
- Overall score out of 10
- Key strengths identification
- Areas for improvement
- Skills extraction
- Best matching job roles
- Professional summary generation

## 🛠️ Tech Stack
- **Backend:** Python + Flask
- **AI:** LangChain + Groq API (llama-3.1-8b-instant)
- **Frontend:** HTML + CSS + JavaScript
- **PDF Processing:** PyPDF2

## 🚀 How to Run Locally
1. Clone the repository
2. Install dependencies: pip install -r requirements.txt
3. Add your GROQ_API_KEY in .env file: GROQ_API_KEY=your_key_here
4. Run the app: python app.py
5. Open browser: http://127.0.0.1:5000

## 📁 Project Structure
ResumeAnalyzer/
├── app.py           → Flask backend + AI logic
├── requirements.txt → Dependencies
├── templates/
│   └── index.html   → Frontend UI
└── .env             → API key (not shared)

## 👩‍💻 Built By
Saba Yasmeen — AI Developer
