from flask import Flask, render_template, request, jsonify
import PyPDF2
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv("../LangChain/.env")
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant",
    temperature=0.7
)
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an expert HR consultant. Analyze the resume and provide:

## Overall Score
Score out of 10 with brief reason.

## Key Strengths
4-5 specific strengths.

## Areas for Improvement
4-5 specific improvements.

## Skills Found
All technical and soft skills.

## Best Job Roles
5 best matching roles.

## Professional Summary
One powerful sentence.

Be specific and professional."""),
    ("human", "Analyze this resume:\n\n{resume_text}")
])
chain = prompt | llm | StrOutputParser()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"})
    
    file = request.files["resume"]
    pdf_reader = PyPDF2.PdfReader(file)
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()
    
    result = chain.invoke({"resume_text": resume_text})
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)