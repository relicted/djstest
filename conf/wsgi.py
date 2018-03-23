"""
WSGI config for djstest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from conf.env import SETTINGS_FILE

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_FILE)

application = get_wsgi_application()
