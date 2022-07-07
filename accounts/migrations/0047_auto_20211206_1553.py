# Generated by Django 3.0.8 on 2021-12-06 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_company_contact_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmaster',
            name='category',
        ),
        migrations.AddField(
            model_name='productmaster',
            name='base_bill_rate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='base_sale_rate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='bill_royalty_charges',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='crusher_mine',
            field=models.CharField(blank=True, choices=[('crusher', 'Crusher'), ('mines', 'Mines')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='hsn_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_hsn_code', to='accounts.HsnCode'),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='sale_royalty_charges',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='unit_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_unit', to='accounts.UnitType', verbose_name='UOM'),
        ),
        migrations.CreateModel(
            name='BaseProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(blank=True, max_length=100, null=True)),
                ('company_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_product_base', to='accounts.Company')),
                ('customer_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_product_basbe', to='accounts.NewCustomer')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_product_base', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='productmaster',
            name='product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_products_master', to='accounts.BaseProduct'),
        ),
    ]
