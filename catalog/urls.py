from django.urls import path
from .views import BookListView, BookDetailView, book_create_view, author_create_view

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path("book/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("book/add/", book_create_view, name="book-add"),
    path("author/add/", author_create_view, name="author-add")
]
