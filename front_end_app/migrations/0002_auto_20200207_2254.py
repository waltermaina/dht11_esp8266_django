# Generated by Django 3.0.3 on 2020-02-07 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_end_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dht11data',
            name='id',
        ),
        migrations.AddField(
            model_name='dht11data',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now, primary_key=True, serialize=False),
        ),
    ]
