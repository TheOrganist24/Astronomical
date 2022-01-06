"""Utilities related to the heavenly spheres."""

from datetime import datetime, time, timedelta
from typing import Optional, Dict
from .physics import angular_velocity, gravitational_force, law_of_periods
from .location import Location


reference_date = datetime


class CelestialBody:
    """Base class for astronomical objects."""

    def __init__(self,
                 name: str,
                 # bulk parameters
                 mass: float,
                 daughters: Dict[str, "CelestialBody"] = {},
                 # orbital parameters
                 semimajor_axis: float = 0,
                 perihelion: datetime = datetime(year=2000,
                                                 month=1,
                                                 day=1,
                                                 hour=12),
                 vernal_equinox: datetime = datetime(year=2000,
                                                     month=3,
                                                     day=21,
                                                     hour=12),
                 ecliptic_obliquity: float = 0,
                 # rotational parameters
                 sidereal_period: timedelta = timedelta(seconds=1)
                 ) -> None:
        """Define all instance attributes here."""
        self.name = name
        self.mass = mass
        self.sidereal_period = sidereal_period
        self.daughters = daughters
        self.semimajor_axis = semimajor_axis
        self.perihelion = perihelion
        self.ecliptic_obliquity = ecliptic_obliquity
        self.vernal_equinox = vernal_equinox

    def __repr__(self) -> str:
        """Procuce code to initialise this class."""
        return f"CelestialBody({self.name!r}, {self.mass})"

    def __str__(self) -> str:
        """Generate summary of class with minimal inputs."""
        return f"CelestialBody \"{self.name.title()}\": ({self.mass:.2e}kg)"

    def add_semimajor_axis(self, semimajor_axis: float) -> None:
        """Add orbital distance to parent."""
        self.semimajor_axis = semimajor_axis

    def add_daughters(self, daughter: "CelestialBody",
                      semimajor_axis: float) -> None:
        """Add daugters to self."""
        daughter.add_semimajor_axis(semimajor_axis)
        self.daughters[daughter.name] = daughter

    def orbittal_force(self, daughter: str) -> float:
        """Apply Universal Law of Gravitation to specific daughter."""
        return gravitational_force(self.mass,
                                   self.daughters[daughter].mass,
                                   self.daughters[daughter].semimajor_axis)

    def orbittal_period(self, daughter: str) -> timedelta:
        """Apply Kepler's Law of Periods to specific daughter."""
        return law_of_periods(self.mass,
                              self.daughters[daughter].mass,
                              self.daughters[daughter].semimajor_axis)

    def orbittal_velocity(self, daughter: str) -> float:
        """Convert orbittal period to orbittal velocity."""
        return angular_velocity(
            self.orbittal_period(
                self.daughters[daughter].name))

    def axial_velocity(self) -> float:
        """Convert sidereal period to axial velocity."""
        return angular_velocity(self.sidereal_period)

    def azimuth(self, location: Location, daughter: str) -> float:
        """Calculate horizontal angle of self from POV of daughter."""
        return location.longitude

    def elevation(self, location: Location, daughter: str) -> float:
        """Calculate vertical angle of self from POV of daughter."""
        return location.latitude


earth = CelestialBody(name="Earth",
                      mass=5.9722*10**24,
                      sidereal_period=timedelta(hours=23,
                                                minutes=56,
                                                seconds=4,
                                                microseconds=90053),
                      ecliptic_obliquity=23.44,
                      perihelion=datetime(year=2022,
                                          month=1,
                                          day=4,
                                          hour=6,
                                          minute=52),
                      vernal_equinox=datetime(year=2021,
                                              month=3,
                                              day=20,
                                              hour=9,
                                              minute=37))
