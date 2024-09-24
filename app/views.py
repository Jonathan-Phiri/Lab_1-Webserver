from django.shortcuts import render
from rest_framework import generics
from .models import TemperatureHumidity
from .serializer import TemperatureHumiditySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class TemperatureHumidityDetailView(generics.RetrieveAPIView):
    queryset = TemperatureHumidity.objects.all()
    serializer_class = TemperatureHumiditySerializer

class TemperatureHumidityListView(generics.ListAPIView):
    queryset = TemperatureHumidity.objects.all()
    serializer_class = TemperatureHumiditySerializer


class TemperatureHumidityCreateAPIView(generics.CreateAPIView):
    queryset = TemperatureHumidity.objects.all()
    serializer_class = TemperatureHumiditySerializer

class LatestTemperatureHumidityAPIView(APIView):
    def get(self, request, *args, **kwargs):
        latest_record = TemperatureHumidity.objects.latest('timestamp')
        return Response({
            'temperature': latest_record.temperature,
            'humidity': latest_record.humidity
        })
    
def temperature_monitor(request):
    return render(request, 'temperature.html')

def humidity_monitor(request):
    return render(request, 'humidity.html')


def history_view(request):
    date_query = request.GET.get('date')
    
    if date_query:
        selected_date = datetime.strptime(date_query, "%Y-%m-%d").date()
        readings = TemperatureHumidity.objects.filter(timestamp__date=selected_date).order_by('-timestamp')
    else:
        readings = TemperatureHumidity.objects.all().order_by('-timestamp')
    return render(request, 'history.html', {'readings': readings, 'date_query': date_query})

def save_reading(temperature, humidity):
    reading = TemperatureHumidity(temperature=temperature, humidity=humidity)
    reading.save()



relay_state = False  # Initially, relay is OFF

@csrf_exempt
def relay_control_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Check if the command is sent
            if 'command' in data:
                command = data['command']
                if command == 'ON':
                    # Turn the relay ON (call your function or send signal to ESP32)
                    relay_state = True
                    return JsonResponse({'message': 'Relay turned ON'})
                elif command == 'OFF':
                    # Turn the relay OFF
                    relay_state = False
                    return JsonResponse({'message': 'Relay turned OFF'})
                else:
                    return JsonResponse({'error': 'Invalid command'}, status=400)

            # Check if the relay state is being toggled from the switch
            if 'relay_state' in data:
                relay_state = data['relay_state'] == 'true'
                # Toggle the relay (you can send a signal to ESP32 here)
                return JsonResponse({'message': f"Relay is {'ON' if relay_state else 'OFF'}"})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_relay_status(request):
    global relay_state

    # Return relay status as JSON
    return JsonResponse({'relay_state': relay_state})



