# Generated by Django 3.0.8 on 2021-09-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20210921_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crusherdetail',
            name='customer_name',
        ),
        migrations.AddField(
            model_name='crusherdetail',
            name='customer_name',
            field=models.ManyToManyField(blank=True, to='accounts.NewCustomer'),
        ),
    ]
