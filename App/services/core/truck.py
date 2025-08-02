from app.models.truck import Truck
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
