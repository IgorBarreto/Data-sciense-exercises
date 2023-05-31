from rest_framework import serializers

from projeto5.models import Cliente, Pedido, Vendedor, Vendas


class ClienteLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id',
            'id_cliente',
            'nome_cliente',
            'endereco_cliente',
            'cidade_cliente',
            'estado_cliente',
        ]


class ClientesPorCidadeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    cidade = serializers.CharField()
    quantidade = serializers.IntegerField()


class ClienteLoadListSerializer(serializers.ListSerializer):
    child = ClienteLoadSerializer()


class PedidoLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = [
            'id',
            'id_pedido',
            'id_cliente',
            'id_vendedor',
            'data_pedido',
            'id_entrega',
            'valor_pedido',
        ]

    data_pedido = serializers.DateTimeField(read_only=True)


class PedidoLoadListSerializer(serializers.ListSerializer):
    child = PedidoLoadSerializer()


class PedidoMediaSerializer(serializers.Serializer):
    cidade = serializers.CharField()
    estado = serializers.CharField(required=False)
    media = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
    )
    total = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
    )


class VendedorLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = [
            'id',
            'id_vendedor',
            'nome_vendedor',
            'dept_vendedor',
        ]


class VendedorLoadListSerializer(serializers.ListSerializer):
    child = VendedorLoadSerializer()


class VendasLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendas
        fields = [
            'id',
            'ano',
            'pais',
            'produto',
            'faturamento',
        ]


class VendasLoadListSerializer(serializers.ListSerializer):
    child = VendasLoadSerializer()
