from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def similar_movies(request):
    query = request.GET.get('title', '')
    movies = [
        {'title': 'Inception', 'year': 2010},
        {'title': 'Interstellar', 'year': 2010},
        {'title': 'Tenet', 'year': 2010},
    ]

    return Response({
        'results': movies
    })


def api_info(request):
    return render(request, 'api_info.html')


@api_view(['GET'])
def similar_books(request):
    query = request.GET.get('title', '')
    books = [
        {'title': 'Harry Potter', 'year': 2010},
        {'title': 'Lord of the Rings', 'year': 2010},
        {'title': 'The Witcher', 'year': 2010},
    ]

    return Response({
        'results': books
    })
