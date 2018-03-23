from django.db import models
from django.shortcuts import reverse

from app.store.models.fields import ISBNField
from app.store.models.author import Author


class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = ISBNField()
    price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField()
    authors = models.ManyToManyField(Author)

    publish_date = models.DateField(null=True)

    @staticmethod
    def get_absolute_url():
        return reverse('store:list')