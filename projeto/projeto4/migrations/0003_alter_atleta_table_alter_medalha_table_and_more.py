# Generated by Django 4.2.1 on 2023-05-18 18:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projeto4", "0002_rename_rank_medalha_rank"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="atleta",
            table="p04Atletas",
        ),
        migrations.AlterModelTable(
            name="medalha",
            table="p04Medalhas",
        ),
        migrations.AlterModelTable(
            name="registro",
            table="p04Registros",
        ),
        migrations.AlterModelTable(
            name="time",
            table="p04Times",
        ),
        migrations.AlterModelTable(
            name="treinador",
            table="p04Treinadores",
        ),
    ]