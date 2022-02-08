import unittest
from os.path import expanduser

from astronomical.interface.configuration import UserDefaults


class TestUserDefaultsClass(unittest.TestCase):
    def test_external_default_location_is_users_home_dir(self):
        """R BICEP: Right"""
        test_user_defaults_path = f"{expanduser('~')}/.astronomical"

        user_defaults = UserDefaults()

        assert user_defaults.path == test_user_defaults_path

    def test_defaults_are_loaded(self):
        """R BICEP: Right"""
        test_config_location: str = "/home/nicholas/astronomical/tests/data/config.ini"
        test_location: str = "London"
        test_longitude: float = 0.1276
        test_latitude: float = 51.5072
        test_planet_name: str = "Earth"

        defaults = UserDefaults(test_config_location)

        assert defaults.location == test_location \
            and defaults.longitude == test_longitude \
            and defaults.latitude == test_latitude \
            and defaults.locale.planet.name == test_planet_name

