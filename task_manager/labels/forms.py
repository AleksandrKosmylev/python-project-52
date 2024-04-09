from django import forms
from task_manager.labels.models import Labels
from django.utils.translation import gettext as _


class LabelsForm(forms.ModelForm):
    class Meta:
        model = Labels
        fields = ['name']
