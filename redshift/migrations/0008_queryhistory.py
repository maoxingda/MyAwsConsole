# Generated by Django 4.1 on 2025-02-26 03:14

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('redshift', '0007_alter_restoretabletask_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('query_id', models.BigIntegerField(verbose_name='查询ID')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('elapsed', models.BigIntegerField(help_text='单位：秒', verbose_name='耗时')),
                ('query_text', models.TextField(verbose_name='查询文本')),
            ],
            options={
                'verbose_name': '查询历史',
                'verbose_name_plural': '查询历史',
            },
        ),
    ]
