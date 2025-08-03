import app.services.core.order_list as order_list
from app.utils.date_utils import parse_date

def upload_order_list(args):
    if len(args) < 1:
        print("Usage: upload <filename>")
        return

    csv_file_name = args[0]

    print(f"Inputting orders from {csv_file_name}...")
    orders_count, routes_created_count, trucks_created_count = order_list.upload_order_list(csv_file_name)
    print(f"Successfully inputted and saved {orders_count} order(s) from {csv_file_name}.\nAutomatically created {routes_created_count} routes.\nAutomatically created {trucks_created_count} trucks.")

def generate_order_list(args):
    if len(args) < 2:
        print("Usage: generate <filename> <YYYY-MM-DD> [truck_number]")
        return
    
    pdf_file_name = args[0]
    truck_number = args[2]

    try:
        date = parse_date(args[1])
    except Exception:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    print(f"Generating order list for truck {truck_number} on {date} to {pdf_file_name}...")
    orders_count = order_list.generate_order_list(pdf_file_name, date)
    print(f"Successfully generated order list for truck {truck_number} on {date} with {orders_count} order(s) in {pdf_file_name}")

def print_order_list(args):
    if len(args) < 1:
        print("Usage: print <YYYY-MM-DD> [truck_number]")
        return

    try:
        date = parse_date(args[0])
    except Exception:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    truck_number = None
    if len(args) == 2:
        truck_number = args[1]

    order_list.print_order_list(date, truck_number)
