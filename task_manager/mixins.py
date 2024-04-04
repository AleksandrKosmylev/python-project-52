from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_message = _("You are not authorized! Log in, please.")
    login_url = reverse_lazy('login')

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, self.login_message)
            return redirect(self.login_url)
        return super().handle_no_permission()
