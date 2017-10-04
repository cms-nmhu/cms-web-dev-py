from .base import *

import os
from django.core.exceptions import ImproperlyConfigured


# Handling Key Import Errors
def get_env_variable(var_name):
	""" Get the environment variable or return exception """
	try:
		return os.environ[var_name]
	except KeyError:
		error_msg = "Set the %s environment variable" % var_name
		raise ImproperlyConfigured(error_msg)

# Get ENV VARIABLES key
ENV_ROLE = get_env_variable('ENV_ROLE')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'cswebDB',
			'USER': 'postgres',
			'PASSWORD': get_env_variable('DB_PASS'),
			'HOST': 'localhost',
			'PORT': '5432'
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, 'static')
]

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "www", "static")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
