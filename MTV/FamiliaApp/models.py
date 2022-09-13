from django.db import models

class DatosFamilia(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    dni=models.IntegerField()
    genero=models.CharField(max_length=60)
    profesion=models.CharField(max_length=60)
    correo=models.EmailField()

