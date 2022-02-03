"""Collection of Physics Equations for use in the rest of the package."""

import math
import sys
from datetime import timedelta
from typing import Tuple

from ..model.custom_types import eccentricity, mass, radius, real_time
from ..service.logging import logger

# Constants
G: float = 6.67408*10**-11


# Conversions
@logger.catch
def angular_velocity(T: real_time) -> float:
    """Calculate angular velocity.

    Where:
    w = Anugular velocity
    T = Period of rotation (orbit)
    """
    logger.debug(f"BASE FUNCTION: \"angular_velocity\" invoked.")
    w: float = 360 / T.total_seconds()
    return w


@logger.catch
def a_sin_theta(a: float, theta: float) -> float:
    """Calulate sin curve of function f(a, theta) = a sin(theta).

    Where:
    a -> magnitude
    theta -> fractional revolution
    """
    logger.debug(f"BASE FUNCTION: \"a_sin_theta\" invoked.")
    result: float = a * math.sin(theta * (2*math.pi))
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
    F: float = G * (M*m) / r**2
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
def law_of_periods(M: mass, m: mass, a: radius) -> real_time:
    """Calculate Kepler's Law of Orbits.

    Where:
    T = Period
    G = Universal Gravitational Constant
    M = Mass of (major) body
    m = Mass of (minor) body
    a = Semimajor axis
    """
    logger.debug(f"BASE FUNCTION: \"law_of_periods\" invoked.")
    T_sqrd: float = ((4*math.pi**2) / (G * (M+m))) * a**3
    seconds: float = math.sqrt(T_sqrd)
    T: real_time = real_time(seconds=seconds)
    return T


# Coordinate calculations for relative celestial bodies
@logger.catch
def equatorial_coordinates(time_since_vernal_equinox: timedelta,
                           synodic_day: real_time,
                           orbittal_obliquity: float,
                           sidereal_period: real_time,
                           time_since_march_equinox: timedelta
                           ) -> Tuple[timedelta, float]:
    """Calculate Right Ascension/Declination relative to equator."""
    logger.debug(f"BASE FUNCTION: \"equatorial_coordinates\" invoked.")
    return right_ascension(time_since_vernal_equinox,
                           synodic_day), \
        declination(orbittal_obliquity,
                    sidereal_period,
                    time_since_march_equinox)


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
    time_through_day: timedelta = time_since_vernal_equinox % synodic_day
    ra_sun: timedelta = time_through_day  # since the sun is at ra at noon
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
    orbit_completed: float = (time_since_march_equinox / sidereal_period)
    dec: float = a_sin_theta(orbittal_obliquity, orbit_completed)
    return dec


@logger.catch
def solar_hour_angle(synodic_day: real_time,
                     time_since_midnight: timedelta) -> float:
    """Calculate soloar hour angle."""
    second_angle: float = 360 / synodic_day.total_seconds()
    elapsed_angle: float = time_since_midnight.total_seconds() * second_angle
    solar_hour_angle: float = elapsed_angle - 180
    return solar_hour_angle


@logger.catch
def elevation(latitude: float,
              declination: float,
              hour_angle: float) -> Tuple[float, float]:
    """Calculate Azimuth/Altitude of body relative to local position."""
    logger.debug(f"BASE FUNCTION: \"elevation\" invoked.")

    alt: float = altitude(latitude, declination, hour_angle)
    az: float = azimuth(latitude, declination, hour_angle, alt)
    return az, alt


@logger.catch
def azimuth(latitude: float,
            declination: float,
            hour_angle: float,
            altitude: float) -> float:
    """Calculate Azimuth of body from local position.

    Azimuth is the angle round the horizon where a relative body is. North is
    defined as 0 degrees, with East at 90 degrees.
    """
    logger.debug(f"BASE FUNCTION: \"azimuth\" invoked.")

    lat: float = ((2*math.pi)/360) * latitude
    dec: float = ((2*math.pi)/360) * declination
    ha: float = ((2*math.pi)/360) * hour_angle
    alt: float = ((2*math.pi)/360) * altitude

    s_az: float = (math.cos(lat)*math.sin(dec)
                   - math.sin(lat)*math.cos(dec)*math.cos(ha)) \
        / math.cos(alt)

    # correct for Python3 rounding errors
    if s_az < -1:
        s_az = -1
    elif s_az > 1:
        s_az = 1

    az: float
    if hour_angle < 0.0:
        az = (360/(2*math.pi)) * math.acos(s_az)
    else:
        az = 360 - ((360/(2*math.pi)) * math.acos(s_az))

    return az


@logger.catch
def altitude(latitude: float,
             declination: float,
             hour_angle: float) -> float:
    """Calculate Altitude from of local postition.

    Altitude is the angle of the body above the horizon where 0 degrees is the
    horizon, 90 degrees is directly over head, and -90 is directly beneath.
    """
    logger.debug(f"BASE FUNCTION: \"altitude\" invoked.")

    lat: float = ((2*math.pi)/360) * latitude
    dec: float = ((2*math.pi)/360) * declination
    ha: float = ((2*math.pi)/360) * hour_angle

    s_alt: float = math.sin(lat)*math.sin(dec) \
        + math.cos(lat)*math.cos(dec)*math.cos(ha)
    alt: float = (360/(2*math.pi)) * math.asin(s_alt)
    return alt


@logger.catch
def synodic_day(year: float, day: float) -> real_time:
    """Calculate synodic day from sidereal day and period."""
    synodic_seconds: float = (year*day) / (year - day)
    synodic_day = real_time(seconds=synodic_seconds)

    return synodic_day
