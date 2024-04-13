from task_manager.tasks.mixins import TaskAuthorMixin
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomLoginRequiredMixin
# from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as _
from django_filters.views import FilterView
from task_manager.tasks.filter import TaskFilter


class TaskView(CustomLoginRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/tasks.html'


class TaskInfoView(DetailView):
    model = Task
    template_name = 'tasks/task_card.html'


class TaskCreateView(CustomLoginRequiredMixin,
                     SuccessMessageMixin,
                     CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Create Task'),
        'btn_text': _('Create'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully created")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(CustomLoginRequiredMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'form.html'
    extra_context = {
        'title': _('Update Task'),
        'btn_text': _('Update'),
        'btn_class': 'btn-primary'}
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully updated")


class TaskDeleteView(CustomLoginRequiredMixin,
                     SuccessMessageMixin,
                     TaskAuthorMixin,
                     DeleteView):
    model = Task
    extra_context = {
        'description': _('Are you sure you want to delete'),
        'title': _('Delete Task'),
        'btn_text': _('Yes, delete'),
        'btn_class': 'btn-danger'}
    template_name = 'form.html'
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully deleted")
