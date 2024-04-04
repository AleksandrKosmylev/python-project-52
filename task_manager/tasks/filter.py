import django_filters
from task_manager.tasks.models import Task
from task_manager.labels.models import Labels
from django import forms
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    label = django_filters.ModelChoiceFilter(queryset=Labels.objects.all(),
                                             label=_('Label'),
                                             field_name='labels')
    author_tasks = django_filters.BooleanFilter(field_name='author',
                                             widget=forms.CheckboxInput,
                                             method='filter_author_tasks',
                                             label=_('Only my tasks'))
    class Meta:
        model = Task
        fields = ['status', 'executor']


    def filter_author_tasks(self, queryset, arg, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
