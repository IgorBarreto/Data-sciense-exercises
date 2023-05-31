from projeto6.models import Channel, Delivery
from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    file = serializers.FileField()


class channelOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'channel_id',
            'channel_name',
            'channel_type',
        ]


class DeliveryOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = [
            'delivery_id',
            'delivery_order_id',
            'delivery_distance_meters',
            'delivery_status',
        ]


# QUESTÕES
class Questao01Serializer(serializers.Serializer):
    hub_id = serializers.IntegerField()
    total = serializers.IntegerField()
    cidade = serializers.CharField()


class Questao02Serializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    status = serializers.CharField()
    total = serializers.IntegerField()


class Questao03Serializer(serializers.Serializer):
    store_id = serializers.IntegerField()
    total = serializers.IntegerField()
    cidade = serializers.CharField()


class Questao04Serializer(serializers.Serializer):
    payment_id = serializers.IntegerField()
    maior = serializers.DecimalField(decimal_places=2, max_digits=10)
    menor = serializers.DecimalField(decimal_places=2, max_digits=10)


class Questao05Serializer(serializers.Serializer):
    driver_id = serializers.IntegerField()
    total = serializers.IntegerField()
    driver_type = serializers.CharField()


class Questao06Serializer(serializers.Serializer):
    driver_id = serializers.IntegerField()
    modal = serializers.CharField()
    media = serializers.DecimalField(decimal_places=4, max_digits=10)


class Questao07Serializer(serializers.Serializer):
    store_id = serializers.IntegerField()
    name = serializers.CharField
    media = serializers.DecimalField(decimal_places=4, max_digits=10)


class Questao08Serializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    name = serializers.CharField()
    total = serializers.IntegerField()


class Questao09Serializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    soma = serializers.DecimalField(decimal_places=2, max_digits=15)


class Questao10Serializer(serializers.Serializer):
    payment_id = serializers.IntegerField()
    status = serializers.CharField()
    quantidade = serializers.IntegerField()


class Questao11Serializer(serializers.Serializer):
    payment_id = serializers.IntegerField()
    cashback = serializers.DecimalField(max_digits=10, decimal_places=2)


class Questao12Serializer(serializers.Serializer):
    payment_id = serializers.IntegerField()
    payment_method = serializers.CharField()
    cashback_average = serializers.DecimalField(
        max_digits=10, decimal_places=2
    )


class Questao13Serializer(serializers.Serializer):
    payment_id = serializers.IntegerField()
    payment_method = serializers.CharField()
    cashback_average = serializers.DecimalField(
        max_digits=10, decimal_places=2
    )


class Questao14Serializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    amount_average = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.CharField()
    segment = serializers.CharField()
    channel = serializers.CharField()


class Questao15Serializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    amount_average = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.CharField()
    segment = serializers.CharField()
    channel = serializers.CharField()


class Questao16Serializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    amount_average = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.CharField()
    segment = serializers.CharField()
    channel = serializers.CharField()


class Questao17Serializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    amount_average = serializers.DecimalField(max_digits=10, decimal_places=2)
    state = serializers.CharField()
    segment = serializers.CharField()
    channel = serializers.CharField()


class Questao18Serializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    state = serializers.CharField()


class Questao19Serializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    state = serializers.CharField()


class Questao20Serializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    state = serializers.CharField()
