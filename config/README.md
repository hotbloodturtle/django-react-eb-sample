### django, eb setting

참고
https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/create-deploy-python-django.html

```python

1. 기본적인 django 세팅
pip install django
pip install awscli
pip install awsebcli
pip freeze > requirements.txt

2. awsebcli 설치

```


```python

2. django.config 세팅

# .ebextensions/django.conf
option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: config.settings
    PYTHONPATH: /opt/python/current/app:$PYTHONPATH
  aws:elasticbeanstalk:container:python:
    WSGIPath: config.wsgi:application

```

```python

3. 01_packages.config 세팅

# .ebextensions/_packages.conf
packages:
  yum:
    python3-devel: []
    mariadb-devel: []
    gcc: []

```

```python
4. eb cli 세팅
eb init

eb create

코드 수정 후
eb deploy

배포 완료후 (웹 열때)
eb open
```

```python
elasticbeanstalk ssh server 정보

서버 내의 코드 경로
/var/app/current

서버 내에서 가상환경 실행
source /var/app/venv/*/bin/activate
```