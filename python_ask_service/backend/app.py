# app.py

from python_ask_service.backend import create_app, db
from python_ask_service.backend.models import Question
import openai
from flask import request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()
app = create_app()

client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.get("/ping")
def hello():
    return "pong!"

@app.post("/ask")
def ask_question():
    data = request.json
    question_text = data.get("question")
    
    if not question_text:
        return jsonify({"error": "No question provided"}), 400
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": question_text}]
        )
        answer_text = response.choices[0].message.content.strip()

        new_question = Question(question_text=question_text, answer_text=answer_text)
        db.session.add(new_question)
        db.session.commit()

        return jsonify({"answer": answer_text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
