from django.db import models
from django.contrib.auth.models import User
from task_manager.users.models import CustomUser
from task_manager.statuses.models import Status
from task_manager.labels.models import Labels


class Task(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author' )
    name = models.CharField('name', max_length=255, unique=True)
    description = models.CharField('description', max_length=255)
    timestamp = models.DateTimeField("time_stamp", auto_now_add=True)
    executor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, models.SET_NULL, blank=True, null=True)
    # labels = models.ForeignKey(Labels, models.SET_NULL, blank=True, null=True)
    labels = models.ManyToManyField(Labels)

    def __str__(self):
        return '{} {} {} {} {} {}'.format(
            self.author, self.name, self.description, self.executor, self.status, self.labels)

    """
        def __str__(self):
            return self.name, self.description, self.executor, self.status, self.labels
    """