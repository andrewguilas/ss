from app.models.route import Route
from app.models.route import Truck
import app.services.infra.db as db_service
from sqlalchemy.exc import SQLAlchemyError

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

from sqlalchemy.orm import joinedload

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
