# Generated by Django 3.0.8 on 2022-06-28 10:36

from django.db import migrations, models
import django.db.models.deletion
import mobi58.models


class Migration(migrations.Migration):

    dependencies = [
        ('mobi58', '0006_auto_20220516_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transporter',
            name='cin_file',
            field=models.FileField(blank=True, null=True, upload_to='transporter/', validators=[mobi58.models.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='transporter',
            name='gst_file',
            field=models.FileField(blank=True, null=True, upload_to='transporter/', validators=[mobi58.models.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='transporter',
            name='pan_file',
            field=models.FileField(blank=True, null=True, upload_to='transporter/', validators=[mobi58.models.validate_file_size]),
        ),
        migrations.CreateModel(
            name='addTrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, choices=[('dilpura', 'DILPURA'), ('banar', 'BANAR'), ('naurangpur', 'nauramgpur')], max_length=50, null=True)),
                ('destination', models.CharField(blank=True, choices=[('jaipur', 'JAIPUR'), ('ahmedabad', 'AHMEDABAD'), ('delhi', 'DELHI')], max_length=50, null=True)),
                ('approx_distance', models.PositiveIntegerField()),
                ('Fixed_amount_btw_s_d', models.PositiveIntegerField()),
                ('transporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mobi58.Transporter')),
                ('vehicle', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='mobi58.vehicleRegister')),
            ],
        ),
    ]