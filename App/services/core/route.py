from app.models.route import Route
from app.models.route import Truck
import app.services.infra.db as db_service
import app.services.core.truck as truck_service
from app.utils.debug_utils import print_message
from sqlalchemy.orm import joinedload
from enum import Enum

class Status(Enum):
    ASSIGNED = "assigned"
    ASSIGNED_AND_GENERATED = "assigned_and_generated"

def add_route(date, driver_name=None, comments=None, truck_id=None, session=None):
    trucks_created_count = 0

    is_own_session = session is None
    if is_own_session:
        session = db_service.get_session()

    try:
        status = None

        truck = None
        if truck_id:
            truck = session.query(Truck).filter(Truck.truck_id == truck_id).first()
            if truck is None:
                raise ValueError(f"Truck with ID {truck_id} not found.")
        else:
            # If no truck_id, assign first truck or create a default one
            truck = session.query(Truck).first()
            if truck:
                status = Status.ASSIGNED
            else:
                truck = truck_service.add_truck(model="Model TBD", comments="Automatically generated to initialize a route", session=session)
                status = Status.ASSIGNED_AND_GENERATED

        new_route = Route(date=date, driver_name=driver_name, comments=comments or "", truck=truck)
        session.add(new_route)
        session.flush()

        if status == Status.ASSIGNED:
            print_message(f"Automatically assigned truck {truck.truck_id} to route {new_route.route_id}")
        elif status == Status.ASSIGNED_AND_GENERATED:
            print_message(f"Automatically generated truck {truck.truck_id} for route {new_route.route_id}")
            trucks_created_count += 1

        if is_own_session:
            session.commit()
    
        return new_route, trucks_created_count
    except Exception:
        if is_own_session:
            session.rollback()
        raise
    finally:
        if is_own_session:
            session.close()

def remove_route(route_id):
    session = db_service.get_session()
    try:
        route = session.query(Route).filter(Route.route_id == route_id).first()
        if not route:
            raise ValueError(f"Route {route_id} not found")

        session.delete(route)
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def list_routes(date=None):
    session = db_service.get_session()
    try:
        query = session.query(Route).options(
            # lazy-loading by default
            # when you query Route, only Route columns are loaded, not Route.truck or Route.orders
            # fix by eagerly loading relationships while session is still open
            joinedload(Route.truck),   
            joinedload(Route.orders)
        )
        if date:
            query = query.filter(Route.date == date)
        return query.order_by(Route.route_id).all()
    finally:
        session.close()

def assign_route_to_truck(route_id, truck_id):
    session = db_service.get_session()
    try:
        route = session.query(Route).filter(Route.route_id == route_id).first()
        if not route:
            raise ValueError(f"Route {route_id} not found")

        truck = session.query(Truck).filter(Truck.truck_id == truck_id).first()
        if not truck:
            raise ValueError(f"Truck {truck_id} not found")

        existing_route = session.query(Route).filter(
            Route.truck_id == truck_id,
            Route.date == route.date,
            Route.route_id != route_id  # exclude current route
        ).first()
        if existing_route:
            raise ValueError(f"Truck {truck_id} is already assigned to route {existing_route.route_id} on {route.date}")

        if route.truck == truck:
            raise ValueError(f"Route {route_id} is already assigned to {truck_id}")

        route.truck = truck
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
