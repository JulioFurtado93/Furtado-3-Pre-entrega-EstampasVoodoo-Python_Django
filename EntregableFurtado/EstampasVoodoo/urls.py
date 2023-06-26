from django.urls import path
from EstampasVoodoo.views import *

urlpatterns = [
    path('inicio/', inicio, name="Inicio"),
    path('clientes/', clientes, name="Clientes"),
    path('remeras/', remeras,name="Remeras"),
    path('tazas/', tazas, name="Tazas"),
    path('setCliente/', setCliente, name="setCliente"),
    path('getCliente/', getCliente, name="getCliente"),
    path('searchCliente/', searchCliente, name="searchCliente"),
]