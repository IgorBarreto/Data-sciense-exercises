from rest_framework import serializers
from projeto3.models import Cliente, Pedido, Vendedor


class ClienteLoaddataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id_cliente',
            'nome_cliente',
            'endereco_cliente',
            'cidade_cliente',
            'estado_cliente',
        ]


class ClienteLoadListDataSerializer(serializers.ListSerializer):
    child = ClienteLoaddataSerializer()


class PedidoLoaddataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = [
            'id_pedido',
            'id_cliente',
            'id_vendedor',
            'data_pedido',
            'id_entrega',
        ]


class PedidoLoadListDataSerializer(serializers.ListSerializer):
    child = PedidoLoaddataSerializer()


class VendedorLoaddataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['id_vendedor', 'nome_vendedor']


class VendedorLoadListDataSerializer(serializers.ListSerializer):
    child = VendedorLoaddataSerializer()


class PedidoClienteSerializer(serializers.Serializer):
    id_pedido = serializers.IntegerField()
    nome_cliente = serializers.CharField()
    nome_vendedor = serializers.CharField(required=False)
    data_pedido = serializers.SerializerMethodField(required=False)
    cidade_cliente = serializers.CharField()

    def get_data_pedido(self, obj):
        # Logic to determine the value based on obj or other data
        # Return the value of the field based on the determined type
        # print(f'GET - {obj.data_pedido}')
        # obj.data_pedido = 'Sem Pedido'
        return obj.data_pedido

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['data_pedido'] is None:
            data['data_pedido'] = "Sem Pedido"
        if data['nome_cliente'] is None:
            data['nome_cliente'] = "Sem Pedido"
        return data


class ClienteMesmaCidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'id_cliente',
            'nome_cliente',
            'cidade_cliente',
        ]
