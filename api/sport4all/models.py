from django.db import models

    
class PrecioH(models.Model):
    precio = models.FloatField()

    def __str__(self):
        return self.precio
    
class Iva(models.Model):
    porcentaje = models.FloatField()

    def __str__(self):
        return self.porcentaje
        
class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    precio = models.ForeignKey(PrecioH, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Provedor(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Compra(models.Model):
    status = models.CharField(max_length=20)
    fecha = models.DateField()
    proveedor = models.ForeignKey(Provedor, on_delete=models.CASCADE)
    iva = models.ForeignKey(Iva, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk
    
class CompraProducto(models.Model):
    cantidad = models.IntegerField()
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    compra = models.OneToOneField(Compra, on_delete=models.CASCADE)

    def __str__(self):
        return self.cantidad
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    status = models.CharField(max_length=20)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    iva = models.ForeignKey(Iva, on_delete=models.CASCADE)

    def __str__(self):
        return self.pk
    
class VentaProducto(models.Model):
    cantidad = models.IntegerField()
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE)

    def __str__(self):
        return self.cantidad

class Devolucion(models.Model):
    fecha = models.DateField()
    status = models.CharField(max_length=20)
    venta = models.OneToOneField(VentaProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.status
    
class Inventario(models.Model):
    cantidad = models.IntegerField()
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.cantidad

class FotoProducto(models.Model):
    foto = models.ImageField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
