from servicable import Servicable

class Car(Servicable):
    def __init__(self, engine, battery, tire):
        """
        type engine = Engine
        type battery = Battery
        """
        self.engine = engine
        self.battery = battery
        #self.tire = tire



    def needs_service(self):
        """
        rtype = bool
        """
        
        defective_parts = []

        battery_status = self.battery.needs_service()
        engine_status  = self.engine.needs_service()
        # tire_status = self.tire.needs_service()


        if not battery_status:
            defective_parts.append(self.battery.name)
        
        if not engine_status:
            defective_parts.append(self.engine.name)

        # if not tire_status:
        #     defective_parts.append(self.tire.name)
        
        return defective_parts if (battery_status or engine_status) else False
 