# Generated by Django 4.0 on 2024-06-13 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doris', '0017_alter_s3loadtask_doris_db'),
    ]

    operations = [
        migrations.AddField(
            model_name='s3loadtask',
            name='is_create_table',
            field=models.BooleanField(default=False, verbose_name='建表'),
        ),
    ]
