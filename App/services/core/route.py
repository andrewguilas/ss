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
