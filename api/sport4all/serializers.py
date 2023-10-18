from rest_framework import serializers
from . import models

class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrecioH
        fields = '__all__'


class IvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Iva
        fields = '__all__'
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Producto
        fields = '__all__'
        
class ProvedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Provedor
        fields = '__all__'
        
class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Compra
        fields = '__all__'
        
class CompraProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompraProducto
        fields = '__all__'
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'
        
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Venta
        fields = '__all__'
        
class VentaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VentaProducto
        fields = '__all__'
        
class DevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Devolucion
        fields = '__all__'
        
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inventario
        fields = '__all__'
        
class FotoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FotoProducto
        fields = '__all__'
        