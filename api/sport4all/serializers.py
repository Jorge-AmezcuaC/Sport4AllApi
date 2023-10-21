from rest_framework import serializers
from . import models

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
        
class CompraProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompraProducto
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    compra_producto = CompraProductoSerializer(source='compraproducto_set', many=True, read_only=True)
    class Meta:
        model = models.Compra
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
        
class FotoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FotoProducto
        fields = '__all__'
        
class PrecioHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrecioHistorico
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Direccion
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'

class TallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Talla
        fields = '__all__'

class TallaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TallaProducto
        fields = '__all__'

class ProductoCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductoCarrito
        fields = '__all__'

class PruebasDevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PruebasDevolucion
        fields = '__all__'