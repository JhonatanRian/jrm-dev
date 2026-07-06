import os
from pathlib import Path

from django.contrib.messages import constants as django_messages
from environ import Env

BASE_DIR = Path(__file__).resolve().parent.parent

env = Env(
    DEBUG=(bool, False),
    SECURE_SSL_REDIRECT=(bool, False),
    SESSION_COOKIE_SECURE=(bool, False),
    CSRF_COOKIE_SECURE=(bool, False),
)
Env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "debug_toolbar",
    "django_filters",
    "crispy_forms",
    "crispy_neurobrutalist",
    "django_select2",
    "storages",
    "core.apps.CoreConfig",
    "portfolio.apps.PortfolioConfig",
    "accounts.apps.AccountsConfig",
    "blog.apps.BlogConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTH_USER_MODEL = "accounts.User"
LOGIN_REDIRECT_URL = "core:painel"
LOGOUT_REDIRECT_URL = "portfolio"

WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": env.db(
        "DATABASE_URL", default="postgres://postgres:postgres@localhost:5432/jrmdev"
    )
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

if DEBUG:
    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"

    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
else:
    # AWS S3 Storage Settings
    AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID", default=None)
    AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY", default=None)
    AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", default=None)
    AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME", default=None)
    AWS_S3_ENDPOINT_URL = env.str("AWS_S3_ENDPOINT_URL", default=None)
    AWS_S3_CUSTOM_DOMAIN = env.str("AWS_S3_CUSTOM_DOMAIN", default=None)
    
    if not AWS_S3_CUSTOM_DOMAIN and AWS_STORAGE_BUCKET_NAME:
        if AWS_S3_REGION_NAME:
            AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
        else:
            AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "location": "media",
                "querystring_auth": False,
                "default_acl": "public-read",
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "location": "static",
                "querystring_auth": False,
                "default_acl": "public-read",
            },
        },
    }

    if AWS_S3_CUSTOM_DOMAIN:
        STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
        MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
    elif AWS_STORAGE_BUCKET_NAME:
        # Default bucket domain if no custom domain is provided
        if AWS_S3_ENDPOINT_URL:
            # Custom endpoint (e.g. MinIO, Cloudflare R2, DigitalOcean Spaces)
            clean_endpoint = AWS_S3_ENDPOINT_URL.replace("https://", "").replace("http://", "")
            STATIC_URL = f"https://{clean_endpoint}/{AWS_STORAGE_BUCKET_NAME}/static/"
            MEDIA_URL = f"https://{clean_endpoint}/{AWS_STORAGE_BUCKET_NAME}/media/"
        else:
            region_suffix = f"-{AWS_S3_REGION_NAME}" if AWS_S3_REGION_NAME else ""
            STATIC_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3{region_suffix}.amazonaws.com/static/"
            MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3{region_suffix}.amazonaws.com/media/"
    else:
        STATIC_URL = "/static/"
        MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
INTERNAL_IPS = env.list("INTERNAL_IPS", default=["127.0.0.1", "::1"])

if DEBUG:
    # Ensure local loopbacks are present
    if "127.0.0.1" not in INTERNAL_IPS:
        INTERNAL_IPS.append("127.0.0.1")
    if "::1" not in INTERNAL_IPS:
        INTERNAL_IPS.append("::1")

    # Discover Docker gateway IP for development inside containers
    import socket

    try:
        hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
        for ip in ips:
            gateway_ip = ip[: ip.rfind(".")] + ".1"
            if gateway_ip not in INTERNAL_IPS:
                INTERNAL_IPS.append(gateway_ip)
    except Exception:
        pass

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


CRISPY_ALLOWED_TEMPLATE_PACKS = "neobrutalist"
CRISPY_TEMPLATE_PACK = "neobrutalist"

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

MESSAGE_TAGS = {
    django_messages.DEBUG: "debug",
    django_messages.INFO: "info",
    django_messages.SUCCESS: "success",
    django_messages.WARNING: "warning",
    django_messages.ERROR: "error",
}

# Security & Session Settings
SECURE_SSL_REDIRECT = env("SECURE_SSL_REDIRECT")
SESSION_COOKIE_SECURE = env("SESSION_COOKIE_SECURE")
CSRF_COOKIE_SECURE = env("CSRF_COOKIE_SECURE")
SESSION_COOKIE_NAME = env.str("SESSION_COOKIE_NAME", default="jrm_dev")
SESSION_COOKIE_AGE = env.int("SESSION_COOKIE_AGE", default=21600)
SESSION_SAVE_EVERY_REQUEST = env.bool("SESSION_SAVE_EVERY_REQUEST", default=True)
SESSION_COOKIE_HTTPONLY = env.bool("SESSION_COOKIE_HTTPONLY", default=True)


# Production Security Headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=0)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "SECURE_HSTS_INCLUDE_SUBDOMAINS", default=False
)
SECURE_HSTS_PRELOAD = env.bool("SECURE_HSTS_PRELOAD", default=False)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
