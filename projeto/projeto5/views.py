from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from projeto5.serializers import (
    ClienteLoadListSerializer,
    ClientesPorCidadeSerializer,
    PedidoLoadListSerializer,
    VendedorLoadListSerializer,
    PedidoMediaSerializer,
    VendasLoadListSerializer,
)
from projeto5.models import Cliente, Vendedor, Pedido, Vendas


# Create your views here.
class ClientesLoadData(generics.CreateAPIView):
    serializer_class = ClienteLoadListSerializer

    def create(self, request, *args, **kwargs):
        Cliente.truncate()
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class PedidosLoadData(generics.CreateAPIView):
    serializer_class = PedidoLoadListSerializer

    def create(self, request, *args, **kwargs):
        Pedido.truncate()
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VendedoresLoadData(generics.CreateAPIView):
    serializer_class = VendedorLoadListSerializer

    def create(self, request, *args, **kwargs):
        Vendedor.truncate()
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class VendasLoadData(generics.CreateAPIView):
    serializer_class = VendasLoadListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        v = Vendas
        print(v.__class__)
        Vendas.truncate()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ClientesList(generics.ListAPIView):
    serializer_class = ClientesPorCidadeSerializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Quantidade de clientes por cidade"""
        SQL = (
            """SELECT
            1 AS id, COUNT(*) as quantidade,
            cidade_cliente as cidade
        FROM "cp05Clientes"
        GROUP BY cidade_cliente
        ORDER BY COUNT(*) ASC""".replace(
                '       ', ''
            )
            .replace('\n', '')
            .replace('      ', ' ')
        )

        results = Cliente.objects.raw(SQL)

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


class PedidosMediaValor(generics.ListAPIView):
    serializer_class = PedidoMediaSerializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Media dos valores dos pedidos"""
        SQL = """SELECT
            1 AS id ,AVG(valor_pedido) AS media
        FROM "cp05Pedidos" """
        result = Pedido.objects.raw(SQL)

        serializer = self.get_serializer(
            instance=result,
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


class PedidosMediaPorCidade(generics.ListAPIView):
    serializer_class = PedidoMediaSerializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Media do valor dos pedidos por cliente"""  # noqa
        SQL = (
            """
        SELECT
            1 AS id, AVG(P.valor_pedido) AS media,
            C.cidade_cliente AS cidade
        FROM "cp05Pedidos" AS P,"cp05Clientes" AS C
        where C.id_cliente = P.id_cliente
        GROUP BY cidade_cliente
        ORDER BY AVG(P.valor_pedido) DESC
    """.replace(
                '       ', ''
            )
            .replace('\n', '')
            .replace('      ', ' ')
        )
        result = Pedido.objects.raw(SQL)
        print(dir(result))
        serializer = self.get_serializer(
            instance=result,
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


class PedidosMediaPorCidadeIncluindoSemPedidos(generics.ListAPIView):
    serializer_class = PedidoMediaSerializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Media do valor dos pedidos por cliente incluindo cidades sem pedido"""  # noqa
        SQL = (
            """
        SELECT
            1 AS id,
            CASE
                WHEN AVG(P.valor_pedido) IS NULL THEN 0
                ELSE AVG(P.valor_pedido)
            END AS media,
            C.cidade_cliente AS cidade
        FROM "cp05Pedidos" AS P
        RIGHT JOIN "cp05Clientes" AS C
        ON C.id_cliente = P.id_cliente
        GROUP BY cidade_cliente
        ORDER BY AVG(P.valor_pedido) DESC
    """.replace(
                '       ', ''
            )
            .replace('\n', '')
            .replace('      ', ' ')
        )
        result = Pedido.objects.raw(SQL)
        print(dir(result))
        serializer = self.get_serializer(
            instance=result,
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


class PedidosSomaPorCidadeIncluindoSemPedidos(generics.ListAPIView):
    serializer_class = PedidoMediaSerializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Media do valor dos pedidos por cliente incluindo cidades sem pedido"""  # noqa
        SQL = (
            """
        SELECT
            1 AS id,
            CASE
                WHEN SUM(P.valor_pedido) IS NULL THEN 0
                ELSE AVG(P.valor_pedido)
            END AS total,
            C.cidade_cliente AS cidade
        FROM "cp05Pedidos" AS P
        RIGHT JOIN "cp05Clientes" AS C
        ON C.id_cliente = P.id_cliente
        GROUP BY cidade_cliente
        ORDER BY AVG(P.valor_pedido) DESC
    """.replace(
                '       ', ''
            )
            .replace('\n', '')
            .replace('      ', ' ')
        )
        result = Pedido.objects.raw(SQL)
        print(dir(result))
        serializer = self.get_serializer(
            instance=result,
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


class PedidosSomaPorCidadeIncluindoSemPedidosEEstado(generics.ListAPIView):
    serializer_class = PedidoMediaSerializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Media do valor dos pedidos por cliente incluindo cidades sem pedido"""  # noqa
        SQL = (
            """
        SELECT
            1 AS id,
            CASE
                WHEN SUM(P.valor_pedido) IS NULL THEN 0
                ELSE AVG(P.valor_pedido)
            END AS total,
            C.cidade_cliente AS cidade,
            C.estado_cliente AS estado
        FROM "cp05Pedidos" AS P
        RIGHT JOIN "cp05Clientes" AS C
        ON C.id_cliente = P.id_cliente
        GROUP BY C.cidade_cliente,C.estado_cliente
        ORDER BY AVG(P.valor_pedido) DESC
    """.replace(
                '           ', ''
            )
            .replace('\n', '')
            .replace('      ', ' ')
            .strip()
        )
        result = Pedido.objects.raw(SQL)
        print(dir(result))
        serializer = self.get_serializer(
            instance=result,
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
