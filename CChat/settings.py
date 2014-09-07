"""
Django settings for CChat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a7^b0m^g5$d%_!m!578uojj$qw2lszpi3pcp!3kh69^g0+&f+_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'auth',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'CChat.middleware.SQLAlchemySessionMiddleware',
    'CChat.middleware.SQLAlchemyAuthMiddleware',
)

ROOT_URLCONF = 'CChat.urls'

WSGI_APPLICATION = 'CChat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASE = "postgresql://cchatdb:cchatdb@localhost:5432/cchat_dev"

ENGINE = create_engine(DATABASE)
SESSION = scoped_session(sessionmaker(bind=ENGINE))

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Media files (pictures, files)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# HTML templates

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'), ]

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader')

AUTHENTICATION_BACKENDS = (
    'CChat.backends.EmailBackend',
)

# AUTH_USER_MODEL = 'Model.User'

# Settings to store sessions in local folder

SESSION_ENGINE = 'django.contrib.sessions.backends.file'

SESSION_FILE_PATH = os.path.join(BASE_DIR, 'sessions')

# SMTP server settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'denself@gmail.com'
EMAIL_HOST_PASSWORD = '1708382786750386denya'
EMAIL_USE_TLS = True

LOGIN_URL = "/auth/login/"