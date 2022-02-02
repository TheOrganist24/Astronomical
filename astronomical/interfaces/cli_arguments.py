"""Command line interfaces for astronomical."""

import math
from datetime import date, datetime, time, timedelta
from typing import Tuple

from suntime import Sun as Sun_Import  # type: ignore
from suntime import SunTimeException

from ..model.custom_types import angle
from ..model.location import Location
from ..model.solar_system import earth
from ..utils.configuration import Defaults
from ..utils.logging import logger

d = u"\N{DEGREE SIGN}"


class Sun:
    """Return sunrise/set times, and the sun's relative position."""

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
               f"- Azimuth, Altitude:\t\t({az},{alt})")

    def _sun_times(self,
                   day: date = date.today()) -> Tuple[datetime, datetime]:
        """Return sunrise and sunset times."""
        sun = Sun_Import(self.location.latitude, self.location.longitude)  # d
        sunrise = sun.get_sunrise_time(day)  # disable
        sunset = sun.get_sunset_time(day)  # disable
        # sunrise, sunset = self.location.calculate_sun_times()  # enable

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

    def __init__(self) -> None:
        """Initialise variables."""
        logger.info(f"INTERFACE: \"{self.__class__.__name__}\" "
                    f"instantiating.")
        locale = Defaults()
        self.location = locale.location()
        self.get_up = self._set_alarm()
        self.start_work = self.get_up + timedelta(hours=1)

    def __str__(self) -> str:
        """Generate summary of class."""
        rise = self.get_up.strftime("%I:%M%p")
        work = self.start_work.strftime("%I:%M%p")
        return(f"Alarms:\n"
               f"- Get up:\t{rise}\n"
               f"- Start work:\t{work}")

    def _set_alarm(self) -> datetime:
        ref_midnight = datetime.now().date() + timedelta(hours=24)
        latest = datetime.combine(ref_midnight, time(hour=7))
        earliest = datetime.combine(ref_midnight, time(hour=6))
        margin = latest - earliest
        year = self.location.planet._calculate_orbittal_period()
        annual_procession = (datetime.combine(ref_midnight, time())
                             - self.location.planet.ref_march_equinox) / year
        math_diff = margin * math.sin((2*math.pi)*annual_procession)
        diff = (math_diff + margin) / 2
        alarm = latest - diff
        return alarm


class Time:
    """Return current time as defined by me."""

    def __str__(self) -> str:
        """Generate summary of class."""
        return(f"Time:")
