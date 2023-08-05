from django.db import models

# Create your models here.
class Restaurante(models.Model):
    nombre=models.CharField(max_length=50)
    numero_de_pedido=models.IntegerField()

class Repartidor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()