from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import generics
from .models import Publikasi
from .serializers import PublikasiSerializer


class PublikasiList(generics.ListCreateAPIView):
    queryset = Publikasi.objects.all()
    serializer_class = PublikasiSerializer

class PublikasiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publikasi.objects.all()
    serializer_class = PublikasiSerializer