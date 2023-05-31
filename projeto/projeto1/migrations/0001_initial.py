# Generated by Django 4.2.1 on 2023-05-09 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cp02Navios",
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
                ("nome_navio", models.CharField(max_length=50, null=True)),
                ("mes_ano", models.CharField(max_length=10, null=True)),
                ("classificacao_risco", models.CharField(max_length=15, null=True)),
                ("indice_conformidade", models.FloatField(null=True)),
                ("pontuacao_risco", models.IntegerField()),
                ("temporada", models.CharField(max_length=200, null=True)),
            ],
            options={
                "db_table": "cp02Navios",
            },
        ),
    ]