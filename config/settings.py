import os
import random
import string
import json

from pathlib import Path


# server mode, allow
DEBUG = True if os.getenv('SERVER_MODE') == 'dev' else False
ALLOWED_HOSTS = ['*']

# path
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_SETTINGS_COMMON_FILE = os.path.join(BASE_DIR, 'secret.json')
FRONT_PATH = 'frontend'

# env
CONFIG_SECRET = {} if DEBUG else json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
SECRET_KEY = CONFIG_SECRET.get('SECRET_KEY') or ''.join(random.choices(string.ascii_uppercase + string.digits, k=30))
DB_NAME = CONFIG_SECRET.get('DB_NAME', 'aquanode_dev')
DB_USER = CONFIG_SECRET.get('DB_USER', 'root')
DB_PASSWORD = CONFIG_SECRET.get('DB_PASSWORD', '')
DB_HOST = CONFIG_SECRET.get('DB_HOST', 'localhost')


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [f'{FRONT_PATH}/build', f'{FRONT_PATH}/public'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

AUTH_USER_MODEL = 'accounts.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# static
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
FRONT_STATIC_DIR = os.path.join(BASE_DIR, FRONT_PATH, 'build', 'static')
STATICFILES_DIRS = [STATIC_DIR, FRONT_STATIC_DIR]

# media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
