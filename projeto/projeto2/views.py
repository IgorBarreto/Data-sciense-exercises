from rest_framework import generics

# import pandas as pd
import csv
import io
from rest_framework.response import Response
from rest_framework import status
from projeto2.models import CancerMama, CancerMamaOutFile

from projeto2.serializers import (
    CancerMamaSerializerOut,
    CancerMamaSerializerUploadFile,
)


class LoadFiles(generics.CreateAPIView):
    serializer_class = CancerMamaSerializerUploadFile

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['file']
        file = csv_file.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        data = [line for line in reader]
        aux = []
        for item in data:
            classe = item.get('classe')
            idade = item.get('idade')
            menopausa = item.get('menopausa')
            tamanho_tumor = item.get('tamanho_tumor')
            inv_nodes = item.get('inv_nodes')
            node_caps = item.get('node_caps')
            deg_malig = item.get('deg_malig')
            seio = item.get('seio')
            quadrante = item.get('quadrante')
            irradiando = item.get('irradiando')
            obj = CancerMama(
                classe=classe,
                idade=idade,
                menopausa=menopausa,
                tamanho_tumor=tamanho_tumor,
                inv_nodes=inv_nodes,
                node_caps=node_caps,
                deg_malig=deg_malig,
                seio=seio,
                quadrante=quadrante,
                irradiando=irradiando,
            )
            aux.append(obj)
        CancerMama.truncate()
        CancerMama.objects.bulk_create(aux)

        return Response(
            {"status": "File loaded."},
            status.HTTP_201_CREATED,
        )


class Binarizacao(generics.ListAPIView):
    serializer_class = CancerMamaSerializerOut
    queryset = CancerMama.objects.all()

    def get(self, request, *args, **kwargs):
        QUESTA0 = """Binarizando classe"""  # noqa
        SQL = """SELECT * FROM "cp03CancerMama" """

        cancer_mama = CancerMama.objects.raw(SQL)
        serializer = CancerMamaSerializerOut(
            instance=cancer_mama,
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


class BinarizacaoGerandoDataset(generics.ListCreateAPIView):
    queryset = CancerMama.objects.all()

    def create(self, request, *args, **kwargs):
        cancer_mama = CancerMama.objects.all()
        lista = []
        for cancer in cancer_mama:
            destino = CancerMamaOutFile()
            destino.classe = cancer.classe
            destino.idade = cancer.idade
            destino.menopausa = cancer.menopausa
            destino.tamanho_tumor = cancer.tamanho_tumor
            destino.inv_nodes = cancer.inv_nodes
            destino.node_caps = cancer.node_caps
            destino.deg_malig = cancer.deg_malig
            destino.seio = cancer.seio
            destino.quadrante = cancer.quadrante
            destino.irradiando = cancer.irradiando
            # destino._handle_data()
            lista.append(destino)
        for linha in lista:
            print(linha)
        CancerMamaOutFile.truncate()
        CancerMamaOutFile.objects.bulk_create(lista)
        return Response(
            {'status': 'Loaded new dataset'},
            status=status.HTTP_201_CREATED,
        )
