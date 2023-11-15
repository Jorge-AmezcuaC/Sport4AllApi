from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'Iva', views.IvaView)
router.register(r'Producto', views.ProductoView)
router.register(r'Proveedor', views.ProvedorView)
router.register(r'Compra', views.CompraView)
router.register(r'CompraProducto', views.CompraProductoView)
router.register(r'Venta', views.VentaView)
router.register(r'VentaProducto', views.VentaProductoView)
router.register(r'Devolucion', views.DevolucionView)
router.register(r'Foto', views.FotoProductoView)
router.register(r'Direccion', views.DireccionView)
router.register(r'User', views.UserView)
router.register(r'Marca', views.MarcaView)
router.register(r'Talla', views.TallaView)
router.register(r'TallaProducto', views.TallaProductoView)
router.register(r'ProductoCarrito', views.ProductoCarritoView)
router.register(r'PruebasDevolucion', views.PruebasDevolucionView)

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)