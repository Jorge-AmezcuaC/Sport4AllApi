from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import VentaProducto, CompraProducto, Compra, Venta, User
from django.db.models import Sum
from django.contrib.auth.models import Group

@receiver(pre_save, sender=Compra)
def update_stock_on_purchase_status_change(sender, instance, **kwargs):
    # Verificar si el estado de la compra está cambiando a "pagado"
    if instance.pk:  # Asegurarse de que la compra ya exista en la base de datos
        old_purchase = Compra.objects.get(pk=instance.pk)
        if old_purchase.status != 'pagado' and instance.status == 'pagado':
            # El estado ha cambiado a "pagado", actualiza el stock
            for compra_producto in instance.compraproducto_set.all():
                talla_producto = compra_producto.producto
                talla_producto.cantidadInventario += compra_producto.cantidad
                talla_producto.save()

@receiver(pre_save, sender=Venta)
def update_stock_on_sale_status_change(sender, instance, **kwargs):
    # Verificar si el estado de la venta está cambiando a "entregado"
    if instance.pk:  # Asegurarse de que la venta ya exista en la base de datos
        old_sale = Venta.objects.get(pk=instance.pk)
        if old_sale.status != 'entregado' and instance.status == 'entregado':
            # El estado ha cambiado a "entregado", decrementar el stock
            for venta_producto in instance.ventaproducto_set.all():
                talla_producto = venta_producto.producto
                talla_producto.cantidadInventario -= venta_producto.cantidad
                talla_producto.save()

@receiver(post_save, sender=User)
def assign_user_to_group(sender, instance, created, **kwargs):
    if created:
        # Definir la lógica para asignar usuarios a grupos según el valor de 'role'
        if instance.role == 'administrador':
            group_name = 'Administradores'
        elif instance.role == 'almacenista':
            group_name = 'Almacenistas'
        elif instance.role == 'repartidor':
            group_name = 'Repartidores'
        else:
            group_name = 'Clientes'  # El valor predeterminado para usuarios con otros roles

        try:
            group = Group.objects.get(name=group_name)
            instance.groups.add(group)
        except Group.DoesNotExist:
            pass