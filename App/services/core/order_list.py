from tabulate import tabulate
import app.services.infra.file_io as file_service
import app.services.infra.db as db_service
import app.services.core.route as route_service
import app.utils.date_utils as date_utils
from app.utils.debug_utils import print_message
import app.models.order as order_model
import app.models.route as route_model
import app.config as config
import os
from sqlalchemy.orm import joinedload
from enum import Enum
from alive_progress import alive_bar

class Status(Enum):
    ASSIGNED = "assigned"
    ASSIGNED_AND_GENERATED = "assigned_and_generated"

def upload_order_list(csv_file_name):
    routes_created_count = 0
    trucks_created_count = 0

    rows = file_service.get_rows_from_csv(csv_file_name)
    session = db_service.get_session()
    try:
        rows_count = len(rows)
        with alive_bar(rows_count, title="Uploading Orders") as bar:
            for current_row_index, row in enumerate(rows):
                status = None

                order = order_model.Order(row)
                if order.campus != config.CAMPUS:
                    print_message(f"Skipped order because campus != {config.CAMPUS}")
                    bar()
                    continue
                elif order.item_count == 0:
                    print_message(f"Skipped order because item count is 0")
                    bar()
                    continue

                if order.dropoff_date:
                    route = session.query(route_model.Route).filter(
                        route_model.Route.date == order.dropoff_date
                    ).first()
                    if route:
                        status = Status.ASSIGNED
                    else:
                        # if the order has a dropoff date,
                        # automatically assign it a default route
                        route, is_truck_created = route_service.add_route(date=order.dropoff_date, session=session)
                        trucks_created_count += 1 if is_truck_created else 0
                        status = Status.ASSIGNED_AND_GENERATED
                    order.route = route

                session.add(order)

                if status == Status.ASSIGNED:
                    print_message(f"Automatically assigned route {route.route_id} to order {order.order_id}")
                elif status == Status.ASSIGNED_AND_GENERATED:
                    print_message(f"Automatically generated route {route.route_id} for {order.dropoff_date} and assigned to order {order.order_id}")
                    routes_created_count += 1

                print_message(f"Added order {order.order_id}")
                bar()
                
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
    return len(rows), routes_created_count, trucks_created_count

def _extract_order_fields(order):
    return {
        "Order ID": order.order_id,
        "Name": order.name,
        "Phone": order.phone,
        "Location": order.dropoff_location,
        "Items Ct": order.item_count,
        "Items": order.items,
        "Comments": "\n".join(order.comments) if isinstance(order.comments, list) else order.comments,
        "Pronunciation": order.pronunciation,
        "Time Loaded": " ",
        "Time Delivered": " "
    }

def _generate_title(date, orders):
    if not orders:
        return "No orders"

    route = orders[0].route
    truck_number = 1 # _calculate_truck_number() TODO
    max_truck_number = 1 # _calculate_max_truck_number() TODO
    driver = route.driver_name or "Unknown"

    date_text = date_utils.format_date_short(date)
    orders_count = len(orders)
    return f"{date_text} - Truck {truck_number} (Driver: {driver}) - {orders_count} order(s)"

def print_order_list(date, truck_number=None):
    session = db_service.get_session()
    try:
        query = session.query(order_model.Order)
        if config.IS_DROPOFF_SEASON:
            query = query.filter(order_model.Order.dropoff_date == date)
        else:
            query = query.filter(order_model.Order.pickup_date == date)

        orders = query.options(joinedload(order_model.Order.route).joinedload(route_model.Route.truck))\
              .order_by(order_model.Order.order_id)\
              .all()
        if not orders:
            print("No orders found")
            return

        rows = [list(_extract_order_fields(order).values()) for order in orders]
        print(_generate_title(date, orders))
        print(tabulate(rows, headers=config.ORDER_LIST_HEADERS_WIDTHS))
    finally:
        session.close()

def generate_order_list(pdf_file_name, date):
    xlsx_file_name = os.path.splitext(pdf_file_name)[0] + ".xlsx"

    session = db_service.get_session()
    try:
        query = session.query(order_model.Order)
        if config.IS_DROPOFF_SEASON:
            query = query.filter(order_model.Order.dropoff_date == date)
        else:
            query = query.filter(order_model.Order.pickup_date == date)

        orders = query.options(joinedload(order_model.Order.route).joinedload(route_model.Route.truck))\
              .order_by(order_model.Order.order_id)\
              .all()
        if not orders:
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
    finally:
        session.close()
