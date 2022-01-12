"""Sun interface for astronomical.

This module provides sunrise and sunset times.
"""

from datetime import date, datetime
from typing import Tuple
from suntime import (  # type: ignore
    Sun as Sun_Import,
    SunTimeException
)
from .location import Location


home = Location("Ivybridge", -3.9413, 50.3921)


class Sun:
    """Interface class for the Sun."""

    def __init__(self) -> None:
        """Initialise variables."""
        self.rise, self.set = self.__sun_times(home)

    def __sun_times(self,
                    location: Location,
                    day: date = date.today()) -> Tuple[datetime, datetime]:
        """Return sunrise and sunset times.

        This function should be retired in favour of one part of the Sun
        class. That class should calculate this from first principles instead
        of pulling from an API.
        """
        sun = Sun_Import(location.latitude, location.longitude)
        sunrise = sun.get_sunrise_time(day)
        sunset = sun.get_sunset_time(day)
        return sunrise, sunset


def sun_times(location: Location,
              day: date = date.today()) -> Tuple[datetime, datetime]:
    """Return sunrise and sunset times.

    This function should be retired in favour of one part of the Sun
    class. That class should calculate this from first principles instead
    of pulling from an API.
    """
    sun = Sun_Import(location.latitude, location.longitude)
    sunrise = sun.get_sunrise_time(day)
    sunset = sun.get_sunset_time(day)
    return sunrise, sunset
