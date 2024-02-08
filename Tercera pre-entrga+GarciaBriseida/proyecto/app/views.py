
from django.shortcuts import render, redirect
from .forms import ProductoForm, PedidoForm, BuscarForm
from .models import Producto, Pedido

def formulario_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario_producto')
    else:
        form = ProductoForm()
    return render(request, 'cafeteria_app/formulario_producto.html', {'form': form})

def formulario_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario_pedido')
    else:
        form = PedidoForm()
    return render(request, 'cafeteria_app/formulario_pedido.html', {'form': form})

def buscar(request):
    if request.method == 'GET':
        form = BuscarForm(request.GET)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            productos = Producto.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'cafeteria_app/buscar.html', {'productos': productos})
    else:
        form = BuscarForm()
    return render(request, 'cafeteria_app/buscar.html', {'form': form})
