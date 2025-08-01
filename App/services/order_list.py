from collections import defaultdict
from tabulate import tabulate

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

def print_order_list(orders):
    rows = [
        [order.order_id, order.name, order.phone, order.dropoff_location, order.item_count, order.items, order.get_comments(is_dropoff=True), order.get_pronunciation()]
        for order in orders
    ]

    print(tabulate(rows, headers=["Order ID", "Name", "Phone", "Location", "Items Ct", "Items", "Comments", "Pronunciation"]))

def generate_order_list(orders, filename):
    pass
