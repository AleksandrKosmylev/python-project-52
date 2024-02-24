from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Users(models.Model):
class Users(models.Model):
    first_name = models.CharField('first_name', max_length=255)
    last_name = models.CharField('last_name', max_length=255)
    username = models.CharField('username', max_length=255)
    ###PASSWORD CHECK FIELD TYPE###
    password = models.CharField('password', max_length=255)
    # password = models.CharField('password', widget=PasswordInput())
    ###PASSWORD CHECK FIELD TYPE###
    timestamp = models.DateTimeField("time_stamp", auto_now_add=True)

    def __str__(self):
        return self.username
