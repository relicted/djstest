from django.contrib import admin

from app.store.models import Book, Author

admin.site.register(Author)
admin.site.register(Book)