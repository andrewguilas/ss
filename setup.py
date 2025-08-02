from app.database import Base, engine
from sqlalchemy import event

# Import all models here
from app.models.truck import Truck
from app.models.route import Route
from app.models.order import Order

@event.listens_for(engine, "connect")
def enable_sqlite_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
