from django.shortcuts import render, redirect
from django.views.generic import ListView
from http import HttpResponse
from .models import Producto
from .forms import ProductoForm

import threading
import time

# Create your views here.
def hello_world(request):
    return render(request, 'pages/inicio.html')

def productos_list(request):
    productos = Producto.objects.all()
    formulario = ProductoForm(request.POST or None)

    if formulario.is_valid() and request.method == 'POST':
        producto = formulario.save(commit=False)
        producto.precio = float(formulario.cleaned_data['precio'])
        producto.existencias = int(formulario.cleaned_data['existencias'])
        formulario.save()
        return redirect('productos')
    return render(request, 'pages/productos.html', {'productos': productos, 'formulario': formulario})
    
def editar_producto(request, id):
    producto = Producto.objects.get(id = id)
    formulario = ProductoForm(request.POST or None, instance=producto)

    if formulario.is_valid() and request.POST:
        nuevo_producto = formulario.save(commit=False)
        nuevo_producto.precio = float(formulario.cleaned_data['precio'])
        nuevo_producto.existencias = int(formulario.cleaned_data['existencias'])
        formulario.save()
        return redirect('productos')
    return render(request, 'pages/editar_producto.html', {'formulario': formulario})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')
