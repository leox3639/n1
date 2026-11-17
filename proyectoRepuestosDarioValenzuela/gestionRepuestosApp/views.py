from django.contrib import admin
from .models import Proveedor, OrdenServicio
from django.shortcuts import render


def index_view(request):
    proveedores = Proveedor.objects.all()
    ordenes = OrdenServicio.objects.all()
    
    context = {
        'proveedores': proveedores,
        'ordenes': ordenes,
    }
    return render(request, 'gestionRepuestosApp/index.html', context)