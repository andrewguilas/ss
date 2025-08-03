import app.services.core.route as route_service
from app.utils.date_utils import parse_date

def add_route(subargs):
    if len(subargs) == 0:
        print("Usage: route add <YYYY-MM-DD> [driver_name] [comments] [truck_id]")
        return

    try:
        date = parse_date(subargs[0])
    except Exception:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    driver_name = subargs[1] if len(subargs) >= 2 else None
    truck_id = int(subargs[3]) if len(subargs) >= 4 else None
    comments = subargs[2] if len(subargs) >= 3 else None

    try:
        new_route, trucks_created_count = route_service.add_route(date=date, driver_name=driver_name, comments=comments, truck_id=truck_id)
        print(f"Successfully added route {new_route.route_id} for {date} with driver {driver_name or 'N/A'} for truck {truck_id or 'N/A'}")
    except Exception as e:
        print(f"Failed to add route for {date} with driver {driver_name or 'N/A'} for truck {truck_id or 'N/A'}: {e}")

def remove_route(subargs):
    if len(subargs) == 0:
        print("Usage: route remove <route_id>")
        return

    route_id = subargs[0]

    try:
        route_service.remove_route(route_id=route_id)
        print(f"Successfully removed route {route_id}")
    except Exception as e:
        print(f"Failed to remove route {route_id}: {e}")

def list_routes(subargs):
    date = None
    if len(subargs) > 0:
        try:
            date = parse_date(subargs[0])
        except Exception:
            print("Invalid date format. Use YYYY-MM-DD.")
            return
    
    try:
        routes = route_service.list_routes(date=date)
        if not routes:
            print("No routes found")
            return
        
        for route in routes:
            print(route)
    except Exception as e:
        print(f"Failed to list routes: {e}")

def assign_route_to_truck(subargs):
    if len(subargs) < 2:
        print("Usage: route assign <route_id> <truck_id>")
        return

    route_id = int(subargs[0])
    truck_id = int(subargs[1])

    try:
        route_service.assign_route_to_truck(route_id=route_id, truck_id=truck_id)
        print(f"Successfully assigned route {route_id} to truck {truck_id}")
    except Exception as e:
        print(f"Failed to assign route {route_id} to truck {truck_id}: {e}")
