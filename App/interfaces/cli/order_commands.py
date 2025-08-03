import app.services.core.order as order_service
from app.utils.date_utils import parse_date
from tabulate import tabulate

def assign_order_to_route(subargs):
    if len(subargs) < 2:
        print("Usage: order assign <order_id> <route_id>")
        return

    order_id = int(subargs[0])
    route_id = int(subargs[1])

    try:
        order_service.assign_order_to_route(order_id=order_id, route_id=route_id)
        print(f"Successfully assigned order {order_id} to route {route_id}")
    except Exception as e:
        print(f"Failed to assign order {order_id} to route {route_id}: {e}")

def list_orders(subargs):
    date = None
    if len(subargs) > 0:
        try:
            date = parse_date(subargs[0])
        except Exception:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

    try:
        orders = order_service.list_orders(date=date)
        if not orders:
            print("No orders found")
            return
        
        for order in orders:
            print(order)
    except Exception as e:
        print(f"Failed to list orders: {e}")

def details(subargs):
    if len(subargs) != 1:
        print("Usage: order details <order_id>")
        return

    try:
        order_id = int(subargs[0])
    except ValueError:
        print("Order ID must be an integer.")
        return

    try:
        order = order_service.get_order_details(order_id=order_id)

        headers = [
            "order_id",
            "campus",
            "name",
            "phone",
            "pronunciation",
            "comments",
            "pickup_date",
            "pickup_location",
            "pickup_proxy_name",
            "pickup_proxy_phone",
            "dropoff_date",
            "dropoff_location",
            "dropoff_proxy_name",
            "dropoff_proxy_phone",
            "item_count",
            "items"
        ]

        item_summary = ", ".join(str(item) for item in order.items) if order.items else ""

        data = [
            order.order_id,
            order.campus,
            order.name,
            order.phone,
            order.pronunciation,
            order.comments,
            order.pickup_date,
            order.pickup_location,
            order.pickup_proxy_name,
            order.pickup_proxy_phone,
            order.dropoff_date,
            order.dropoff_location,
            order.dropoff_proxy_name,
            order.dropoff_proxy_phone,
            order.item_count,
            item_summary
        ]

        table = list(zip(headers, data))
        print(tabulate(table, headers=["Field", "Value"]))

    except Exception as e:
        print(f"Failed to list order details: {e}")
