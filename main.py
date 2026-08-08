import requests
from dotenv import load_dotenv
import os

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

print(response.json())