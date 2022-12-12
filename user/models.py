from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):

    class Meta:
        verbose_name        = 'کاربر'
        verbose_name_plural = 'کاربران'

    username        = None
    email           = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
