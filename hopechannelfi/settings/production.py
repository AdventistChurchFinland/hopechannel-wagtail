from .base import *

DEBUG = False

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True

CSRF_COOKIE_DOMAIN = "hopechannel.fi"
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = ['hopechannel.fi']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'hopechannelfi',
#         'USER': 'hopechannelfi_user',
#         'PASSWORD': 'mypassword',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

try:
    from .local import *
except ImportError:
    pass
