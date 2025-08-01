import csv

def get_rows_from_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
