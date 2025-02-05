import os
from config.env import env_to_enum
from app.emails.enums import EmailSendingStrategy

EMAIL_SENDING_STRATEGY = env_to_enum(EmailSendingStrategy, os.environ.get("EMAIL_SENDING_STRATEGY", "local"))

EMAIL_SENDING_FAILURE_TRIGGER = bool(os.environ.get("EMAIL_SENDING_FAILURE_TRIGGER", 0))
EMAIL_SENDING_FAILURE_RATE = float(os.environ.get("EMAIL_SENDING_FAILURE_RATE", 0.2))

if EMAIL_SENDING_STRATEGY == EmailSendingStrategy.LOCAL:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

if EMAIL_SENDING_STRATEGY == EmailSendingStrategy.PRODUCTION:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
    EMAIL_PORT = os.environ.get("EMAIL_PORT", "")
    # EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "admin@3ia-demos.inria.fr")
SERVER_EMAIL = os.environ.get("SERVER_EMAIL", "admin@3ia-demos.inria.fr")
