import unittest
from django.test import Client
from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from task_manager.users.models import CustomUser
from django.urls import reverse, reverse_lazy
from . import get_content
from django.utils.translation import gettext_lazy as _



class UsersTest(TestCase):
    fixtures = ['tests/fixtures/db.json']

    def setUp(self):
        self.dump_data = get_content('data.json')

    def test_index_page(self):
        response = self.client.get(reverse('users_index'))
        self.assertEqual(response.status_code, 200)

        users = CustomUser.objects.all()
        count = users.count()
        self.assertEqual(count, 2)
        self.assertQuerysetEqual(
            response.context['customuser_list'],
            users,
            ordered=False,
        )


    def test_create(self):
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)

        new_user = self.dump_data.get('users').get('new')
        response = self.client.post(reverse('user_create'),
                                    new_user,
                                    follow=True)
        print(new_user.get('first_name'), 'pk!!!')
        created_user = CustomUser.objects.get(id=new_user.get('pk'))
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(created_user.username, "test_username")
        self.assertContains(response, _('Successfully registered!'))
        users = CustomUser.objects.all()
        print(users.values(), 'users')
"""
    def test_update(self):
        created_user = CustomUser.objects.get(username="test_username")
        print(created_user)
        # self.client.force_login(user=CustomUser.objects.get(id=1))
        users = CustomUser.objects.all()
        print(users.values(), 'users_update')
"""