from rest_framework import serializers
from projeto1.models import Navios


class FileNavioSerializer(serializers.Serializer):
    file = serializers.FileField()


class NavioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Navios
        fields = [
            'id',
            'nome_navio',
            'mes_ano',
            'classificacao_risco',
            'indice_conformidade',
            'pontuacao_risco',
            'temporada',
        ]
