# Generated by Django 5.0.1 on 2024-04-05 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id',
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('name', models.CharField(
                    max_length=255,
                    verbose_name='status')),
                ('timestamp', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='time_stamp')),
            ],
        ),
    ]
