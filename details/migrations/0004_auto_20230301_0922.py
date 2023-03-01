# Generated by Django 3.2.18 on 2023-03-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_alter_container_container_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='container_location',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='container',
            name='container_size',
            field=models.IntegerField(choices=[(20, 20), (40, 40)], default=40),
        ),
    ]