from openai import OpenAI
from dotenv import load_dotenv
import config

load_dotenv()
client = OpenAI()

def ask_openai(input):
    return client.responses.create(
        model=config.OPENAI_MODEL,
        input=input
    ).output_text
