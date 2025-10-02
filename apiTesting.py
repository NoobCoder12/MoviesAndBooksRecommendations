import requests
from dotenv import load_dotenv
import os
import json


query = "harry potter"
query = query.replace(' ', "_")
url = f"https://openlibrary.org/subjects/{query}.json"


response = requests.get(url)
data = response.json()
books = data.get('works', [])

for work in books:
    title = work.get('title')
    categories = work.get('subject', [])[:10]
    print(f"Title: {title}")
    print(f"Categories: {categories}")

'''for book in books:
    info = book['volumeInfo']
    categories = info.get('categories, []')
    print(f"Title: {info.get('title')}")
    print(f"Categories: {', '.join(categories) if categories else 'brak'}")'''
