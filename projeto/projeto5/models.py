from django.db import models
from django.utils.timezone import now
from django.db import connection

# Create your models here.


class Cliente(models.Model):
    class Meta:
        db_table = 'p05Clientes'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    id_cliente = models.IntegerField(null=True)
    nome_cliente = models.CharField(max_length=50, null=True)
    endereco_cliente = models.CharField(max_length=50, null=True)
    cidade_cliente = models.CharField(max_length=50, null=True)
    estado_cliente = models.CharField(max_length=50, null=True)


class Pedido(models.Model):
    class Meta:
        db_table = 'p05Pedidos'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    id_pedido = models.IntegerField(null=True)
    id_cliente = models.IntegerField(null=True)
    id_vendedor = models.IntegerField(null=True)
    data_pedido = models.DateField(default=now, null=True)
    id_entrega = models.IntegerField(null=True)
    valor_pedido = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )


class Vendedor(models.Model):
    class Meta:
        db_table = 'p05Vendedores'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    id_vendedor = models.IntegerField(null=True)
    nome_vendedor = models.CharField(50, null=True)
    dept_vendedor = models.CharField(max_length=50, null=True)


class Vendas(models.Model):
    class Meta:
        db_table = 'p05Vendas'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )
    ano = models.IntegerField(null=True)
    pais = models.CharField(max_length=45, null=True)
    produto = models.CharField(max_length=45, null=True)
    faturamento = models.IntegerField(null=True)
