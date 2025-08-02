import sys
import app.services.order_list as order_list
from app.utils.date_utils import parse_date

# Order List

def upload_order_list(csv_file_name):
    print(f"Inputting orders from {csv_file_name}...")
    orders_count = order_list.upload_order_list(csv_file_name)
    print(f"Successfully inputted and saved {orders_count} order(s) from {csv_file_name}")

def generate_order_list(pdf_file_name, date):
    print(f"Generating order list for {date} to {pdf_file_name}...")
    orders_count = order_list.generate_order_list(pdf_file_name, date)
    print(f"Successfully generated order list with {orders_count} order(s) for {date} in {pdf_file_name}")

# Truck

def add_truck(model='', comments=''):
    pass

def remove_truck(truck_id):
    pass

def assign_truck_to_route(truck_id, route_id):
    pass

def list_trucks():
    pass

# Route

def add_route(date, driver_name='', comments=''):
    pass

def remove_route(route_id):
    pass

def assign_route_to_order(route_id, order_id):
    pass

def list_routes(date=None):
    pass

# Order

def add_item(order_id, item_name):
    pass

def list_orders(date):
    order_list.print_order_list(date)

# Main

def main():
    if len(sys.argv) < 2:
        print("Usage: <command> [subcommand] [arguments...]")
        return

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    if command in ("truck", "route", "order"):
        if len(args) == 0:
            print(f"Usage: {command} <subcommand> [arguments...]")
            print(f"Available {command} subcommands: add, remove, assign, list")
            return

        subcommand = args[0].lower()
        subargs = args[1:]

        if command == "truck":
            match subcommand:
                case "add":
                    print("truck add not implemented yet")
                case "remove":
                    print("truck remove not implemented yet")
                case "assign":
                    print("truck assign not implemented yet")
                case "list":
                    print("truck list not implemented yet")
                case _:
                    print(f"Unknown truck subcommand: {subcommand}")

        elif command == "route":
            match subcommand:
                case "add":
                    print("route add not implemented yet")
                case "remove":
                    print("route remove not implemented yet")
                case "assign":
                    print("route assign not implemented yet")
                case "list":
                    print("route list not implemented yet")
                case _:
                    print(f"Unknown route subcommand: {subcommand}")

        else:  # order
            match subcommand:
                case "add-item":
                    print("order add-item not implemented yet")
                case "list":
                    print("order list not implemented yet")
                case _:
                    print(f"Unknown order subcommand: {subcommand}")

        return

    # Original flat commands
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
            generate_order_list(args[0], date)

        case "list_orders":
            if len(args) < 1:
                print("Usage: list_orders <YYYY-MM-DD> [truck_number]")
                return
            try:
                date = parse_date(args[0])
            except Exception:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
            list_orders(date)

        case "help":
            print("Commands:")
            print("  upload <csv_file_name>")
            print("  generate <pdf_file_name> <YYYY-MM-DD> [truck_number]")
            print("  list_orders <YYYY-MM-DD> [truck_number]")
            print("  truck <subcommand> [args...]")
            print("  route <subcommand> [args...]")
            print("  order <subcommand> [args...]")
            print("  help")

        case _:
            print(f"Unknown command: {command}. Run 'help' for options.")

if __name__ == "__main__":
    main()
