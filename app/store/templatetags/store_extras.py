from django import template
from django.shortcuts import reverse


register = template.Library()


@register.simple_tag
def admin_edit(obj):
    return reverse('admin:store_book_change', kwargs={'object_id': obj.id})
