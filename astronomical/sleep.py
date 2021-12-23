"""Utilities related to sleep."""

from datetime import timedelta, date


class Requirements:
    """User defined sleep requirements."""

    def __init__(self,
                 duration=timedelta(hours=8),
                 seasonal_variance=timedelta(hours=1),
                 min_rise=None,
                 max_rise=None):
        """Define all instance attributes here."""
        self.duration = duration
        self.seasonal_variance = seasonal_variance
        self.min_rise = min_rise
        self.max_rise = max_rise

    def __repr__(self):
        """Produce code to initialise this class."""
        return f"Requirments()"

    def __str__(self):
        """Generate summary of class with minimal inputs."""
        return f"""Requirements \
        \n- hours sleep: {self.duration} \
        \n- seasonal varience: {self.duration}
        """


def duration(location, requirements, night_start):
    """Calculate duration of sleep for a given night."""
    return timedelta(hours=24)
