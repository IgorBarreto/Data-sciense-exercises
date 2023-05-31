from django.db import models
from django.db import connection

from django.utils import timezone


# Create your models here.
class Cliente(models.Model):
    class Meta:
        db_table = 'p03Clientes'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    id_cliente = models.IntegerField(primary_key=True)
    nome_cliente = models.CharField(max_length=50)
    endereco_cliente = models.CharField(50, null=True)
    cidade_cliente = models.CharField(max_length=50, null=True)
    estado_cliente = models.CharField(max_length=50, null=True)


class Vendedor(models.Model):
    class Meta:
        db_table = 'p03Vendedores'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    id_vendedor = models.IntegerField(primary_key=True)
    nome_vendedor = models.CharField(max_length=50, null=True)


class Pedido(models.Model):
    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    class Meta:
        db_table = 'p03Pedidos'

    id_pedido = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(
        Cliente,
        on_delete=models.DO_NOTHING,
        null=True,
    )
    id_vendedor = models.ForeignKey(
        Vendedor,
        on_delete=models.DO_NOTHING,
        null=True,
    )
    data_pedido = models.DateTimeField(null=True, default=timezone.now)
    id_entrega = models.IntegerField(null=True)
