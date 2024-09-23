from django.urls import path
from . import views

urlpatterns = [
    path('api/questions/', views.ShowMeQuestionList.as_view(), name='showme-question-list'),
    path('api/questions/<int:pk>/', views.ShowMeQuestionDetail.as_view(), name='showme-question-detail'),
    path('', views.show_me, name='show_me'),
]
