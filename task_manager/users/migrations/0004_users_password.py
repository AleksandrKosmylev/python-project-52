# Generated by Django 5.0.1 on 2024-02-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_users_full_name_remove_users_user_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='qwerty123', max_length=255, verbose_name='password'),
            preserve_default=False,
        ),
    ]
