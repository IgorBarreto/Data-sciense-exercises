# Generated by Django 4.2.1 on 2023-05-11 01:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clinete",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_cliente", models.IntegerField(null=True)),
                ("nome_cliente", models.CharField(max_length=50)),
                ("endereco_cliente", models.CharField(null=True, verbose_name=50)),
                ("cidade_cliente", models.CharField(max_length=50, null=True)),
                ("estado_cliente", models.CharField(max_length=50, null=True)),
            ],
            options={
                "db_table": "cp04Clientes",
            },
        ),
        migrations.CreateModel(
            name="Pedido",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_pedido", models.IntegerField(null=True)),
                ("id_cliente", models.IntegerField(null=True)),
                ("id_vendedor", models.IntegerField(null=True)),
                ("data_pedido", models.DateTimeField(null=True)),
                ("id_entrega", models.IntegerField(null=True)),
            ],
            options={
                "db_table": "cp04Pedidos",
            },
        ),
        migrations.CreateModel(
            name="Vendedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("id_vendedor", models.IntegerField(null=True)),
                ("nome_vendedor", models.CharField(max_length=50, null=True)),
            ],
            options={
                "db_table": "cp04Vendedores",
            },
        ),
    ]
