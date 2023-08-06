from django.db import models

# Create your models here.
class Restaurante(models.Model):
    nombre=models.CharField(max_length=50)
    numero_de_pedido=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - ({self.numero_de_pedido})"

class Repartidor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.email}"

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.email}"