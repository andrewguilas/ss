import app.services.core.truck as truck_service

def add_truck(subargs):
    model = subargs[0] if len(subargs) >= 1 else None
    comments = subargs[1] if len(subargs) >= 2 else ""

    try:
        new_truck = truck_service.add_truck(model=model, comments=comments)
        print(f"Successfully added truck {new_truck.truck_id} of model '{new_truck.model or 'N/A'}'")
    except Exception as e:
        print(f"Failed to add truck: {e}")

def remove_truck(truck_id):
    pass

def assign_truck_to_route(truck_id, route_id):
    pass

def list_trucks():
    pass
