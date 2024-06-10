# Generated by Django 4.0 on 2024-06-09 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doris', '0011_alter_s3loadtask_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s3loadtask',
            name='attempts',
            field=models.SmallIntegerField(default=0, editable=False, verbose_name='执行次数'),
        ),
        migrations.AlterField(
            model_name='s3loadtask',
            name='load_label',
            field=models.CharField(default='', editable=False, max_length=128),
        ),
    ]
