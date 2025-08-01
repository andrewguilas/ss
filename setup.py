from app.database import Base, engine
from app.models.order import Order  # import all models so metadata is complete

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
