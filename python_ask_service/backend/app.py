from python_ask_service.backend import create_app
import openai
from flask import request, jsonify
import os
from dotenv import load_dotenv

app = create_app()
load_dotenv()
client = openai.OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


@app.get("/ping")
def hello():
    return "pong!"


@app.post("/ask")
def ask_question():
    data = request.json
    question = data.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": question}]
        )
        answer = response.choices[0].message.content.strip()
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
