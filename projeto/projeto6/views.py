import os

import pandas as pd
from django.conf import settings
from django.core.files.storage import default_storage
from projeto6.models import Channel, Driver, Hub, Order, Payment, Store
from projeto6.serializers import (
    FileSerializer,
    Questao01Serializer,
    Questao02Serializer,
    Questao03Serializer,
    Questao04Serializer,
    Questao05Serializer,
    Questao06Serializer,
    Questao07Serializer,
    Questao08Serializer,
    Questao09Serializer,
    Questao10Serializer,
    Questao11Serializer,
    Questao12Serializer,
    Questao13Serializer,
    Questao14Serializer,
    Questao15Serializer,
    Questao16Serializer,
    Questao17Serializer,
    Questao18Serializer,
    Questao19Serializer,
    Questao20Serializer,
    channelOutSerializer,
)
from projeto6.tasks import (
    load_deliveries_file,
    load_hubs_file,
    load_orders_file,
    load_payment_file,
    load_store_file,
)
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ChannelAPIView(generics.CreateAPIView):
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        df = pd.read_csv(file, delimiter=',')
        channel_list = []
        Channel.truncate()
        for _, row in df.iterrows():
            new_file = Channel(
                channel_id=row['channel_id'],
                channel_name=row['channel_name'],
                channel_type=row['channel_type'],
            )
            channel_list.append(new_file)
        Channel.objects.bulk_create(channel_list)
        channels = Channel.objects.all()
        serializer = channelOutSerializer(
            instance=channels,
            many=True,
            context={'request': request},
        )
        return Response(
            serializer.data,
            status.HTTP_201_CREATED,
        )


class DeliveryAPIView(generics.CreateAPIView):
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        file_path = os.path.join(
            settings.MEDIA_ROOT, 'projeto06', uploaded_file.name
        )
        with default_storage.open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        load_deliveries_file.delay(file_path)
        return Response(
            {'status': 'File being loaded'},
            status.HTTP_201_CREATED,
        )


class HubAPIView(generics.CreateAPIView):
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        file_path = os.path.join(
            settings.MEDIA_ROOT, 'projeto06', uploaded_file.name
        )
        with default_storage.open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        load_hubs_file.delay(file_path)
        return Response(
            {'status': 'File being loaded'},
            status.HTTP_201_CREATED,
        )


class DriverAPIView(generics.CreateAPIView):
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        df = pd.read_csv(file, delimiter=',')
        driver_list = []
        Driver.truncate()
        for _, row in df.iterrows():
            new_file = Driver(
                driver_id=row['driver_id'],
                driver_modal=row['driver_modal'],
                driver_type=row['driver_type'],
            )
            driver_list.append(new_file)
        Driver.objects.bulk_create(driver_list)
        return Response(
            {'status': 'File being loaded'},
            status.HTTP_201_CREATED,
        )


class OrderAPIView(generics.CreateAPIView):
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        file_path = os.path.join(
            settings.MEDIA_ROOT, 'projeto06', uploaded_file.name
        )
        with default_storage.open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        load_orders_file.delay(file_path)
        return Response(
            {'status': 'File being loaded'},
            status.HTTP_201_CREATED,
        )


class PaymentAPIView(generics.CreateAPIView):
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        file_path = os.path.join(
            settings.MEDIA_ROOT, 'projeto06', uploaded_file.name
        )
        print(file_path)
        with default_storage.open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        load_payment_file.delay(file_path)
        return Response(
            {'status': 'File being loaded'},
            status.HTTP_201_CREATED,
        )


