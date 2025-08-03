from app.models.order import Order
from app.models.route import Route
import app.services.infra.db as db_service 
import app.config as config

def assign_order_to_route(order_id, route_id):
    session = db_service.get_session()
    try:
        order = session.query(Order).filter(Order.order_id == order_id).first()
        if not order:
            raise ValueError(f"Order {order_id} not found")

        route = session.query(Route).filter(Route.route_id == route_id).first()
        if not route:
            raise ValueError(f"Route {route_id} not found")

        if order.route == route:
            raise ValueError(f"Order {order_id} is already assigned to {route_id}")

        order.route = route
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def list_orders(date=None):
    session = db_service.get_session()
    try:
        query = session.query(Order)
        if date:
            if config.IS_DROPOFF_SEASON:
                query = query.filter(Order.dropoff_date == date)
            else:
                query = query.filter(Order.pickup_date == date)
        return query.order_by(Order.order_id).all()
    finally:
        session.close()

def get_order_details(order_id):
    session = db_service.get_session()
    try:
        return session.query(Order).filter(Order.order_id == order_id).first()
    finally:
        session.close() 
