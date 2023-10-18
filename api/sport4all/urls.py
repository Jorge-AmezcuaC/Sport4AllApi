from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Precio', views.PrecioView)
router.register(r'Iva', views.IvaView)
router.register(r'Producto', views.ProductoView)
router.register(r'Proveedor', views.ProvedorView)
router.register(r'Compra', views.CompraView)
router.register(r'CompraProducto', views.CompraProductoView)
router.register(r'Cliente', views.ClienteView)
router.register(r'Venta', views.VentaView)
router.register(r'VentaProducto', views.VentaProductoView)
router.register(r'Devolucion', views.DevolucionView)
router.register(r'Inventario', views.InventarioView)
router.register(r'Foto', views.FotoProductoView)

urlpatterns = [
    path('', include(router.urls)),
]