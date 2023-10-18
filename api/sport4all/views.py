from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers


class PrecioView(viewsets.ModelViewSet):
	queryset = models.PrecioH.objects.all()
	serializer_class = serializers.PrecioSerializer

	
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
	
class ClienteView(viewsets.ModelViewSet):
	queryset = models.Cliente.objects.all()
	serializer_class = serializers.ClienteSerializer
	
class VentaView(viewsets.ModelViewSet):
	queryset = models.Venta.objects.all()
	serializer_class = serializers.VentaSerializer
	
class VentaProductoView(viewsets.ModelViewSet):
	queryset = models.VentaProducto.objects.all()
	serializer_class = serializers.VentaProductoSerializer
	
class DevolucionView(viewsets.ModelViewSet):
	queryset = models.Devolucion.objects.all()
	serializer_class = serializers.DevolucionSerializer
	
class InventarioView(viewsets.ModelViewSet):
	queryset = models.Inventario.objects.all()
	serializer_class = serializers.InventarioSerializer
	
class FotoProductoView(viewsets.ModelViewSet):
	queryset = models.FotoProducto.objects.all()
	serializer_class = serializers.FotoProductoSerializer
