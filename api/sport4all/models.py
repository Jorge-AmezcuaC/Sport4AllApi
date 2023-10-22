from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.utils import timezone
# from .customPermissions import *

class UserManager(BaseUserManager):

    def create_user(self, username, email, password, role):
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, role):
        user = self.create_user(username, email, password, role='administrador')
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLES = (
        ('cliente', 'Cliente'),
        ('almacenista', 'Almacenista'),
        ('repartidor', 'Repartidor'),
        ('administrador', 'Administrador'),
    )
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=15, choices=ROLES, default='cliente')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'role',
    ]

    
    def __str__(self):
        return f"{self.username}"
    
class Direccion(models.Model):
    cp = models.CharField(max_length=5)
    calle = models.CharField(max_length=20)
    numeroExterno = models.CharField(max_length=5)
    numeroInterno = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.cp} {self.calle}"

class Marca(models.Model):
    nombre = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"
    
class Color(models.Model):
    nombre = models.CharField(max_length=20)
    codigoHex = models.CharField(max_length=7)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"

class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.marca}"

class Talla(models.Model):
    tallas = [
        ('XL', 'XL'),
        ('X', 'X'),
        ('M', 'M'),
        ('S', 'S'),
        ('XS', 'XS')
    ]
    talla = models.CharField(max_length=2, choices=tallas)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.talla}"

class TallaProducto(models.Model):
    cantidadInventario = models.IntegerField(default=0)
    minStock = models.IntegerField()
    maxStock = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.producto, self.talla} min:{self.minStock} max:{self.maxStock} stock:{self.cantidadInventario}"
    
class PrecioHistorico(models.Model):
    precio = models.FloatField()
    fecha = models.DateField(default=timezone.now)
    producto = models.ForeignKey(TallaProducto, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.precio}$ {self.producto.producto.nombre} {self.producto.talla} {self.producto.color}"

class FotoProducto(models.Model):
    foto = models.ImageField(upload_to='producto')
    producto = models.ForeignKey(TallaProducto, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.producto}"
    
class Iva(models.Model):
    porcentaje = models.FloatField()
    fecha = models.DateField(default=timezone.now)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.porcentaje}"
    
class Provedor(models.Model):
    nombre = models.CharField(max_length=25)
    correo = models.EmailField(unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre}"
    
    
class ProductoCarrito(models.Model):
    cantidad = models.IntegerField()
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(PrecioHistorico, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.cantidad} {self.producto}"
    
class Venta(models.Model):
    statusChoices = (
        ('procesando', 'PROCESANDO'),
        ('preparando', 'PREPARANDO'),
        ('en transito', 'EN TRANSITO'),
        ('entregado', 'ENTREGADO'),
    )
    status = models.CharField(max_length=20, choices=statusChoices, default='procesando')
    fecha = models.DateField(default=timezone.now)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras_totales')
    iva = models.ForeignKey(Iva, on_delete=models.CASCADE)
    repartidor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='pedidos_repartidos')
    subtotal = models.FloatField(null=True)
    total = models.FloatField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} {self.fecha} {self.status} {self.cliente}"
    
class VentaProducto(models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(PrecioHistorico, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    subtotal = models.FloatField(null=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad * self.producto.precio
        
        super(VentaProducto, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.cantidad} {self.producto}"

class Devolucion(models.Model):
    statusChoices = (
        ('pendiente', 'PENDIENTE'),
        ('aceptada', 'ACEPTADA'),
        ('rechazada', 'RECHAZADA'),
        ('finalizada', 'FINALIZADA'),
    )
    fecha = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=statusChoices, default='pendiente')
    descripcion = models.CharField(max_length=250)
    venta = models.ForeignKey(VentaProducto, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.status} {self.venta}"
    
class PruebasDevolucion(models.Model):
    foto = models.ImageField()
    devolucion = models.ForeignKey(Devolucion, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} {self.devolucion}"
    
class Compra(models.Model):
    statusChoices = (
        ('en proceso', 'EN PROCESO'),
        ('entregado', 'ENTREGADO'),
        ('cancelado', 'CANCELADO'),
        ('pagado', 'PAGADO'),
    )
    status = models.CharField(max_length=20, choices=statusChoices, default='en proceso')
    fecha = models.DateField(default=timezone.now)
    proveedor = models.ForeignKey(Provedor, on_delete=models.CASCADE)
    iva = models.ForeignKey(Iva, on_delete=models.CASCADE)
    subtotal = models.FloatField(null=True)
    total = models.FloatField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk} {self.status} {self.fecha}"
    
class CompraProducto(models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(TallaProducto, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    subtotal = models.FloatField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.cantidad} {self.producto}"