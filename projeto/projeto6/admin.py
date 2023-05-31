from django.contrib import admin
from projeto6.models import Delivery


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        'delivery_id',
        'delivery_order_id',
        'driver_id',
        'delivery_distance_meters',
        'delivery_status',
    )
    list_per_page = 100
    readonly_fields = (
        'delivery_id',
        'delivery_order_id',
        'driver_id',
        'delivery_distance_meters',
        'delivery_status',
    )
    list_filter = (
        # 'delivery_id',
        # 'delivery_order_id',
        # 'driver_id',
        # 'delivery_distance_meters',
        'delivery_status',
    )
    search_fields = (
        'delivery_id',
        'delivery_order_id',
        'driver_id',
        'delivery_distance_meters',
        'delivery_status',
    )


# admin.site.register(Delivery, DeliveryAdmin)
