from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, email, is_active=True, is_superuser=False):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            is_active=is_active,
            is_superuser=is_superuser,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, email):
        user = self.create_user(username, password, email, is_superuser=True)
        return user


class User(AbstractBaseUser):
    class Meta:
        verbose_name = '회원'
        verbose_name_plural = verbose_name

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    @property
    def is_staff(self):
        return self.is_superuser

    username = models.CharField('아이디', max_length=255, unique=True)
    email = models.EmailField('이메일', max_length=255, blank=True)
    is_active = models.BooleanField('활성 상태', default=True)
    is_superuser = models.BooleanField('관리자 여부', default=False)
