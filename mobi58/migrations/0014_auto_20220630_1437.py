# Generated by Django 3.0.8 on 2022-06-30 09:07

from django.db import migrations, models
import mobi58.models


class Migration(migrations.Migration):

    dependencies = [
        ('mobi58', '0013_auto_20220630_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleregister',
            name='insurance_file',
            field=models.FileField(blank=True, null=True, upload_to='vehicle/', validators=[mobi58.models.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='vehicleregister',
            name='pollution_file',
            field=models.FileField(blank=True, null=True, upload_to='vehicle/', validators=[mobi58.models.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='vehicleregister',
            name='rc_file',
            field=models.FileField(blank=True, null=True, upload_to='vehicle/', validators=[mobi58.models.validate_file_size]),
        ),
    ]