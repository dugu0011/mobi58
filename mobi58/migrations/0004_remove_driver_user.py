# Generated by Django 3.0.8 on 2022-04-07 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobi58', '0003_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='user',
        ),
    ]
