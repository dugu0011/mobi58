# Generated by Django 3.0.8 on 2021-09-10 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_newcustomer_customer_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerMine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mine_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mine_no', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('company_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_customermine', to='accounts.Company')),
                ('customer_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='new_customermine', to='accounts.NewCustomer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_customermine', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='newcustomer',
            name='customer_mine',
            field=models.ManyToManyField(to='accounts.CustomerMine'),
        ),
    ]
