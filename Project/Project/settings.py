"""
Django settings for Project project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v!)@_sg6!u)e_ctqc^3dy@kl2dj6--8nc@zv#@xr92e+#2*s$e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'fpages',
    'simplesimpleapp',
    'django_filters'
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'full.mobile.middlewaretest.MobileOrFullMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'for_debug': {
            'format': '(levelname) (asctime) (message)'
        },
        'for_warning': {
            'format': '(levelname) (asctime) (message) (pathname)'
        },
        'for_error_and_critical': {
            'format': '(levelname) (asctime) (message) (pathname)s (exc_info)'
        },
        'for_info': {
            'format': '(levelname) (asctime) (message) (module)'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'for_debug'
        },
        'event_path': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'for_warning'
        },
        'critical_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'for_error_and_critical'
        },
        'critical': {
            'level': 'CRITICAL',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'for_error_and_critical'
        },
        'into_errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'for_error_and_critical',
            'filename': '/Project/log/errors.log'
        },
        'into_critical': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'formatter': 'for_error_and_critical',
            'filename': '/Project/log/errors.log'
        },
        'into_general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filters': ['require_debug_false'],
            'formatter': 'for_info',
            'filename': '/Project/log/general.log'
        },
        'into_security': {
            'class': 'logging.FileHandler',
            'formatter': 'for_info',
            'filename': '/Project/log/security.log'
        },
        'mail_error': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
            'formatter': 'for_warning',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['critical_error', 'critical', 'into_general'],
            'propagate': False,
        },
        'custom_logger': {
            'handlers': ['event_path', 'for_warning', 'console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['into_errors', 'into_critical', 'mail_error'],
            'propagate': False,
        },
        'django.server': {
            'handlers': ['into_errors', 'into_critical', 'mail_error'],
            'propagate': False,
        },
        'django.template': {
            'handlers': ['into_errors', 'into_critical'],
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['into_errors', 'into_critical'],
            'propagate': False,
        },
        'django.security': {
            'handlers': ['into_security'],
            'propagate': False,
        }
    }
}