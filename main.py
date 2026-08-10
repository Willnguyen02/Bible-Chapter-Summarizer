import requests
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.markdown import Markdown
from src.config import base_url, model
from openai import OpenAI

load_dotenv()

querystring = {
    "book_id":"1",
    "chapter_num":"2"
}

headers = {
	"x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
	"x-rapidapi-host": os.getenv("RAPIDAPI_HOST"),
	"Content-Type": "application/json"
}

response = requests.get(os.getenv("ENDPOINT"), headers=headers, params=querystring)

#print(response.json())






client = OpenAI(
    base_url=base_url,
    api_key="not-needed"  
)

result = client.chat.completions.create(
    model=model,  # get this from /v1/models or the LM Studio UI
    messages=[
        {"role": "system", "content": f"You are a helpful catholic teacher. Today's chapter: {response.json()}."},
        {"role": "user", "content": f"Summarize this bible chapter, main take away, and key points: {response.json()}"}
    ]
)

console = Console()
console.print(Markdown(result.choices[0].message.content))
#print(result.choices[0].message.content)