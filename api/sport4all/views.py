from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
	
class IvaView(viewsets.ModelViewSet):
	queryset = models.Iva.objects.all()
	serializer_class = serializers.IvaSerializer
	
class ProductoView(viewsets.ModelViewSet):
	queryset = models.Producto.objects.all()
	serializer_class = serializers.ProductoSerializer
	
class ProvedorView(viewsets.ModelViewSet):
	queryset = models.Provedor.objects.all()
	serializer_class = serializers.ProvedorSerializer
	
class CompraView(viewsets.ModelViewSet):
	queryset = models.Compra.objects.all()
	serializer_class = serializers.CompraSerializer
	
class CompraProductoView(viewsets.ModelViewSet):
	queryset = models.CompraProducto.objects.all()
	serializer_class = serializers.CompraProductoSerializer
		
class VentaView(viewsets.ModelViewSet):
	queryset = models.Venta.objects.all()
	serializer_class = serializers.VentaSerializer
	
class VentaProductoView(viewsets.ModelViewSet):
	queryset = models.VentaProducto.objects.all()
	serializer_class = serializers.VentaProductoSerializer
	
class DevolucionView(viewsets.ModelViewSet):
	queryset = models.Devolucion.objects.all()
	serializer_class = serializers.DevolucionSerializer
	
class FotoProductoView(viewsets.ModelViewSet):
	queryset = models.FotoProducto.objects.all()
	serializer_class = serializers.FotoProductoSerializer

class PrecioHistoricoView(viewsets.ModelViewSet):
	queryset = models.PrecioHistorico.objects.all()
	serializer_class = serializers.PrecioHistoricoSerializer

class DireccionView(viewsets.ModelViewSet):
	queryset = models.Direccion.objects.all()
	serializer_class = serializers.DireccionSerializer

class UserView(viewsets.ModelViewSet):
	queryset = models.User.objects.all()
	serializer_class = serializers.UserSerializer

class MarcaView(viewsets.ModelViewSet):
	queryset = models.Marca.objects.all()
	serializer_class = serializers.MarcaSerializer

class TallaView(viewsets.ModelViewSet):
	queryset = models.Talla.objects.all()
	serializer_class = serializers.TallaSerializer

class TallaProductoView(viewsets.ModelViewSet):
	queryset = models.TallaProducto.objects.all()
	serializer_class = serializers.TallaProductoSerializer

class ProductoCarritoView(viewsets.ModelViewSet):
	queryset = models.ProductoCarrito.objects.all()
	serializer_class = serializers.ProductoCarritoSerializer

class PruebasDevolucionView(viewsets.ModelViewSet):
	queryset = models.PruebasDevolucion.objects.all()
	serializer_class = serializers.PruebasDevolucionSerializer