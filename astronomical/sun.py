from suntime import Sun, SunTimeException

def sun_times(latitude, longitude):
    sun = Sun(latitude, longitude)
    sunrise = sun.get_sunrise_time()
    sunset = sun.get_sunset_time()
    return sunrise, sunset
