"""Utilities related to sleep."""

from datetime import timedelta, date


class Requirements:
    """User defined sleep requirements."""

    def __init__(self,
                 duration=timedelta(hours=8),
                 seasonal_variance=timedelta(hours=1),
                 min_rise=None,
                 max_rise=None,
                 schedule_till=date.today() + timedelta(days=7)):
        """Define all instance attributes here."""
        self.duration = duration
        self.seasonal_variance = seasonal_variance
        self.min_rise = min_rise
        self.max_rise = max_rise
