# api_app/views.py
from rest_framework import generics

from front_end_app import models
from . import serializers

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import datetime

"""
class ListData(generics.ListCreateAPIView):
    queryset = models.DHT11Data.objects.all()
    serializer_class = serializers.Dht11DataSerializer


class DetailData(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DHT11Data.objects.all()
    serializer_class = serializers.Dht11DataSerializer
"""

"""
List all snippets, or create a new snippet.
"""
class ListData(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
    	queryset = models.DHT11Data.objects.all()
    	serializer = serializers.Dht11DataSerializer(queryset, many=True)
    	return Response(serializer.data)
    def post(self, request, format=None):
    	# Convert received time from seconds to datetime format
        newDataDict = request.data
        print(newDataDict)
        time_seconds = newDataDict['time']
        old_time = datetime.datetime.now().replace(microsecond=0)
        new_time = old_time - datetime.timedelta(seconds=int(time_seconds))
        newDataDict['time'] = str(new_time)

        serializer = serializers.Dht11DataSerializer(data=newDataDict)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataDetail(APIView):
    """
    Retrieve, update or delete a data instance.
    """
    def get_object(self, pk):
        try:
            return models.DHT11Data.objects.get(pk=pk)
        except models.DHT11Data.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = serializers.Dht11DataSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = serializers.Dht11DataSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)