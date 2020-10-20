from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager



class user_reg(AbstractUser):
    mobile = models.CharField(max_length=100, blank=True, null=True)
    objects = UserManager()

    class Meta:
        verbose_name='user'

