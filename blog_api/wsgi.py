"""
WSGI config for blog_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# TODO: change this to production settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_api.settings.local") # new

application = get_wsgi_application()
