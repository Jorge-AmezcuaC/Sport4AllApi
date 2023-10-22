from django.contrib import admin
from django.db.models import F
from django import forms

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
    search_fields = ('producto__nombre', 'producto__marca__nombre')

class ProvedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')
    search_fields = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca')
    search_fields = ('nombre',)

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
    search_fields = ('nombre',)

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('cp', 'calle', 'usuario')
    search_fields = ('cp',)

class FotoProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto')
    search_fields = ('producto__producto__nombre',)

class PruebasDevolucionAdmin(admin.ModelAdmin):
    list_display = ('id', 'devolucion')
    search_fields = ('devolucion__id',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username',)
    list_filter = ('role',)

class DevolucionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'status', 'venta')
    search_fields = ('venta__id',)
    list_filter = ('status',)

class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'status', 'proveedor', 'subtotal', 'total')
    list_filter = ('status',)
    search_fields = ('id', 'fecha', 'proveedor__nombre')

class CompraProductoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'compra', 'subtotal')
    list_filter = ('compra',)
    search_fields = ('compra__id',)

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'status', 'cliente', 'repartidor', 'total')
    list_filter = ('status',)
    search_fields = ('id', 'fecha', 'cliente__username', 'repartidor__username')

class PrecioHistoricoAdmin(admin.ModelAdmin):
    list_display = ('producto', 'precio', 'fecha')
    search_fields = ('fecha', 'producto__producto__nombre')