from django.http import HttpResponse
from django.shortcuts import render
from EstampasVoodoo.models import Cliente
from EstampasVoodoo.forms import formSetCliente

# Create your views here.

def inicio(request):
    return render(request, "EstampasVoodoo/inicio.html")

def clientes(request):
    return render(request, "EstampasVoodoo/clientes.html")

def remeras(request):
    return render(request, "EstampasVoodoo/remeras.html")

def tazas(request):
    return render(request, "EstampasVoodoo/tazas.html")

def setCliente(request):
    if request.method == 'POST':
        miFormulario = formSetCliente(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            cliente = Cliente(nombre=data["nombre"],apellido=data["apellido"],telefono=data["telefono"], email=data["email"])    
            cliente.save()
            return render(request,"EstampasVoodoo/inicio.html")    
    else:
        miFormulario = formSetCliente()
    return render(request, "EstampasVoodoo/setCliente.html", {"miFormulario":miFormulario})