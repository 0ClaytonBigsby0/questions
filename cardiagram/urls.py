from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_diagram, name='car_diagram'),
]
