"""Collection of Physics Equations for use in the rest of the package."""

from datetime import timedelta
import math
import sys
from typing import Tuple
from ..utils.logging import (
    logger
)
from ..model.custom_types import (
    mass,
    radius,
    eccentricity,
    real_time
)


# Constants
G = 6.67408*10**-11


# Conversions
@logger.catch
def angular_velocity(T: real_time) -> float:
    """Calculate angular velocity.

    Where:
    w = Anugular velocity
    T = Period of rotation (orbit)
    """
    logger.debug(f"BASE FUNCTION: \"angular_velocity\" invoked.")
    w = 360 / T.total_seconds()
    return w


@logger.catch
def a_sin_theta(a: float, theta: float) -> float:
    """Calulate sin curve of function f(a, theta) = a sin(theta).

    Where:
    a -> magnitude
    theta -> fractional revolution
    """
    logger.debug(f"BASE FUNCTION: \"a_sin_theta\" invoked.")
    result = a * math.sin(theta * (2*math.pi))
    return result


# Laws
@logger.catch
def gravitational_force(M: mass, m: mass, r: radius) -> float:
    """Calculate force between two bodies.

    According to Newton's Law of Universal Gravitation. Where:
    F = Force
    G = Universal Gravitational Constant
    M = Mass of (major) body
    m = Mass of (minor) body
    r = Body displacement
    """
    logger.debug(f"BASE FUNCTION: \"gravitational_force\" invoked.")
    F = G * (M*m) / r**2
    return F


@logger.catch
def law_of_orbits_aphelion(a: radius, e: eccentricity) -> radius:
    """Calculate aphelion from Kepler's Law or Orbits.

    Where:
    R = Displacement from major body to aphelion
    a = Semi-major axis
    e = eccentricity
    """
    logger.debug(f"BASE FUNCTION: \"law_of_orbits_aphelion\" invoked.")
    R: radius = radius(a * (1+e))
    return R


@logger.catch
def law_of_orbits_perihelion(a: radius, e: eccentricity) -> radius:
    """Calculate aphelion from Kepler's Law or Orbits.

    Where:
    R = Displacement from major body to perihelion
    a = Semimajor axis
    e = eccentricity
    """
    logger.debug(f"BASE FUNCTION: \"law_of_orbits_perihelion\" invoked.")
    R: radius = radius(a * (1-e))
    return R


@logger.catch
def law_of_orbits(a: radius, e: eccentricity) -> Tuple[radius, radius]:
    """Calculate Kepler's Law of Orbits.

    Where:
    a = Semimajor axis
    e = eccentricity
    """
    logger.debug(f"BASE FUNCTION: \"law_of_orbits\" invoked.")
    return law_of_orbits_aphelion(a, e), law_of_orbits_perihelion(a, e)


@logger.catch
def law_of_periods(M: mass, m: mass, a: radius) -> timedelta:
    """Calculate Kepler's Law of Orbits.

    Where:
    T = Period
    G = Universal Gravitational Constant
    M = Mass of (major) body
    m = Mass of (minor) body
    a = Semimajor axis
    """
    logger.debug(f"BASE FUNCTION: \"law_of_periods\" invoked.")
    T_sqrd = ((4*math.pi**2) / (G * (M+m))) * a**3
    seconds = math.sqrt(T_sqrd)
    T = timedelta(seconds=seconds)
    return T


# Coordinate calculations for relative celestial bodies
@logger.catch
def equatorial_coordinates() -> Tuple[timedelta, float]:
    """Calculate Right Ascension/Declination relative to equator."""
    logger.debug(f"BASE FUNCTION: \"equatorial_coordinates\" invoked.")
    return right_ascension(timedelta(days=0),
                           real_time(days=0)), \
        declination(0.0,
                    real_time(seconds=1),
                    timedelta(seconds=1))


@logger.catch
def right_ascension(time_since_vernal_equinox: timedelta,
                    synodic_day: real_time) -> timedelta:
    """Calculate Right Ascension of parent body.

    Resembles longitude in the equatorial coordinate system. It is the angular
    distance of the reletive body measured eastwards from the Vernal Equinox,
    or First Point of Aries.

    This function returns the "Longitudinal" position of relative body given
    the time since the vernal equinox.

    The return is a timedelta object with 24 hours being a full circle.
    """
    logger.debug(f"BASE FUNCTION: \"right_ascension\" invoked.")
    time_through_day = time_since_vernal_equinox % synodic_day
    ra_sun = time_through_day  # since the sun is at right ascension at noon
    return time_through_day


@logger.catch
def declination(orbittal_obliquity: float,
                sidereal_period: real_time,
                time_since_march_equinox: timedelta) -> float:
    """Calculate declination of the parent body above celestial equator.

    The celestial equator is the projection of the equator into space. This
    assumes that the orbitting body processes round it's orbit in a uniform
    manner and not according to KII (equal areas swept in equal times).
    """
    logger.debug(f"BASE FUNCTION: \"declination\" invoked.")
    orbit_completed = (time_since_march_equinox / sidereal_period)
    dec = a_sin_theta(orbittal_obliquity, orbit_completed)
    return dec


@logger.catch
def elevation() -> Tuple[float, float]:
    """Calculate Azimuth/Altitude of body relative to local position."""
    logger.debug(f"BASE FUNCTION: \"elevation\" invoked.")
    return azimuth(), altitude()


@logger.catch
def azimuth() -> float:
    """Calculate Azimuth of body from local position.

    Azimuth is the angle round the horizon where a relative body is. North is
    defined as 0 degrees, with East at 90 degrees.
    """
    logger.debug(f"BASE FUNCTION: \"azimuth\" invoked.")
    return 0.0


@logger.catch
def altitude() -> float:
    """Calculate Altitude from of bodylocal postition.

    Altitude is the angle of the body above the horizon where 0 degrees is the
    horizon, 90 degrees is directly over head, and -90 is directly beneath.
    """
    logger.debug(f"BASE FUNCTION: \"altitude\" invoked.")
    return 0.0
