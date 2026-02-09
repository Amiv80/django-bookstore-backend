from django import forms
from .models import Book, Author
from django.utils import timezone


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "price", "publication_date", "summary"]

        def clean_price(self):
            price = self.cleaned_data.get("price")
            if price is not None and price <= 0:
                raise forms.ValidationError(
                    "قیمت نمی‌تواند خالی باشد. همجنین باید بزرگتر از صفر باشد"
                )
            return price

    def clean(self):
        cleaned_data = super().clean()
        publication_date = cleaned_data.get("publication_date")

        if publication_date and publication_date > timezone.now().date():
            raise forms.ValidationError("تاریخ انتشار نمی‌تواند در آینده باشد.")

        return cleaned_data


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "date_of_birth"]
