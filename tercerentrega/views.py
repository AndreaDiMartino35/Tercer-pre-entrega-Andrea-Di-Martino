from django.http import HttpResponse
from aplicacion.models import cliente

def crear_cliente(request, nombre, apellido, email):
    cliente= cliente(nombre=pnombre, apellido=papellido, email=pemail)
    cliente.save
    respuesta=f"El cliente es {cliente.nombre} de apellido {cliente.apellido} cuyo email es {cliente.email}"
    return HttpResponse(respuesta)

    