import os

from .base import *  # noqa

DEBUG = bool(int(os.environ.get("DJANGO_DEBUG", 0)))

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
USE_X_FORWARDED_HOST = True

INSTALLED_APPS = [app for app in INSTALLED_APPS if app != "django_extensions"]  # noqa

CORS_ALLOW_ALL_ORIGINS = False
CSRF_TRUSTED_ORIGINS = [f"https://{url}" for url in ALLOWED_HOSTS]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ROOT_URL = os.environ.get("ROOT_URL", "")
FORCE_SCRIPT_NAME = f"{ROOT_URL}/"
SESSION_COOKIE_PATH = f"{ROOT_URL}/"
SESSION_COOKIE_NAME = "agirvieverte-sessionid"

LOGIN_URL = f"{ROOT_URL}{LOGIN_URL}"  # noqa
LOGIN_REDIRECT_URL = f"{ROOT_URL}{LOGIN_REDIRECT_URL}"  # noqa
LOGOUT_REDIRECT_URL = f"{ROOT_URL}{LOGOUT_REDIRECT_URL}"  # noqa

STATIC_URL = f"{ROOT_URL}{STATIC_URL}"  # noqa
MEDIA_URL = f"{ROOT_URL}{MEDIA_URL}"  # noqa
