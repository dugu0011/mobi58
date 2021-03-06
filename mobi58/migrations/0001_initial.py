# Generated by Django 3.0.8 on 2022-04-06 11:01

from django.db import migrations, models
import django.db.models.deletion
import mobi58.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transporter_name', models.CharField(max_length=200)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('address', models.TextField(blank=True, max_length=500, null=True)),
                ('pan_no', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('pan_file', models.FileField(blank=True, null=True, upload_to='file/', validators=[mobi58.models.validate_file_size])),
                ('gst_no', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('gst_file', models.FileField(blank=True, null=True, upload_to='file/', validators=[mobi58.models.validate_file_size])),
                ('cin_no', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('cin_file', models.FileField(blank=True, null=True, upload_to='file/', validators=[mobi58.models.validate_file_size])),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='vehicleRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registeration_no', models.CharField(max_length=12, unique=True)),
                ('registeration_date', models.DateField()),
                ('registered_upto', models.DateField()),
                ('owner_name', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_model', models.CharField(blank=True, max_length=50, null=True)),
                ('vehicle_class', models.CharField(blank=True, max_length=50, null=True)),
                ('vehicle_color', models.CharField(blank=True, max_length=50, null=True)),
                ('engine_no', models.CharField(max_length=50, unique=True)),
                ('chasis_no', models.CharField(max_length=50, unique=True)),
                ('rto_details', models.CharField(blank=True, max_length=50, null=True)),
                ('fuel_type', models.CharField(blank=True, max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('trransporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobi58.Transporter')),
            ],
        ),
    ]
