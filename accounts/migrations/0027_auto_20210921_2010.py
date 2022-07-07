# Generated by Django 3.0.8 on 2021-09-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20210918_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcustomer',
            name='kaata_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_type',
            field=models.CharField(choices=[('kaata', 'Kaata'), ('client', 'Client'), ('vendor', 'Vendor'), ('mine', 'Mine'), ('crusher', 'Crusher'), ('minecrusher', 'Mine&Crusher'), ('contractor', 'Contractor'), ('transporter', 'Transporter'), ('individual', 'Individual'), ('properitor', 'Properitor'), ('partner', 'Partner'), ('llp', 'LLP'), ('pvt_ltd', 'PVT LTD'), ('ltd', 'LTD')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='customer_category',
            field=models.CharField(choices=[('kaata', 'Kaata'), ('client', 'Client'), ('vendor', 'Vendor'), ('mine', 'Mine'), ('crusher', 'Crusher'), ('minecrusher', 'Mine&Crusher'), ('contractor', 'Contractor'), ('transporter', 'Transporter'), ('individual', 'Individual'), ('properitor', 'Properitor'), ('partner', 'Partner'), ('llp', 'LLP'), ('pvt_ltd', 'PVT LTD'), ('ltd', 'LTD')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='customer_type',
            field=models.CharField(choices=[('kaata', 'Kaata'), ('client', 'Client'), ('vendor', 'Vendor'), ('mine', 'Mine'), ('crusher', 'Crusher'), ('minecrusher', 'Mine&Crusher'), ('contractor', 'Contractor'), ('transporter', 'Transporter'), ('individual', 'Individual'), ('properitor', 'Properitor'), ('partner', 'Partner'), ('llp', 'LLP'), ('pvt_ltd', 'PVT LTD'), ('ltd', 'LTD')], max_length=50, null=True),
        ),
    ]