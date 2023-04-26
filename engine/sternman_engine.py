from abc import ABC
import Engine


class SternmanEngine(Engine, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        self.name = "SternmanEngine"
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
