"""Requirements for astronomical."""

import math
from datetime import date, datetime, time, timedelta
from typing import Tuple

import pytz
from suntime import Sun as Sun_Import  # type: ignore
from suntime import SunTimeException

from ..model.custom_types import angle
from ..model.location import Location
from ..model.real_world_calculations import Alarms
from ..model.solar_system import PlanetaryLocation, earth
from ..service.configuration import Defaults
from ..service.logging import logger

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


class AlarmsService:
    """Return alarm type objects for going to sleep and getting up."""

    def __init__(self, alarm: Alarms) -> None:
        """Initialise variables."""
        logger.info(f"INTERFACE: \"{self.__class__.__name__}\" "
                    f"instantiating.")
        self.bedtime = alarm.sleep
        self.get_up = alarm.wake
        self.start_work = alarm.work

    def __str__(self) -> str:
        """Generate summary of class."""
        sleep = self.bedtime.strftime("%I:%M%p")
        rise = self.get_up.strftime("%I:%M%p")
        work = self.start_work.strftime("%I:%M%p")
        return(f"Alarms:\n"
               f"- Bedtime:\t{sleep}\n"
               f"- Get up:\t{rise}\n"
               f"- Start work:\t{work}")


class Time:
    """Return current time as defined by me."""

    def __init__(self) -> None:
        """Initialise variables."""
        logger.info(f"INTERFACE: \"{self.__class__.__name__}\" "
                    f"instantiating.")
        locale = Defaults()
        self.location = locale.location()
        self.gmt = datetime.now()
        self.nac = self._calc_nac_time()

    def __str__(self) -> str:
        """Generate summary of class."""
        gmt = self.gmt.strftime("%I:%M%p")
        nac = self.nac.strftime("%I:%M%p")
        return(f"Time:\n"
               f"- GMT: {gmt}\n"
               f"- NAC: {nac}")

    def _calc_nac_time(self) -> datetime:
        now = pytz.utc.localize(datetime.now())
        day: date = date.today()
        sun = Sun_Import(self.location.latitude, self.location.longitude)  # d
        sunrise = sun.get_sunrise_time(day)  # disable
        sunset = sun.get_sunset_time(day)  # disable
        # sunrise, sunset = self.location.calculate_sun_times()  # enable

        gs_per_n_day: float = (sunset - sunrise).total_seconds() / 43200
        gs_per_n_night: float = (86400 - (sunset - sunrise).total_seconds()) \
            / 43200

        if now < sunrise:
            ref_time = datetime.combine(date.today(), time())  # midnight
            diff = (datetime.now() - ref_time) * gs_per_n_night
            nac_now = ref_time + diff
        elif now > sunset:
            ref_time = datetime.combine(date.today(), time(hour=18))  # sunset
            diff = (datetime.now() - ref_time) * gs_per_n_night
            nac_now = ref_time + diff
        else:
            ref_time = datetime.combine(date.today(), time(hour=6))  # sunset
            diff = (datetime.now() - ref_time) * gs_per_n_day
            nac_now = ref_time + diff
        return nac_now