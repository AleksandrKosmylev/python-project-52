from django.shortcuts import render, redirect
from django.views import View
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from task_manager.users.mixins import AccessCheck
from task_manager.mixins import CustomLoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class StatusView(CustomLoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
"""
def main_statuses(request):
    statuses = Status.objects.all()
    return render(request, 'statuses/statuses.html', {'statuses': statuses})
"""
class StatusCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Create status'),
        'btn_text': _('Create'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully added!')

"""
class StatusCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'statuses/status_create.html')

    def post(self, request, *args, **kwargs):
        status_form = StatusForm(request.POST)
        if status_form.is_valid():
            status_form.save()
            messages.success(request, 'Статус успешно создан')
            return redirect('statuses')
        else:
            return HttpResponse("STATUSES FAILED. CREATE FLASH FOR IT")
"""
class StatusUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Update status'),
        'btn_text': _('Update'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully update!')
"""
class StatusUpdateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        return render(request, 'statuses/status_update.html', {'status': status})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        status_form = StatusForm(request.POST, instance=status)
        if status_form.is_valid():
            status_form.save()
            messages.success(request, 'Статус успешно изменен')
            return redirect('statuses')

"""

class StatusDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'form.html'
    extra_context = {
        'description': _('Are you sure you want to delete'),
        'title': _('Delete status'),
        'btn_text': _('Yes, delete'),
        'btn_class': 'btn-danger'}
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted!')
"""
class StatusDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        return render(request, 'statuses/status_delete.html', {'status': status})

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('id')
        status = Status.objects.get(id=status_id)
        if status:
            status.delete()
            messages.success(request, 'Статус успешно удален')
            return redirect('statuses')
        return HttpResponse("DELETE STATUS FAILED. CREATE FLASH FOR IT")
"""