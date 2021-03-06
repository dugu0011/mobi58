# Generated by Django 3.0.8 on 2021-11-19 17:44

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_auto_20211114_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivermaster',
            name='aadhar_file',
            field=models.FileField(blank=True, null=True, upload_to='file/aadhar/', validators=[accounts.models.validate_file_size]),
        ),
        migrations.AddField(
            model_name='drivermaster',
            name='aadhar_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='drivermaster',
            name='license_file',
            field=models.FileField(blank=True, null=True, upload_to='file/dl/', validators=[accounts.models.validate_file_size]),
        ),
        migrations.AddField(
            model_name='drivermaster',
            name='license_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
