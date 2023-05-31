from rest_framework import serializers


class CarregarArquivoOlimpiadas(serializers.Serializer):
    file = serializers.FileField()


class TecnicosAtletas(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
