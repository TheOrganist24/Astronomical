"""Collection of Physics Equations for use in the rest of the package."""

from datetime import timedelta
import math
import sys
from typing import Tuple
from ..utils.logging import (
    logger
)


# Constants
G = 6.67408*10**-11


# Conversions
@logger.catch
def angular_velocity(T: timedelta) -> float:
    """Calculate angular velocity.

    Where:
    w = Anugular velocity
    T = Period of rotation (orbit)
    """
    logger.debug(f"BASE FUNCTION: \"angular_velocity\" invoked.")
    try:
        w = 360 / T.total_seconds()
    except ZeroDivisionError as err:
        logger.warning(f"FUNCTION: \"angular_velocity\" needs T > 0s {err}")
        w = 0.0
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
def gravitational_force(M: float, m: float, r: float) -> float:
    """Calculate force between two bodies.

    According to Newton's Law of Universal Gravitation. Where:
    F = Force
    G = Universal Gravitational Constant
    M = Mass of (major) body
    m = Mass of (minor) body
    r = Body displacement
    """
    logger.debug(f"BASE FUNCTION: \"gravitational_force\" invoked.")
    try:
        F = G * (M*m) / r**2
    except ZeroDivisionError:
        logger.warning(f"FUNCTION: \"gravitational_force\" needs r > 0m")
        F = 0.0
    return F


def law_of_orbits_aphelion(a: float, e: float) -> float:
    """Calculate aphelion from Kepler's Law or Orbits.

    Where:
    R = Displacement from major body to aphelion
    a = Semi-major axis
    e = eccentricity
    """
    logger.debug(f"BASE FUNCTION: \"law_of_orbits_aphelion\" invoked.")
    R = a * (1+e)
    return R


def law_of_orbits_perihelion(a: float, e: float) -> float:
    """Calculate aphelion from Kepler's Law or Orbits.

    Where:
    R = Displacement from major body to perihelion
    a = Semimajor axis
    e = eccentricity
    """
    logger.debug(f"BASE FUNCTION: \"law_of_orbits_perihelion\" invoked.")
    R = a * (1-e)
    return R


@logger.catch
def law_of_orbits(a: float, e: float) -> Tuple[float, float]:
    """Calculate Kepler's Law of Orbits.

    Where:
    a = Semimajor axis
    e = eccentricity
    """
    return law_of_orbits_aphelion(a, e), law_of_orbits_perihelion(a, e)


@logger.catch
def law_of_periods(M: float, m: float, a: float) -> timedelta:
    """Calculate Kepler's Law of Orbits.

    Where:
    T = Period
    G = Universal Gravitational Constant
    M = Mass of (major) body
    m = Mass of (minor) body
    a = Semimajor axis
    """
    logger.debug(f"BASE FUNCTION: \"law_of_periods\" invoked.")
    try:
        T_sqrd = ((4*math.pi**2) / (G * (M+m))) * a**3
    except ZeroDivisionError:
        logger.warning(f"FUNCTION: \"law_of_periods\" needs (M,m)>0kg, a>0m")
        t_sqrd = 0.0
    try:
        seconds = math.sqrt(T_sqrd)
    except ValueError as err:
        if T_sqrd < 0:
            logger.warning(f"FUNCTION: \"law_of_periods\" T^2 is negative")
        else:
            logger.error(f"FUNCTION: \"law_of_periods\" returned \"{err}\"")
            sys.exit(1)
        seconds = 0
    T = timedelta(seconds=seconds)
    return T


# Coordinate calculations for relative celestial bodies
@logger.catch
def declination_coordinates() -> Tuple[float, float]:
    """Calculate Right Ascension/Declination relative to equator."""
    return right_ascension(), declination()


def right_ascension() -> float:
    """Calculate Right Ascension from equator."""
    logger.debug(f"BASE FUNCTION: \"right_ascension\" invoked.")
    return 0.0


def declination() -> float:
    """Calculate declination from equator."""
    logger.debug(f"BASE FUNCTION: \"declination\" invoked.")
    return 0.0


@logger.catch
def elevation() -> Tuple[float, float]:
    """Calculate Azimuth/Altitude relative to local horizon."""
    return azimuth(), altitude()


def azimuth() -> float:
    """Calculate Azimuth from local horizon."""
    logger.debug(f"BASE FUNCTION: \"azimuth\" invoked.")
    return 0.0


def altitude() -> float:
    """Calculate Altitude from local horizon."""
    logger.debug(f"BASE FUNCTION: \"altitude\" invoked.")
    return 0.0
