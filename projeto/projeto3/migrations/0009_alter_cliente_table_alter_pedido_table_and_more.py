# Generated by Django 4.2.1 on 2023-05-18 18:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projeto3", "0008_rename_clinete_cliente"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="cliente",
            table="p03Clientes",
        ),
        migrations.AlterModelTable(
            name="pedido",
            table="p03Pedidos",
        ),
        migrations.AlterModelTable(
            name="vendedor",
            table="p03Vendedores",
        ),
    ]
