# Generated by Django 5.0.1 on 2024-02-27 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_users_password'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
