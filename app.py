from openai import OpenAI

client = OpenAI(
    # api_key
)
CONVERSATION = []
def get_gpt_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }
    CONVERSATION.append(message)
    response = client.chat.completions.create(
        messages = CONVERSATION,
        model = "gpt-3.5-turbo"
    )
    response_content = response.choices[0].message.content
    CONVERSATION.append(response.choices[0].message)
    return response_content


def chat():
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            print("Chatbot: Good Bye")
            break
        response = get_gpt_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
