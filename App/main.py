from collections import defaultdict
from datetime import date
from services.csv_loader import get_orders_from_csv

CSV_FILE_NAME = 'Data/Order List.csv'

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
    return dropoff_dates

def print_orders_by_dropoff_date(orders):
    dropoff_dates = group_orders_by_dropoff_date(orders)

    # lambda sorts by tuple (False, False)
    for dropoff_date in sorted(dropoff_dates, key=lambda d: (d is None, d)):
        orders = dropoff_dates[dropoff_date]
        print(f"{dropoff_date} - {len(orders)} order(s)")
        for order in orders:
            print(order)
        print()

def generate_order_list(orders):
    for order in orders:
        order_id = order.order_id
        name = order.name
        phone = order.phone
        location = order.dropoff_location
        comments = "".join(order.generate_comments(is_dropoff=True))
        print(f"{order_id}\t{name}\t{phone}\t{location}\t{comments}")

def main():
    orders = get_orders_from_csv(CSV_FILE_NAME)
    orders = filter_orders(orders, 
                           campus="University of Virginia", 
                           min_item_count=1, 
                           dropoff_date=date(2025, 8, 22))
    
    generate_order_list(orders)

if __name__ == '__main__':
    main()
