# Generated by Django 3.0.8 on 2022-06-28 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobi58', '0007_auto_20220628_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addtrip',
            old_name='transporter',
            new_name='transporter_name',
        ),
    ]