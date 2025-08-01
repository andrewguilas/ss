from App.services.csv_handler import get_orders_from_csv
from services.order_list import filter_orders, print_order_list
from models.Order import Order as Order
import config

def main():
    rows = get_orders_from_csv(config.FILE_NAME_ORDER_LIST_RAW)
    orders = [Order(row) for row in rows]
    orders = filter_orders(orders, 
                           campus=config.CAMPUS, 
                           min_item_count=1, 
                           dropoff_date=config.MOVE_DATE)
    
    print_order_list(orders)

if __name__ == '__main__':
    main()
