import os
from pathlib import Path

from environ import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = 'django-insecure-l!dth02*r^!5_u@=^d+l$$dl%8$w$a-%82r_&!^r7-3(%zi^ub'
FIELD_ENCRYPTION_KEY = env.str('FIELD_ENCRYPTION_KEY')

DEBUG = env.bool( 'DEBUG' )

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'crispy_forms',
    'crispy_neurobrutalist',
    'core.apps.CoreConfig',
    'portfolio.apps.PortfolioConfig',
    'accounts.apps.AccountsConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_USER_MODEL = 'accounts.User'
LOGIN_REDIRECT_URL = 'core:painel'
LOGOUT_REDIRECT_URL = 'portfolio'

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = env.list('INTERNAL_IPS')

LOG_FOLDER = BASE_DIR / "logs"

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "\033[1;32m[%(levelname)s]\033[0m %(asctime)s \033[1;34m%(name)s\033[0m: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "DEBUG", "propagate": True},
        "system": {
            "handlers": ["console"],
            "level": env.str("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
    },
}


CRISPY_ALLOWED_TEMPLATE_PACKS = ("neobrutalist")
CRISPY_TEMPLATE_PACK = "neobrutalist"

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT")
SESSION_COOKIE_SECURE = env.bool("SESSION_COOKIE_SECURE")
CSRF_COOKIE_SECURE = env.bool("CSRF_COOKIE_SECURE")
SESSION_COOKIE_NAME = env.str("SESSION_COOKIE_NAME", default="jrm_dev")
SESSION_COOKIE_AGE = env.int("SESSION_COOKIE_AGE", default=21600)
SESSION_SAVE_EVERY_REQUEST = env.bool("SESSION_SAVE_EVERY_REQUEST", default=True)
SESSION_COOKIE_HTTPONLY = env.bool("SESSION_COOKIE_HTTPONLY", default=True)