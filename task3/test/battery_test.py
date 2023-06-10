from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

import unittest
import datetime


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2023,6,10)
        last_service_date = datetime.datetime(2016,11,22)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2023,6,10)
        last_service_date = datetime.datetime(2022,2,11)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
        

class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = datetime.datetime(2023,6,10)
        last_service_date = datetime.datetime(2016,11,22)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = datetime.datetime(2023,6,10)
        last_service_date = datetime.datetime(2022,2,11)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())