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


class SunTimes:
    """Interface class for the Sun."""

    def __init__(self, location: Location) -> None:
        """Initialise variables."""
        self.rise, self.set = self.__sun_times()
        self.location = location

    def __sun_times(self,
                    day: date = date.today()) -> Tuple[datetime, datetime]:
        """Return sunrise and sunset times.

        This function should be retired in favour of one part of the Sun
        class. That class should calculate this from first principles instead
        of pulling from an API.
        """
        sun = Sun_Import(self.location.latitude, self.location.longitude)
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
