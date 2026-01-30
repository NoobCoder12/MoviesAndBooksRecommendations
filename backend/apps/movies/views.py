from django.shortcuts import render

# Create your views here.


def movies_recommendations_search(request):
    return render(request, "movies/search_movie.html")
