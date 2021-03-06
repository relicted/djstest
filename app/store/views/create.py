from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView

from app.store.forms.update import BookForm
from app.store.models import Book


class CreateBook(CreateView):
    form_class = BookForm
    template_name = 'store/book_form.html'
    model = Book
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous or not (user.is_manager or user.is_staff):
            messages.error(request, 'Only managers can visit edit page')
            return redirect('store:list')

        return super(CreateBook, self).dispatch(request, *args, **kwargs)
