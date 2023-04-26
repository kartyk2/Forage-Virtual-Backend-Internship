from datetime import timedelta
from abc import ABC
import Battery

class SpindlerBattery(Battery, ABC):
    def __init__(self, last_service_date, current_date):
        self.name = "SpindlerBattery"
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.current_date - self.last_service_date > timedelta(days=365*2)
    
