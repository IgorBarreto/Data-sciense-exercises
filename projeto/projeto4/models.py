from django.db import models
from django.db import connection


# Create your models here.
class Atleta(models.Model):
    class Meta:
        db_table = 'p04Atletas'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    name = models.CharField(max_length=255, null=True)
    noc = models.CharField(max_length=255, null=True)
    discipline = models.CharField(max_length=255, null=True)


class Treinador(models.Model):
    class Meta:
        db_table = 'p04Treinadores'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    name = models.CharField(max_length=255)
    noc = models.CharField(max_length=255, null=True)
    discipline = models.CharField(max_length=255, null=True)
    event = models.CharField(max_length=255, null=True)


class Registro(models.Model):
    class Meta:
        db_table = 'p04Registros'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    discipline = models.CharField(max_length=255, null=True)
    female = models.IntegerField(null=True)
    male = models.IntegerField(null=True)
    total = models.IntegerField(null=True)


class Medalha(models.Model):
    class Meta:
        db_table = 'p04Medalhas'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    rank = models.IntegerField(null=True)
    team_noc = models.CharField(max_length=255, null=True)
    gold = models.IntegerField(null=True)
    silver = models.IntegerField(null=True)
    bronze = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    rank_by_total = models.IntegerField(null=True)


class Time(models.Model):
    class Meta:
        db_table = 'p04Times'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    name = models.CharField(max_length=255, null=True)
    discipline = models.CharField(max_length=255, null=True)
    noc = models.CharField(max_length=255, null=True)
    event = models.CharField(max_length=255, null=True)
