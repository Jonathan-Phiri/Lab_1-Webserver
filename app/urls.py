from django.urls import path
from .views import TemperatureDetailView,  TemperatureListView

urlpatterns = [
    path('temperatures/', TemperatureListView.as_view(), name='temperature-list'),
    path('temperatures/<int:pk>/', TemperatureDetailView.as_view(), name='temperature-detail'),
]
