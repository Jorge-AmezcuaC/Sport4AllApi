from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import VentaProducto, CompraProducto, Compra, Venta
from django.db.models import Sum

@receiver(post_save, sender=VentaProducto)
def update_venta_subtotal_total(sender, instance, created, **kwargs):
    if created:
        # Actualizar subtotal y total de la venta
        instance.venta.subtotal = instance.venta.ventaproducto_set.aggregate(Sum('subtotal'))['subtotal__sum'] or 0
        instance.venta.total = instance.venta.subtotal * (1 + instance.venta.iva.porcentaje / 100)
        instance.venta.save()

@receiver(post_save, sender=CompraProducto)
def update_compra_subtotal_total(sender, instance, created, **kwargs):
    if created:
        # Actualizar subtotal y total de la compra
        instance.compra.subtotal = instance.compra.compraproducto_set.aggregate(Sum('subtotal'))['subtotal__sum'] or 0
        instance.compra.total = instance.compra.subtotal * (1 + instance.compra.iva.porcentaje / 100)
        instance.compra.save()

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
                talla_producto = venta_producto.producto.producto
                talla_producto.cantidadInventario -= venta_producto.cantidad
                talla_producto.save()