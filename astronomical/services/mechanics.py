"""This module calculates the orbittal mechanics."""

from datetime import timedelta
from ..model.celestials import (
    OrbittalBody,
    SpinningBody
)
from .physics import (
    angular_velocity,
    gravitational_force,
    law_of_periods
)


class RotationalMechanicsService(SpinningBody):
    """Execute orbittal calculations."""

    def __calculate_axial_velocity(self) -> float:
        """Convert sidereal period to axial velocity.

        Returns angular velocity (degrees/s).
        """
        return angular_velocity(self.sidereal_period)


class OrbittalMechanicsService(OrbittalBody):
    """Execute orbittal calculations."""

    def __calculate_gravitational_force(self) -> float:
        """Apply Universal Law of Gravitation.

        Returns force (N).
        """
        return gravitational_force(self.mass,
                                   self.parent.mass,
                                   self.semimajor_axis)

    def __calculate_orbittal_period(self) -> timedelta:
        """Apply Kepler's Law of Periods to specific daughter.

        Returns period (timedelta).
        """
        return law_of_periods(self.mass,
                              self.parent.mass,
                              self.semimajor_axis)
