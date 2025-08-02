import sys
import app.order_list as order_list
from app.utils.date_utils import parse_date

# Order List

def upload_order_list(csv_file_name):
    print(f"Inputting orders from {csv_file_name}...")
    orders_count = order_list.upload_order_list(csv_file_name)
    print(f"Successfully inputted and saved {orders_count} order(s) from {csv_file_name}")

def print_order_list(date, truck_number=1):
    order_list.print_order_list(date, truck_number)

def generate_order_list(pdf_file_name, date, truck_number=1):
    print(f"Generating order list for {date} to {pdf_file_name}...")
    orders_count = order_list.generate_order_list(pdf_file_name, date, truck_number)
    print(f"Successfully generated order list with {orders_count} order(s) for {date} in {pdf_file_name}")

# Truck

def add_truck(model='', comments=''):
    pass

def assign_truck_to_route(truck_id, route_id):
    pass

def remove_truck(truck_id):
    pass

# Route

def add_route(date, driver_name='', comments=''):
    pass

def assign_route_to_order(route_id, order_id):
    pass

def remove_route(route_id):
    pass

# Main

def main():
    if len(sys.argv) < 2:
        print("Usage: <command> [arguments...]")
        return

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    match command:
        case "upload":
            if len(args) < 1:
                print("Usage: upload <filename>")
                return
            upload_order_list(args[0])

        case "generate":
            if len(args) < 2:
                print("Usage: generate <filename> <YYYY-MM-DD> [truck_number]")
                return
            try:
                date = parse_date(args[1])
            except Exception:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
            truck_number = int(args[2]) if len(args) > 2 else 1
            generate_order_list(args[0], date, truck_number)

        case "print":
            if len(args) < 1:
                print("Usage: print <YYYY-MM-DD> [truck_number]")
                return
            try:
                date = parse_date(args[0])
            except Exception:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
            truck_number = int(args[1]) if len(args) > 1 else 1
            print_order_list(date, truck_number)

        case "set_truck":
            if len(args) < 2:
                print("Usage: set_truck <order_id> <truck_number> <driver>")
                return
            set_truck(args[0], int(args[1]), args[2])

        case "help":
            print("Commands:")
            print("  upload <csv_file_name>")
            print("  generate <pdf_file_name> <YYYY-MM-DD> [truck_number]")
            print("  print <YYYY-MM-DD> [truck_number]")
            print("  set_truck <order_id> <truck_number>")
            print("  help")

        case _:
            print(f"Unknown command: {command}. Run 'help' for options.")

if __name__ == "__main__":
    main()
