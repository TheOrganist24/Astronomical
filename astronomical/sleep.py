"""Utilities related to sleep."""

from datetime import timedelta as td


class Requirements:
    """User defined sleep requirements."""

    def __init__(self,
                 duration=td(hours=8),
                 seasonal_variance=td(hours=1),
                 min_rise=None,
                 max_rise=None):
        """Define all instance attributes here."""
        self.duration = duration
        self.seasonal_variance = seasonal_variance
        self.min_rise = min_rise
        self.max_rise = max_rise
