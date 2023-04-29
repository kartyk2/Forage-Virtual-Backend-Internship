# import sys 
# sys.path.append("E:\desktop\ForageApp")
# for path in sys.path:
#     print(path)

from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from car import Car

class CarFactory():

    """
    Interface to make sure all Car Engine have a needs_service interface
    """
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine()
        battery = SpindlerBattery()

        return Car(engine, battery)
    
    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine()
        battery = SpindlerBattery()

        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool):
        engine = SternmanEngine()
        battery = SpindlerBattery()

        return Car(engine, battery)
    
    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine()
        battery = NubbinBattery()

        return Car(engine, battery)
    
    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine()
        battery = NubbinBattery()

        return Car(engine, battery)