from flask import Flask, jsonify, request
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
context = open("./cricket.txt", "r").read()
app = Flask(__name__)
CORS(app)  # Allow Cross-Origin requests from frontend

# Example route
@app.route('/api/message', methods=['POST'])
def get_message():
    data = request.get_json()  # Get data from the frontend request
    query = data.get('message')
    print(query)
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Use the provided content to answer questions."},
            {"role": "user", "content": f"Context: {context}"},
            {"role": "user", "content": f"Question: {query}"}
        ]
    )
    print(response)
    return {"response": response.choices[0].message.content}

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
