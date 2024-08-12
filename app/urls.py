from django.urls import path
from .views import TemperatureDetailView,  TemperatureListView, LatestTemperatureAPIView, TemperatureCreateAPIView, temperature_monitor

urlpatterns = [
    path('temperatures/', TemperatureListView.as_view(), name='temperature-list'),
    path('temperatures/<int:pk>/', TemperatureDetailView.as_view(), name='temperature-detail'),
    path('temperatures/', TemperatureCreateAPIView.as_view(), name='temperature-create'),
    path('api/latest-temperature/', LatestTemperatureAPIView.as_view(), name='latest-temperature'),
    path('temperature-monitor/', temperature_monitor, name='temperature-monitor'),
]

