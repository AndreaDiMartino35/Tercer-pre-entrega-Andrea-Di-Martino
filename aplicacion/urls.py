from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('repartidores', repartidores, name="repartidores"),
    path('restaurantes', restaurantes, name="restaurantes"),
    path('clientes', clientes, name="clientes"),
]