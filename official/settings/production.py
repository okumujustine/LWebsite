from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url
import os


env = os.environ.copy()
SECRET_KEY = env('SECRET_KEY')

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
COMPRESS_OFFLINE = True 
COMPRESS_CSS_FILTERS = [ 
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter'
 ]
COMPRESS_CSS_HASHING_METHOD = 'content'

DATABASES['default'] = dj_database_url.config()

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# allowed header
ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
