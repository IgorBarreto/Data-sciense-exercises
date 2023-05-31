import csv
from datetime import datetime

import pandas as pd
from celery import shared_task
from django.core.files.storage import default_storage

from projeto6.models import Delivery, Hub, Order, Payment, Store


@shared_task(bind=True, max_retries=1, default_retry_delay=1)
def load_deliveries_file(self, file):
    df = pd.read_csv(file, delimiter=',')
    df['driver_id'].fillna(-1, inplace=True)
    df['delivery_distance_meters'].fillna(-1, inplace=True)

    delivery_list = []
    Delivery.truncate()
    for _, row in df.iterrows():
        print(f"{_} {row['delivery_id']}")
        new_file = Delivery(
            delivery_id=row['delivery_id'],
            delivery_order_id=row['delivery_order_id'],
            driver_id=row['driver_id'],
            delivery_distance_meters=row['delivery_distance_meters'],
            delivery_status=row['delivery_status'],
        )
        delivery_list.append(new_file)
    Delivery.objects.bulk_create(delivery_list)
    if default_storage.exists(file):
        default_storage.delete(file)


@shared_task(bind=True, max_retries=1, default_retry_delay=1)
def load_hubs_file(self, file):
    df = pd.read_csv(file, delimiter=',', encoding='windows-1252')
    hub_list = []
    Hub.truncate()
    for _, row in df.iterrows():
        new_file = Hub(
            hub_id=row['hub_id'],
            hub_name=row['hub_name'],
            hub_city=row['hub_city'],
            hub_state=row['hub_state'],
            hub_latitude=row['hub_latitude'],
            hub_longitude=row['hub_longitude'],
        )
        hub_list.append(new_file)
    Hub.objects.bulk_create(hub_list)
    if default_storage.exists(file):
        default_storage.delete(file)


def read_csv(file):
    order_list = []
    with open(file, 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=',')

        cabecalho = next(leitor_csv)

        for linha in leitor_csv:
            obj = {}
            for c, v in zip(cabecalho, linha):
                obj[c.strip()] = v.strip()
            order_list.append(obj)
    return order_list


def data_handling(orders):
    FORMAT_STR_ALT = "%m/%d/%Y %I:%M:%S %p"
    new_orders = []
    for order in orders:
        for k, v in order.items():
            if len(v.strip()) == 0:
                order[k] = None
        new_obj = {}
        new_obj['order_id'] = (
            int(order['order_id']) if order['order_id'] else None
        )
        new_obj['store_id'] = (
            int(order['store_id']) if order['store_id'] else None
        )
        new_obj['channel_id'] = (
            int(order['channel_id']) if order['channel_id'] else None
        )
        new_obj['payment_order_id'] = (
            int(order['payment_order_id'])
            if order['payment_order_id']
            else None
        )
        new_obj['delivery_order_id'] = (
            int(order['delivery_order_id'])
            if order['delivery_order_id']
            else None
        )
        new_obj['order_status'] = str(order['order_status'])
        new_obj['order_amount'] = (
            float(order['order_amount']) if order['order_amount'] else None
        )
        new_obj['order_delivery_fee'] = (
            float(order['order_delivery_fee'])
            if order['order_delivery_fee']
            else None
        )
        new_obj['order_delivery_cost'] = (
            float(order['order_delivery_cost'])
            if order['order_delivery_cost']
            else None
        )
        new_obj['order_created_hour'] = int(order['order_created_hour'])
        new_obj['order_created_minute'] = int(order['order_created_minute'])
        new_obj['order_created_day'] = int(order['order_created_day'])
        new_obj['order_created_month'] = int(order['order_created_month'])
        new_obj['order_created_year'] = int(order['order_created_year'])
        new_obj['order_moment_created'] = datetime.strptime(
            order['order_moment_created'], FORMAT_STR_ALT
        )
        new_obj['order_moment_accepted'] = (
            datetime.strptime(order['order_moment_accepted'], FORMAT_STR_ALT)
            if order['order_moment_accepted']
            else None
        )
        new_obj['order_moment_ready'] = (
            datetime.strptime(order['order_moment_ready'], FORMAT_STR_ALT)
            if order['order_moment_ready']
            else None
        )
        new_obj['order_moment_collected'] = (
            datetime.strptime(order['order_moment_collected'], FORMAT_STR_ALT)
            if order['order_moment_collected']
            else None
        )
        new_obj['order_moment_in_expedition'] = (
            datetime.strptime(
                order['order_moment_in_expedition'], FORMAT_STR_ALT
            )
            if order['order_moment_in_expedition']
            else None
        )
        new_obj['order_moment_delivering'] = (
            datetime.strptime(order['order_moment_delivering'], FORMAT_STR_ALT)
            if order['order_moment_delivering']
            else None
        )
        new_obj['order_moment_delivered'] = (
            datetime.strptime(order['order_moment_delivered'], FORMAT_STR_ALT)
            if order['order_moment_delivered']
            else None
        )
        new_obj['order_moment_finished'] = (
            datetime.strptime(order['order_moment_finished'], FORMAT_STR_ALT)
            if order['order_moment_finished']
            else None
        )
        new_obj['order_metric_collected_time'] = (
            float(order['order_metric_collected_time'])
            if order['order_metric_collected_time']
            else None
        )
        new_obj['order_metric_paused_time'] = (
            float(order['order_metric_paused_time'])
            if order['order_metric_paused_time']
            else None
        )
        new_obj['order_metric_production_time'] = (
            float(order['order_metric_production_time'])
            if order['order_metric_production_time']
            else None
        )
        new_obj['order_metric_walking_time'] = (
            float(order['order_metric_walking_time'])
            if order['order_metric_walking_time']
            else None
        )
        new_obj['order_metric_expediton_speed_time'] = (
            float(order['order_metric_expediton_speed_time'])
            if order['order_metric_expediton_speed_time']
            else None
        )
        new_obj['order_metric_transit_time'] = (
            float(order['order_metric_transit_time'])
            if order['order_metric_transit_time']
            else None
        )
        new_obj['order_metric_cycle_time'] = (
            float(order['order_metric_cycle_time'])
            if order['order_metric_cycle_time']
            else None
        )
        new_orders.append(new_obj)
    return new_orders


