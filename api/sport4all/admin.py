from django.contrib import admin
from . import models

admin.site.register(models.PrecioH)
admin.site.register(models.Iva)
admin.site.register(models.Producto)
admin.site.register(models.Provedor)
admin.site.register(models.Compra)
admin.site.register(models.CompraProducto)
admin.site.register(models.Cliente)
admin.site.register(models.Venta)
admin.site.register(models.VentaProducto)
admin.site.register(models.Devolucion)
admin.site.register(models.Inventario)
admin.site.register(models.FotoProducto)