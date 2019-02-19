# -*- coding: utf-8 -*-
"""
Django settings for qdc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG404 = True

TEMPLATE_DEBUG = DEBUG

# SECURITY WARNING: don't run with "is testing" in production
IS_TESTING = True

ALLOWED_HOSTS = ['localhost']

SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 3600

# Application definition

INSTALLED_APPS = (
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_jenkins',
    'simple_history',
    'jsonrpc_requests',
    'solo',
    'fixture_magic'
)

PROJECT_APPS = (
    'quiz',
    'patient',
    'custom_user',
    'experiment',
    'survey',
    'export',
    'configuration'
)

PROJECT_TAGS_APPS = (
    'quiz.templatetags.qdc_tags',
    'experiment.templatetags.subjects_tags',
    'survey.templatetags.subjects_tags_survey',
)

INSTALLED_APPS += PROJECT_APPS
INSTALLED_APPS += PROJECT_TAGS_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'qdc.middleware.PasswordChangeMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.template.context_processors.request",
)


ROOT_URLCONF = 'qdc.urls'

WSGI_APPLICATION = 'qdc.wsgi.application'

# LimeSurvey configuration
LIMESURVEY = {
    'URL_API': '',
    'URL_WEB': '',
    'USER': '',
    'PASSWORD': '',
}

# Portal API configuration
PORTAL_API = {
    'URL': '',
    'PORT': '',
    'USER': '',
    'PASSWORD': ''
}

# Show button to send experiments to Portal
SHOW_SEND_TO_PORTAL_BUTTON = False

# AUTH_USER_MODEL = 'quiz.UserProfile'
# AUTH_PROFILE_MODULE = 'quiz.UserProfile'

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pt-br'
# LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('pt-br', 'Português'),
    ('en', 'English'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'patient/locale'),
    os.path.join(BASE_DIR, 'experiment/locale'),
    os.path.join(BASE_DIR, 'survey/locale'),
    os.path.join(BASE_DIR, 'custom_user/locale'),
    os.path.join(BASE_DIR, 'quiz/locale'),
    os.path.join(BASE_DIR, 'export/locale'),
    os.path.join(BASE_DIR, 'qdc/locale'),
)

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Database Translation
MODELTRANSLATION_LANGUAGES = ('pt-br', 'en')
MODELTRANSLATION_FALLBACK_LANGUAGES = ('pt-br', 'en')

MODELTRANSLATION_TRANSLATION_FILES = (
    'patient.translation',
    'experiment.translation',
    # '<APP2_MODULE>.translation',
)

MODELTRANSLATION_CUSTOM_FIELDS = ('name', 'description', 'abbreviated_description', )

MODELTRANSLATION_AUTO_POPULATE = 'all'

MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'


FIXTURE_DIRS = (
    'patient.fixtures',
    'experiment.fixtures',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = ''
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

try:
    from .settings_local import *
except ImportError:
    pass

VERSION = '1.54.2'
