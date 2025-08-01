from collections import defaultdict
from tabulate import tabulate
import services.csv_service as csv_service

ORDER_LIST_HEADERS = headers = ["Order ID", "Name", "Phone", "Location", "Items Ct", "Items", "Comments", "Pronunciation", "Time Loaded", "Time Delivered"]

def filter_orders(orders, campus=None, min_item_count=None, dropoff_date=None):
    return [
        order for order in orders
        if (campus is None or order.campus == campus)
        and (min_item_count is None or order.item_count >= min_item_count)
        and (dropoff_date is None or order.dropoff_date == dropoff_date)
    ]

def group_orders_by_dropoff_date(orders):
    dropoff_dates = defaultdict(list)
    for order in orders:
        dropoff_dates[order.dropoff_date].append(order)
    # lambda sorts by tuple (False, False)
    return sorted(dropoff_dates, key=lambda d: (d is None, d))

def extract_order_fields(order):
    return {
        "Order ID": order.order_id,
        "Name": order.name,
        "Phone": order.phone,
        "Location": order.dropoff_location,
        "Items Ct": order.item_count,
        "Items": order.items,
        "Comments": order.get_comments(is_dropoff=True),
        "Pronunciation": order.get_pronunciation(),
        "Time Loaded": " ",
        "Time Delivered": " "
    }

def print_order_list(orders):
    rows = [list(extract_order_fields(order).values()) for order in orders]
    print(tabulate(rows, headers=ORDER_LIST_HEADERS))

def generate_order_list(orders, file_name):
    rows = [extract_order_fields(order) for order in orders]
    csv_service.write_rows_to_csv(file_name, ORDER_LIST_HEADERS, rows)
