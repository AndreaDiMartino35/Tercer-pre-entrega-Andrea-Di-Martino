from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def repartidores(request):
    return render(request, "aplicacion/repartidores.html")

def restaurantes(request):
    return render(request, "aplicacion/restaurantes.html")

def proveedores(request):
    return render(request, "aplicacion/proveedores.html")