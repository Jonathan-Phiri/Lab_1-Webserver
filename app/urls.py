from django.urls import path
from .views import TemperatureHumidityDetailView,  TemperatureHumidityListView, LatestTemperatureHumidityAPIView, TemperatureHumidityCreateAPIView, TemperatureHumidityCreateAPIView, temperature_monitor

urlpatterns = [
    path('temperatures/', TemperatureHumidityListView.as_view(), name='temperature-list'),
    path('temperatures/<int:pk>/', TemperatureHumidityDetailView.as_view(), name='temperature-detail'),
    path('createtemperatures/', TemperatureHumidityCreateAPIView.as_view(), name='temperature-create'),
    path('api/latest-temperature/', LatestTemperatureHumidityAPIView.as_view(), name='latest-temperature'),
    path('temperature-monitor/', temperature_monitor, name='temperature-monitor'),
]

