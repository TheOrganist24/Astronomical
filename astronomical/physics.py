"""Collection of Physics Equations for use in the rest of the package."""


G = 6.67408*10**-11


def gravitational_force(M: float,
                        m: float,
                        r: float) -> float:
    """Calculate force between two bodies.

    According to Newton's Law of Universal Gravitation.
    """
    F = G * (M*m) / r**2
    return F
