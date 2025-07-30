import csv
import models.Order as Order

CSV_FILE_NAME = 'Data/Order List.csv'

def read_csv_as_dicts(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def convert_dicts_to_orders(dicts):
    orders = []
    for row in dicts:
        order = Order.Order(row)
        orders.append(order)
    return orders

def main():
    dicts = read_csv_as_dicts(CSV_FILE_NAME)
    orders = convert_dicts_to_orders(dicts)
    print(orders[0])

if __name__ == '__main__':
    main()
