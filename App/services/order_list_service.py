from collections import defaultdict
from tabulate import tabulate
import services.file_service as file_service
import config
import utils.date_utils as date_utils
import utils.phone_utils as phone_utils

ORDER_LIST_HEADERS_WIDTHS = {
    "Order ID": 8,
    "Name": 23,
    "Phone": 13,
    "Location": 30, # text wrap
    "Items Ct": 8,
    "Items": 30, # text wrap
    "Comments": 35, # text wrap
    "Pronunciation": 21,
    "Time Loaded": 13,
    "Time Delivered": 13,
}
ORDER_LIST_HEADERS_WRAPPED = ["Location", "Items", "Comments"]

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
        "Phone": phone_utils.format_phone_number(order.phone),
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
    print(tabulate(rows, headers=ORDER_LIST_HEADERS_WIDTHS))

def generate_order_list(orders, file_name):
    rows = [extract_order_fields(order) for order in orders]

    footer_rows = [
        ["Automatically generated"],
    ]

    xlsx_output_file_name = file_service.write_orders_to_xlsx(
        file_name,
        ORDER_LIST_HEADERS_WIDTHS,
        ORDER_LIST_HEADERS_WRAPPED,
        rows,
        title=f"{date_utils.format_date_short(config.MOVE_DATE)} - Truck 1/2 (Andrew) - {len(orders)} orders", # TODO: Implement trucks
        footer_rows=footer_rows
    )

    return xlsx_output_file_name
