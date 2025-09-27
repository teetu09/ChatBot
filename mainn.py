Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# 🔑 Set your OpenAI API Key here
openai.api_key = "YOUR_OPENAI_API_KEY"

... # In-memory mood tracker (for demo)
... user_moods = []
... 
... @app.route("/chat", methods=["POST"])
... def chat():
...     data = request.json
...     user_message = data.get("message")
... 
...     # OpenAI prompt for empathetic responses
...     prompt = f"""
...     You are a friendly mental health buddy. Respond empathetically, provide
...     stress-relief tips, journaling prompts, or relaxation exercises. 
...     If the user says something dangerous (suicide thoughts), provide helpline info.
...     User says: "{user_message}"
...     """
... 
...     response = openai.Completion.create(
...         engine="text-davinci-003",
...         prompt=prompt,
...         max_tokens=150
...     )
... 
...     bot_message = response.choices[0].text.strip()
...     return jsonify({"reply": bot_message})
... 
... @app.route("/mood", methods=["POST"])
... def mood():
...     data = request.json
...     mood = data.get("mood")  # e.g., 1-10 scale
...     user_moods.append(mood)
...     return jsonify({"message": "Mood recorded!", "all_moods": user_moods})
... 
... @app.route("/mood", methods=["GET"])
... def get_mood():
...     return jsonify({"all_moods": user_moods})
... 
... if __name__ == "__main__":
...     app.run(debug=True)
