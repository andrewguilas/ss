import sys
from app.utils.date_utils import parse_date
import app.interfaces.cli.truck_commands as truck_commands
import app.interfaces.cli.route_commands as route_commands
import app.interfaces.cli.order_commands as order_commands
import app.interfaces.cli.order_list_commands as order_list_commands

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
                    truck_commands.add_truck(subargs)
                case "remove":
                    truck_commands.remove_truck(subargs)
                case "assign":
                    truck_commands.assign_truck_to_route(subargs)
                case "list":
                    truck_commands.list_trucks(subargs)
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
            order_list_commands.upload_order_list(args[0])

        case "generate":
            if len(args) < 2:
                print("Usage: generate <filename> <YYYY-MM-DD> [truck_number]")
                return
            try:
                date = parse_date(args[1])
            except Exception:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
            order_list_commands.generate_order_list(args[0], date)

        case "print":
            if len(args) < 1:
                print("Usage: print <YYYY-MM-DD> [truck_number]")
                return
            try:
                date = parse_date(args[0])
            except Exception:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
            order_list_commands.print_order_list(date)

        case "help":
            print("Commands:")
            print("  upload <csv_file_name>")
            print("  generate <pdf_file_name> <YYYY-MM-DD> [truck_number]")
            print("  print <YYYY-MM-DD> [truck_number]")
            print("  truck <subcommand> [args...]")
            print("  route <subcommand> [args...]")
            print("  order <subcommand> [args...]")
            print("  help")

        case _:
            print(f"Unknown command: {command}. Run 'help' for options.")

if __name__ == "__main__":
    main()
