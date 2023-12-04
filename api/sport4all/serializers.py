from rest_framework import serializers
from . import models
from .models import TallaProducto

class IvaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Iva
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'

class TallaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TallaProducto
        fields = '__all__'
        depth = 2

class FotoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FotoProducto
        fields = [
            'id',
            'foto',
        ]
        
class ProductoSerializer(serializers.ModelSerializer):
    tallas = TallaProductoSerializer(read_only = True, many = True)
    fotos = FotoProductoSerializer(read_only = True, many = True)
    class Meta:
        model = models.Producto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'marca',
            'precio',
            'tallas',
            'fotos',
        ]
        depth = 1

class VentaProductoSerializer(serializers.ModelSerializer):
    producto = TallaProductoSerializer(read_only = True)
    productoid = serializers.PrimaryKeyRelatedField(write_only = True, 
    queryset = TallaProducto.objects.all(), source="producto")
    class Meta:
        model = models.VentaProducto
        fields = [
            'cantidad',
            'precioUnitario',
            'venta',
            'producto',
            'productoid',
        ]
        
class VentaSerializer(serializers.ModelSerializer):
    detalles = VentaProductoSerializer(read_only = True, many = True, )
    class Meta:
        model = models.Venta
        fields = [
            'id',
            'status',
            "fecha",
            "cliente",
            'repartidor',
            'subtotal',
            'total',
            'iva_importe',
            'detalles',
        ]
        
class DevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Devolucion
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Direccion
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    direcciones = DireccionSerializer(read_only = True, many = True)
    class Meta:
        model = models.User
        fields = [
            'id',
            'username',
            'username',
            'role',
            'email',
            'is_staff',
            'password',
            'direcciones',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

        def create(self, validated_data):
            user = models.User.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
                role=validated_data['role']
            )

            return user

class ProductoCarritoSerializer(serializers.ModelSerializer):
    producto = TallaProductoSerializer(read_only = True)
    productoId = serializers.PrimaryKeyRelatedField(write_only = True, queryset = TallaProducto.objects.all(), source="producto")
    class Meta:
        model = models.ProductoCarrito
        fields = [
            'id',
            'cantidad',
            'cliente',
            'producto',
            'productoId',
        ]

class PruebasDevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PruebasDevolucion
        fields = '__all__'

class AuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)