import app.order_list as order_list
from app.utils.date_utils import parse_date 
import sys

def upload_order_list(file_name):
    print(f"Inputting orders from {file_name}...")
    orders_count = order_list.upload_order_list(file_name)
    print(f"Successfully inputted and saved {orders_count} order(s) from {file_name}")

def generate_order_list(file_name, date):
    print(f"Generating order list for {date} to {file_name}...")
    orders_count = order_list.generate_order_list(file_name, date)
    print(f"Successfully generated order list with {orders_count} order(s) for {date} in {file_name}")

def main():
    command = sys.argv[1].lower()
    args = sys.argv[2:]

    match command:
        case "upload":
            if len(args) < 1:
                print("Usage: upload <filename>")
            file_name = args[0]
            upload_order_list(file_name)

        case "generate":
            if len(args) < 2:
                print("Usage: generate <filename> <YYYY-MM-DD>")
            file_name = args[0]
            try:
                date = parse_date(args[1])
            except Exception:
                print("Invalid date format. Use YYYY-MM-DD.")
            generate_order_list(file_name, date)

        case "help":
            print("upload <file_name>\ngenerate <file_name> <date YYYY-MM-DD>\nexit\nhelp")

        case _:
            print("Unknown command.")

if __name__ == "__main__":
    main()
