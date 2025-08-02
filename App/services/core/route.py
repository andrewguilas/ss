from app.models.route import Route
from app.models.route import Truck
import app.services.infra.db as db_service
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

def add_route(date, driver_name=None, comments=None, truck_id=None):
    session = db_service.get_session()

    truck = None
    if truck_id:
        truck = session.query(Truck).filter(Truck.truck_id == truck_id).first()
        if truck is None:
            raise ValueError(f"Truck with ID {truck_id} not found.")

    new_route = Route(date=date, driver_name=driver_name, comments=comments, truck=truck)

    try:
        session.add(new_route)
        session.commit()
        session.refresh(new_route)  # Ensure route_id is populated
        return new_route
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
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
