"""This module calculates the orbittal mechanics."""

from .physics import gravitational_force


class OrbittalCalculationService:
    """Execute orbittal calculations."""

    def __calculate_orbittal_force(self,
                                   mass_of_daughter: float,
                                   mass_of_parent: float,
                                   semimajor_axis: float) -> float:
        """Apply Universal Law of Gravitation."""
        return gravitational_force(mass_of_daughter,
                                   mass_of_parent,
                                   semimajor_axis)
