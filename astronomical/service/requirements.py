"""Requirements for astronomical."""

import math
from datetime import date, datetime, time, timedelta
from typing import Tuple

import pytz
from suntime import Sun as Sun_Import  # type: ignore
from suntime import SunTimeException

from ..model.custom_types import angle
from ..model.location import Location
from ..model.real_world_calculations import Alarms, State, Time
from ..model.solar_system import PlanetaryLocation, earth
from ..service.configuration import Defaults
from ..service.logging import logger

d = u"\N{DEGREE SIGN}"


class SunService:
    """Return sunrise/set times, and the sun's relative position."""

    def __init__(self, state: State) -> None:
        """Initialise variables."""
        logger.info(f"INTERFACE: \"{self.__class__.__name__}\" "
                    f"instantiating.")
        self.rise, self.set = state.suntimes
        self.ra, self.dec = state.equatorial_coords
        self.az, self.alt = state.elevation

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


class TimeService:
    """Return current time as defined by me."""

    def __init__(self, time: Time) -> None:
        """Initialise variables."""
        logger.info(f"INTERFACE: \"{self.__class__.__name__}\" "
                    f"instantiating.")
        self.std = datetime.now()
        self.nac = time.nac

    def __str__(self) -> str:
        """Generate summary of class."""
        std = self.std.strftime("%I:%M%p")
        nac = self.nac.strftime("%I:%M%p")
        return(f"Time:\n"
               f"- STD: {std}\n"
               f"- NAC: {nac}")
