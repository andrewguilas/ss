from sqlalchemy import Column, String, Integer, Date, Text
from app.database import Base
from app.services.openai_service import ask_openai
from app.utils.date_utils import parse_date
import app.config as config

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(String, primary_key=True, index=True)
    campus = Column(String(100))
    name = Column(String(200))
    phone = Column(String(20))
    pronunciation = Column(String(200))
    comments = Column(String(512))

    pickup_date = Column(Date)
    pickup_location = Column(Text)
    pickup_proxy_name = Column(String(200))
    pickup_proxy_phone = Column(String(20))

    dropoff_date = Column(Date)
    dropoff_location = Column(Text)
    dropoff_proxy_name = Column(String(200))
    dropoff_proxy_phone = Column(String(20))

    item_count = Column(Integer)
    items = Column(Text, default="[]") # store items as JSON text
    truck_number = Column(String(1))
    driver = Column(String(200))

    def __init__(self, data):
        self.order_id = data["OrderID"].strip()
        self.campus = data["CampusName"].strip()
        self.name = data["FullName"].strip()
        self.phone = self._clean_phone(data["StudentPhone"])
        self.pronunciation = self._fetch_pronunciation()
        self.comments = ". ".join(self._get_comments())

        self.pickup_date = parse_date(data["PickupDate"])
        self.pickup_location = " ".join([
            data["PickupLocation"].strip(), 
            data["PickupDormRoomNumber"].strip(), 
            data["PickupDormRoomLetter"].strip(), 
            data["PickupAddress"].strip(), 
            data["PickupAddressLine2"].strip()
        ])
        self.pickup_proxy_name = data["PickupPersonName"].strip()
        self.pickup_proxy_phone = data["PickupPersonPhone"].strip()

        self.dropoff_date = parse_date(data["DropoffDate"])
        self.dropoff_location = " ".join([
            data["DropoffLocation"].strip(), 
            data["DropoffDormRoomNumber"].strip(), 
            data["DropoffDormRoomLetter"].strip(), 
            data["DropoffAddressLine1"].strip(), 
            data["DropoffAddressLine2"].strip()
        ])
        self.dropoff_proxy_name = data["DropoffPersonName"].strip() 
        self.dropoff_proxy_phone = data["DropoffPersonPhone"].strip()

        self.item_count = self._parse_int(data["ItemCount"])
        self.items = "[]"  # Initialize empty JSON list string
        self.truck_number = 1
        self.driver = "Driver TBD"

    def _clean_phone(self, phone):
        return "".join(c for c in phone if c.isdigit())
        
    def _parse_int(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return 0

    def __repr__(self):
        return f"Order {self.order_id} - {self.name}, {self.item_count} item(s)"

    def _fetch_pronunciation(self):
        first_name = self.name.split(" ")[0]
        try:
            return ask_openai(f"In one word, no fluff, give me the pronunciation of the first name {first_name}")
        except Exception:
            return

    def _get_comments(self):
        comments = []
        if not config.IS_DROPOFF_SEASON and self.pickup_proxy_name and self.pickup_proxy_phone:
            comments.append(f"Call Proxy {self.pickup_proxy_name} {self.pickup_proxy_phone}")
        if config.IS_DROPOFF_SEASON and self.dropoff_proxy_name and self.dropoff_proxy_phone:
            comments.append(f"Call Proxy {self.dropoff_proxy_name} {self.dropoff_proxy_phone}")
        return comments

    def set_truck(self, truck_number, driver):
        self.truck_number = truck_number
        self.driver = driver

