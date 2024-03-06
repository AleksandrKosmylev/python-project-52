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


def show_task_card(request, *args, **kwargs):
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
            print(task_form.cleaned_data.values(), 'cleaned')
            task_form.save()
            messages.success(request, 'Задача успешно создана')
            return redirect('tasks')
        else:
            f = task_form.errors.as_data()
            print(f)
            return HttpResponse("TASKS FAILED. CREATE FLASH FOR IT")


class TaskUpdateView(View):

    def get(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        statuses = Status.objects.all()
        users = User.objects.all()
        return render(request, 'tasks/task_update.html',{'task': task, 'statuses': statuses, 'users': users})


    def post(self, request, *args, **kwargs):
        task_id = kwargs.get('id')
        task = Task.objects.get(id=task_id)
        task_form = TaskForm(request.POST, instance=task)
        print("in it")
        data = {'name': task_form['name'].value(),
                'description': task_form['description'].value(),
                'executor': task_form['executor'].value(),
                'status': task_form['status'].value()
                }
        print(data,'data =')
        form = TaskForm(data)
        if task_form.is_valid():
            form.save()
            print(form.errors.as_data(), 'errors1')
            messages.success(request, 'Пользователь успешно изменен')
            return redirect('users_index')
        else:
            print(form.errors.as_data(), 'errors2')
            return HttpResponse("Error form")
        print(form.errors.as_data(), 'errors3')
        return render(request, 'tasks/task_update.html',{'form': form, 'task': task, 'statuses': statuses, 'users': users})


"""
    def post(self, request, *args, **kwargs):
        task_form = TaskForm(request.POST)
        print(task_form['name'].value(), 'task_form')
        print(task_form['executor'].value(), 'task_form')
        print(task_form['description'].value(), 'task_form')
        print(task_form['status'].value(), 'task_form')
        data = {'name': task_form['name'].value(),
                'description': task_form['description'].value(),
                'executor': task_form['executor'].value(),
                'status':task_form['status'].value()
                }
        print(data, data)
        form = TaskForm(data)
        if form.is_valid():
            form.save()
            print(form.errors.as_data(), 'errors1')
            messages.success(request, 'Задача успешно изменена')
            return redirect('tasks')
        else:
            f = form.errors.as_data()
            print(f, 'errors2')
            return HttpResponse("Error task")



"""