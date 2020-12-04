# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('', views.PublikasiList.as_view()),
    path('<int:pk>/', views.PublikasiDetail.as_view()),
]