import unittest
from datetime import datetime, timedelta

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


# Test for all kinds of engines

class testEngineCapulet(unittest.TestCase):

    def test_capulet_engine(self):
        self.engine = CapuletEngine(30001, 0)
        self.assertEqual(self.engine.needs_service(), True)


class testEngineSternman(unittest.TestCase):
    
    def test_capulet_engine(self):
        self.engine = SternmanEngine(True)
        self.assertEqual(self.engine.needs_service(), True)


class testEngineWilloughby(unittest.TestCase):
    
    def test_capulet_engine(self):
        self.engine = WilloughbyEngine(60005, 0)
        self.assertEqual(self.engine.needs_service(), True)

# Tests for all kinds of batteries

class testBatteryNubbin(unittest.TestCase):

    def test_nubbin_battery(self):
        self.battery = NubbinBattery(datetime.fromisoformat("2019-05-01"), datetime.today())
        self.assertEqual(self.battery.needs_service(), True) 

class testBatterySpindler(unittest.TestCase):

    def test_spindler_battery(self):
        self.battery = SpindlerBattery(datetime.fromisoformat("2021-04-30"), datetime.today())
        self.assertEqual(self.battery.needs_service(), False) 


if __name__ == "__main__":
    unittest.main()