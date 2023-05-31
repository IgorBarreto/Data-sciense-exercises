from rest_framework import generics
import pandas as pd
from rest_framework.response import Response
from rest_framework import status
from projeto1.models import Navios
from rest_framework.pagination import PageNumberPagination
from projeto1.serializers import FileNavioSerializer, NavioSerializers


class CustomPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response(
            {
                'proximo': self.get_next_link(),
                'anterior': self.get_previous_link(),
                'total': self.page.paginator.count,
                'dados': data,
            }
        )


class NavioCreateView(generics.CreateAPIView):
    serializer_class = FileNavioSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        df = pd.read_csv(file, sep=';')

        Navios.truncate()
        lista_navios = []
        for _, row in df.iterrows():
            new_file = Navios(
                nome_navio=row['NOME_NAVIO'],
                mes_ano=row['MES_ANO_ABERTURA'],
                classificacao_risco=row['CLASSIFICACAO_RISCO'],
                indice_conformidade=float(
                    str(row['INDICE_CONFORMIDADE'].replace(',', '.'))
                ),
                pontuacao_risco=row['PONTUACAO_RISCO'],
                temporada=row['TEMPORADA'],
            )
            lista_navios.append(new_file)
        Navios.objects.bulk_create(lista_navios)
        return Response(
            {"status": "File loaded."},
            status.HTTP_201_CREATED,
        )


class NavioListviewQuestao1(generics.ListAPIView):
    serializer_class = NavioSerializers
    queryset = Navios.objects.all()

    def get(self, request, *args, **kwargs):
        QUESTA0 = """Quais embarcações possuem pontuação de risco igual a 310?"""  # noqa
        SQL = """SELECT * from "cp02Navios" WHERE pontuacao_risco = 310 order by nome_navio"""  # noqa

        navios = Navios.objects.raw(SQL)
        serializer = NavioSerializers(
            instance=navios,
            many=True,
            context={'request': request},
        )
        return Response(
            data={
                'Question': QUESTA0,
                'data': serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# 2-Quais embarcações têm classificação de risco A e índice de conformidade maior ouigual a 95%? # noqa
class NavioListviewQuestao2(generics.ListAPIView):
    serializer_class = NavioSerializers
    queryset = Navios.objects.all()

    def get(self, request, *args, **kwargs):
        QUESTA0 = """Quais embarcações têm classificação de risco A e índice de conformidade maior ou igual a 95%?"""  # noqa
        SQL = """SELECT * from "cp02Navios" WHERE classificacao_risco = 'A' AND indice_conformidade >= 95 ORDER BY nome_navio"""  # noqa

        navios = Navios.objects.raw(SQL)
        serializer = NavioSerializers(
            instance=navios,
            many=True,
            context={'request': request},
        )
        return Response(
            data={
                'Question': QUESTA0,
                'data': serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# 3-Quais embarcações têmclassificação de risco C ou De índice de conformidade menor ou igual a 95%? # noqa
class NavioListviewQuestao3(generics.ListAPIView):
    serializer_class = NavioSerializers
    queryset = Navios.objects.all()

    def get(self, request, *args, **kwargs):
        QUESTA0 = """Quais embarcações têmclassificação de risco Cou D e índice de conformidade menor ou igual a 95%?"""  # noqa
        SQL = """SELECT * from "cp02Navios" WHERE classificacao_risco IN ('C','D') AND indice_conformidade >= 95 ORDER BY nome_navio"""  # noqa

        navios = Navios.objects.raw(SQL)
        serializer = NavioSerializers(
            instance=navios,
            many=True,
            context={'request': request},
        )
        return Response(
            data={
                'Question': QUESTA0,
                'data': serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# 4-Quais embarcações têmclassificação de riscoA oupontuação de risco igual a 0? # noqa
class NavioListviewQuestao4(generics.ListAPIView):
    serializer_class = NavioSerializers
    queryset = Navios.objects.all()

    def get(self, request, *args, **kwargs):
        QUESTA0 = """Quais embarcações têm classificação de risco A ou pontuação de risco igual a 0?"""  # noqa
        SQL = """SELECT * from "cp02Navios" WHERE classificacao_risco = 'D' OR pontuacao_risco = 0 ORDER BY nome_navio"""  # noqa

        navios = Navios.objects.raw(SQL)
        serializer = NavioSerializers(
            instance=navios,
            many=True,
            context={'request': request},
        )
        return Response(
            data={
                'Question': QUESTA0,
                'data': serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# 5-[DESAFIO]Quais embarcações foram inspecionadas em Dezembro de 2016?
class NavioListviewQuestao5(generics.ListAPIView):
    serializer_class = NavioSerializers
    queryset = Navios.objects.all()

    def get(self, request, *args, **kwargs):
        QUESTA0 = """[DESAFIO]Quais embarcações foram inspecionadas em Dezembro de 2016"""  # noqa
        SQL = r"""SELECT * FROM "cp02Navios" WHERE temporada LIKE %s"""

        navios = Navios.objects.raw(SQL, [r'%Dezembro 2016'])
        serializer = NavioSerializers(
            instance=navios,
            many=True,
            context={'request': request},
        )
        return Response(
            data={
                'Question': QUESTA0,
                'data': serializer.data,
            },
            status=status.HTTP_200_OK,
        )
