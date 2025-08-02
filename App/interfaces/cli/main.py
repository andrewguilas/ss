import sys
import app.interfaces.cli.truck_commands as truck_commands
import app.interfaces.cli.route_commands as route_commands
import app.interfaces.cli.order_commands as order_commands
import app.interfaces.cli.order_list_commands as order_list_commands
import app.interfaces.cli.global_commands as global_commands

def main():
    if len(sys.argv) < 2:
        print("Usage: <command> [subcommand] [arguments...]")
        return

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    if command in ("truck", "route", "order"):
        if len(args) == 0:
            print(f"Usage: {command} <subcommand> [arguments...]")
            return

        subcommand = args[0].lower()
        subargs = args[1:]

        if command == "truck":
            match subcommand:
                case "add":
                    truck_commands.add_truck(subargs)
                case "remove":
                    truck_commands.remove_truck(subargs)
                case "list":
                    truck_commands.list_trucks(subargs)
                case _:
                    print(f"Unknown truck subcommand: {subcommand}")

        elif command == "route":
            match subcommand:
                case "add":
                    route_commands.add_route(subargs)
                case "remove":
                    route_commands.remove_route(subargs)
                case "list":
                    route_commands.list_routes(subargs)
                case "assign":
                    route_commands.assign_route_to_truck(subargs)
                case _:
                    print(f"Unknown route subcommand: {subcommand}")

        elif command == "route":
            match subcommand:
                case "assign":
                    print("order assign not implemented yet")
                case "add_item":
                    print("order add_item not implemented yet")
                case "info":
                    print("order info not implemented yet")
                case _:
                    print(f"Unknown order subcommand: {subcommand}")

        return

    # Original global commands
    match command:
        case "upload":
            order_list_commands.upload_order_list(args)

        case "generate":
            order_list_commands.generate_order_list(args)

        case "print":
            order_list_commands.print_order_list(args)

        case "help":
            global_commands.show_commands(args)

        case _:
            print(f"Unknown command: {command}. Run 'help' for options.")

if __name__ == "__main__":
    main()
