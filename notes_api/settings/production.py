from .base import *

DEBUG = True # make debug for development

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['notes.girlsgoit.org', 'notes-api.girlsgoit.org', 'ggit-notes-api.azurewebsites.net', 'localhost']
CORS_ORIGIN_WHITELIST = ('notes.girlsgoit.org', 'notes-api.girlsgoit.org', 'ggit-notes-api.azurewebsites.net')
CSRF_TRUSTED_ORIGINS = ['notes.girlsgoit.org', 'notes-api.girlsgoit.org']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USERNAME'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ.get('DB_POST', 5432),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}
