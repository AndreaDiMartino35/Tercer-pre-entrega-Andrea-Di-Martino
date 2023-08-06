from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('repartidores/', repartidores, name="repartidores"),
    path('restaurantes/', restaurantes, name="restaurantes"),
    path('clientes/', clientes, name="clientes"),

    path('cliente_form/', clienteForm, name="cliente_form"),
    path('cliente_form2/', clienteForm2, name="cliente_form2"),

    path('restaurante_form/', restauranteForm, name="restaurante_form"),
    path('restaurante_form2/', restauranteForm2, name="restaurante_form2"),

    path('repartidor_form/', repartidorForm, name="repartidor_form"),
    path('repartidor_form2/', repartidorForm2, name="repartidor_form2"),

    path('buscar_email/', buscarEmail, name="buscar_email"),
    path('buscar2', buscar2, name="buscar2"),
]