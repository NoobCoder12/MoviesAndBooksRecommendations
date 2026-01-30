from django.shortcuts import render
from apps.books.books_additional_files.books_recommender import fetch_best_book_category, fetch_books_by_category, fetch_cover_image
from django.http import JsonResponse


# Create your views here.


def books_recommendations_search(request):
    return render(request, "books/search_book.html")


def get_books(request):
    query = request.GET.get('title')
    if not query:
        return render(request, "books/search_book.html", {'error': 'no title provided'})
    
    category = fetch_best_book_category(query)
    books = fetch_books_by_category(category)
    for book in books:
        cover_id = book.get('cover_id')
        book['cover_url'] = fetch_cover_image(cover_id)

    return render(request, 'books/books_found.html', {'books': books})