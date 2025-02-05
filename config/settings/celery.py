import os

from config.django.base import TIME_ZONE

CELERY_ACCEPT_CONTENT = ["application/json"]

REDIS_URL = f"redis://{os.environ.get('REDIS_HOST', default='broker')}:{os.environ.get('REDIS_PORT', default='6379')}"
CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL

CELERY_TIMEZONE = TIME_ZONE
