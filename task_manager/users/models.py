from django.db import models


# Create your models here.
class Users(models.Model):
    user_name = models.CharField('user_name', max_length=255)
    full_name = models.CharField('full_name', max_length=255)
    timestamp = models.DateTimeField("time_stamp", auto_now_add=True)

    def __str__(self):
        return self.user_name, self.full_name, self.timestamp
