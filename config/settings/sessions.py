import os

"""
Do read:
    1. https://docs.djangoproject.com/en/3.1/ref/settings/#sessions
    2. https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
"""
SESSION_COOKIE_AGE = os.environ.get("SESSION_COOKIE_AGE", 1209600)  # Default - 2 weeks in seconds
SESSION_COOKIE_HTTPONLY = bool(int(os.environ.get("SESSION_COOKIE_HTTPONLY", 1)))
SESSION_COOKIE_NAME = os.environ.get("SESSION_COOKIE_NAME", "sessionid")
SESSION_COOKIE_SAMESITE = os.environ.get("SESSION_COOKIE_SAMESITE", "Lax")
SESSION_COOKIE_SECURE = bool(int(os.environ.get("SESSION_COOKIE_SECURE", 0)))

CSRF_USE_SESSIONS = bool(int(os.environ.get("CSRF_USE_SESSIONS", 0)))
