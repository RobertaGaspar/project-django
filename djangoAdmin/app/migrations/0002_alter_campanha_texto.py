# Generated by Django 3.2.9 on 2021-11-28 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campanha',
            name='texto',
            field=models.CharField(max_length=500),
        ),
    ]
