# Generated by Django 3.0.8 on 2022-02-14 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0018_remove_comment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automation',
            name='time_period',
            field=models.CharField(blank=True, choices=[('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='raiseticket',
            name='time_period',
            field=models.CharField(blank=True, choices=[('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=50, null=True),
        ),
    ]
