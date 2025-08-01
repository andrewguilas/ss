from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def ask_openai(input):
    return client.responses.create(
        model="gpt-4.1-nano",
        input=input
    ).output_text
