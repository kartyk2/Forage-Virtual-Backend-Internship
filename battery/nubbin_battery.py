import sys
sys.path.append("e:\desktop\ForageApp")
from datetime import timedelta
from battery.abs_Battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.name = "NubbinBattery"
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_date - self.last_service_date > timedelta(days=365*4)
    
