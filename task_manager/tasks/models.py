from django.db import models
from task_manager.users.models import CustomUser
from task_manager.statuses.models import Status
from task_manager.labels.models import Labels
from django.utils.translation import gettext as _


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    author = models.ForeignKey(CustomUser,
                               on_delete=models.PROTECT,
                               related_name='task_author',
                               verbose_name=_('Author'))
    timestamp = models.DateTimeField("time_stamp",
                                     auto_now_add=True)
    executor = models.ForeignKey(CustomUser,
                                 on_delete=models.PROTECT,
                                 blank=True,
                                 null=True,
                                 related_name='task_executor',
                                 verbose_name=_('Executor'))
    status = models.ForeignKey(Status,
                               on_delete=models.PROTECT,
                               verbose_name=_('Status'))
    labels = models.ManyToManyField(Labels,
                                    blank=True,
                                    through="IntermediateModel",
                                    verbose_name=_('Labels'))

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.author,
                                          self.name,
                                          self.description,
                                          self.status,
                                          self.executor,
                                          self.labels)


class IntermediateModel(models.Model):
    label = models.ForeignKey(Labels,
                              on_delete=models.PROTECT,
                              null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
