from django.core.exceptions import ObjectDoesNotExist
from task_manager.statuses.models import Status
from django.urls import reverse
from task_manager.users.models import CustomUser
from tests.test_auth import AuthTestCase
from . import get_content
from django.utils.translation import gettext_lazy as _


class StatusesTestCase(AuthTestCase):
    fixtures = ['tests/fixtures/db.json']
    page = 'statuses'

    def setUp(self):
        self.dump_data = get_content('data.json')
        self.client.force_login(user=CustomUser.objects.get(id=1))

    def test_index_page(self):
        self.client.force_login(user=CustomUser.objects.get(id=1))
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)

        statuses = Status.objects.all()
        count = statuses.count()
        self.assertEqual(count, 2)
        self.assertQuerysetEqual(
            response.context_data['status_list'],
            statuses,
            ordered=False,
        )

    def test_create(self):
        response = self.client.get(reverse('status_create'))
        self.assertEqual(response.status_code, 200)

        new_status = self.dump_data.get('statuses').get('new')
        response = self.client.post(reverse('status_create'),
                                    new_status,
                                    follow=True)
        created_status = Status.objects.get(id=new_status.get('pk'))
        self.assertEqual(created_status.name, new_status.get('name'))
        self.assertRedirects(response, reverse('statuses'))
        self.assertContains(response, _('Status successfully added!'))

    def test_update(self):
        exist_status = Status.objects.get(pk=1)
        response = self.client.get(reverse('status_update',
                                           args=[exist_status.pk]))
        self.assertEqual(response.status_code, 200)

        new_status = self.dump_data.get('statuses').get('updated')
        response = self.client.post(
            reverse('status_update', args=[exist_status.pk]),
            new_status,
            follow=True
        )
        self.assertRedirects(response, reverse('statuses'))
        updated_status = Status.objects.get(pk=exist_status.pk)
        self.assertEqual(updated_status.name, new_status.get('name'))
        self.assertContains(response, _('Status successfully updated!'))

    def test_delete(self):
        exist_status = Status.objects.get(id=2)
        response = self.client.post(reverse('status_delete',
                                            args=[exist_status.pk]),
                                    follow=True)

        self.assertRedirects(response, reverse('statuses'))
        self.assertContains(response, _('Status successfully deleted!'))
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(id=2)
