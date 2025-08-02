def show_commands(args):
    print("Commands:")

    print("  upload <csv_file_name>")
    print("  generate <pdf_file_name> <YYYY-MM-DD> [truck_number]")
    print("  print <YYYY-MM-DD> [truck_number]")

    print("  truck add [model] [comments]")
    print("  truck remove <truck_id>")
    print("  truck list")

    print("  route add <YYYY-MM-DD> [driver_name] [comments]")
    print("  route remove <route_id>")
    print("  route list")
    print("  route assign <route_id <truck_id")

    print("  order assign <order_id> <route_id>")
    print("  order add_item <order_id> <item_name>")
    print("  order info <order_id>")

    print("  help")
