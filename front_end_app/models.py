# front_end_app/models.py
from django.db import models


class DHT11Data(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    time = models.DateTimeField(primary_key=True) # Time data was recorded

    def __str__(self):
        """A string representation of the model."""
        return "DHT11 data model"
