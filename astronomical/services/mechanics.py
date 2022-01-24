"""This module calculates the orbittal mechanics."""

from datetime import timedelta

from ..model.celestials import OrbittalBody, SpinningBody
from ..model.custom_types import eccentricity, mass, radius
from ..model.physics import (angular_velocity, gravitational_force,
                             law_of_periods)
from ..utils.logging import logger


class RotationalMechanicsService(SpinningBody):
    """Execute orbittal calculations."""

    def _calculate_axial_velocity(self) -> float:
        """Convert sidereal period to axial velocity.

        Returns angular velocity (degrees/s).
        """
        result = angular_velocity(self.sidereal_day)
        logger.debug(f"METHOD \"_calculate_axial_velocity\": "
                     f"returns \"{result}\".")
        return result


class OrbittalMechanicsService(OrbittalBody):
    """Execute orbittal calculations."""

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

    def _calculate_orbittal_period(self) -> timedelta:
        """Apply Kepler's Law of Periods.

        Returns period (timedelta); also known as the sidereal period.
        """
        result = law_of_periods(self.mass,
                                self.parent.mass,
                                self.semimajor_axis)
        logger.debug(f"METHOD \"_calculate_orbittal_period\": "
                     f"returns \"{result}\".")
        return result
