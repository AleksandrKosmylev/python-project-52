from django.http import HttpResponse
from django.shortcuts import render, redirect
from task_manager.tasks.models import Task, Status
from django.contrib.auth.models import User
from task_manager.tasks.forms import TaskForm
from django.views import View
from django.contrib import messages


def main_tasks(request):
    tasks = Task.objects.all()
    statuses = Status.objects.all()
    users = User.objects.all()
    return render(request, 'tasks/tasks.html', {'statuses': statuses, 'users': users, 'tasks': tasks})


class TaskCreateView(View):

    def get(self, request):
        statuses = Status.objects.all()
        users = User.objects.all()
        return render(request, 'tasks/task_create.html', {'statuses': statuses, 'users': users})

    def post(self, request):
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            messages.success(request, 'Задача успешно создана')
            return redirect('tasks')
        else:
            f = task_form.errors.as_data()
            print(f)
            return HttpResponse("TASKS FAILED. CREATE FLASH FOR IT")
