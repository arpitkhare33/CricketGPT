import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
context = open("./cricket.txt", "r").read()

# Function to respond to a query using the context
def respond_to_query(query):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Use the provided content to answer questions."},
            {"role": "user", "content": f"Context: {context}"},
            {"role": "user", "content": f"Question: {query}"}
        ]
    )
    return response.choices[0].message.content


def chat():
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            print("Chatbot: Good Bye")
            break
        response = respond_to_query(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
    