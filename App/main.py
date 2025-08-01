import services.file_service as file_service
import services.order_list_service as order_list_service
import services.db_service as db_service
import models.order as order_model
import config

def upload_order_list(file_name):
    rows = file_service.get_rows_from_csv(file_name)
    orders = [order_model.Order(row) for row in rows]
    orders = order_list_service.filter_orders(orders, 
                           campus=config.CAMPUS, 
                           min_item_count=1, 
                           dropoff_date=config.MOVE_DATE)
    for order in orders:
        db_service.update(order)
    print(f"Successfully inputted orders from {file_name}")

def generate_order_list(file_name):
    orders = db_service.get_all()
    xlsx_output_file_name = order_list_service.generate_order_list(orders, file_name)
    pdf_output_file_name = file_service.convert_xlsx_to_pdf(xlsx_output_file_name)
    print(f"Successfully outputted orders to {pdf_output_file_name}")

def main():
    upload_order_list(config.ORDER_LIST_INPUT_FILE_NAME)
    generate_order_list(config.ORDER_LIST_OUTPUT_FILE_NAME)

if __name__ == "__main__":
    main()
