"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os.path, sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
sys.path.append(os.path.dirname(os.getcwd()))
#sys.path.append("/Users/uzairpachhapure/Desktop/desktop/csu/Assignments/sem 2/big data/project/sports_analysis_website/beyond_the_numbers_project")
os.environ["PATH"] += os.getcwd()
import constants
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^uy-t9*hj_i1=msi%o!8klek0mz7x_951@gyp@g%zn7s6b$!py"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','sports-analysis.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    "home",
    "movies",
    "rest_framework",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ['templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
       'ENGINE': constants.ENGINE,
       'OPTIONS': {
                'options': '-c search_path=public'
            },
       'NAME': constants.DATABASE_NAME, #Database Name
       'USER': constants.POSTGRES_USER, #Your Postgresql user
       'PASSWORD': constants.POSTGRES_PASSWORD, #Your Postgresql password
       'HOST': constants.POSTGRES_HOST,
       'PORT': constants.POSTGRES_PORT,},
    'sports_analysis':{
       'ENGINE': constants.ENGINE,
       'OPTIONS': {
                'options': '-c search_path=raw_tables'
            },
       'NAME': constants.DATABASE_NAME, #Database Name
       'USER': constants.POSTGRES_USER, #Your Postgresql user
       'PASSWORD': constants.POSTGRES_PASSWORD, #Your Postgresql password
       'HOST': constants.POSTGRES_HOST,
       'PORT': constants.POSTGRES_PORT
    },
    'movies':{
       'ENGINE': constants.ENGINE,
       'OPTIONS': {
                'options': '-c search_path=movies'
            },
       'NAME': constants.DATABASE_NAME, #Database Name
       'USER': constants.POSTGRES_USER, #Your Postgresql user
       'PASSWORD': constants.POSTGRES_PASSWORD, #Your Postgresql password
       'HOST': constants.POSTGRES_HOST,
       'PORT': constants.POSTGRES_PORT
    }
    }
DATABASE_ROUTERS = ['routers.db_routers.MoviesRouter']
ATOMIC_REQUESTS = "True"

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / 'static'

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
#]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
