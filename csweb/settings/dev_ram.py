from .base import *



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']#'m-sqy&6@h)hb@y3ci_$5ukr8!-$4cjed9#bbc%q$yg55usokic'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# No database required for project.

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
# 			'NAME': 'cmswebdb',
# 			'USER': os.environ['DB_USER'],
# 			'PASSWORD': '1',
# 			'HOST': 'localhost',
# 			'PORT': '5432'
#     }
# }

