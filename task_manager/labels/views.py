from task_manager.labels.models import Labels
from task_manager.labels.forms import LabelsForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomLoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class LabelView(CustomLoginRequiredMixin, ListView):
    model = Labels
    template_name = 'labels/labels.html'


class LabelCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Labels
    form_class = LabelsForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Create Label'),
        'btn_text': _('Create'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created!')


class LabelUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Labels
    form_class = LabelsForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Update label'),
        'btn_text': _('Update'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully update!')


class LabelDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Labels
    extra_context = {
        'description': _('Are you sure you want to delete'),
        'title': _('Delete label'),
        'btn_text': _('Yes, delete'),
        'btn_class': 'btn-danger'}
    template_name = 'form.html'
    success_url = reverse_lazy('labels')
    success_message = _("Label successfully deleted!")
