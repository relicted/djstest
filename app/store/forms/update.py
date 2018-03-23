from django import forms

from app.store.models import Book
from django.contrib.admin.widgets import AdminDateWidget


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'authors', 'description', 'isbn', 'price',
                  'publish_date')
        widgets = {
            'publish_date': AdminDateWidget
        }
