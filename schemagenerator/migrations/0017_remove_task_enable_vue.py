# Generated by Django 4.0 on 2023-12-24 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schemagenerator', '0016_alter_task_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='enable_vue',
        ),
    ]
