from django.db import models
from django.contrib.auth.models import User
from task_manager.statuses.models import Status

# Create your models here.

class Task(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.CharField('description', max_length=255)
    timestamp = models.DateTimeField("time_stamp", auto_now_add=True)
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
