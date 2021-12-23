"""Utilities related to the sun."""

from datetime import date
from suntime import Sun, SunTimeException  # type: ignore


def sun_times(location, day=date.today()):
    """Return sunrise and sunset times."""
    sun = Sun(location.latitude, location.longitude)
    sunrise = sun.get_sunrise_time(day)
    sunset = sun.get_sunset_time(day)
    return sunrise, sunset
