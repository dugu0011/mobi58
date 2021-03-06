# Generated by Django 3.0.8 on 2022-04-07 05:25

from django.db import migrations, models
import mobi58.models


class Migration(migrations.Migration):

    dependencies = [
        ('mobi58', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleregister',
            name='insurance_file',
            field=models.FileField(blank=True, null=True, upload_to='file/', validators=[mobi58.models.validate_file_size]),
        ),
        migrations.AddField(
            model_name='vehicleregister',
            name='insurance_validity',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicleregister',
            name='pollution_file',
            field=models.FileField(blank=True, null=True, upload_to='file/', validators=[mobi58.models.validate_file_size]),
        ),
        migrations.AddField(
            model_name='vehicleregister',
            name='pollution_validity',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vehicleregister',
            name='rc_file',
            field=models.FileField(blank=True, null=True, upload_to='file/', validators=[mobi58.models.validate_file_size]),
        ),
        migrations.AddField(
            model_name='vehicleregister',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('two_wheeler', 'Two-Wheeler'), ('three_wheeler', 'Three-Wheeler'), ('pending', 'Four-Wheeler')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicleregister',
            name='fuel_type',
            field=models.CharField(blank=True, choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('cng', 'CNG'), ('electric', 'Electric')], max_length=20, null=True),
        ),
    ]
