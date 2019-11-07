from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['shortener.com']

SECRET_KEY = os.environ['URL_SHORTENER_SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['URL_SHORTENER_DB_NAME'],
        'USER': os.environ['URL_SHORTENER_DB_USER'],
        'PASSWORD': os.environ['URL_SHORTENER_DB_PASSWORD'],
        'HOST': os.environ['URL_SHORTENER_DB_HOST'],
        'PORT': os.environ['URL_SHORTENER_DB_PORT'],
    }
}
