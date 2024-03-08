from django.http import HttpResponse
from django.shortcuts import render, redirect
from task_manager.tasks.models import Task, Status
from django.contrib.auth.models import User
from task_manager.tasks.forms import TaskForm
from django.views import View
from django.contrib import messages


def main_tasks(request):
    tasks = Task.objects.all().order_by('id')
    statuses = Status.objects.all()
    users = User.objects.all()
    return render(request, 'tasks/tasks.html', {'statuses': statuses, 'users': users, 'tasks': tasks})


def show_task_card(request, **kwargs):
    task_id = kwargs.get('id')
    task = Task.objects.get(id=task_id)
    return render(request, 'tasks/task_card.html', {'task': task})


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
            return HttpResponse("TASKS FAILED. CREATE FLASH FOR IT")


class TaskUpdateView(View):

    def get(self, request, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        statuses = Status.objects.all()
        users = User.objects.all()
        return render(request, 'tasks/task_update.html', {'task': task, 'statuses': statuses, 'users': users})

    def post(self, request, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            messages.success(request, 'Задача успешно изменена')
            return redirect('tasks')
        else:
            return HttpResponse("Error form")
        return render(request, 'tasks/task_update.html', {'form': form})


class TaskDeleteView(View):

    def get(self, request, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        return render(request, 'tasks/task_delete.html', {'task': task})

    def post(self, request, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        if task:
            task.delete()
            messages.success(request, 'Задача успешно удалена')
            return redirect('tasks')
        return HttpResponse("DELETE USER FAILED. CREATE FLASH FOR IT")
