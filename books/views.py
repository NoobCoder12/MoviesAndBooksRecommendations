from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os


# Create your views here.
load_dotenv()

key = os.getenv("API_KEY")

def books_recommendations_search(request):
    return render(request, "books/search_book.html")


def get_books(request):
    query = request.GET.get('title')
    API_KEY = key
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "key": API_KEY,
        "maxResults": 10
    }

    response = requests.get(url, params=params)
    data = response.json()
    books = data.get('items', [])

    return render(request, 'books/books_found.html', {'books': books})
