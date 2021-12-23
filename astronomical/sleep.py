"""Utilities related to sleep."""

from datetime import timedelta, date, datetime
import math
from . import sun


class Requirements:
    """User defined sleep requirements."""

    def __init__(self,
                 duration=timedelta(hours=8),
                 seasonal_variance=timedelta(hours=1),
                 min_rise=None,
                 max_rise=None):
        """Define all instance attributes here."""
        self.duration = duration  # minimum sleep
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


def duration(location, requirements, night_start=date.today()):
    """Calculate duration of sleep for a given night."""
    # find last winter solstice (night time is at maximum)
    last_winter = date(date.today().year - 1, 12, 21)
    this_winter = date(date.today().year, 12, 21)

    if night_start < this_winter:
        winter = last_winter
    elif this_winter <= night_start:
        winter = this_winter

    # calculate cos curve for night length
    day_shift = (night_start - winter).total_seconds() / (60*60*24)
    cos_curve = math.cos(2*math.pi*(day_shift/365))
    cos_curve = (1 + cos_curve) / 2
    variance = requirements.seasonal_variance.total_seconds()
    season_diff = timedelta(seconds=(variance * cos_curve))

    return requirements.duration + season_diff


def alarms(location, requirements, night_start=date.today()):
    """Calculate going to bed, and waking up times."""
    return datetime.now(), datetime.now()
