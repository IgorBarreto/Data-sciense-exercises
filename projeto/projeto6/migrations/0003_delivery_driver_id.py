# Generated by Django 4.2.1 on 2023-05-22 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto6', '0002_remove_delivery_driver_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='driver_id',
            field=models.IntegerField(null=True),
        ),
    ]
