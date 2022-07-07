# Generated by Django 3.0.8 on 2021-10-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20211004_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclemaster',
            name='fuel_type',
            field=models.CharField(choices=[('deisel', 'Diesel'), ('petrol', 'Petrol'), ('cng', 'CNG'), ('electric', 'Electric')], default='deisel', max_length=200),
        ),
        migrations.AlterField(
            model_name='vehiclemaster',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('tractor', 'Tractor'), ('truck 6 tyres', 'Truck 6 Tyres'), ('truck 10 tyres', 'Truck 10 Tyres'), ('truck 12 tyres', 'Truck 12 Tyres'), ('truck 14 tyres', 'Truck 14 Tyres'), ('truck 16 tyres', 'Truck 16 Tyres'), ('truck 18 tyres', 'Truck 18 Tyres'), ('truck 20 tyres', 'Truck 20 Tyres'), ('truck 22 tyres', 'Truck 22 Tyres'), ('truck 24 tyres', 'Truck 24 Tyres'), ('trailer', 'Trailer')], max_length=200, null=True),
        ),
    ]
