# Generated by Django 3.1.2 on 2020-11-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='etd',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='startdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]