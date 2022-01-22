from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'giv-^#4yq#=3u)#_^9z)&7xnu7(2thz9uy&&u7fig4h6e=(_c5'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'django_extensions',
    'wagtail.contrib.styleguide',

]

MIDDLEWARE = MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    "127.0.0.1",
    "172.17.0.1"
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/Users/UserPC/Desktop/LEARNING/PYTHON/WAGTAIL/Website/cache"
    },
}

try:
    from .local import *
except ImportError:
    pass


