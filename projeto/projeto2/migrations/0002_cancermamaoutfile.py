# Generated by Django 4.2.1 on 2023-05-09 23:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projeto2", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CancerMamaOutFile",
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
                ("classe", models.CharField(null=True, verbose_name=100)),
                ("idade", models.CharField(null=True, verbose_name=45)),
                ("menopausa", models.CharField(null=True, verbose_name=45)),
                ("tamanho_tumor", models.CharField(null=True, verbose_name=45)),
                ("inv_nodes", models.CharField(null=True, verbose_name=45)),
                ("node_caps", models.CharField(null=True, verbose_name=3)),
                ("deg_malig", models.IntegerField(null=True)),
                ("seio", models.CharField(null=True, verbose_name=5)),
                ("quadrante", models.CharField(null=True, verbose_name=10)),
                ("irradiando", models.CharField(null=True, verbose_name=3)),
            ],
            options={
                "db_table": "cp03CancerMamaNovoDataset",
            },
        ),
    ]
