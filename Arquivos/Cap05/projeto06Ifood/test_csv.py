import csv
from datetime import datetime

file = 'orders_test.csv'
FORMAT_STR = "%d/%m/%Y %I:%M:%S %p"
order_list = []
with open(file, 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=',')

    cabecalho = next(leitor_csv)

    for linha in leitor_csv:
        obj = {}
        for c, v in zip(cabecalho, linha):
            obj[c.strip()] = v.strip()
        order_list.append(obj)
new_list = []
for order in order_list:
    for k, v in order.items():
        print(len(v))
        if len(v.strip()) == 0:
            order[k] = None
    new_obj = {}
    new_obj['order_id'] = (
        int(order['order_id']) if order['order_id'] else None
    )  # models.IntegerField(primary_key=True)
    new_obj['store_id'] = (
        int(order['store_id']) if order['store_id'] else None
    )  # models.IntegerField(null=True)
    new_obj['channel_id'] = (
        int(order['channel_id']) if order['channel_id'] else None
    )  # models.IntegerField(null=True)
    new_obj['payment_order_id'] = (
        int(order['payment_order_id']) if order['payment_order_id'] else None
    )  # models.IntegerField(null=True)
    new_obj['delivery_order_id'] = (
        int(order['delivery_order_id']) if order['delivery_order_id'] else None
    )  # models.IntegerField(null=True)
    new_obj['order_status'] = str(
        order['order_status']
    )  # models.CharField(max_length=100, null=True)
    new_obj['order_amount'] = (
        float(order['order_amount']) if order['order_amount'] else None
    )  # models.DecimalField(null=True, max_digits=10, decimal_places=2)
    new_obj['order_delivery_fee'] = (
        float(order['order_delivery_fee'])
        if order['order_delivery_fee']
        else None
    )  # models.DecimalField(null=True, max_digits=10, decimal_places=2)
    new_obj['order_delivery_cost'] = (
        float(order['order_delivery_cost'])
        if order['order_delivery_cost']
        else None
    )  # models.DecimalField(null=True, max_digits=10, decimal_places=2)
    new_obj['order_created_hour'] = int(
        order['order_created_hour']
    )  # models.IntegerField(null=True)
    new_obj['order_created_minute'] = int(
        order['order_created_minute']
    )  # models.IntegerField(null=True)
    new_obj['order_created_day'] = int(
        order['order_created_day']
    )  # models.IntegerField(null=True)
    new_obj['order_created_month'] = int(
        order['order_created_month']
    )  # models.IntegerField(null=True)
    new_obj['order_created_year'] = int(
        order['order_created_year']
    )  # models.IntegerField(null=True)
    new_obj['order_moment_created'] = datetime.strptime(
        order['order_moment_created'], FORMAT_STR
    )  # models.DateTimeField(null=True)
    new_obj['order_moment_accepted'] = (
        datetime.strptime(order['order_moment_accepted'], FORMAT_STR)
        if order['order_moment_accepted']
        else None
    )  # models.DateTimeField(null=True)
    new_obj['order_moment_ready'] = (
        datetime.strptime(order['order_moment_ready'], FORMAT_STR)
        if order['order_moment_ready']
        else None
    )  # models.DateTimeField(null=True)
    new_obj['order_moment_collected'] = (
        datetime.strptime(order['order_moment_collected'], FORMAT_STR)
        if order['order_moment_collected']
        else None
    )  # models.DateTimeField(null=True)
    new_obj['order_moment_in_expedition'] = (
        datetime.strptime(order['order_moment_in_expedition'], FORMAT_STR)
        if order['order_moment_in_expedition']
        else None
    )  # models.DateTimeField(null=True)
    new_obj['order_moment_delivering'] = (
        datetime.strptime(order['order_moment_delivering'], FORMAT_STR)
        if order['order_moment_delivering']
        else None
    )  # models.DateTimeField(null=True)
    new_obj['order_moment_delivered'] = (
        datetime.strptime(order['order_moment_delivered'], FORMAT_STR)
        if order['order_moment_delivered']
        else None
    )  # models.DateTimeField(null=True)
    new_obj['order_moment_finished'] = (
        datetime.strptime(order['order_moment_finished'], FORMAT_STR)
        if order['order_moment_finished']
        else None
    )  # models.DateTimeField(null=True)
    new_obj['order_metric_collected_time'] = (
        float(order['order_metric_collected_time'])
        if order['order_metric_collected_time']
        else None
    )  # models.DecimalField(max_digits=10, decimal_places=2, null=True)
    new_obj['order_metric_paused_time'] = (
        float(order['order_metric_paused_time'])
        if order['order_metric_paused_time']
        else None
    )  # models.DecimalField(max_digits=10, decimal_places=2, null=True)
    new_obj['order_metric_production_time'] = (
        float(order['order_metric_production_time'])
        if order['order_metric_production_time']
        else None
    )  # models.DecimalField(max_digits=10, decimal_places=2, null=True)
    new_obj['order_metric_walking_time'] = (
        float(order['order_metric_walking_time'])
        if order['order_metric_walking_time']
        else None
    )  # models.DecimalField(max_digits=10, decimal_places=2, null=True)
    new_obj['order_metric_expediton_speed_time'] = (
        float(order['order_metric_expediton_speed_time'])
        if order['order_metric_expediton_speed_time']
        else None
    )  # models.DecimalField(max_digits=10, decimal_places=2, null=True)
    new_obj['order_metric_transit_time'] = (
        float(order['order_metric_transit_time'])
        if order['order_metric_transit_time']
        else None
    )  # models.DecimalField(max_digits=10, decimal_places=2, null=True)
    new_obj['order_metric_cycle_time'] = (
        float(order['order_metric_cycle_time'])
        if order['order_metric_cycle_time']
        else None
    )  # models.DecimalField(max_digits=10, decimal_places=2, null=True)
    exit()
