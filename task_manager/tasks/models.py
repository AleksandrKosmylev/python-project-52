from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.CharField('description', max_length=255)
    timestamp = models.DateTimeField("time_stamp", auto_now_add=True)

    def __str__(self):
        return self.name
