from django import forms
from task_manager.users.models import Users


class UsersForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255, required=True)
    last_name = forms.CharField(max_length=255, required=True)
    username = forms.CharField(max_length=255,  required=True)
    # password = forms.CharField(max_length=255,  required=True)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
