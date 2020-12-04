# api/serializers.py
from rest_framework import serializers
from .models import Publikasi


class PublikasiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publikasi
        fields = ('judul', 'pranala',)