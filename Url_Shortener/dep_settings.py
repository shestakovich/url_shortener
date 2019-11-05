from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['shortener.com']

SECRET_KEY = '7*7^ll$8c0rf1_vf5y==zc-d&qhae*tw=7=*_fk=uy7jt1^@)w'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'user_name',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
