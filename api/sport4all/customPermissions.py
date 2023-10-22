# custom_permissions.py
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Obtener o crear ContentTypes para los modelos
venta_content_type = ContentType.objects.get(app_label='sport4all', model='venta')
productoventa_content_type = ContentType.objects.get(app_label='sport4all', model='ventaproducto')
compra_content_type = ContentType.objects.get(app_label='sport4all', model='compra')
compraproducto_content_type = ContentType.objects.get(app_label='sport4all', model='compraproducto')
devolucion_content_type = ContentType.objects.get(app_label='sport4all', model='devolucion')
direccion_content_type = ContentType.objects.get(app_label='sport4all', model='direccion')
productocarrito_content_type = ContentType.objects.get(app_label='sport4all', model='productocarrito')
pruebasdevolucion_content_type = ContentType.objects.get(app_label='sport4all', model='pruebasdevolucion')

# Permiso personalizado: Puede ver ventas
can_view_venta = Permission.objects.create(
    codename='view_venta',
    name='Can view Venta',
    content_type=venta_content_type,
)

# Permiso personalizado: Puede cambiar ventas
can_change_venta = Permission.objects.create(
    codename='change_venta',
    name='Can change Venta',
    content_type=venta_content_type,
)

# Permiso personalizado: Puede ver ProductoVenta
can_view_productoventa = Permission.objects.create(
    codename='view_ventaproducto',
    name='Can view ProductoVenta',
    content_type=productoventa_content_type,
)

# Permiso personalizado: Puede cambiar ProductoVenta
can_change_productoventa = Permission.objects.create(
    codename='change_ventaproducto',
    name='Can change ProductoVenta',
    content_type=productoventa_content_type,
)

# Permiso personalizado: Puede ver Compra
can_view_compra = Permission.objects.create(
    codename='view_compra',
    name='Can view Compra',
    content_type=compra_content_type,
)

# Permiso personalizado: Puede cambiar Compra
can_change_compra = Permission.objects.create(
    codename='change_compra',
    name='Can change Compra',
    content_type=compra_content_type,
)

# Permiso personalizado: Puede ver CompraProducto
can_view_compraproducto = Permission.objects.create(
    codename='view_compraproducto',
    name='Can view CompraProducto',
    content_type=compraproducto_content_type,
)

# Permiso personalizado: Puede cambiar CompraProducto
can_change_compraproducto = Permission.objects.create(
    codename='change_compraproducto',
    name='Can change CompraProducto',
    content_type=compraproducto_content_type,
)

# Permiso personalizado: Puede ver Devolucion
can_view_devolucion = Permission.objects.create(
    codename='view_devolucion',
    name='Can view Devolucion',
    content_type=devolucion_content_type,
)

# Permiso personalizado: Puede cambiar Devolucion
can_change_devolucion = Permission.objects.create(
    codename='change_devolucion',
    name='Can change Devolucion',
    content_type=devolucion_content_type,
)

# Permiso personalizado: Puede ver Direccion
can_view_direccion = Permission.objects.create(
    codename='view_direccion',
    name='Can view Direccion',
    content_type=direccion_content_type,
)

# Permiso personalizado: Puede ver Carrito
can_view_productocarrito = Permission.objects.create(
    codename='view_productocarrito',
    name='Can view Carrito',
    content_type=productocarrito_content_type,
)

# Permiso personalizado: Puede cambiar Carrito
can_change_productocarrito = Permission.objects.create(
    codename='change_productocarrito',
    name='Can change Carrito',
    content_type=productocarrito_content_type,
)

# Permiso personalizado: Puede ver ProductoDevolucion
can_view_productodevolucion = Permission.objects.create(
    codename='view_pruebasdevolucion',
    name='Can view ProductoDevolucion',
    content_type=pruebasdevolucion_content_type,
)

# Permiso personalizado: Puede cambiar ProductoDevolucion
can_change_productodevolucion = Permission.objects.create(
    codename='change_pruebasdevolucion',
    name='Can change ProductoDevolucion',
    content_type=pruebasdevolucion_content_type,
)