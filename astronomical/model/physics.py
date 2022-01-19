"""Collection of Physics Equations for use in the rest of the package."""

from datetime import timedelta
import math
from typing import Tuple
from ..utils.logging import (
    logger
)


# Constants
G = 6.67408*10**-11


# Conversions
def angular_velocity(T: timedelta) -> float:
    """Calculate angular velocity.

    Where:
    w = Anugular velocity
    T = Period of rotation (orbit)
    """
    logger.debug(f"BASE FUNCTION: \"angular_velocity\" invoked.")
    if T.total_seconds() == 0.0:
        w = 0.0
    else:
        w = 360 / T.total_seconds()
    return w


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
    F = G * (M*m) / r**2
    return F


def law_of_orbits_aphelion(a: float, e: float) -> float:
    """Calculate aphelion from Kepler's Law or Orbits.

    Where:
    R = Displacement from major body to aphelion
    a = Semi-major axis
    e = eccentricity
    """
    R = a * (1+e)
    return R


def law_of_orbits_perihelion(a: float, e: float) -> float:
    """Calculate aphelion from Kepler's Law or Orbits.

    Where:
    R = Displacement from major body to perihelion
    a = Semimajor axis
    e = eccentricity
    """
    R = a * (1-e)
    return R


def law_of_orbits(a: float, e: float) -> Tuple[float, float]:
    """Calculate Kepler's Law of Orbits.

    Where:
    a = Semimajor axis
    e = eccentricity
    """
    logger.debug(f"BASE FUNCTION: \"law_of_orbits\" invoked.")
    return law_of_orbits_aphelion(a, e), law_of_orbits_perihelion(a, e)


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
    T_sqrd = ((4*math.pi**2) / (G * (M+m))) * a**3
    T = timedelta(seconds=math.sqrt(T_sqrd))
    return T
