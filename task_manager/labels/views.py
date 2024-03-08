from django.shortcuts import render, redirect
from django.contrib import messages
from task_manager.labels.models import Labels
from django.views import View
from task_manager.labels.forms import LabelsForm
from django.http import HttpResponse


def main_labels(request):
    labels = Labels.objects.all().order_by('id')
    return render(request, 'labels/labels.html', {'labels': labels})


class LabelCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'labels/label_create.html')

    def post(self, request):
        label_form = LabelsForm(request.POST)
        if label_form.is_valid():
            label_form.save()
            messages.success(request, 'Метка успешно создана')
            return redirect('labels')

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

