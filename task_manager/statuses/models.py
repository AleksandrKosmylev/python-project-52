from django.db import models

# Create your models here.


class Status(models.Model):
    name = models.CharField('status', max_length=255)
    timestamp = models.DateTimeField("time_stamp", auto_now_add=True)

    def __str__(self):
        return self.name
