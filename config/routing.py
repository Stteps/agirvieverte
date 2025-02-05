import os

from django.urls import path
from channels.routing import URLRouter

import app.core.routing

websocket_prefix = "ws/" if os.environ.get("DJANGO_SETTINGS_MODULE") == "config.django.base" else ""

websocket_urlpatterns = [
    path(websocket_prefix, URLRouter(app.core.routing.urlpatterns)),
]
