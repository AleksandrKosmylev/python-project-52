from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


class TaskAuthorMixin(UserPassesTestMixin):
    permission_denied_message = _("Only task's author can delete it!")
    tasks_url = reverse_lazy('tasks')

    def test_func(self):
        task = self.get_object()
        return task.author == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return redirect(self.tasks_url)
