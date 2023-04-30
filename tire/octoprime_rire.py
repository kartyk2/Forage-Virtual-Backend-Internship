from tire.abs_Tire import Tire

class OctoprimeTime(Tire):
    
    def __init__(self):
        self.name = "Octaprime"
    
    def need_service(self, sensor_report):
        total_damage = 0
        for tire_damage in sensor_report:
            total_damage += tire_damage
        
        return True if tire_damage >= 3 else False
    