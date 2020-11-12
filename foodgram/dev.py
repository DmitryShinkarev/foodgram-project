from .settings import *


DEBUG = True


STATICFILES_DIR = os.path.join(BASE_DIR, 'static')

# settings for debug-toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Logging
if DEBUG:
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {"level": "DEBUG", "class": "logging.StreamHandler"}
        },
        "loggers": {
            "django.db.backends": {"handlers": ["console"], "level": "DEBUG"}
        },
    }
