import os
import shutil
from app.services.infra.db import Base, engine
from sqlalchemy import event
import app.config as config

# Import models to initialize
from app.models.truck import Truck
from app.models.route import Route
from app.models.order import Order

@event.listens_for(engine, "connect")
def enable_sqlite_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON;")
    cursor.close()

def delete_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted file: {path}")

def delete_pycache_folders(root_path):
    for dirpath, dirnames, _ in os.walk(root_path):
        if "__pycache__" in dirnames:
            pycache_path = os.path.join(dirpath, "__pycache__")
            shutil.rmtree(pycache_path)
            print(f"Deleted {pycache_path}")

def init_db():
    print("Starting setup...")
    delete_file_if_exists(config.DB_FILE_NAME)
    delete_pycache_folders("app/")
    Base.metadata.create_all(bind=engine)
    print("Database initialized")
    print("Successfully completed setup")

if __name__ == "__main__":
    init_db()
