"""This module calculates the orbital mechanics."""

from datetime import timedelta

from ..model.celestials import OrbitalBody, SpinningBody
from ..model.custom_types import eccentricity, mass, radius, real_time
from ..model.physics import (angular_velocity, gravitational_force,
                             law_of_periods)
from ..service.logging import logger


class RotationalMechanicsService(SpinningBody):
    """Execute orbital calculations."""

    def _calculate_axial_velocity(self) -> float:
        """Convert sidereal day to axial velocity.

        Returns angular velocity (degrees/s).
        """
        result = angular_velocity(self.sidereal_day)
        logger.debug(f"METHOD \"_calculate_axial_velocity\": "
                     f"returns \"{result}\".")
        return result


class OrbitalMechanicsService(OrbitalBody):
    """Execute orbital calculations."""

    def _calculate_gravitational_force(self) -> float:
        """Apply Universal Law of Gravitation.

        Returns force (N).
        """
        result = gravitational_force(self.mass,
                                     self.parent.mass,
                                     self.semimajor_axis)
        logger.debug(f"METHOD \"_calculate_gravitational_force\": "
                     f"returns \"{result}\".")
        return result

    def _calculate_orbital_period(self) -> real_time:
        """Apply Kepler's Law of Periods.

        Returns period (timedelta); also known as the sidereal period.
        """
        result = law_of_periods(self.mass,
                                self.parent.mass,
                                self.semimajor_axis)
        logger.debug(f"METHOD \"_calculate_orbital_period\": "
                     f"returns \"{result}\".")
        return result
