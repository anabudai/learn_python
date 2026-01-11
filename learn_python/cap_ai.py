# open_api_key="practice_1"
# open_api_secret="take from Open API Dashboard"

from openai import OpenAI
client = OpenAI(api_key=open_api_secret)

response = client.responses.create(
    model="gpt-5.2",
    messages=[
    ]
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)

