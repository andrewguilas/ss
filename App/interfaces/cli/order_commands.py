import app.services.core.order as order_service
from app.utils.date_utils import parse_date

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

def details(order_id):
    pass
