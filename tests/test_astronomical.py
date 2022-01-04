from datetime import datetime, timedelta, date
from astronomical import __version__
from astronomical.location import Location
from astronomical import sun
from astronomical.sleep import Requirements, alarms

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
        location = Location("Ivybridge", -3.941355, 50.392189)
        sunrise, sunset = sun.sun_times(location)
        assert isinstance(sunset, datetime) \
            and isinstance(sunrise, datetime)

    def test_sunset_is_after_sunrise(self):
        location = Location("Ivybridge", -3.941355, 50.392189)
        sunrise, sunset = sun.sun_times(location)
        assert sunset > sunrise


class TestSleepModule:
    def test_sleep_requirement_defaults(self):
        requirements = Requirements()
        assert requirements.min_duration == timedelta(hours=8) \
            and requirements.seasonal_variance == timedelta(hours=1) \
            and requirements.max_rise == None \
            and requirements.min_rise == None
    
    def test_sleep_duration_is_within_tolerance(self):
        location = Location("Ivybridge", -3.941355, 50.392189)
        sleep_duration = timedelta(hours=8)
        variance = timedelta(hours=1)
        requirements = Requirements(min_duration=sleep_duration, seasonal_variance=variance)
        max_duration = sleep_duration + variance
        min_duration = sleep_duration
        for day in range(365):
            specific_date = date.today() + timedelta(days=day)
            assert min_duration <= requirements.duration(specific_date) <= max_duration
        
    def test_sleep_alarms_are_overnight(self):
        location = Location("Ivybridge", -3.941355, 50.392189)
        requirements = Requirements()
        night = date.today()
        go_to_bed, get_up = alarms(location, requirements, night)
        assert go_to_bed.date() == date.today() \
            and get_up.date() == (date.today() + timedelta(days=1))
