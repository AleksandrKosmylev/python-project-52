from django import forms
from task_manager.tasks.models import Task, User, Status, Labels, CustomUser


class TaskForm(forms.ModelForm):
    executor = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    labels = forms.ModelMultipleChoiceField(queryset=Labels.objects.all())

    class Meta:
        model = Task
        fields = ['name', 'description', 'executor', 'status', 'labels']

"""
    executor = forms.ModelForm (queryset=User.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())
"""

"""
class Meta:
    model = Task
    fields = ['name', 'description', 'executor', 'status']
"""
