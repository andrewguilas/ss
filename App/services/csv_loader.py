import csv
from models.Order import Order as Order

def get_orders_from_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        return [Order(row) for row in rows]
