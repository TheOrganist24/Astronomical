"""Utilities related to the sun; including sunrise and sunset times."""

from datetime import date, datetime
from typing import Tuple
from suntime import Sun, SunTimeException  # type: ignore
from . import location


def sun_times(location: location.Location,
              day: date = date.today()) -> Tuple[datetime, datetime]:
    """Return sunrise and sunset times.

    This function should be retired in favour of one part of the Sun class.
    That class should calculate this from first principles instead of pulling
    from an API.
    """
    sun = Sun(location.latitude, location.longitude)
    sunrise = sun.get_sunrise_time(day)
    sunset = sun.get_sunset_time(day)
    return sunrise, sunset
