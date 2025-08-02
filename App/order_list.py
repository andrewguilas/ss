from tabulate import tabulate
import app.services.file_service as file_service
import app.services.db_service as db_service
import app.utils.date_utils as date_utils
import app.utils.phone_utils as phone_utils
import app.models.order as order_model
import app.config as config
import os

def upload_order_list(csv_file_name):
    rows = file_service.get_rows_from_csv(csv_file_name)
    for row in rows:
        order = order_model.Order(row)
        db_service.add_or_update_order(order)
    return len(rows)

def _extract_order_fields(order):
    return {
        "Order ID": order.order_id,
        "Name": order.name,
        "Phone": phone_utils.format_phone_number(order.phone),
        "Location": order.dropoff_location,
        "Items Ct": order.item_count,
        "Items": order.items,
        "Comments": order.get_comments(is_dropoff=True),
        "Pronunciation": order.pronunciation,
        "Time Loaded": " ",
        "Time Delivered": " "
    }

def _print_order_list(orders):
    rows = [list(_extract_order_fields(order).values()) for order in orders]
    print(tabulate(rows, headers=config.ORDER_LIST_HEADERS_WIDTHS))

def generate_order_list(pdf_file_name, date):
    xlsx_file_name = os.path.splitext(pdf_file_name)[0] + ".xlsx"
    orders = db_service.filter_orders(campus=config.CAMPUS, min_item_count=1, date=date)
    rows = [_extract_order_fields(order) for order in orders]

    file_service.write_orders_to_xlsx(
        xlsx_file_name,
        config.ORDER_LIST_HEADERS_WIDTHS,
        config.ORDER_LIST_HEADERS_WRAPPED,
        rows,
        title=f"{date_utils.format_date_short(date)} - Truck 1/2 (Andrew) - {len(orders)} orders", # TODO: Implement trucks
        footer_rows=config.ORDER_LIST_FOOTERS
    )

    file_service.convert_xlsx_to_pdf(xlsx_file_name, pdf_file_name)
    return len(orders)
