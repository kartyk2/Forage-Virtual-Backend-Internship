from abc import ABC, abstractmethod
from tire.abs_Tire import Tire

class CarriganTire(Tire):
    
    def __init__(self):
        self.name = "Carrigan"
    
    
    def need_service(self, sensor_report):
        for tire_damage in sensor_report:
            return True if tire_damage >= 0.9 else False
