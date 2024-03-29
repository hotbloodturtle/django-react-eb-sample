from .base import *

import json

DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['storages']

CONFIG_SETTINGS_COMMON_FILE = os.path.join(BASE_DIR, 'secret.json')

CONFIG_SECRETS: dict = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())
CONFIG_SECRET = CONFIG_SECRETS.get('PROD')

SECRET_KEY = CONFIG_SECRET.get('SECRET_KEY')

AWS_ACCESS_KEY_ID = CONFIG_SECRET.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = CONFIG_SECRET.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_REGION_NAME = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'mybucket'


DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

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
