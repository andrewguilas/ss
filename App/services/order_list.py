from collections import defaultdict

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

def generate_order_list(orders):
    for order in orders:
        order_id = order.order_id
        name = order.name
        phone = order.phone
        location = order.dropoff_location
        comments = "".join(order.generate_comments(is_dropoff=True))
        print(f"{order_id}\t{name}\t{phone}\t{location}\t{comments}")
