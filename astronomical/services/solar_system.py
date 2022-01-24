"""This module calculates solar system mechanics."""

from dataclasses import dataclass
from datetime import datetime, timedelta

from ..model.celestials import Body
from ..model.custom_types import eccentricity, mass, radius, real_time
from ..model.location import Location
from ..model.physics import (altitude, declination, solar_hour_angle,
                             synodic_day)
from .mechanics import OrbittalMechanicsService, RotationalMechanicsService


@dataclass
class Star(Body):
    """Solar system structure; the primary object."""

    pass


@dataclass
class Planet(RotationalMechanicsService, OrbittalMechanicsService):
    """Solar system structure; an orbitting object."""

    parent: Star
    ref_march_equinox: datetime  # orbittal obliquity spring equinox
    ref_midnight: datetime  # any old midnight

    def _calculate_synodic_day(self) -> real_time:
        """Calculate synodic day from sidereal day and period."""
        sidereal_period: timedelta = \
            self._calculate_orbittal_period()
        year: float = sidereal_period.total_seconds()
        day: float = self.sidereal_day.total_seconds()

        syn_day: real_time = synodic_day(year, day)

        return syn_day


@dataclass
class Moon(RotationalMechanicsService, OrbittalMechanicsService):
    """Solar system structure; the orbitter of an orbitting object."""

    parent: Planet


@dataclass
class PlanetaryLocation(Location):
    """Location situated on a planet."""

    planet: Planet

    def _calculate_sunrise(self, instant: datetime = datetime.now()
                           ) -> real_time:
        """Calculate the sunrise.

        # if altitude >= 0 or time is after noon:
        #     iterate backwards to find sunrise
        # else:
        #     iterate forwards
        """
        # declare variables
        lat = self.latitude
        lon = self.longitude
        year: timedelta = self.planet._calculate_orbittal_period()
        sidereal_day: real_time = self.planet.sidereal_day
        syn_day: real_time = self.planet._calculate_synodic_day()

        # calculate variables
        time_since_march_equinox: timedelta = instant \
            - self.planet.ref_march_equinox
        time_since_midnight: timedelta = (instant
                                          - self.planet.ref_midnight) \
            % syn_day
        ha = solar_hour_angle(syn_day, time_since_midnight) - lon
        dec = declination(self.planet.orbittal_obliquity,
                          sidereal_day,
                          time_since_march_equinox)

        # iterate
        if altitude(lat, dec, ha) >= 0.0 \
                or time_since_midnight >= (syn_day) / 2:
            # iterate back
            print("")
        else:
            # iterate forward
            print("")
        return real_time(seconds=1)


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
