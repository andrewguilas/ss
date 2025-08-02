from app.models.truck import Truck
from app.models.route import Route
import app.services.infra.db as db_service
from sqlalchemy.exc import SQLAlchemyError

def add_truck(model="", comments=""):
    new_truck = Truck(model, comments)

    session = db_service.get_session()
    try:
        session.add(new_truck)
        session.commit()
        session.refresh(new_truck)  # Ensure truck_id is populated
        return new_truck
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()

def remove_truck(truck_id):
    session = db_service.get_session()
    try:
        truck = session.query(Truck).filter(Truck.truck_id == truck_id).first()
        if not truck:
            raise ValueError(f"Truck with ID {truck_id} not found")

        session.delete(truck)
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
