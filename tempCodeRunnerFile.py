
import servicable

class Car(servicable):
    def __init__(self, engine, battery):
        """
        type engine = Engine
        type battery = Battery
        """
        self.engine = engine
        self.battery = battery


    def needs_service(self):
        """
        rtype = bool
        """
        
        defective_parts = []

        battery_status = self.battery.needs_servicing()
        engine_status  = self.engine.needs_servicing()

        if not battery_status:
            defective_parts.append(self.battery.name)
        
        if not engine_status:
            defective_parts.append(self.engine.name)
        
        return defective_parts if (battery_status or engine_status) else False
 