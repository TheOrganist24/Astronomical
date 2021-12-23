"""Utilities related to the sun."""

from suntime import Sun, SunTimeException  # type: ignore


def sun_times(longitude, latitude):
    """Return sunrise and sunset times."""
    sun = Sun(latitude, longitude)
    sunrise = sun.get_sunrise_time()
    sunset = sun.get_sunset_time()
    return sunrise, sunset
