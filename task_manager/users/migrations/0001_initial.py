# Generated by Django 5.0.1 on 2024-01-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255, verbose_name='user_name')),
                ('full_name', models.CharField(max_length=255, verbose_name='full_name')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
