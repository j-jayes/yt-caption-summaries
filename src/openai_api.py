import openai
from .config import config

OPENAI_API_KEY = config["openai"]["key"]

openai.api_key = OPENAI_API_KEY

def summarize_text(text):
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are an expert at summarizing complex thoughts."},
                    {"role": "user", "content": f"Summarise the following text: {text}"}
            ]
        )

    return response.choices[0].message.content.strip()
