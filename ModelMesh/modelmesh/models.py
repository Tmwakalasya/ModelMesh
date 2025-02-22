import os
from dotenv import load_dotenv
import requests

API_KEYS = {
    "GPT-4": os.getenv("OPENAI_API_KEY"),
    "Claude": os.getenv("anthropic_api_key"),
    "Gemini": os.getenv("GOOGLE_API_KEY")
}

API_URLS = {
    "GPT-4": "https://api.openai.com/v1/completions",
    "Gemini": "https://api.google.com/gemini/v1/query",
    "Claude": "https://api.anthropic.com/v1/completions"
}


def call_model(api_name, prompt):
    if api_name not in API_KEYS:
        print(f"API key not found {{API_KEYS}}")

    url = API_URLS[api_name]
    headers = {"Authentication": f"Bearer {API_KEYS[api_name]}",
               "Content-Type": "application/json"}

    data = {
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


