from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
from .forms import BookForm, AuthorForm
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "catalog/home.html"
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "catalog/book_detail.html"
    context_object_name = "book"


@staff_member_required
def book_create_view(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = BookForm()

    return render(request, "catalog/book_form.html", {"form": form})


@staff_member_required
def author_create_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AuthorForm()

    return render(request, "catalog/author_form.html", {"form": form})
