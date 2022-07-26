from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aquanode_dev',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

# static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
FRONT_STATIC_DIR = os.path.join(BASE_DIR, FRONT_PATH, 'build', 'static')
STATICFILES_DIRS = [STATIC_DIR, FRONT_STATIC_DIR]

# media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
