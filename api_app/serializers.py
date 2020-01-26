# api_app/serializers.py
from rest_framework import serializers
from front_end_app import models


class Dht11DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'temperature',
            'humidity',
            'time',
        )
        model = models.DHT11Data