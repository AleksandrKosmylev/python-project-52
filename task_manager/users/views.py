from task_manager.users.forms import UsersForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _
from task_manager.users.models import CustomUser
from task_manager.mixins import CustomLoginRequiredMixin
from task_manager.users.mixins import AccessCheck


class IndexView(ListView):
    model = CustomUser
    template_name = 'users/users_list.html'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = UsersForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Registration'),
        'btn_text': _('Sign up'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('login')
    success_message = _('Successfully registered!')


class UserUpdateView(CustomLoginRequiredMixin,
                     AccessCheck,
                     SuccessMessageMixin,
                     UpdateView):
    model = CustomUser
    form_class = UsersForm
    extra_context = {
        'title': _('Edit user'),
        'btn_text': _('Update'),
        'btn_class': 'btn-primary'}
    template_name = 'form.html'
    success_url = reverse_lazy('users_index')
    success_message = _('Successfully updated!')


class UserDeleteView(CustomLoginRequiredMixin,
                     AccessCheck,
                     SuccessMessageMixin,
                     DeleteView):
    model = CustomUser
    extra_context = {
        'description': _('Are you sure you want to delete'),
        'title': _('Delete user'),
        'btn_text': _('Yes, delete'),
        'btn_class': 'btn-danger'}
    template_name = 'form.html'
    success_url = reverse_lazy('users_index')
    success_message = _("User successfully deleted!")


from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    a = None
    a.hello()  # Creating an error with an invalid line of code
    return HttpResponse("Hello, world. You're at the pollapp index.")
