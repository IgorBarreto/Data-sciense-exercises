from django.db import models
from django.db import connection


# Create your models here.
class CancerMama(models.Model):
    class Meta:
        db_table = 'p02CancerMama'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    classe = models.CharField(100, null=True)
    idade = models.CharField(45, null=True)
    menopausa = models.CharField(45, null=True)
    tamanho_tumor = models.CharField(45, null=True)
    inv_nodes = models.CharField(45, null=True)
    node_caps = models.CharField(3, null=True)
    deg_malig = models.IntegerField(null=True)
    seio = models.CharField(5, null=True)
    quadrante = models.CharField(10, null=True)
    irradiando = models.CharField(3, null=True)


class CancerMamaManager(models.Manager):
    def bulk_create(self, objs, batch_size=None, ignore_conflicts=None):
        new_objs = []
        for obj in objs:
            new_objs.append(obj.clean())
        return super().bulk_create(objs, batch_size, ignore_conflicts)


class CancerMamaOutFile(models.Model):
    class Meta:
        db_table = 'p02CancerMamaNovoDataset'

    objects = CancerMamaManager()

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    classe = models.CharField(100, null=True)
    idade = models.CharField(45, null=True)
    menopausa = models.CharField(45, null=True)
    tamanho_tumor = models.CharField(45, null=True)
    inv_nodes = models.CharField(45, null=True)
    node_caps = models.CharField(3, null=True)
    deg_malig = models.IntegerField(null=True)
    seio = models.CharField(5, null=True)
    quadrante = models.CharField(10, null=True)
    irradiando = models.CharField(3, null=True)

    def __str__(self) -> str:
        return f'{self.idade} {self.tamanho_tumor}'

    def clean(self):
        if self.classe == 'no-recurrence-events':
            self.classe = 0
        elif self.classe == 'recurrence-events':
            self.classe = 1

        if self.irradiando == 'no':
            self.irradiando = 0
        elif self.irradiando == 'yes':
            self.irradiando = 1

        if self.node_caps == 'no':
            self.node_caps = 0
        elif self.node_caps == 'yes':
            self.node_caps = 1
        else:
            self.node_caps = 2

        if self.seio == 'left':
            self.seio = 'E'
        elif self.seio == 'right':
            self.seio = 'D'

        if self.quadrante == 'left_low':
            self.quadrante = 1
        elif self.quadrante == 'right_up':
            self.quadrante = 2
        elif self.quadrante == 'left_up':
            self.quadrante = 3
        elif self.quadrante == 'right_low':
            self.quadrante = 4
        elif self.quadrante == 'central':
            self.quadrante = 5
        else:
            self.quadrante = 0

        if self.tamanho_tumor == '0-4' or self.tamanho_tumor == '5-9':
            self.tamanho_tumor = 'Muito Pequeno'
        elif self.tamanho_tumor == '10-14' or self.tamanho_tumor == '15-19':
            self.tamanho_tumor = 'Pequeno'
        elif self.tamanho_tumor == '20-24' or self.tamanho_tumor == '25-29':
            self.tamanho_tumor = 'Médio'
        elif self.tamanho_tumor == '30-34' or self.tamanho_tumor == '35-39':
            self.tamanho_tumor = 'Grande'
        elif self.tamanho_tumor == '40-44' or self.tamanho_tumor == '45-49':
            self.tamanho_tumor = 'Muito Grande'
        elif self.tamanho_tumor == '50-54' or self.tamanho_tumor == '55-59':
            self.tamanho_tumor = 'Tratamento Urgente'
