from django.contrib import admin
from .models import TallaProducto, FotoProducto, CompraProducto, VentaProducto, Compra
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
    
class TallaProductoInline(admin.TabularInline):
    model = TallaProducto
    extra = 1
    readonly_fields = ('cantidadInventario', )

class FotoProductoInline(admin.TabularInline):  
    model = FotoProducto
    extra = 1 

class CompraProductoInLine(admin.TabularInline):
    autocomplete_fields = ('producto',)
    model = CompraProducto
    extra = 1

class VentaProductoInLine(admin.TabularInline):
    model = VentaProducto
    extra = 0

class TallaProductoAdmin(admin.ModelAdmin):
    list_filter = (StockMinFilter, 'talla',)
    list_display = ('producto', 'talla','cantidadInventario', 'minStock', 'maxStock',)
    search_fields = ('producto__nombre',)
    autocomplete_fields = ('producto',)
    readonly_fields = ('cantidadInventario', )

class ProvedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo')
    search_fields = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    inlines = [TallaProductoInline, FotoProductoInline]
    list_display = ('nombre', 'marca', 'precio')
    search_fields = ('nombre',)
    autocomplete_fields = ('marca',)
    fieldsets = (
        ('Producto', {
            'fields': ('nombre', 'descripcion', 'marca', 'precio')
        }),
    )

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', )
    search_fields = ('nombre',)

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('cp', 'calle', 'usuario')
    search_fields = ('cp','usuario')
    autocomplete_fields = ('usuario',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    search_fields = ('username',)
    list_filter = ('role',)

class DevolucionAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'status', 'venta')
    search_fields = ('venta__id',)
    list_filter = ('status',)

class CompraAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha', 'folio')
    list_display = ('id', 'fecha', 'status', 'proveedor')
    list_filter = ('status',)
    search_fields = ('id', 'fecha', 'proveedor__nombre')
    autocomplete_fields = ('proveedor',)
    inlines = [CompraProductoInLine]
    date_hierarchy = ('fecha')

    fieldsets = (
        (None, {'fields': ('folio', 'fecha', 'status', 'proveedor',)}),
    )

    def folio(self, obj=None):
        try:
            last_id = Compra.objects.latest('id').id
        except Compra.DoesNotExist:
            last_id = 0
        return last_id + 1

    folio.short_description = 'Folio'

class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha', 'status', 'cliente', 'repartidor',)
    list_filter = ('status',)
    search_fields = ('id', 'fecha', 'cliente__username', 'repartidor__username')
    date_hierarchy = 'fecha'
    readonly_fields = ('cliente',)
    autocomplete_fields = ('repartidor',)
    inlines = [VentaProductoInLine]