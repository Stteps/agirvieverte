import os

DEBUG_TOOLBAR_ENABLED = bool(int(os.environ.get("DEBUG_TOOLBAR_ENABLED", 1)))
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": "config.settings.debug_toolbar.setup.show_toolbar"}

# You can place additional settings below
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html
