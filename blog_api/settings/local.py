from .base import *  # noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-(%+!_7&zkx9cd^zxfu9k-nlp0%1cjh0hzqhi(m-2zx7_leboqd"
SECRET_KEY = env("DJANGO_SECRET_KEY", default="%+!_7&zkx9cd^zxfu9k-nlp0%1cjh0hzqhi(m-2zx7_leboqd")

# generate a new key with: 
# import secrets print(secrets.token_urlsafe(50))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

