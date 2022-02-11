import unittest
from datetime import timedelta, time
from os.path import expanduser

from astronomical.interface.configuration import UserDefaults
from astronomical.model.configuration import earth, SleepRequirements


class TestUserDefaultsClass(unittest.TestCase):
    def test_external_default_location_is_users_home_dir(self):
        """R BICEP: Right"""
        test_user_defaults_path = f"{expanduser('~')}/.astronomical"

        user_defaults = UserDefaults()

        assert user_defaults.path == test_user_defaults_path

    def test_defaults_are_loaded(self):
        """R BICEP: Right"""
        test_config_location: str = "/home/nicholas/astronomical/tests/data/config.ini"
        test_config = {"name": "London", "longitude": 0.1276, "latitude": 51.5072, "planet": earth,
                       "sleep_duration": timedelta(hours=8), "latest_wake_up": time(hour=7),
                       "earliest_wake_up": time(hour=6), "ablutions": timedelta(hours=1)}

        defaults = UserDefaults(test_config_location)

        assert defaults.config == test_config

