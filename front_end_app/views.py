from django.shortcuts import render
from django.http import JsonResponse
from . import models
from api_app import serializers

def home(request):
    return render(request, 'home.html')

def humidity(request):
    return render(request, 'humidity.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contactus.html')

def temperature_chart(request):
    labels = []
    data = []
    # Get the last n records
    queryset = models.DHT11Data.objects.all().order_by('-time')[:24]
    # Sort them in ascending order
    queryset = reversed(queryset)
    # There was a need to serilize the data
    serializer = serializers.Dht11DataSerializer(queryset, many=True)
    for entry in serializer.data:
        time_rec = entry['time']
        tim_rec_no_time_zone = time_rec.replace(":00+03:00","")
        labels.append(tim_rec_no_time_zone)
        #labels.append(entry['time'])
        data.append(entry['temperature'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def humidity_chart(request):
    labels = []
    data = []
    # Get the last n records
    queryset = models.DHT11Data.objects.all().order_by('-time')[:24]
    # Sort them in ascending order
    queryset = reversed(queryset)
    # There was a need to serilize the data
    serializer = serializers.Dht11DataSerializer(queryset, many=True)
    for entry in serializer.data:
        time_rec = entry['time']
        tim_rec_no_time_zone = time_rec.replace(":00+03:00","")
        labels.append(tim_rec_no_time_zone)
        #labels.append(entry['time'])
        data.append(entry['humidity'])
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
