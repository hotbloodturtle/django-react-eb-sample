from .base import *

import json

DEBUG = False
ALLOWED_HOSTS = ['*']

CONFIG_SETTINGS_COMMON_FILE = os.path.join(BASE_DIR, 'secret.json')

CONFIG_SECRETS: dict = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
CONFIG_SECRET = CONFIG_SECRETS.get('PROD')

SECRET_KEY = CONFIG_SECRET.get('SECRET_KEY')
DB_NAME = CONFIG_SECRET.get('DB_NAME')
DB_USER = CONFIG_SECRET.get('DB_USER')
DB_PASSWORD = CONFIG_SECRET.get('DB_PASSWORD')
DB_HOST = CONFIG_SECRET.get('DB_HOST')

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
