# Generated by Django 4.2.1 on 2023-05-18 18:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projeto5", "0005_alter_vendas_table"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="cliente",
            table="p05Clientes",
        ),
        migrations.AlterModelTable(
            name="pedido",
            table="p05Pedidos",
        ),
        migrations.AlterModelTable(
            name="vendas",
            table="p05Vendas",
        ),
        migrations.AlterModelTable(
            name="vendedor",
            table="p05Vendedores",
        ),
    ]
