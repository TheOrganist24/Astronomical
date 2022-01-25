"""Command line interfaces for astronomical."""

from datetime import date, datetime
from typing import Tuple

from suntime import Sun as Sun_Import  # type: ignore
from suntime import SunTimeException

from ..model.custom_types import angle
from ..model.location import Location
from ..services.solar_system import earth
from ..utils.configuration import Defaults
from ..utils.logging import logger

d = u"\N{DEGREE SIGN}"


class Sun:
    """Return sunrise/set times, elevation/azimuth, and distance."""

    def __init__(self) -> None:
        """Initialise variables."""
        logger.info(f"INTERFACE: \"{self.__class__.__name__}\" "
                    f"instantiating.")
        locale = Defaults()
        self.location = locale.location()
        self.rise, self.set = self._sun_times()
        self.ra, self.dec = self._equatorial_cooridnates()
        self.az, self.alt = self._elevation()

    def __str__(self) -> str:
        """Generate summary of class."""
        sunrise = self.rise.strftime("%I:%M%p")
        sunset = self.set.strftime("%I:%M%p")
        ra: angle = angle(round(self.ra, 2))
        dec: angle = angle(round(self.dec, 2))
        az: angle = angle(round(self.az, 2))
        alt: angle = angle(round(self.alt, 2))
        return(f"Sun data:\n"
               f"- Rise-> set: \t\t\t{sunrise}-> {sunset}\n"
               f"- Right Ascension, Declination:\t({ra},{dec})\n"
               f"- Elevation/Azimuth:\t\t({az},{alt})\n"
               f"- Current Distance:\t\t{sunrise}")

    def _sun_times(self,
                   day: date = date.today()) -> Tuple[datetime, datetime]:
        """Return sunrise and sunset times."""
        # sun = Sun_Import(self.location.latitude, self.location.longitude)
        # sunrise = sun.get_sunrise_time(day)
        # sunset = sun.get_sunset_time(day)
        sunrise, sunset = self.location.calculate_sun_times()

        logger.info(f"METHOD: completed.")
        return sunrise, sunset

    def _equatorial_cooridnates(self, day: date = date.today()
                                ) -> Tuple[angle, angle]:
        """Return right ascension and declination angles."""
        ra, dec = self.location.calculate_equatorial_coords()

        logger.info(f"METHOD: completed.")
        return ra, dec

    def _elevation(self, day: date = date.today()) -> Tuple[angle, angle]:
        """Return azimuth and altitude angles."""
        az, alt = self.location.calculate_elevation()

        logger.info(f"METHOD: completed.")
        return az, alt


class Alarms:
    """Return alarm type objects for going to sleep and getting up."""

    def __str__(self) -> str:
        """Generate summary of class."""
        return(f"Alarms:")


class Time:
    """Return current time as defined by me."""

    def __str__(self) -> str:
        """Generate summary of class."""
        return(f"Time:")
