"""Model module for providing sensible defaults."""

from dataclasses import dataclass
from datetime import datetime, time, timedelta

from astronomical.model.custom_types import (eccentricity, mass, radius,
                                             real_time)
from astronomical.model.real_world_calculations import State
from astronomical.model.solar_system import Planet, PlanetaryLocation, Star

sun = Star(name="The Sun",
           mass=mass(1.9885*10**30),
           radius=radius(696340000))

earth = Planet(name="Earth",
               mass=mass(5.9722*10**24),
               radius=radius(6371000),
               semimajor_axis=radius(149.598*10**9),
               eccentricity=eccentricity(0.014710219),
               orbital_obliquity=23.44,
               parent=sun,
               sidereal_day=real_time(hours=23,
                                      minutes=56,
                                      seconds=4,
                                      microseconds=90053),
               ref_march_equinox=datetime(year=2021,
                                          month=3,
                                          day=20,
                                          hour=9,
                                          minute=37),
               ref_midnight=datetime(year=1970,
                                     month=1,
                                     day=1))


@dataclass
class SleepRequirements:
    """Sleep requirements."""

    sleep: timedelta = timedelta(hours=7, minutes=10)
    latest_wake_up: time = time(hour=7)
    earliest_wake_up: time = time(hour=6)
    ablutions: timedelta = timedelta(hours=1)


class Defaults:
    """Base defaults class for providing sensible defaults.

    Attributes
    ----------
    location (str)              name of the location
    longitude (float)           positional longitude
    latitude (float)            positional latitude
    locale (PlanetaryLocation)  localized location to a planet
    state (State)               time dependent PlanetaryLocation
    sleep (SleepRequirements)   sleeping pattern requirements
    """

    def __init__(self, sleep: SleepRequirements = SleepRequirements(),
                 location: str = "London", longitude: float = 0.1276,
                 latitude: float = 51.5072, planet: Planet = earth,
                 instant: datetime = datetime.now()) -> None:
        """Initialise with sensible defaults.

        Parameters
        ----------
        sleep (SleepRequirements)   sleeping pattern requirements (as parent)
        location (str)              name of the location ("London")
        longitude (float)           positional longitude (0.1276)
        latitude (float)            positional latitude (51.5072)
        planet (Planet)             localized planet (earth)
        instant (datetime)          required for parent (now)

        Returns
        -------
        None
        """
        self.location: str = location.title()
        self.longitude: float = longitude
        self.latitude: float = latitude
        self.locale: PlanetaryLocation\
            = PlanetaryLocation(name=location, longitude=longitude,
                                latitude=latitude, planet=planet)
        self.state: State = State(instant=instant, location=self.locale)
        self.sleep_requirements = sleep
