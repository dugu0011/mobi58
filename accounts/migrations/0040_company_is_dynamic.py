# Generated by Django 3.0.8 on 2021-10-23 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_newcustomer_customer_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_dynamic',
            field=models.BooleanField(default=False),
        ),
    ]
