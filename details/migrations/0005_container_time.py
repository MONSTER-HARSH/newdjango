# Generated by Django 3.2.18 on 2023-03-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_auto_20230301_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='time',
            field=models.DateTimeField(default=0),
        ),
    ]