@shared_task(bind=True, max_retries=1, default_retry_delay=1)
def load_orders_file(self, file):
    orders = read_csv(file)
    orders = data_handling(orders)
    order_list = []
    for order in orders:
        new_file = Order(
            order_id=order['order_id'],
            store_id=order['store_id'],
            channel_id=order['channel_id'],
            payment_order_id=order['payment_order_id'],
            delivery_order_id=order['delivery_order_id'],
            order_status=order['order_status'],
            order_amount=order['order_amount'],
            order_delivery_fee=order['order_delivery_fee'],
            #
            order_delivery_cost=order['order_delivery_cost'],
            # order_created_hour=order['order_created_hour'],
            # order_created_minute=order['order_created_minute'],
            # order_created_day=order['order_created_day'],
            # order_created_month=order['order_created_month'],
            #
            # order_created_year=order['order_created_year'],
            # order_moment_created=order['order_moment_created'],
            # order_moment_accepted=order['order_moment_accepted'],
            # order_moment_ready=order['order_moment_ready'],
            # order_moment_collected=order['order_moment_collected'],
            # order_moment_in_expedition=order['order_moment_in_expedition'],
            # order_moment_delivering=order['order_moment_delivering'],
            # order_moment_delivered=order['order_moment_delivered'],
            # order_moment_finished=order['order_moment_finished'],
            # order_metric_collected_time=order['order_metric_collected_time'],
            # order_metric_paused_time=order['order_metric_paused_time'],
            # order_metric_production_time=order['order_metric_production_time'],
            # order_metric_walking_time=order['order_metric_walking_time'],
            # order_metric_expediton_speed_time=order[
            #     'order_metric_expediton_speed_time'
            # ],
            # order_metric_transit_time=order['order_metric_transit_time'],
            # order_metric_cycle_time=order['order_metric_cycle_time'],
        )
        print(f"NF = {new_file.order_id} - {new_file.order_delivery_cost}")
        order_list.append(new_file)
    Order.objects.bulk_create(order_list)
    if default_storage.exists(file):
        default_storage.delete(file)


@shared_task(bind=True, max_retries=1, default_retry_delay=1)
def load_payment_file(self, file):
    df = pd.read_csv(file, delimiter=',')
    df['payment_id'].fillna(-1, inplace=True)
    df['payment_order_id'].fillna(-1, inplace=True)
    df['payment_amount'].fillna(-1, inplace=True)
    df['payment_fee'].fillna(-1, inplace=True)
    payment_list = []
    Payment.truncate()
    for _, row in df.iterrows():
        # print(row)
        new_file = Payment(
            payment_id=row['payment_id'],
            payment_order_id=row['payment_order_id'],
            payment_amount=row['payment_amount'],
            payment_fee=row['payment_fee'],
            payment_method=row['payment_method'],
            payment_status=row['payment_status'],
        )
        payment_list.append(new_file)
    Payment.objects.bulk_create(payment_list)
    if default_storage.exists(file):
        default_storage.delete(file)


@shared_task(bind=True, max_retries=1, default_retry_delay=1)
def load_store_file(self, file):
    df = pd.read_csv(file, delimiter=',', encoding='windows-1252')
    df['store_plan_price'].fillna(-1, inplace=True)
    df['store_latitude'].fillna(-1, inplace=True)
    df['store_longitude'].fillna(-1, inplace=True)
    store_list = []
    Store.truncate()
    for _, row in df.iterrows():
        # print(row)
        new_file = Store(
            store_id=row['store_id'],
            hub_id=row['hub_id'],
            store_name=row['store_name'],
            store_segment=row['store_segment'],
            store_plan_price=row['store_plan_price'],
            store_latitude=row['store_latitude'],
            store_longitude=row['store_longitude'],
        )
        store_list.append(new_file)
    Store.objects.bulk_create(store_list)
    if default_storage.exists(file):
        default_storage.delete(file)
