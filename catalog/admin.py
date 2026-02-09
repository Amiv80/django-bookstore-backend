from django.contrib import admin
from .models import Author, Book


# Customize the Django admin site header, title and index title
admin.site.site_header = "Bookstore Administration"
admin.site.site_title = "Bookstore Admin"
admin.site.index_title = "Site Administration"


class BookInline(admin.TabularInline):
	model = Book
	extra = 0
	fields = ("title", "price", "publication_date")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "date_of_birth")
	search_fields = ("first_name", "last_name")
	inlines = (BookInline,)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ("title", "author", "price", "publication_date")
	list_filter = ("publication_date", "author")
	search_fields = ("title", "author__first_name", "author__last_name")
	date_hierarchy = "publication_date"
	ordering = ("-publication_date",)
	list_editable = ("price",)