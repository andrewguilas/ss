import csv

ORDER_LIST_FILENAME = 'Data/Order List.csv'

def main():
    rows = []

    with open(ORDER_LIST_FILENAME, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            rows.append(', '.join(row))

    print(rows[1])

if __name__ == '__main__':
    main()
