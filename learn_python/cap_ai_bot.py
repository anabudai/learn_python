open_api_key=""

import os
from openai import OpenAI

client = OpenAI(
    api_key=open_api_key,
)

messages = []

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content" : message
        }
    )

    chat_completion = client.chat.completions.create( messages = messages, model="gpt-4o")
    response = chat_completion.choices[0].message.content
    response_message = {
        "role": "assistant",
        "content": response
    }
    messages.append(response_message)

    print(f"Jarvis: {response}")

if __name__ == "__main__":
    print("Jarvis: Hi, I am Jarvis. How may I help you?")
    while (user_input:=input("User: ")) != "quit":
        completion(user_input)