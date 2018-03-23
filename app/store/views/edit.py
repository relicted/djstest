from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from app.store.forms.update import BookForm
from app.store.models import Book


class EditBook(UpdateView):

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous or not (user.is_manager or user.is_staff):
            messages.error(request, 'Only managers can visit edit page')
            return redirect('store:list')
        return super(EditBook, self).dispatch(request, *args, **kwargs)

    form_class = BookForm
    template_name = 'store/book_form.html'
    model = Book


class DeleteBook(DeleteView):
    model = Book

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_anonymous or not (user.is_manager or user.is_staff):
            messages.error(request, 'Only managers can delete books')
            return redirect('store:list')
        return super(DeleteBook, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        messages.success(self.request, 'Book was deleted!')
        return reverse_lazy('store:list')
