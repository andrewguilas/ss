import csv
from models.Order import Order as Order
from collections import defaultdict

CSV_FILE_NAME = 'Data/Order List.csv'

def read_csv_as_dicts(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def parse_orders_from_dicts(dicts):
    orders = []
    for row in dicts:
        order = Order(row)
        orders.append(order)
    return orders

def filter_orders(orders):
    return [
        order for order in orders
        if order.campus == "University of Virginia" and order.item_count > 0
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

def main():
    dicts = read_csv_as_dicts(CSV_FILE_NAME)
    orders = filter_orders(parse_orders_from_dicts(dicts))
    print_orders_by_dropoff_date(orders)

if __name__ == '__main__':
    main()
