from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.database import Base

class Truck(Base):
    __tablename__ = 'trucks'

    truck_id = Column(Integer, primary_key=True)
    model = Column(String(64), nullable=True)  # Ex: "U-Haul 15'"
    comments = Column(String) # Store serialized list as string

    # To prevent circular imports, don't import Order
    # String will resolve after all models are loaded
    routes = relationship("Route", back_populates="truck")

    def __init__(self, model="", comments=""):
        self.model = model and model.strip() or None
        self.comments = model and comments.strip() or None

    def __repr__(self):
        return f"Truck {self.truck_id} - {self.model}, {len(self.routes)} route(s)"
