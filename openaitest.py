import os
import openai

from config import OPENAI_API_KEY

# Set your OpenAI API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is set
if api_key is None:
    raise Exception("API key not found. Set the OPENAI_API_KEY environment variable.")

openai.api_key = OPENAI_API_KEY

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "write an email to my boss about resignation"
        },
        {
            "role": "user",
            "content": ""
        }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

print(response)
