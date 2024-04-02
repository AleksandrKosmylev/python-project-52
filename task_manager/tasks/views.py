from django.http import HttpResponse
from django.shortcuts import render, redirect
from task_manager.tasks.models import Task, Status
from task_manager.labels.models import Labels
from django.contrib.auth.models import User
from task_manager.tasks.forms import TaskForm
from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomLoginRequiredMixin
from django.utils.translation import gettext_lazy as _


class TaskView(ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    
"""
def main_tasks(request):
    tasks = Task.objects.all().order_by('id')
    statuses = Status.objects.all()
    users = User.objects.all()
    labels = Labels.objects.all()
    return render(request, 'tasks/tasks.html', {
        'statuses': statuses, 'users': users, 'tasks': tasks, 'labels': labels})
"""
class TaskInfoView(DetailView):
    model = Task
    template_name = 'tasks/task_card.html'
    
"""
def show_task_card(request, **kwargs):
    print(request.user.id, "зарегистрированный пользователь")
    task_id = kwargs.get('id')
    task = Task.objects.get(id=task_id)
    print(task, 'all objects')
    return render(request, 'tasks/task_card.html', {'task': task})
"""

class TaskCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Create Task'),
        'btn_text': _('Create'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully created")# нужно  перевести

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


"""
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["logged_in_user"] = self.request.user # c авторизацией
        return kwargs


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = form.logged_in_user # from string 48
        self.object.save()
        form._save_m2m()
        return super().form_valid(form)
"""
"""
    def post(self, request):

        author_user = request.user
        print(author_user, "зарегистрированный пользователь")
        form = TaskForm(request.POST)
        a1 = form["name"].value()
        a2 = form["description"].value()
        a3 = form["executor"].value()
        a4 = form["status"].value()
        a5 = form["labels"].value()
        print(a1, a2, a3, a4, a5, "before_valid")
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            executor = form.cleaned_data['executor']
            status = form.cleaned_data['status']
            labels = form.cleaned_data['labels']
            obj = Task(author=author_user, name=name, description=description, executor=executor, status=status,
                       # labels =labels
                       )
            # obj.labels.set(1)
            obj.save()
            task_form = TaskForm(request.POST, instance=obj)
            task_form.labels = labels
            # task_form.save(commit=False)
            task_form.save()
            # form.save_m2m()
        new_task = Task.objects.get(name=a1)
        # new_task.labels.add(2)
        add_lebels = task_form.labels
        for i in add_lebels:
            new_task.labels.add(i)
            new_task.save()
        print(new_task, '33new_task33')
        return redirect('tasks')



        if form.is_valid():
            print('curwa')
            x = form.cleaned_data
            print(x, 'XXX')
            #ctask_form = form.save(commit=False)
            # print(task_form.cleaned_data(), "cleaned data")
            #print(self.object.author, 'self.author')
            # self.object.author = self.request.user.id
            # task_form.save()
            form.save_m2m()
            # return super().form_valid(form)

            # Task.author = user
            self.author = self.request.user
            task_form.save()
            form.save_m2m()

            # print(form.cleaned_data, 'data_create')
            messages.success(request, 'Задача успешно создана')
            return redirect('tasks')
        else:
            print(form.errors.as_data(), 'errors')
            return HttpResponse("TASKS FAILED. CREATE FLASH FOR IT")

    """
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
