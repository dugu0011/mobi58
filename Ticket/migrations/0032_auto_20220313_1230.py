# Generated by Django 3.0.8 on 2022-03-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0031_auto_20220313_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiseticket',
            name='assigned_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
