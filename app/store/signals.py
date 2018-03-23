import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from app.store.models import Book

logging.basicConfig(filename='test.log', level=logging.INFO,
                    format='%(asctime)s %(message)s')


@receiver(post_save, sender=Book)
def save(sender, instance, created, **kwargs):
    if created:
        logging.info(f'{instance} was CREATED')
        print('CREATED')
        return
    print('EDITED')

    logging.info(f'Book "{instance.title}" with id {instance.pk}'
                 f' was EDITED')


@receiver(post_delete, sender=Book)
def delete(sender, instance, **kwargs):
    logging.info(f'Book "{instance.title}" with id {instance.pk}'
                 f' was DELETED')
