class Order:
    def __init__(self, dict):
        self.order_id = dict['OrderID']
        self.campus = dict['CampusName']
        self.name = dict['FullName']
        self.phone = dict['StudentPhone']
        self.pickup_date = dict['PickupDate']
        self.pickup_location = dict['PickupLocation']
        self.dropoff_date = dict['DropoffDate']
        self.dropoff_location = dict['DropoffLocation']
        self.item_count = dict['ItemCount']
