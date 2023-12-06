from django.contrib import admin
from . import models
from .models import TallaProducto
from .forms import (
    TallaProductoAdmin,
    TallaProductoAdmin, 
    ProvedorAdmin, 
    ProductoAdmin, 
    MarcaAdmin, 
    DireccionAdmin,
    UserAdmin,
    DevolucionAdmin,
    CompraAdmin,
    VentaAdmin,
    
    )

admin.site.site_header = 'Sport4All Administration'
admin.site.site_title = 'Sport4All'
# admin.site.disable_action('delete_selected')

#No necesitan personalizado
admin.site.register(models.Iva)
admin.site.register(models.Color)

#genericos

admin.site.register(models.Provedor ,ProvedorAdmin)
admin.site.register(models.Producto ,ProductoAdmin)
admin.site.register(models.Marca ,MarcaAdmin)
admin.site.register(models.Direccion ,DireccionAdmin)

#Con Filtros
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Devolucion, DevolucionAdmin)
admin.site.register(models.Compra, CompraAdmin)
admin.site.register(models.Venta, VentaAdmin)
admin.site.register(TallaProducto, TallaProductoAdmin)


