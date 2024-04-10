from django.db import models
from task_manager.users.models import CustomUser
from task_manager.statuses.models import Status
from task_manager.labels.models import Labels


class Task(models.Model):
    name = models.CharField('name', max_length=255, unique=True)
    description = models.TextField('description', blank=True)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='author')
    timestamp = models.DateTimeField("time_stamp",
                                     auto_now_add=True)
    executor = models.ForeignKey(CustomUser,
                                 on_delete=models.CASCADE)
    status = models.ForeignKey(Status,
                               models.SET_NULL,
                               blank=True,
                               null=True)
    labels = models.ManyToManyField(Labels,
                                    through="IntermediateModel",
                                    verbose_name='labels')

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.author,
                                          self.name,
                                          self.description,
                                          self.executor,
                                          self.status,
                                          self.labels)


class IntermediateModel(models.Model):
    label = models.ForeignKey(Labels,
                              on_delete=models.PROTECT,
                              null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
