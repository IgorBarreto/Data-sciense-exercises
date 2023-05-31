from django.db import models
from django.db import connection


# Create your models here.
class Navios(models.Model):
    class Meta:
        db_table = 'p01Navios'

    @classmethod
    def truncate(cls):
        print(cls._meta.db_table)
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    nome_navio = models.CharField(max_length=50, null=True)
    mes_ano = models.CharField(max_length=10, null=True)
    classificacao_risco = models.CharField(max_length=15, null=True)
    indice_conformidade = models.FloatField(null=True)
    pontuacao_risco = models.IntegerField()
    temporada = models.CharField(max_length=200, null=True)
