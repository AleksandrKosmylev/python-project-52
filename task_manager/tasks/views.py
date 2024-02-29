from django.shortcuts import render
from task_manager.tasks.models import Task
from django.views import View
# Create your views here.


def main_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})

class TaskCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/task_create.html')
    """
    def post(self, request, *args, **kwargs):
        status_form = StatusForm(request.POST)
        if status_form.is_valid():
            status_form.save()
            messages.success(request, 'Статус успешно создан')
            return redirect('statuses')
        else:
            return HttpResponse("STATUSES FAILED. CREATE FLASH FOR IT")
    """
