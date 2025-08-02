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
        new_route = route_service.add_route(date=date, driver_name=driver_name, comments=comments, truck_id=truck_id)
        print(f"Successfully added route {new_route.route_id} for {date} with driver {driver_name or 'N/A'} for truck {truck_id or 'N/A'}")
    except Exception as e:
        print(f"Failed to add route for {date} with driver {driver_name or 'N/A'} for truck {truck_id or 'N/A'}: {e}")

def remove_route(subargs):
    # route_id
    pass

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
    # route_idm, truck_id
    pass
