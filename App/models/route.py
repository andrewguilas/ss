from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint, Date
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.truck import Truck

class Route(Base):
    __tablename__ = 'routes'

    route_id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    driver_name = Column(String(200), nullable=True)
    comments = Column(String) # Store serialized list as string

    truck_id = Column(Integer, ForeignKey("trucks.truck_id", ondelete="SET NULL"), nullable=True)
    truck = relationship(Truck, back_populates="routes")

    # To prevent circular imports, don't import Order
    # String will resolve after all models are loaded
    orders = relationship("Order", back_populates="route") 

    __table_args__ = (
        UniqueConstraint('truck_id', 'date', name='uq_truck_date'),
    )

    def __init__(self, date, driver_name="", comments="", truck=None):
        self.date = date
        self.driver_name = driver_name.strip() if driver_name else ""
        self.comments = comments.strip() if comments else ""
        self.truck = truck

    def __repr__(self):
        truck_model = self.truck.model if self.truck else "Truck TBD"
        driver_name = self.driver_name or "Driver TBD"
        return f"Route {self.route_id} - {self.date}, {truck_model}, {driver_name}, {len(self.orders)} order(s)"
