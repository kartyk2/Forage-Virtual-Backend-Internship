from datetime import datetime
from engine import capulet_engine, sternman_engine, willoughby_engine
from battery import NubbinBattery, SpindlerBattery
from car import Car

class CarFactory():

    """
    Interface to make sure all Car Engine have a needs_service interface
    """
    @staticmethod
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = capulet_engine()
        battery = SpindlerBattery()

        return Car(engine, battery)
    
    @staticmethod
    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = willoughby_engine()
        battery = SpindlerBattery()

        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on: bool):
        engine = sternman_engine()
        battery = SpindlerBattery()

        return Car(engine, battery)
    
    @staticmethod
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = willoughby_engine()
        battery = NubbinBattery()

        return Car(engine, battery)
    
    @staticmethod
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage: int, last_service_mileage: int):
        engine = capulet_engine()
        battery = NubbinBattery()

        return Car(engine, battery)