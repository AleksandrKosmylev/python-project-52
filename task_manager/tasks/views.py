from django.http import HttpResponse
from django.shortcuts import render, redirect
from task_manager.tasks.models import Task, Status
from task_manager.labels.models import Labels
from django.contrib.auth.models import User
from task_manager.tasks.forms import TaskForm
from django.views import View
from django.contrib import messages


def main_tasks(request):
    tasks = Task.objects.all().order_by('id')
    statuses = Status.objects.all()
    users = User.objects.all()
    labels = Labels.objects.all()
    return render(request, 'tasks/tasks.html', {
        'statuses': statuses, 'users': users, 'tasks': tasks, 'labels': labels})


def show_task_card(request, **kwargs):
    task_id = kwargs.get('id')
    task = Task.objects.get(id=task_id)
    print(task, 'all objects')
    return render(request, 'tasks/task_card.html', {'task': task})


class TaskCreateView(View):

    def get(self, request):
        statuses = Status.objects.all()
        users = User.objects.all()
        labels = Labels.objects.all()
        print(labels, "lebels_create_get")
        return render(request, 'tasks/task_create.html', {
            'statuses': statuses, 'users': users, 'labels': labels})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
   
            task_form = form.save(commit=False)
            """
            print(request.POST['name'], 'request.name')
            print(request.POST['description'], 'request.description')
            print(request.POST['status'], 'request.status')
            print(request.POST['executor'], 'request.executor')
            print(request.POST['labels'], 'request.labels')
            # print(request.POST)

            task_form.name = request.POST['name']
            task_form.description = request.POST['description']
            task_form.status = request.POST['status']
            task_form.executor = request.POST['executor']
            task_form.labels = request.POST['labels']

            task_form.save()
            form.save_m2m()
        """
            task_form.save()
            form.save_m2m()
            # print(form.cleaned_data, 'data_create')
            messages.success(request, 'Задача успешно создана')
            return redirect('tasks')
        else:
            print(form.errors.as_data(), 'errors')
            return HttpResponse("TASKS FAILED. CREATE FLASH FOR IT")


class TaskUpdateView(View):

    def get(self, request, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        statuses = Status.objects.all()
        users = User.objects.all()
        labels = Labels.objects.all()
        return render(request, 'tasks/task_update.html', {'task': task, 'statuses': statuses, 'users': users, 'labels': labels})

    def post(self, request, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(request.POST, instance=task)

        if task_form.is_valid():
            task_form.save(commit=False)
            task_form.save_m2m()
            print(task_form.cleaned_data, 'data_update')
            messages.success(request, 'Задача успешно изменена')
            return redirect('tasks')
        else:
            print(task_form.errors.as_data(), 'errors')
            return HttpResponse("Error form update")
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
