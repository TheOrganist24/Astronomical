"""Create custom types for astronomical."""


class mass(float):
    """Custom type: mass (kg)."""

    def __init__(self, *args, **kwargs):
        """Initialise eccentricity."""
        super(mass, self).__init__()
        if args[0] <= 0.0:
            raise TypeError("Mass cannot be 0 or negative")
        self.value = args[0]

    def __str__(self):
        """Return mass representation."""
        return f"{self.value}kg"


class radius(float):
    """Custom type: radius (m)."""

    def __init__(self, *args, **kwargs):
        """Initialise radius."""
        super(radius, self).__init__()
        if args[0] < 0.0:
            raise TypeError("Radius cannot be negative")
        self.value = args[0]

    def __str__(self):
        """Return radius representation."""
        return f"{self.value}m"


class eccentricity(float):
    """Custom type: eccentricity."""

    def __init__(self, *args, **kwargs):
        """Initialise eccentricity."""
        super(eccentricity, self).__init__()
        if not 0.0 < args[0] < 1.0:
            raise TypeError("Elliptic eccentricity can only take values "
                            "between 0 and 1")
        self.value = args[0]

    def __str__(self):
        """Return eccentricity representation."""
        return f"{self.value}"
