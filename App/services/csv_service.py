import csv

def get_rows_from_csv(file_name):
    with open(file_name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def write_rows_to_csv(file_name, fieldnames, data):
    with open(file_name, "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
