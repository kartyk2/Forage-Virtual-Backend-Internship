import sys
sys.path.append("e:\desktop\ForageApp")
from engine.abs_Engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        self.name = "SternmanEngine"
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
