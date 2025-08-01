import app.services.file_service as file_service
import app.services.order_list_service as order_list_service
import app.services.db_service as db_service
import app.models.order as order_model
from app.utils.date_utils import parse_date 
import app.config as config
import sys

def upload_order_list(file_name):
    print(f"Inputting orders from {file_name}...")
    rows = file_service.get_rows_from_csv(file_name)
    for row in rows:
        order = order_model.Order(row)
        db_service.add_or_update_order(order)
    print(f"Successfully inputted and saved {len(row)} order(s) from {file_name}")

def generate_order_list(file_name, date):
    print(f"Generating order list for {date} to {file_name}...")
    orders = db_service.filter_orders(campus=config.CAMPUS, min_item_count=1, date=date)
    order_list_service.generate_order_list(orders, file_name, date)
    pdf_output_file_name = file_service.convert_xlsx_to_pdf(file_name)
    print(f"Successfully generated order list with {len(orders)} order(s) for {date} in {pdf_output_file_name}")

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
