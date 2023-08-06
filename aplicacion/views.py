from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def repartidores(request):
    ctx={"repartidores": Repartidor.objects.all()}
    return render(request, "aplicacion/repartidores.html", ctx)

def restaurantes(request):
    ctx={"restaurantes": Restaurante.objects.all()}
    return render(request, "aplicacion/restaurantes.html", ctx)

def clientes(request):
    ctx={"clientes": Cliente.objects.all()}
    return render(request, "aplicacion/clientes.html", ctx)

def clienteForm(request):
    if request.method == "POST":
        cliente = Cliente(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])
        cliente.save()
    return HttpResponse("El cliente se grabó con éxito!")

    return render(request, "aplicacion/clienteForm.html")

def clienteForm2(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            cliente = Cliente(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            cliente.save()
            return render(request, "aplicacion/base.html")
        else:
            miForm = ClienteForm()
    miForm= ClienteForm()

    return render(request, "aplicacion/clienteForm2.html", {"form":miForm})

def buscarEmail(request):
    return render(request, "aplicacion/buscarEmail.html")

def buscar2(request):
    if request.GET['email']:
        email = request.GET['email']
        clientes = Cliente.objects.filter(email__icontains=email)
        return render(request, "aplicacion/resultadosEmail.html", {"email": email, "clientes": clientes})
    return HttpResponse("No se ingresaron datos para buscar")

def restauranteForm(request):
    if request.method == "POST":
        restaurante = Restaurante(nombre=request.POST['nombre'], numero_de_pedido=request.POST['numero_de_pedido'], email=request.POST['email'])
        restaurante.save()
    return HttpResponse("El restaurante se grabó con éxito!")
    return render(request, "aplicacion/restauranteForm.html")

def restauranteForm2(request):
    if request.method == "POST":
        miForm = RestauranteForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            restaurante = Restaurante(nombre = informacion['nombre'], numero_de_pedido = informacion['numero_de_pedido'])
            restaurante.save()
            return render(request, "aplicacion/base.html")
        else:
            miForm = RestauranteForm()
    miForm= RestauranteForm()

    return render(request, "aplicacion/restauranteForm2.html", {"form":miForm})

def repartidorForm(request):
    if request.method == "POST":
        repartidor = Repartidor(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])
        repartidor.save()
    return HttpResponse("El repartidor se grabó con éxito!")

    return render(request, "aplicacion/repartidorForm.html")

def repartidorForm2(request):
    if request.method == "POST":
        miForm = RepartidorForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            repartidor = Repartidor(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])
            repartidor.save()
            return render(request, "aplicacion/base.html")
        else:
            miForm = RepartidorForm()
    miForm= RepartidorForm()

    return render(request, "aplicacion/repartidorForm2.html", {"form":miForm})


