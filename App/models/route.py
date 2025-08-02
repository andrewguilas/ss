from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Route(Base):
    __tablename__ = 'routes'

    route_id = Column(Integer, primary_key=True)
    driver_name = Column(String(200), nullable=True)
    comments = Column(String(512), nullable=True)

    truck = relationship("Truck", back_populates="routes")
    truck_id = Column(Integer, ForeignKey("trucks.truck_id", ondelete="SET NULL"), nullable=True)

    orders = relationship("Order", back_populates="route")

    def __init__(self, driver_name="", comments="", truck=None):
        self.driver_name = driver_name.strip()
        self.comments = comments.strip()
        self.truck = truck

    def __repr__(self):
        return f"Route {self.route_id} - {self.truck}, {self.driver_name}, {len(self.orders)} order(s)"
