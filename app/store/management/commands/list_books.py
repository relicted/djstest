from django.core.management.base import BaseCommand
from app.store.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '--order',
            dest='order',
            help='List books',
            default='',
        )

    def handle(self, *args, **options):
        # ...
        sort = options.get('order', '').lower()
        qs = Book.objects.all()

        if sort == 'desc':
            for book in qs.order_by('-publish_date'):
                self.stdout.write(f'{book.title} | {book.publish_date}')
        elif sort == 'asc':
            for book in qs.order_by('publish_date'):
                self.stdout.write(f'{book.title} | {book.publish_date}')
        else:
            self.stdout.write('--order arg takes values "asc" and "desc"')

        if not sort:
            for book in qs.order_by('publish_date'):
                self.stdout.write(f'{book.title} | {book.publish_date}')