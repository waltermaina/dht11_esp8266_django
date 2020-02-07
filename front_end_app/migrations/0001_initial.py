# Generated by Django 3.0.3 on 2020-02-07 19:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DHT11Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(default=0.0, validators=[django.core.validators.MaxValueValidator(100.0), django.core.validators.MinValueValidator(0.0)])),
                ('humidity', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(100.0), django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
    ]
