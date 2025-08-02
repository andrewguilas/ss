import app.services.core.truck as truck_service

def add_truck(subargs):
    model = subargs[0] if len(subargs) >= 1 else None
    comments = subargs[1] if len(subargs) >= 2 else ""

    try:
        new_truck = truck_service.add_truck(model=model, comments=comments)
        print(f"Successfully added truck {new_truck.truck_id} of model '{new_truck.model or 'N/A'}'")
    except Exception as e:
        print(f"Failed to add truck: {e}")

def remove_truck(subargs):
    if len(subargs) == 0:
        print("Usage: truck remove <truck_id>")
        return

    truck_id = subargs[0]

    try:
        truck_service.remove_truck(truck_id=truck_id)
        print(f"Successfully removed truck {truck_id}")
    except Exception as e:
        print(f"Failed to remove truck {truck_id}: {e}")

def list_trucks():
    pass
