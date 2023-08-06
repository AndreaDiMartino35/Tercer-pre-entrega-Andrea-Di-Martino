from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del cliente", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido del cliente", max_length=50, required=True)
    email = forms.EmailField(label="Email del cliente", required=True)

class RestauranteForm(forms.Form):
    nombre = forms.CharField(label="Nombre del restaurante", max_length=50, required=True)
    numero_de_pedido = forms.IntegerField(label="Número de pedido", required=True)

class RepartidorForm(forms.Form):
    nombre = forms.CharField(label="Nombre del repartidor", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido del repartidor", max_length=50, required=True)
    email = forms.EmailField(label="Email del repartidor", required=True) 