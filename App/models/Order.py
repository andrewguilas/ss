from datetime import datetime
from services.openai_service import ask_openai

class Order:
    def __init__(self, data):
        self.order_id = data["OrderID"].strip()
        self._primary_key = self.order_id
        self.campus = data["CampusName"].strip()
        self.name = data["FullName"].strip()
        self._pronunciation = None
        self.phone = self._clean_phone(data["StudentPhone"])

        self.pickup_date = self._parse_date(data["PickupDate"])
        self.pickup_location = " ".join([
            data["PickupLocation"].strip(), 
            data["PickupDormRoomNumber"].strip(), 
            data["PickupDormRoomLetter"].strip(), 
            data["PickupAddress"].strip(), 
            data["PickupAddressLine2"].strip(), 
        ])
        self.pickup_proxy_name = data["PickupPersonName"].strip(), 
        self.pickup_proxy_phone = data["PickupPersonPhone"].strip()

        self.dropoff_date = self._parse_date(data["DropoffDate"])
        self.dropoff_location = " ".join([
            data["DropoffLocation"].strip(), 
            data["DropoffDormRoomNumber"].strip(), 
            data["DropoffDormRoomLetter"].strip(), 
            data["DropoffAddressLine1"].strip(), 
            data["DropoffAddressLine2"].strip(), 
        ])
        self.dropoff_proxy_name = data["DropoffPersonName"].strip(), 
        self.dropoff_proxy_phone = data["DropoffPersonPhone"].strip()
        self.item_count = self._parse_int(data["ItemCount"])
        self.items = []

    def _clean_phone(self, phone):
        return "".join(c for c in phone if c.isdigit())
    
    def _parse_date(self, date_str):
        try:
            return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
        except (ValueError, AttributeError):
            return None
        
    def _parse_int(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return 0
        
    def __repr__(self):
        return f"Order {self.order_id} - {self.name}, {self.item_count} item(s)"

    def get_comments(self, is_pickup=False, is_dropoff=False):
        comments = []
        if is_pickup and self.pickup_proxy_name and self.pickup_proxy_phone:
            comments.append(f"Call Proxy {self.pickup_proxy_name[0]} {self.pickup_proxy_phone}")
        if is_dropoff and self.dropoff_proxy_name and self.dropoff_proxy_phone:
            comments.append(f"Call Proxy {self.dropoff_proxy_name[0]} {self.dropoff_proxy_phone}")
        return comments

    def get_pronunciation(self):
        if not self._pronunciation:
            first_name = self.name.split(" ")[0]
            self._pronunciation = ask_openai(f"In one word, no fluff, give me the pronunciation of the first name {first_name}")
        
        return self._pronunciation
