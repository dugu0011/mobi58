# Generated by Django 3.0.8 on 2021-08-24 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210824_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='crusherdetail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_crushers_detail', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='minedetail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_mines_detail', to=settings.AUTH_USER_MODEL),
        ),
    ]
