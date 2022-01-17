"""Utilities related to sleep; including duration and alarms.

FOR DELETION: Only keeping around for reference.
"""

from datetime import timedelta, date, datetime, time
from typing import Optional, Tuple
import math
import pytz

from .interfaces import sun, location

utc = pytz.UTC


class Requirements:
    """User defined sleep requirements.

    This is where the user can tailor their needs. Defaults are based around
    needing 8 hours sleep, and 1 hour of seasonal variance in wake-up times.
    If not limits are set on wake-up times then it defaults to sunrise.
    """

    def __init__(self,
                 min_duration: timedelta = timedelta(hours=8),
                 seasonal_variance: timedelta = timedelta(hours=1),
                 min_rise: Optional[time] = None,
                 max_rise: Optional[time] = None) -> None:
        """Define all instance attributes here."""
        self.min_duration = min_duration  # minimum sleep
        self.seasonal_variance = seasonal_variance
        self.min_rise = min_rise
        self.max_rise = max_rise

    def __repr__(self) -> str:
        """Produce code to initialise this class."""
        return f"Requirments()"

    def __str__(self) -> str:
        """Generate summary of class with minimal inputs."""
        return f"""Requirements \
        \n- hours sleep: {self.min_duration} \
        \n- seasonal varience: {self.seasonal_variance}
        """

    def duration(self, night_start: date = date.today()) -> timedelta:
        """Calculate duration of sleep for a given night.

        This function calculates sleep duration based on the requirements,
        including the length of sleep and the seasonal shift. This has no need
        to know about location since it is purely based on user preference.
        """
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
        variance = self.seasonal_variance.total_seconds()
        season_diff = timedelta(seconds=(variance * cos_curve))

        # round to minutes
        seconds = int((self.min_duration + season_diff).total_seconds())
        td = timedelta(minutes=seconds//60)
        return td


def alarms(location: location.Location,
           requirements: Requirements,
           night_start: date = date.today()) -> Tuple[datetime, datetime]:
    """Calculate going to bed, and waking up times.

    This function provides the time for waking up according to location and
    user requirements, and the calulcated time to go to sleep according to
    wake-up time and duration.
    """
    # get sleep duration
    tomorrow = date.today() + timedelta(days=1)
    sleep_duration = requirements.duration(tomorrow)

    # calculate getting up time
    sunrise, sunset = sun.sun_times(location, tomorrow)

    # What is the logic here?
    # if min and max rise times are defined return cos curve between the two
    # if neither, get_up is sunrise
    # if one or t'othergo for sunrise or max(/min) whichever is earlier(/later)
    if requirements.max_rise is None \
            and requirements.min_rise is None:
        get_up = sunrise

    elif requirements.max_rise is not None \
            and requirements.min_rise is not None:
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

        variance = ((requirements.max_rise.hour
                     - requirements.min_rise.hour)*60*60
                    + (requirements.max_rise.minute
                       - requirements.min_rise.minute)*60
                    )
        season_diff = timedelta(seconds=(variance * cos_curve))
        get_up = datetime.combine(tomorrow, requirements.min_rise) \
            + season_diff

    elif requirements.max_rise is None \
            and requirements.min_rise is not None:
        limit = utc.localize(datetime.combine(tomorrow, requirements.min_rise))
        if limit >= sunrise:
            get_up = limit
        else:
            get_up = sunrise

    elif requirements.max_rise is not None \
            and requirements.min_rise is None:
        limit = utc.localize(datetime.combine(tomorrow, requirements.max_rise))
        if limit <= sunrise:
            get_up = limit
        else:
            get_up = sunrise

    # floor to minutes
    discard = timedelta(seconds=get_up.second,
                        microseconds=get_up.microsecond)
    get_up -= discard

    # calculate bed time
    bed_time = get_up - sleep_duration

    return bed_time, get_up
