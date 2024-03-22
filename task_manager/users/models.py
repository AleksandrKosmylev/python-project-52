from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

"""
# Create your models here.
# class Users(models.Model):
class Users(models.Model):
    first_name = models.CharField('first_name', max_length=255)
    last_name = models.CharField('last_name', max_length=255)
    username = models.CharField('username', max_length=255)
    password = models.CharField('password', widget=PasswordInput())
    timestamp = models.DateTimeField("time_stamp", auto_now_add=True)

    def __str__(self):
        return self.username
"""


class CustomUser(AbstractUser):

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.username

    # may cause problem because of usage id instead pk
    def get_absolute_url(self):
        # return reverse('user_update', kwargs={'pk': self.pk})
        return reverse('users:index')
