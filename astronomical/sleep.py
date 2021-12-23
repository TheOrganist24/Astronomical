"""Utilities related to sleep."""

from datetime import timedelta, date


class Requirements:
    """User defined sleep requirements."""

    def __init__(self,
                 duration=timedelta(hours=8),
                 seasonal_variance=timedelta(hours=1),
                 min_rise=None,
                 max_rise=None,
                 schedule_from=date.today(),
                 schedule_till=date.today() + timedelta(days=7)):
        """Define all instance attributes here."""
        self.duration = duration
        self.seasonal_variance = seasonal_variance
        self.min_rise = min_rise
        self.max_rise = max_rise
        self.dates = []
        for day in range(int((schedule_till - schedule_from).days) + 1):
            self.dates.append(schedule_from + timedelta(days=day))

    def __repr__(self):
        """Procuce code to initialise this class."""
        return f"Requirments()"

    def __str__(self):
        """Generate summary of class with minimal inputs."""
        return f"""Requirements \
        \n- hours sleep: {self.duration} \
        \n- seasonal varience: {self.duration}
        """
