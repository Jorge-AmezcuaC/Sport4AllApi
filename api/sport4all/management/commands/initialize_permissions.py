from django.contrib.auth.models import Permission, Group
from sport4all.models import User  
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Crea permisos y grupos personalizados'

    def handle(self, *args, **options):
        # Crea los permisos personalizados para cada modelo
        can_view_venta = Permission.objects.get(codename='view_venta')
        can_change_venta = Permission.objects.get(codename='change_venta')
        can_view_ventaproducto = Permission.objects.get(codename='view_ventaproducto')
        can_change_ventaproducto = Permission.objects.get(codename='change_ventaproducto')
        can_view_compra = Permission.objects.get(codename='view_compra')
        can_change_compra = Permission.objects.get(codename='change_compra')
        can_view_compraproducto = Permission.objects.get(codename='view_compraproducto')
        can_change_compraproducto = Permission.objects.get(codename='change_compraproducto')
        can_view_devolucion = Permission.objects.get(codename='view_devolucion')
        can_change_devolucion = Permission.objects.get(codename='change_devolucion')
        can_view_direccion = Permission.objects.get(codename='view_direccion')
        can_view_carrito = Permission.objects.get(codename='view_productocarrito')
        can_change_carrito = Permission.objects.get(codename='change_productocarrito')
        can_view_pruebasdevolucion = Permission.objects.get(codename='view_pruebasdevolucion')
        can_change_pruebasdevolucion = Permission.objects.get(codename='change_pruebasdevolucion')

        # Define los grupos y asigna los permisos
        # Almacenista
        almacenista_group, created = Group.objects.get_or_create(name='Almacenistas')
        almacenista_group.permissions.add(
            can_view_venta, can_change_venta, can_view_ventaproducto, can_change_ventaproducto,
            can_view_compra, can_change_compra, can_view_compraproducto, can_change_compraproducto,
            can_view_devolucion, can_change_devolucion
        )

        # Repartidor
        repartidor_group, created = Group.objects.get_or_create(name='Repartidores')
        repartidor_group.permissions.add(can_view_direccion, can_view_venta, can_change_venta, can_view_ventaproducto,)

        # Cliente
        cliente_group, created = Group.objects.get_or_create(name='Clientes')
        cliente_group.permissions.add(
            can_view_carrito, can_change_carrito, can_view_pruebasdevolucion, can_change_pruebasdevolucion,
            can_view_venta, can_change_venta, can_view_ventaproducto, can_change_ventaproducto, can_view_devolucion,
            can_change_devolucion, 
        )

        self.stdout.write(self.style.SUCCESS('Permisos y grupos creados con éxito'))
