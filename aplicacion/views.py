from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def repartidores(request):
    return render(request, "aplicacion/repartidores.html")

def restaurantes(request):
    return render(request, "aplicacion/restaurantes.html")

def clientes(request):
    ctx={"clientes": Cliente.objects.all()}
    return render(request, "aplicacion/clientes.html", ctx)