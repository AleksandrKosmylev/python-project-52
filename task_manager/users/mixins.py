from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin


class AccessCheck(UserPassesTestMixin):
    login_url = reverse_lazy('users_index')
    permission_denied_message = _("You do not have permission to change another user.")

    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request,
                         self.permission_denied_message)
        return redirect(self.login_url)
