from django.urls import path
from . import views


app_name = "books"

urlpatterns = [
    path("", views.books_recommendations_search,
         name="books_recommendations_search"),
    path("found/", views.get_books, name="get_books")
]
