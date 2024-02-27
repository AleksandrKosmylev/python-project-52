from django.shortcuts import render, redirect
from django.views import View
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def main_statuses(request):
    statuses = Status.objects.all()
    return render(request, 'statuses/statuses.html', {'statuses': statuses})


class StatusCreateView(View):

    def get(self, request, *args, **kwargs):
        # form = StatusForm()
        # print(form, "form")
        return render(request, 'statuses/status_create.html')

    def post(self, request, *args, **kwargs):
        print("before_status")
        status_form = StatusForm(request.POST)
        check_status = status_form['name']
        print(check_status , "check_status" )
        if status_form.is_valid():
            status_form.save()
            messages.success(request, 'Статус успешно создан')
            return redirect('statuses')
        else:
            return HttpResponse("STATUSES FAILED. CREATE FLASH FOR IT")
        
