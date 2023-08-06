from django.contrib import admin
from .models import Cliente, Repartidor, Restaurante

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Repartidor)
admin.site.register(Restaurante)