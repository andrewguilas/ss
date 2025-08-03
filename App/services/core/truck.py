from app.models.truck import Truck
import app.services.infra.db as db_service
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload

def add_truck(model="", comments="", session=None):
    is_own_session = session is None
    if is_own_session:
        session = db_service.get_session()

    new_truck = Truck(model, comments)

    try:
        session.add(new_truck)
        if is_own_session: # only close session if this method created it
            session.commit()
            session.refresh(new_truck)
        else:
            session.flush()
        return new_truck
    except SQLAlchemyError:
        if is_own_session:
            session.rollback()
        raise
    finally:
        if is_own_session:
            session.close()

def remove_truck(truck_id):
    session = db_service.get_session()
    try:
        truck = session.query(Truck).filter(Truck.truck_id == truck_id).first()
        if not truck:
            raise ValueError(f"Truck {truck_id} not found")

        session.delete(truck)
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def list_trucks():
    session = db_service.get_session()
    try:
        return session.query(Truck).options(joinedload(Truck.routes)).order_by(Truck.truck_id).all()
    finally:
        session.close()
