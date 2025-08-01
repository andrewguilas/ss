from datetime import date
from services.csv_loader import get_orders_from_csv
from services.order_list import filter_orders, generate_order_list

CSV_FILE_NAME = 'Data/Order List.csv'

def main():
    orders = get_orders_from_csv(CSV_FILE_NAME)
    orders = filter_orders(orders, 
                           campus="University of Virginia", 
                           min_item_count=1, 
                           dropoff_date=date(2025, 8, 22))
    
    generate_order_list(orders)

if __name__ == '__main__':
    main()
