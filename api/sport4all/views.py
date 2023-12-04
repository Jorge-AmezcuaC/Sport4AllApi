from rest_framework import viewsets
from . import models, serializers
from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
	
class IvaView(viewsets.ModelViewSet):
	queryset = models.Iva.objects.all()
	serializer_class = serializers.IvaSerializer
	
class ProductoView(viewsets.ModelViewSet):
	queryset = models.Producto.objects.all().order_by('id')
	serializer_class = serializers.ProductoSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['nombre']
	
class VentaView(viewsets.ModelViewSet):
	queryset = models.Venta.objects.all()
	serializer_class = serializers.VentaSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['cliente__id']
	
class VentaProductoView(viewsets.ModelViewSet):
	queryset = models.VentaProducto.objects.all()
	serializer_class = serializers.VentaProductoSerializer
	
class DevolucionView(viewsets.ModelViewSet):
	queryset = models.Devolucion.objects.all()
	serializer_class = serializers.DevolucionSerializer
	
class FotoProductoView(viewsets.ModelViewSet):
	queryset = models.FotoProducto.objects.all()
	serializer_class = serializers.FotoProductoSerializer

class DireccionView(viewsets.ModelViewSet):
	queryset = models.Direccion.objects.all()
	serializer_class = serializers.DireccionSerializer

class MarcaView(viewsets.ModelViewSet):
	queryset = models.Marca.objects.all()
	serializer_class = serializers.MarcaSerializer

class TallaProductoView(viewsets.ModelViewSet):
	queryset = models.TallaProducto.objects.all()
	serializer_class = serializers.TallaProductoSerializer

class ProductoCarritoView(viewsets.ModelViewSet):
	queryset = models.ProductoCarrito.objects.all()
	serializer_class = serializers.ProductoCarritoSerializer
	filter_backends = [filters.SearchFilter]
	search_fields = ['cliente__id']

class PruebasDevolucionView(viewsets.ModelViewSet):
	queryset = models.PruebasDevolucion.objects.all()
	serializer_class = serializers.PruebasDevolucionSerializer

class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

    def perform_create(self, serializer):
        try:
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
        except Exception as exc:
            return Response({'error':'Error desconocido'},status=status.HTTP_400_BAD_REQUEST)
        

    def perform_update(self, serializer):
        try:
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()
        except Exception as exc:
            return Response({'error':'Error desconocido'},status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(user.password)
        user.save()

        token, created = Token.objects.get_or_create(user=user)
        response_data = {
            'token': token.key,
            'user': serializers.UserSerializer(user).data,
            'mensaje': 'Registro exitoso',
        }

        if created:
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(response_data, status=status.HTTP_201_CREATED)

class UserLoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        try:
            login_serializer = self.serializer_class(
                data=request.data,
                context={'request': request}
            )
            if login_serializer.is_valid():
                user = login_serializer.validated_data['user']
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = serializers.AuthSerializer(user)
                if created:
                    return Response({
                        'token': token.key,
                        'user': serializers.UserSerializer(user).data,
                        'mensaje': 'Inicio de sesion exitoso',
                    }, status=status.HTTP_201_CREATED)
                else:
                    token = Token.objects.get(user=user)
                    return Response({
                        'token': token.key,
                        'user': serializers.UserSerializer(user).data,
                        'mensaje': 'Inicio de sesion exitoso',
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({'mensaje': 'El usuario o la contraseña es '
                                            'incorrecta'},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            print(exc)
            return Response({'error':'Error desconocido'},status=status.HTTP_400_BAD_REQUEST)