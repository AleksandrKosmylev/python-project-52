# Generated by Django 5.0.1 on 2024-03-09 14:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0002_task_executor_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='labels.labels'),
        ),
    ]
