from django.urls import path
from . import views

urlpatterns = [
    path('', views.tell_me, name='tell_me'),
    path('page2/', views.tell_me2, name='tell_me2'),
]
