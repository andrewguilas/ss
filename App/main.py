import csv

CSV_FILE_NAME = 'Data/Order List.csv'

def get_rows(file_name):
    rows = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            rows.append(row)
    return rows

def convert_rows_to_objects(rows):
    header = rows[0]
    new_objects = []
    for row in rows[1:]:
        new_object = {}
        for column_index, value in enumerate(row):
            column_header = header[column_index]
            new_object[column_header] = value
        new_objects.append(new_object)
    return new_objects

def main():
    rows = get_rows(CSV_FILE_NAME)
    customers = convert_rows_to_objects(rows)
    print(customers[0])

if __name__ == '__main__':
    main()
