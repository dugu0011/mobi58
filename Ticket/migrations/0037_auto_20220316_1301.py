# Generated by Django 3.0.8 on 2022-03-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0036_auto_20220316_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiseticket',
            name='status',
            field=models.CharField(blank=True, choices=[('Hold', 'Hold'), ('Re-open', 'Re-open'), ('Active', 'Active'), ('Closed', 'Closed'), ('Complete', 'Complete'), ('WIP', 'WIP')], max_length=30, null=True),
        ),
    ]