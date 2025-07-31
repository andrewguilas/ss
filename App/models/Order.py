from datetime import datetime

class Order:
    def __init__(self, data):
        self.order_id = data['OrderID'].strip()
        self.campus = data['CampusName'].strip()
        self.name = data['FullName'].strip()
        self.phone = self._clean_phone(data['StudentPhone'])
        self.pickup_date = self._parse_date(data['PickupDate'])
        self.pickup_location = data['PickupLocation'].strip()
        self.dropoff_date = self._parse_date(data['DropoffDate'])
        self.dropoff_location = data['DropoffLocation'].strip()
        self.item_count = self._parse_int(data['ItemCount'])

    def _clean_phone(self, phone):
        return ''.join(c for c in phone if c.isdigit())
    
    def _parse_date(self, date_str):
        try:
            return datetime.strptime(date_str.strip(), "%Y-%m-%d").date
        except (ValueError, AttributeError):
            return None
        
    def _parse_int(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            return 0
        
    def __repr__(self):
        return f"Order {self.order_id} - {self.name}, {self.item_count} item(s)"
