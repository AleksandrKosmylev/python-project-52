from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class AuthTestCase(TestCase):
    page = 'tasks'

    def test_auth(self):
        # redirect to login page if no authorization
        self.client.logout()
        response = self.client.get(reverse(f'{self.page}'), follow=True)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(response, _("You are not authorized! Log in, please."))
