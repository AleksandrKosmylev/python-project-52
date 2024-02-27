from django.shortcuts import render, redirect
from django.views import View
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def main_statuses(request):
    statuses = Status.objects.all()
    return render(request, 'statuses/statuses.html', {'statuses': statuses})


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
