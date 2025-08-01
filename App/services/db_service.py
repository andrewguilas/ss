from sqlalchemy.exc import SQLAlchemyError
from app.database import SessionLocal, engine
from app.models.order import Order

def get_session():
    return SessionLocal()

def close_session(session):
    """Close DB session."""
    session.close()

def add_or_update_order(order_obj):
    """Insert or update an Order in DB."""
    session = get_session()
    try:
        session.merge(order_obj)  # merge handles insert or update by PK
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    finally:
        close_session(session)

def get_all_orders():
    """Fetch all Order records from DB."""
    session = get_session()
    try:
        orders = session.query(Order).all()
        return orders
    finally:
        close_session(session)

def filter_orders(campus=None, min_item_count=None, dropoff_date=None):
    """Query Orders with optional filters."""
    session = get_session()
    try:
        query = session.query(Order)
        if campus is not None:
            query = query.filter(Order.campus == campus)
        if min_item_count is not None:
            query = query.filter(Order.item_count >= min_item_count)
        if dropoff_date is not None:
            query = query.filter(Order.dropoff_date == dropoff_date)
        return query.all()
    finally:
        close_session(session)

def delete_order(order_obj):
    """Delete an Order from DB."""
    session = get_session()
    try:
        session.delete(order_obj)
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        close_session(session)

"""
def group_orders_by_dropoff_date(orders):
    dropoff_dates = defaultdict(list)
    for order in orders:
        dropoff_dates[order.dropoff_date].append(order)
    # lambda sorts by tuple (False, False)
    return sorted(dropoff_dates, key=lambda d: (d is None, d))
"""
