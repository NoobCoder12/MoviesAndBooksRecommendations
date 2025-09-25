from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_info, name="api_info"),
    path("movies/", views.similar_movies, name="similar_movies"),
    path("books/", views.similar_books, name="similar_books"),
]
