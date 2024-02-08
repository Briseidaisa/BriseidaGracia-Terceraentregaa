from django import forms
from .models import Producto, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'

class BuscarForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar')
