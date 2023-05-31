from django.db import connection, models


# Create your models here.
class Channel(models.Model):
    class Meta:
        db_table = 'p06Channels'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    channel_id = models.IntegerField(primary_key=True)
    channel_name = models.CharField(max_length=50)
    channel_type = models.CharField(max_length=50)


class Delivery(models.Model):
    class Meta:
        db_table = 'p06Deliveries'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    delivery_id = models.IntegerField(primary_key=True)
    delivery_order_id = models.IntegerField()
    driver_id = models.IntegerField(null=True)
    delivery_distance_meters = models.IntegerField()
    delivery_status = models.CharField(max_length=50)


class Driver(models.Model):
    class Meta:
        db_table = 'p06Drivers'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    driver_id = models.IntegerField(primary_key=True)
    driver_modal = models.CharField(max_length=50)
    driver_type = models.CharField(max_length=50)


class Hub(models.Model):
    class Meta:
        db_table = 'p06Hubs'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    hub_id = models.IntegerField(primary_key=True)
    hub_name = models.CharField(max_length=100)
    hub_city = models.CharField(max_length=100)
    hub_state = models.CharField(max_length=100)
    hub_latitude = models.DecimalField(max_digits=10, decimal_places=6)
    hub_longitude = models.DecimalField(max_digits=10, decimal_places=6)


class Order(models.Model):
    class Meta:
        db_table = 'p06Orders'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    order_id = models.IntegerField(primary_key=True)
    store_id = models.IntegerField(null=True)
    channel_id = models.IntegerField(null=True)
    payment_order_id = models.IntegerField(null=True)
    delivery_order_id = models.IntegerField(null=True)
    order_status = models.CharField(max_length=100, null=True)
    order_amount = models.DecimalField(
        null=True, max_digits=10, decimal_places=2
    )
    order_delivery_fee = models.DecimalField(
        null=True, max_digits=10, decimal_places=2
    )
    order_delivery_cost = models.DecimalField(
        null=True, max_digits=10, decimal_places=2
    )
    order_created_hour = models.IntegerField(null=True)
    order_created_minute = models.IntegerField(null=True)
    order_created_day = models.IntegerField(null=True)
    order_created_month = models.IntegerField(null=True)
    order_created_year = models.IntegerField(null=True)
    order_moment_created = models.DateTimeField(null=True)
    order_moment_accepted = models.DateTimeField(null=True)
    order_moment_ready = models.DateTimeField(null=True)
    order_moment_collected = models.DateTimeField(null=True)
    order_moment_in_expedition = models.DateTimeField(null=True)
    order_moment_delivering = models.DateTimeField(null=True)
    order_moment_delivered = models.DateTimeField(null=True)
    order_moment_finished = models.DateTimeField(null=True)
    order_metric_collected_time = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    order_metric_paused_time = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    order_metric_production_time = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    order_metric_walking_time = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    order_metric_expediton_speed_time = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    order_metric_transit_time = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    order_metric_cycle_time = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )


class Payment(models.Model):
    class Meta:
        db_table = 'p06Payments'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    payment_id = models.IntegerField(primary_key=True)
    payment_order_id = models.IntegerField(null=True)
    payment_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    payment_fee = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    payment_method = models.CharField(max_length=50, null=True)
    payment_status = models.CharField(max_length=100, null=True)


class Store(models.Model):
    class Meta:
        db_table = 'p06Stores'

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f'TRUNCATE TABLE "{cls._meta.db_table}" RESTART IDENTITY'
            )

    store_id = models.IntegerField(primary_key=True)
    hub_id = models.IntegerField(null=True)
    store_name = models.CharField(max_length=100)
    store_segment = models.CharField(max_length=100)
    store_plan_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    store_latitude = models.IntegerField(null=True)
    store_longitude = models.IntegerField(null=True)
