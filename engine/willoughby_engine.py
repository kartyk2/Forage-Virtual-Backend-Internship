import sys
sys.path.append("e:\desktop\ForageApp")
from engine.abs_Engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.name = "WilloughbyEngine"
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
 