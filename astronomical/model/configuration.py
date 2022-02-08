"""This module provides base classes for configuration."""
from datetime import datetime

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
               orbittal_obliquity=23.44,
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


class Defaults:
    """Base defaults class."""

    def __init__(self, location: str = "London", longitude: float = 0.1276,
                 latitude: float = 51.5072, planet: Planet = earth,
                 instant: datetime = datetime.now()) -> None:
        """Initialise variables."""
        self.location: str = location.title()
        self.longitude: float = longitude
        self.latitude: float = latitude
        self.locale: PlanetaryLocation\
            = PlanetaryLocation(name=location, longitude=longitude,
                                latitude=latitude, planet=planet)
        self.state: State = State(instant=instant, location=self.locale)
