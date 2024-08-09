from django.shortcuts import render
from rest_framework import generics
from .models import Temperature
from .serializer import TemperatureSerializer

class TemperatureDetailView(generics.RetrieveAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

class TemperatureListView(generics.ListAPIView):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer
