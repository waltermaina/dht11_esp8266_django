# front_end_app/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class DHT11Data(models.Model):
    temperature = models.FloatField(
        default=0.0,
        validators=[
            MaxValueValidator(100.0),
            MinValueValidator(0.0)
        ]
     )
    humidity = models.FloatField(
        default=0,
        validators=[
            MaxValueValidator(100.0),
            MinValueValidator(0.0)
        ]
     )
    time = models.DateTimeField(default=datetime.datetime.now,primary_key=True) # Time data was recorded

    def __str__(self):
        """A string representation of the model."""
        return "DHT11 data model"

# New model to handle data that has a record id
class NewDHT11Data(models.Model):
    record_id = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(2147483647),
            MinValueValidator(0)
        ],unique=True,primary_key=True
     )
    temperature = models.FloatField(
        default=0.0,
        validators=[
            MaxValueValidator(100.0),
            MinValueValidator(0.0)
        ]
     )
    humidity = models.FloatField(
        default=0,
        validators=[
            MaxValueValidator(100.0),
            MinValueValidator(0.0)
        ]
     )
    time = models.DateTimeField(default=datetime.datetime.now) # Time data was recorded

    class Meta:
        db_table = 'new_dht11_data'

    def __str__(self):
        """A string representation of the model."""
        return f"Record ID {self.record_id}"