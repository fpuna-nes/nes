SECRET_KEY = ' ^ri1i@33v@5^84ql#wwv62zw66_wj)n=%j=z6!n*4c=1%m(y(= '

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEBUG404 = True

TEMPLATE_DEBUG = DEBUG

# SECURITY WARNING: don't run with "is testing" on in production
IS_TESTING = False

ALLOWED_HOSTS = []

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-STATIC_ROOT
STATIC_ROOT = '/usr/local/nes-system/nes/patientregistrationsystem/qdc/static'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nes',
        'USER': 'nes',
        'PASSWORD': 'nes',
        'HOST': 'localhost',
    }
}

# LimeSurvey configuration
LIMESURVEY = {
    'URL_API': 'http://example.limesurvey.server.com',
    'URL_WEB': 'http://example.limesurvey.server.com',
    'USER': 'limesurvey_user',
    'PASSWORD': 'limesurvey_password'
}

# Settings to send emails
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'smtp.user@example.com'
EMAIL_HOST_PASSWORD = 'smtp.user_pwd'
DEFAULT_FROM_EMAIL = 'smtp.user@example.com'
SERVER_EMAIL = EMAIL_HOST_USER

CONTACT_INSTITUTION = 'Developer environment'
CONTACT_EMAIL = 'contact at example dot com'
CONTACT_URL = 'https://example.com'
LOGO_INSTITUTION = 'logo-institution.png'