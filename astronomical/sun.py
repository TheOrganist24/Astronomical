"""Utilities related to the sun."""

from datetime import date, datetime
from typing import Tuple
from suntime import Sun, SunTimeException  # type: ignore
from . import location


def sun_times(location: location.Location,
              day: date = date.today()) -> Tuple[datetime, datetime]:
    """Return sunrise and sunset times."""
    sun = Sun(location.latitude, location.longitude)
    sunrise = sun.get_sunrise_time(day)
    sunset = sun.get_sunset_time(day)
    return sunrise, sunset
