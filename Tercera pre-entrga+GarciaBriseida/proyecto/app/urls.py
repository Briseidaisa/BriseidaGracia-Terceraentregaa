from django.urls import path
from . import views

urlpatterns = [
    path('formulario_producto/', views.formulario_producto, name='formulario_producto'),
    path('formulario_pedido/', views.formulario_pedido, name='formulario_pedido'),
    path('buscar/', views.buscar, name='buscar'),
]
    