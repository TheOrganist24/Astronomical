from datetime import datetime
from astronomical import __version__
from astronomical.location import Location
from astronomical import sun

def test_version():
    assert __version__ == '0.1.0'

class TestLocationClass:
    def test_name_is_string(self):
        location = Location("Ivybridge", -3.941355, 50.392189)
        assert isinstance(location.name, str)

    def test_location_is_tuple(self):
        location = Location("Ivybridge", -3.941355, 50.392189)
        assert isinstance(location.location, tuple)

    def test_location_tuple_are_floats(self):
        location = Location("Ivybridge", -3.941355, 50.392189)
        assert isinstance(location.location[0], float) \
            and isinstance(location.location[1], float)

class TestSunModule:
    def test_sun_times_are_times(self):
        sunset, sunrise = sun.sun_times(-3.941355, 50.392189)
        assert isinstance(sunset, datetime) \
            and isinstance(sunrise, datetime)
    
