# Generated by Django 4.1 on 2023-06-13 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0007_endpoint_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endpoint',
            name='database',
            field=models.CharField(max_length=32, null=True, verbose_name='数据库'),
        ),
    ]
