"""Command line interfaces for astronomical."""

from datetime import date, datetime
from typing import Tuple
from suntime import (  # type: ignore
    Sun as Sun_Import,
    SunTimeException
)
from ..utils.configuration import (
    Defaults
)
from ..utils.logging import (
    logger
)
from ..model.location import (
    Location
)
from ..services.solar_system import (
    earth
)


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

    def __str__(self) -> str:
        """Generate summary of class."""
        sunrise = self.rise.strftime("%I:%M%p")
        sunset = self.set.strftime("%I:%M%p")
        return(f"Sun data:\n"
               f"- Rise-> set: \t\t{sunrise}-> {sunset}\n"
               f"- Elevation/Azimuth:\t{sunrise}{d}/{sunset}{d}\n"
               f"- Current Distance:\t{sunrise}m")

    def _sun_times(self,
                   day: date = date.today()) -> Tuple[datetime, datetime]:
        """Return sunrise and sunset times.

        This function should be retired in favour of one part of the Sun
        class. That class should calculate this from first principles instead
        of pulling from an API.
        """
        sun = Sun_Import(self.location.latitude, self.location.longitude)
        sunrise = sun.get_sunrise_time(day)
        sunset = sun.get_sunset_time(day)
        logger.info(f"METHOD: completed.")
        return sunrise, sunset


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
