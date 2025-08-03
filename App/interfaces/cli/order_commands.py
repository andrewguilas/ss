import app.services.core.order as order_service

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

def list_orders(date):
    pass

def details(order_id):
    pass
