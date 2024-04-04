from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:index')
