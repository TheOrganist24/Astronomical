"""Utilities related to the sun."""

from suntime import Sun, SunTimeException  # type: ignore


def sun_times(location, day):
    """Return sunrise and sunset times."""
    sun = Sun(location.latitude, location.longitude)
    sunrise = sun.get_sunrise_time()
    sunset = sun.get_sunset_time()
    return sunrise, sunset
