from django.contrib import admin
from django.db.models import F
from . import models
from .models import TallaProducto

#No necesitan personalizado
admin.site.register(models.Talla)
admin.site.register(models.Iva)
admin.site.register(models.Color)

#genericos
admin.site.register(models.Provedor)
admin.site.register(models.Producto)
admin.site.register(models.FotoProducto)
admin.site.register(models.PruebasDevolucion)
admin.site.register(models.Marca)
admin.site.register(models.Direccion)

admin.site.register(models.PrecioHistorico)
admin.site.register(models.Compra)
admin.site.register(models.CompraProducto)
admin.site.register(models.Venta)
admin.site.register(models.Devolucion)
admin.site.register(models.User)

class StockMinFilter(admin.SimpleListFilter):
    title = 'Stock Menor al Mínimo'
    parameter_name = 'stock_min_filter'

    def lookups(self, request, model_admin):
        return (
            ('below_min', 'Debajo del Mínimo'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'below_min':
            return queryset.filter(cantidadInventario__lt=F('minStock'))
        return queryset

class TallaProductoAdmin(admin.ModelAdmin):
    list_filter = (StockMinFilter, 'talla',)
    list_display = ('producto', 'talla', 'cantidadInventario', 'minStock', 'maxStock')
    search_fields = ('producto__nombre', 'talla__nombre')
    
admin.site.register(TallaProducto, TallaProductoAdmin)