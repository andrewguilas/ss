from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Truck(Base):
    __tablename__ = 'trucks'

    truck_id = Column(Integer, primary_key=True)
    model = Column(String(64), nullable=True)  # Ex: "U-Haul 15'"
    comments = Column(Text, nullable=True)

    routes = relationship("Route", back_populates="truck")

    def __init__(self, model="", comments=""):
        self.model = model.strip()
        self.comments = comments.strip()

    def __repr__(self):
        return f"Truck {self.truck_id} - {self.model}, {len(self.routes)} route(s)"
