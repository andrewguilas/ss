import app.services.core.order_list

def upload_order_list(csv_file_name):
    print(f"Inputting orders from {csv_file_name}...")
    orders_count = order_list.upload_order_list(csv_file_name)
    print(f"Successfully inputted and saved {orders_count} order(s) from {csv_file_name}")

def generate_order_list(pdf_file_name, date):
    print(f"Generating order list for {date} to {pdf_file_name}...")
    orders_count = order_list.generate_order_list(pdf_file_name, date)
    print(f"Successfully generated order list with {orders_count} order(s) for {date} in {pdf_file_name}")

def print_order_list(date):
    order_list.print_order_list(date)