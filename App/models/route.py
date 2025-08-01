from sqlalchemy import Column, String, Integer, ForeignKey, UniqueConstraint, Date, JSON
from sqlalchemy.orm import relationship
from app.database import Base

class Route(Base):
    __tablename__ = 'routes'

    route_id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    driver_name = Column(String(200), nullable=True)
    comments = Column(JSON, default=list)

    truck_id = Column(Integer, ForeignKey("trucks.truck_id", ondelete="SET NULL"), nullable=True)
    truck = relationship("Truck", back_populates="routes")

    orders = relationship("Order", back_populates="route")

    __table_args__ = (
        UniqueConstraint('truck_id', 'date', name='uq_truck_date'),
    )

    def __init__(self, driver_name="", comments="", truck=None):
        self.driver_name = driver_name.strip()
        self.comments = comments.strip()
        self.truck = truck

    def __repr__(self):
        truck_model = self.truck.model if self.truck else "Truck TBD"
        driver_name = self.driver_name or "Driver TBD"
        return f"Route {self.route_id} - {truck_model}, {driver_name}, {len(self.orders)} order(s)"
