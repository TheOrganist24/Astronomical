import unittest
from datetime import datetime

from astronomical.model.configuration import Defaults


class TestConfigurationDefaultsClass(unittest.TestCase):
    def test_unset_class_returns_sensible_defaults(self):
        """RBICEP: Right"""
        test_location = "London"
        test_longitude = 0.1276
        test_latitude = 51.5072
        test_planet_name = "earth"
        test_state_time = datetime.now()

        defaults = Defaults()

        assert defaults.location == test_location \
            and defaults.longitude == test_longitude \
            and defaults.latitude == test_latitude \
            and defaults.planet.name == test_planet_name \
            and defaults.state.instant == test_state_time