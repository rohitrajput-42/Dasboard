# Generated by Django 3.1.2 on 2020-11-25 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20201125_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='etd',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='data',
            name='startdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]