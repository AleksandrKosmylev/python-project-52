import unittest
from django.test import Client
from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from task_manager.users.models import CustomUser
from django.urls import reverse, reverse_lazy
from . import get_content
from django.utils.translation import gettext_lazy as _



class UsersTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username': "test_username",
            'first_name': "test_first_name",
            'last_name': "test_last_name",
            'password1': 'Parol123',
            'password2': 'Parol123',
        }

        self.updateduser_data = {
            'username': "updatedtest_username",
            'first_name': "updatedtest_first_name",
            'last_name': "updatedtest_last_name",
            'password1': 'Parol123',
            'password2': 'Parol123',
        }

    def test_index_page(self):
        response = self.client.get(reverse('users_index'))
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('user_create'),
                                    self.user_data,
                                    follow=True)
        created_user = CustomUser.objects.get(username="test_username")
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(created_user.username, "test_username")
        self.assertContains(response, _('Successfully registered!'))
        users = CustomUser.objects.all()
        print(users.values(), 'users')

    def test_update(self):
        created_user = CustomUser.objects.get(username="test_username")
        print(created_user)
        # self.client.force_login(user=CustomUser.objects.get(id=1))
        users = CustomUser.objects.all()
        print(users.values(), 'users_update')