class StoreAPIView(generics.CreateAPIView):
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        uploaded_file = request.FILES['file']
        file_path = os.path.join(
            settings.MEDIA_ROOT, 'projeto06', uploaded_file.name
        )
        print(file_path)
        with default_storage.open(file_path, 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        load_store_file.delay(file_path)
        return Response(
            {'status': 'File being loaded'},
            status.HTTP_201_CREATED,
        )


# RESPOSTS
class Questao01APIView(generics.ListAPIView):
    serializer_class = Questao01Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Qual o número de hubs por cidade?"""
        SQL = """SELECT 1 as hub_id, COUNT(*) AS total,hub_city AS cidade FROM public."p06Hubs" GROUP BY hub_city ORDER BY hub_city"""  # noqa
        results = Hub.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            # context={'request': request},
        )
        return Response(
            {
                "Questão 1": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao02APIView(generics.ListAPIView):
    serializer_class = Questao02Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Qual o número de pedidos (orders) por status?"""
        SQL = """SELECT	1 AS order_id,count(*) AS total,order_status AS status FROM public."p06Orders" GROUP BY order_status"""  # noqa
        results = Order.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 2": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao03APIView(generics.ListAPIView):
    serializer_class = Questao03Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Qual o número de lojas (stores) por cidade dos hubs?"""
        SQL = """SELECT	1 AS store_id ,count(store.store_id) AS total,hubs.hub_city AS cidade FROM public."p06Stores" AS store inner join public."p06Hubs" AS hubs on hubs.hub_id = store.hub_id group by hubs.hub_city order by total DESC"""  # noqa
        results = Store.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 3": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao04APIView(generics.ListAPIView):
    serializer_class = Questao04Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Qual o maior e o menor valor de pagamento (payment_amount) registrado?"""  # noqa
        SQL = """SELECT 1 AS payment_id, max(payment_amount) AS maior, min(payment_amount) AS menor FROM public."p06Payments" """  # noqa
        results = Payment.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 4": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao05APIView(generics.ListAPIView):
    serializer_class = Questao05Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Qual tipo de driver (driver_type) fez o maior número de entregas?"""  # noqa
        SQL = """SELECT 1 as driver_id, count(driver.driver_id) as total, driver.driver_type as driver_type FROM public."p06Drivers" AS driver INNER JOIN public."p06Deliveries" AS delivery ON delivery.driver_id = driver.driver_id GROUP BY driver.driver_type """  # noqa
        results = Driver.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 5": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao06APIView(generics.ListAPIView):
    serializer_class = Questao06Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Qual a distância média das entregas por tipo de driver (driver_modal)?"""  # noqa
        SQL = """SELECT 1 AS driver_id, dr.driver_modal AS modal, avg(de.delivery_distance_meters) as media FROM public."p06Drivers" AS dr INNER JOIN public."p06Deliveries" AS de ON dr.driver_id = de.driver_id GROUP BY dr.driver_modal """  # noqa
        results = Driver.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 6": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao07APIView(generics.ListAPIView):
    serializer_class = Questao07Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Qual a média de valor de pedido (order_amount) por loja, em ordem decrescente?"""  # noqa
        SQL = """SELECT 1 AS order_id, store.store_name AS name, AVG(o.order_amount) as media FROM public."p06Orders" AS o INNER JOIN public."p06Stores" AS store ON store.store_id = o.store_id GROUP BY store.store_name ORDER BY avg(o.order_amount) DESC """  # noqa
        results = Order.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 7": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class MyPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data, sql, questao):
        return Response(
            {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link(),
                },
                'count': self.page.paginator.count,
                'QUESTAO 8': questao,
                'SQL': sql,
                'results': data,
            }
        )


class Questao08APIView(generics.ListAPIView):
    serializer_class = Questao08Serializer
    pagination_class = MyPagination

    def list(self, request, *args, **kwargs):
        QUESTAO = """Existem pedidos que não estão associados a lojas? Se caso positivo, quantos?"""  # noqa
        SQL = """ SELECT 1 AS order_id, count(o.order_id) AS total, COALESCE(s.store_name,'Sem Loja') AS name FROM public."p06Orders" AS o LEFT JOIN public."p06Stores" AS s ON s.store_id = o.store_id GROUP BY s.store_name ORDER BY total DESC """  # noqa
        results = Order.objects.raw(SQL)

        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(results, request)
        serializer = self.get_serializer(
            instance=paginated_queryset,
            many=True,
            context={'request': request},
        )
        return paginator.get_paginated_response(
            serializer.data,
            sql=SQL,
            questao=QUESTAO,
        )


class Questao09APIView(generics.ListAPIView):
    serializer_class = Questao09Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Qual o valor total de pedido (order_amount) no channel 'FOOD PLACE'?"""  # noqa
        SQL = """SELECT 	1 as order_id, sum(order_amount) soma FROM public."p06Orders" AS o INNER JOIN public."p06Channels" c ON c. channel_id = o.channel_id WHERE c.channel_name = 'FOOD PLACE' """  # noqa
        results = Order.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 9": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao10APIView(generics.ListAPIView):
    serializer_class = Questao10Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = (
            """Quantos pagamentos foram cancelados (chargeback)? """  # noqa
        )
        SQL = """ SELECT 1 as payment_id, payment_status AS status, COUNT(payment_id) quantidade FROM public."p06Payments" WHERE payment_status = 'CHARGEBACK' GROUP BY payment_status """  # noqa
        results = Payment.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 10": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao11APIView(generics.ListAPIView):
    serializer_class = Questao11Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Qual foi o valor médio dos pagamentos cancelados (chargeback)? """  # noqa
        SQL = """ SELECT 1 AS payment_id,payment_status AS status, AVG(payment_amount) AS cashback FROM public."p06Payments" WHERE payment_status = 'CHARGEBACK' GROUP BY payment_status """  # noqa
        results = Payment.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 11": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao12APIView(generics.ListAPIView):
    serializer_class = Questao12Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """ Qual a média do valor de pagamento por método de pagamento (payment_method) em ordem decrescente? """  # noqa
        SQL = """ SELECT 1 AS payment_id, AVG(payment_amount) AS cashback_average, payment_method FROM public."p06Payments" GROUP BY payment_method ORDER BY AVG(payment_amount) DESC """  # noqa
        results = Payment.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 12": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao13APIView(generics.ListAPIView):
    serializer_class = Questao13Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """ Quais métodos de pagamento tiveram valor médio superior a 100?"""  # noqa
        SQL = """ SELECT 1 AS payment_id, AVG(payment_amount) AS cashback_average, payment_method FROM public."p06Payments" GROUP BY payment_method  HAVING AVG(payment_amount) > 100  ORDER BY AVG(payment_amount) DESC """  # noqa
        results = Payment.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 13": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao14APIView(generics.ListAPIView):
    serializer_class = Questao14Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """ Qual a média de valor de pedido (order_amount) por estado do hub (hub_state), segmento da loja (store_segment) e tipo de canal (channel_type)? """  # noqa
        SQL = """ SELECT 1 AS order_id,	AVG(o.order_amount) AS amount_average, h.hub_state AS state, s.store_segment AS segment, c.channel_type AS channel FROM public."p06Orders" AS o INNER JOIN public."p06Stores" AS s ON s.store_id =o.store_id INNER JOIN public."p06Hubs" AS h ON h.hub_id = s.hub_id INNER JOIN public."p06Channels" AS c ON c.channel_id = o.channel_id GROUP BY h.hub_state, s.store_segment, c.channel_type ORDER BY state """  # noqa
        results = Order.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 14": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao15APIView(generics.ListAPIView):
    serializer_class = Questao15Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """ Qual a média de valor de pedido (order_amount) por estado do hub (hub_state), segmento da loja (store_segment) e tipo de canal (channel_type)?  """  # noqa
        SQL = """ SELECT 1 AS order_id,	AVG(o.order_amount) AS amount_average, h.hub_state AS state, s.store_segment AS segment, c.channel_type AS channel FROM public."p06Orders" AS o INNER JOIN public."p06Stores" AS s ON s.store_id =o.store_id INNER JOIN public."p06Hubs" AS h ON h.hub_id = s.hub_id INNER JOIN public."p06Channels" AS c ON c.channel_id = o.channel_id GROUP BY h.hub_state, s.store_segment, c.channel_type ORDER BY state """  # noqa
        results = Order.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 15": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao16APIView(generics.ListAPIView):
    serializer_class = Questao16Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Qual o valor total de pedido (order_amount) por estado do hub (hub_state), segmento da loja (store_segment) e tipo de  canal (channel_type)? Demonstre os totais intermediários e formate o resultado."""  # noqa
        SQL = """SELECT 1 as order_id, H.hub_state state,	S.store_segment as segment,	C.channel_type as channel,	SUM(O.order_amount) as total FROM public."p06Orders" AS O INNER JOIN public."p06Stores" AS S on O.store_id = S.store_id INNER JOIN public."p06Hubs" AS H on S.hub_id = H.hub_id INNER JOIN public."p06Channels" AS C on C.channel_id = O.channel_id GROUP BY ROLLUP (S.store_segment,H.hub_state,C.channel_type) """  # noqa
        results = Order.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 16": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao17APIView(generics.ListAPIView):
    serializer_class = Questao17Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """Quando  o  pedido  era  do  Hub  do  Rio  de  Janeiro  (hub_state),  segmento  de  loja 'FOOD',  tipo  de  canal  Marketplace  e  foi  cancelado,  qual  foi  a  média  de  valor do  pedido (order_amount)?"""  # noqa
        SQL = """SELECT 1 as order_id, H.hub_state AS hub_state, S.store_segment AS store_segment, C.channel_type AS channel_type,	AVG(O.order_amount) as amount_average FROM public."p06Orders" AS O INNER JOIN public."p06Stores" AS S ON O.store_id = S.store_id INNER JOIN public."p06Hubs" AS H ON S.hub_id = H.hub_id INNER JOIN public."p06Channels" AS C ON C.channel_id = O.channel_id WHERE H.hub_state ='RJ' AND	S.store_segment = 'FOOD' AND C.channel_type ='MARKETPLACE' AND O.order_stATUS='CANCELED' GROUP BY H.hub_state , S.store_segment ,C.channel_type """  # noqa
        results = Order.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 17": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao18APIView(generics.ListAPIView):
    serializer_class = Questao18Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """ Quando o pedido era do segmento de loja 'GOOD', tipo de canal Marketplace e foi cancelado, algum hub_state teve total de valor do pedido superior a 100.000? """  # noqa
        SQL = """ SELECT 1 as order_id, H.hub_state AS hub_state, S.store_segment AS store_segment, 	C.channel_type AS channel_type, SUM(O.order_amount) as amount_average FROM public."p06Orders" AS O INNER JOIN public."p06Stores" AS S ON O.store_id = S.store_id INNER JOIN public."p06Hubs" AS H ON S.hub_id = H.hub_id INNER JOIN public."p06Channels" AS C ON C.channel_id = O.channel_id WHERE S.store_segment = 'GOOD' AND C.channel_type ='MARKETPLACE' AND O.order_stATUS='CANCELED' GROUP BY H.hub_state , S.store_segment ,C.channel_type HAVING SUM(O.order_amount) >100000 """  # noqa
        results = Order.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 18": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao19APIView(generics.ListAPIView):
    serializer_class = Questao19Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """ Em que data houve a maior média de valor do pedido (order_amount)?  Dica: Pesquise e use a função SUBSTRING() """  # noqa
        SQL = """ SELECT 1 AS order_id, h.hub_state AS state FROM public."p06Orders" AS o INNER JOIN public."p06Stores" AS s ON s.store_id =o.store_id INNER JOIN public."p06Hubs" AS h ON h.hub_id = s.hub_id INNER JOIN public."p06Channels" AS c ON c.channel_id = o.channel_id WHERE s.store_segment = 'GOOD' AND c.channel_type ='MARKETPLACE' GROUP BY h.hub_state, s.store_segment, c.channel_type HAVING AVG(o.order_amount) >100000 """  # noqa
        results = Order.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 19": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )


class Questao20APIView(generics.ListAPIView):
    serializer_class = Questao20Serializer

    def list(self, request, *args, **kwargs):
        QUESTAO = """ Em quais datas o valor do pedido foi igual a zero (ou seja, não houve venda)? Dica: Use a função SUBSTRING(). """  # noqa
        SQL = """ SELECT 1 AS order_id, h.hub_state AS state FROM public."p06Orders" AS o INNER JOIN public."p06Stores" AS s ON s.store_id =o.store_id INNER JOIN public."p06Hubs" AS h ON h.hub_id = s.hub_id INNER JOIN public."p06Channels" AS c ON c.channel_id = o.channel_id WHERE s.store_segment = 'GOOD' AND c.channel_type ='MARKETPLACE' GROUP BY h.hub_state, s.store_segment, c.channel_type HAVING AVG(o.order_amount) >100000 """  # noqa
        results = Order.objects.raw(SQL)
        serializer = self.get_serializer(
            instance=results,
            many=True,
            context={'request': request},
        )
        return Response(
            {
                "Questão 19": QUESTAO,
                "SQL": SQL,
                "data": serializer.data,
            }
        )
