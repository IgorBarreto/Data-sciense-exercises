from rest_framework import generics
from projeto3.serializers import (
    ClienteLoadListDataSerializer,
    PedidoLoadListDataSerializer,
    VendedorLoadListDataSerializer,
    PedidoClienteSerializer,
    ClienteMesmaCidadeSerializer,
)
from projeto3.models import Cliente, Pedido, Vendedor

from rest_framework.response import Response
from rest_framework import status


class Clientes(generics.CreateAPIView):
    serializer_class = ClienteLoadListDataSerializer
    queryset = Cliente.objects.all()

    def create(self, request, *args, **kwargs):
        Cliente.truncate()
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )


class Pedidos(generics.CreateAPIView):
    serializer_class = PedidoLoadListDataSerializer
    queryset = Pedido.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        Pedido.truncate()
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )


class Vendedores(generics.CreateAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorLoadListDataSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        Vendedor.truncate()
        serializer.save()
        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )


class PedidoCliente(generics.ListAPIView):
    serializer_class = PedidoClienteSerializer

    def list(self, request, *args, **kwargs):
        QUESTAO = 'Retornar id do pedido e nome do cliente.'
        # SQL = """SELECT
        #            p.id_pedido as id,c.nome_cliente as nome_cliente
        #         FROM
        #             "cp04Pedidos" as p, "cp04Clientes" as c
        #         WHERE c.id = p.id_cliente_id
        #         ORDER BY p.id_pedido
        #             """
        SQL = (
            """SELECT
                p.id_pedido as id_pedido,c.nome_cliente as nome_cliente
            FROM
                "cp04Pedidos" as p
            INNER JOIN
                "cp04Clientes" AS C
            ON
                c.id_cliente = p.id_cliente_id::integer""".replace(
                '           ', ''
            )
            .replace('\n', '')
            .replace('    ', '')
        )

        results = Pedido.objects.raw(SQL)
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


class PedidoClienteVendedor(generics.ListAPIView):
    serializer_class = PedidoClienteSerializer

    def get(self, request, *args, **kwargs):
        QUESTAO = 'Retornar id do pedido, nome do cliente e nome do vendedor.'
        SQL = (
            """SELECT
                p.id_pedido as id_pedido,
                c.nome_cliente as nome_cliente,
                v.nome_vendedor as nome_vendedor
            FROM
                "cp04Pedidos" as p, "cp04Clientes" as c,"cp04Vendedores" as v
            WHERE
                c.id_cliente = p.id_cliente_id AND
                v.id_vendedor = p.id_vendedor_id
            ORDER BY p.id_pedido""".replace(
                '           ', ''
            )
            .replace('\n', '')
            .replace('    ', '')
        )
        # SQL = """
        # SELECT
        #     p.id_pedido as id_pedido,
        #     c.nome_cliente as nome_cliente,
        #     v.nome_vendedor as nome_vendedor
        # FROM
        #     "cp04Pedidos" as p
        # INNER JOIN
        #     "cp04Clientes" AS c ON c.id_cliente = p.id_cliente_id::integer
        # INNER JOIN
        #     "cp04Vendedores" AS v ON v.id_vendedor = p.id_cliente_id::integer
        #     """
        results = Pedido.objects.raw(SQL)

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


class PedidoAllClienteLeftJoin(generics.ListAPIView):
    serializer_class = PedidoClienteSerializer

    serializer_class = PedidoClienteSerializer

    def get(self, request, *args, **kwargs):
        QUESTAO = 'Retornar todos os clientes, com ou sem pedido associado (usando Left Join)'  # NOQA
        SQL = (
            """SELECT
                p.id_pedido as id_pedido,
                c.nome_cliente as nome_cliente
            FROM
                "cp04Clientes" as c
            LEFT JOIN "cp04Pedidos" as p ON c.id_cliente = p.id_cliente_id
            ORDER BY p.id_pedido""".replace(
                '           ', ''
            )
            .replace('\n', '')
            .replace('    ', '')
        )
        results = Pedido.objects.raw(SQL)

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


class PedidoAllClienteRightJoin(generics.ListAPIView):
    serializer_class = PedidoClienteSerializer

    serializer_class = PedidoClienteSerializer

    def get(self, request, *args, **kwargs):
        QUESTAO = 'Retornar todos os clientes, com ou sem pedido associado (usando Right Join)'  # NOQA
        SQL = (
            """SELECT
                p.id_pedido as id_pedido,
                c.nome_cliente as nome_cliente
            FROM
                "cp04Pedidos" as p
            RIGHT JOIN
                "cp04Clientes" as c ON c.id_cliente = p.id_cliente_id
            ORDER BY
                p.id_pedido""".replace(
                '           ', ''
            )
            .replace('\n', '')
            .replace('    ', '')
        )
        results = Pedido.objects.raw(SQL)

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


class PedidoDataClienteVendedorOrderByCliente(generics.ListAPIView):
    serializer_class = PedidoClienteSerializer

    def get(self, request, *args, **kwargs):
        QUESTAO = "Retornar a data do pedido, o nome do cliente, todos os vendedores, com ou sem pedido associado, e ordenar o resultado pelo nome do cliente."  # NOQA
        SQL = (
            """SELECT
                p.id_pedido as id_pedido,
                p.data_pedido AS data_pedido,
                c.nome_cliente AS nome_cliente,
                v.nome_vendedor AS nome_vendedor
            FROM
                "cp04Pedidos" as p
            INNER JOIN "cp04Clientes" as c
            ON
                c.id_cliente = p.id_cliente_id
            RIGHT JOIN "cp04Vendedores" as v
            ON
                v.id_vendedor = p.id_vendedor_id
            ORDER BY
                c.nome_cliente""".replace(
                '           ', ''
            )
            .replace('\n', '')
            .replace('    ', '')
        )
        results = Pedido.objects.raw(SQL)
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


class ClienteMesmaCidade(generics.ListAPIView):
    serializer_class = ClienteMesmaCidadeSerializer

    def get(self, request, *args, **kwargs):
        QUESTAO = "Retornar clientes que sejam da mesma cidade  "  # NOQA
        SQL = (
            """SELECT
                C1.id_cliente,
                C1.nome_cliente,
                C1.cidade_cliente
            FROM
                "cp04Clientes" as C1,
                "cp04Clientes" as C2
            WHERE
                C1.cidade_cliente = C2.cidade_cliente AND
                C1.id_cliente <> C2.id_cliente""".replace(
                '           ', ''
            )
            .replace('\n', '')
            .replace('    ', '')
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
