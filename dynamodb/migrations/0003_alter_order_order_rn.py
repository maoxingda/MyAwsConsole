# Generated by Django 4.0 on 2024-08-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamodb', '0002_order_order_rn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_rn',
            field=models.CharField(max_length=100),
        ),
    ]
