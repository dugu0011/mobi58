# Generated by Django 3.0.8 on 2022-03-09 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0026_auto_20220309_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiseticket',
            name='priority',
            field=models.CharField(blank=True, choices=[('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium')], max_length=50, null=True),
        ),
    ]
