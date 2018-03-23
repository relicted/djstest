from django.views.generic import ListView

from app.store.models import Book


class BookList(ListView):
    model = Book
    template_name = 'store/list.html'
    ordering = '-publish_date'
