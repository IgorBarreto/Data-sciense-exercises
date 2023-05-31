import pandas as pd
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from projeto4.models import Atleta, Treinador, Registro, Medalha, Time
from projeto4.serializers import (
    CarregarArquivoOlimpiadas,
    TecnicosAtletas,
)


# Create your views here.
class AtletasLoadFile(generics.CreateAPIView):
    serializer_class = CarregarArquivoOlimpiadas

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        df = pd.read_excel(file)
        lista_atletas = []
        Atleta.truncate()
        for _, row in df.iterrows():
            new_file = Atleta(
                name=row['Name'],
                noc=row['NOC'],
                discipline=row['Discipline'],
            )
            lista_atletas.append(new_file)
        Atleta.objects.bulk_create(lista_atletas)
        return Response(
            {'status': 'File loaded'},
            status.HTTP_201_CREATED,
        )


class TreinadoresLoadFile(generics.CreateAPIView):
    serializer_class = CarregarArquivoOlimpiadas

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        df = pd.read_excel(file)
        lista_treinadores = []
        Treinador.truncate()
        for _, row in df.iterrows():
            new_file = Treinador(
                name=row['Name'],
                noc=row['NOC'],
                discipline=row['Discipline'],
                event=row['Event'],
            )
            lista_treinadores.append(new_file)
        Treinador.objects.bulk_create(lista_treinadores)
        return Response(
            {'status': 'File loaded'},
            status.HTTP_201_CREATED,
        )


class RegistrosLoadFile(generics.CreateAPIView):
    serializer_class = CarregarArquivoOlimpiadas

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        df = pd.read_excel(file)
        lista_registros = []
        Registro.truncate()
        for _, row in df.iterrows():
            new_file = Registro(
                discipline=row['Discipline'],
                male=row['Male'],
                female=row['Female'],
                total=row['Total'],
            )
            lista_registros.append(new_file)
        Registro.objects.bulk_create(lista_registros)
        return Response(
            {'status': 'File loaded'},
            status.HTTP_201_CREATED,
        )


class MedalhasLoadFile(generics.CreateAPIView):
    serializer_class = CarregarArquivoOlimpiadas

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        df = pd.read_excel(file)
        lista_medalhas = []
        Medalha.truncate()
        for _, row in df.iterrows():
            print(row.keys())
            new_file = Medalha(
                rank=row['Rank'],
                team_noc=row['Team/NOC'],
                gold=row['Gold'],
                silver=row['Silver'],
                bronze=row['Bronze'],
                total=row['Total'],
                rank_by_total=row['Rank by Total'],
            )
            lista_medalhas.append(new_file)
        Medalha.objects.bulk_create(lista_medalhas)
        return Response(
            {'status': 'File loaded'},
            status.HTTP_201_CREATED,
        )


class TimesLoadFile(generics.CreateAPIView):
    serializer_class = CarregarArquivoOlimpiadas

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        df = pd.read_excel(file)
        lista_times = []
        Time.truncate()
        for _, row in df.iterrows():
            print(row.keys())
            new_file = Time(
                name=row['Name'],
                discipline=row['Discipline'],
                noc=row['NOC'],
                event=row['Event'],
            )
            lista_times.append(new_file)
        Time.objects.bulk_create(lista_times)
        return Response(
            {'status': 'File loaded'},
            status.HTTP_201_CREATED,
        )


class TecnicosAtletas(generics.ListAPIView):
    serializer_class = TecnicosAtletas

    def list(self, request, *args, **kwargs):
        SQL = """
            SELECT
                id,name FROM "cp04Treinadores"
            WHERE
                discipline = 'Handball'
            UNION
            SELECT
                id, name FROM "cp04Atletas"
            WHERE discipline = 'Handball'"""

        QUESTAO = """Quem são os técnicos (coaches) e atletas das equipes de Handball?"""  # NOQA
        results = Atleta.objects.raw(SQL)

        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 1": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )
