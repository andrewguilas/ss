from tabulate import tabulate
import app.services.infra.file_io as file_service
import app.services.infra.db as db_service
import app.utils.date_utils as date_utils
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
        "Phone": order.phone,
        "Location": order.dropoff_location,
        "Items Ct": order.item_count,
        "Items": order.items,
        "Comments": "\n".join(order.comments),
        "Pronunciation": order.pronunciation,
        "Time Loaded": " ",
        "Time Delivered": " "
    }

def _generate_title(date, orders):
    date_text = date_utils.format_date_short(date)
    truck_number = 1 # orders[0].truck_number
    max_truck_number = 1 # max([order.truck_number for order in orders])
    orders_count = len(orders)
    driver = "Andrew" # orders[0].driver
    return f"{date_text} - Truck {truck_number}/{max_truck_number} ({driver}) - {orders_count} order(s)"

def print_order_list(date, truck_number=None):
    orders = db_service.get_orders(campus=config.CAMPUS, min_item_count=1, date=date)
    if len(orders) == 0:
        print("No orders found")
        return

    rows = [list(_extract_order_fields(order).values()) for order in orders]
    print(_generate_title(date, orders))
    print(tabulate(rows, headers=config.ORDER_LIST_HEADERS_WIDTHS))

def generate_order_list(pdf_file_name, date):
    xlsx_file_name = os.path.splitext(pdf_file_name)[0] + ".xlsx"
    orders = db_service.get_orders(campus=config.CAMPUS, min_item_count=1, date=date)
    if len(orders) == 0:
        print("No orders found")
        return
    rows = [_extract_order_fields(order) for order in orders]

    file_service.write_orders_to_xlsx(
        xlsx_file_name,
        config.ORDER_LIST_HEADERS_WIDTHS,
        config.ORDER_LIST_HEADERS_WRAPPED,
        rows,
        title=_generate_title(date, orders),
        footer_rows=config.ORDER_LIST_FOOTERS
    )

    file_service.convert_xlsx_to_pdf(xlsx_file_name, pdf_file_name)
    return len(orders)
