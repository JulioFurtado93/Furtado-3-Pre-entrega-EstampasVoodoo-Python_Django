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