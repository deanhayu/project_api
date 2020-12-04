from django.db import models

# Create your models here.
class Publikasi(models.Model):
    judul = models.CharField(max_length=255)
    pranala = models.TextField(max_length=500)
   # grade = models.CharField(max_length=255)
   # age = models.IntegerField()

    def __str__(self):
        return self.judul