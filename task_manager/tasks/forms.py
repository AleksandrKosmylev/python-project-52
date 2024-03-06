from django import forms
from task_manager.tasks.models import Task, User, Status


class TaskForm(forms.ModelForm):
    executor = forms.ModelChoiceField(queryset=User.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    class Meta:
        model = Task
        fields = ['name', 'description', 'executor', 'status']

"""
    executor = forms.ModelForm (queryset=User.objects.all())
    status = forms.ModelChoiceField(queryset=Status.objects.all())
"""