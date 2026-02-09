from django.test import TestCase
from .forms import BookForm
from .models import Author
from django.utils import timezone


class BookFormTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name="Test", last_name="Author")

    def test_book_form_valid_data(self):
        form_data = {
            "title": "Django Test Book",
            "author": self.author.id,
            "price": 100000,
            "publication_date": timezone.now().date(),
            "summary": "Test summary",
        }
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())
