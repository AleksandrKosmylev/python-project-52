from django.shortcuts import render, redirect
from django.contrib import messages
from task_manager.labels.models import Labels
from django.views import View
from task_manager.labels.forms import LabelsForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomLoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class LabelView(CustomLoginRequiredMixin, ListView):
    model = Labels
    template_name = 'labels/labels.html'

"""
def main_labels(request):
    labels = Labels.objects.all().order_by('id')
    return render(request, 'labels/labels.html', {'labels': labels})
"""
class LabelCreateView(CustomLoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = Labels
    form_class = LabelsForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Create Label'),
        'btn_text': _('Create'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created!')
    
"""
class LabelCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'labels/label_create.html')

    def post(self, request):
        label_form = LabelsForm(request.POST)
        if label_form.is_valid():
            label_form.save()
            messages.success(request, 'Метка успешно создана')
            return redirect('labels')
"""
class LabelUpdateView(CustomLoginRequiredMixin,SuccessMessageMixin, UpdateView):
    model = Labels
    form_class = LabelsForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Update label'),
        'btn_text': _('Update'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully update!')


"""
class LabelUpdateView(View):

    def get(self, request, **kwargs):
        label_id = kwargs.get('id')
        label = Labels.objects.get(id=label_id)
        return render(request, 'labels/label_update.html',{'label': label})

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('id')
        label = Labels.objects.get(id=label_id)
        form = LabelsForm(request.POST, instance=label)
        if form.is_valid():
            form.save()
            messages.success(request, 'Метка успешно изменена')
            return redirect('labels')
        else:
            print(form.errors.as_data(), 'errors')
            return HttpResponse("Error label")
        return render(request, 'labels/label_update.html',{'form': form})
"""
class LabelDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Labels
    extra_context = {
        'description': _('Are you sure you want to delete'),
        'title': _('Delete label'),
        'btn_text': _('Yes, delete'),
        'btn_class': 'btn-danger'}
    template_name = 'form.html'
    # template_name = 'users/user_delete.html'
    success_url = reverse_lazy('labels')
    success_message = _("Label successfully deleted!")

"""
class LabelDeleteView(View):

    def get(self, request, **kwargs):
        label_id = kwargs.get('id')
        label = Labels.objects.get(id=label_id)
        return render(request, 'labels/label_delete.html',{'label': label})

    def post(self, request, **kwargs):
        label_id = kwargs.get('id')
        label = Labels.objects.get(id=label_id)
        if label:
            label.delete()
            messages.success(request, 'Метка успешно удалена')
            return redirect('labels')
        return HttpResponse("DELETE LABEL FAILED. CREATE FLASH FOR IT")

"""