# Generated by Django 3.0.8 on 2022-03-14 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0033_comment_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='raiseticket',
            name='category',
            field=models.CharField(blank=True, choices=[('CNM', 'CNM'), ('CNM58', 'CNM58'), ('ULTRACON', 'ULTRACON'), ('TECH58', 'TECH58'), ('HR58', 'HR58')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='raiseticket',
            name='subcategory',
            field=models.CharField(blank=True, choices=[('CNM', 'CNM'), ('CNM58', 'CNM58'), ('ULTRACON', 'ULTRACON'), ('TECH58', 'TECH58'), ('HR58', 'HR58')], max_length=50, null=True),
        ),
    ]
