from .base import *
from decouple import config
import dj_database_url

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "DEV_SECRET_KEY",
    default="django-insecure-j$hsu-&b$!gjt@kq6d-n=ey19&gvs9t__=3rgeec37urzgppb7",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = [
    *INSTALLED_APPS,
    "debug_toolbar",
]
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    *MIDDLEWARE,
]

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=config("DEV_DATABASE_URL"),
        conn_max_age=config("CONN_MAX_AGE", cast=int, default=30),
        conn_health_checks=True,
    )
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
