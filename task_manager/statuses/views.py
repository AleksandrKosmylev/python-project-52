from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.mixins import CustomLoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class StatusView(CustomLoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'


class StatusCreateView(CustomLoginRequiredMixin,
                       SuccessMessageMixin,
                       CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Create status'),
        'btn_text': _('Create'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully added!')


class StatusUpdateView(CustomLoginRequiredMixin,
                       SuccessMessageMixin,
                       UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Update status'),
        'btn_text': _('Update'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully updated!')


class StatusDeleteView(CustomLoginRequiredMixin,
                       SuccessMessageMixin,
                       DeleteView):
    model = Status
    template_name = 'form.html'
    extra_context = {
        'description': _('Are you sure you want to delete'),
        'title': _('Delete status'),
        'btn_text': _('Yes, delete'),
        'btn_class': 'btn-danger'}
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted!')
