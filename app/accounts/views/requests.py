from django.views.generic import ListView
from app.accounts.models import WebRequest


class RequestsList(ListView):
    template_name = 'accounts/requests.html'

    def get_queryset(self):
        return WebRequest.objects.order_by('-time')[:10]
