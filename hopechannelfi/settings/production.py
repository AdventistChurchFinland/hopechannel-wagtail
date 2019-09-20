from .base import *

DEBUG = False

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True

CSRF_COOKIE_DOMAIN = "cms.hopechannel.fi"
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['cms.hopechannel.fi']

try:
    from .local import *
except ImportError:
    pass
