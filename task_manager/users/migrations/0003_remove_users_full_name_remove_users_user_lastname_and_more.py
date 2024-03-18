# Generated by Django 5.0.1 on 2024-02-04 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_user_lastname_alter_users_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_lastname',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_name',
        ),
        migrations.AddField(
            model_name='users',
            name='first_name',
            field=models.CharField(default=' 1_f_name', max_length=255, verbose_name='first_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(default='1-l_name', max_length=255, verbose_name='last_name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default='1_user_n', max_length=255, verbose_name='username'),
            preserve_default=False,
        ),
    ]