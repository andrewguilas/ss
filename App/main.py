import csv
import models.Order as Order

CSV_FILE_NAME = 'Data/Order List.csv'

def get_rows(file_name):
    rows = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            rows.append(row)
    return rows

def convert_rows_to_dict(rows):
    header = rows[0]
    new_dict = []
    for row in rows[1:]:
        new_object = {}
        for column_index, value in enumerate(row):
            column_header = header[column_index]
            new_object[column_header] = value
        new_dict.append(new_object)
    return new_dict

def convert_dicts_to_orders(dicts):
    orders = []
    for dict in dicts:
        order = Order.Order(dict)
        orders.append(order)
    return orders

def main():
    rows = get_rows(CSV_FILE_NAME)
    dicts = convert_rows_to_dict(rows)
    orders = convert_dicts_to_orders(dicts)
    print(orders[0])

if __name__ == '__main__':
    main()
