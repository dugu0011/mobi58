# Generated by Django 3.0.8 on 2022-03-09 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0021_raiseticket_assigned_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='raiseticket',
            old_name='img',
            new_name='imgs',
        ),
    ]
