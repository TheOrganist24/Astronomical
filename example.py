from datetime import timedelta, time
from astronomical.globals import CelestialBody, earth
from astronomical import sun
from astronomical.location import Location
from astronomical.sleep import Requirements, alarms

print("""TheOrganist24: Astronomical
Library of utilities related to astronomical movements
""")

print("Heavenly Bodies \
      \n================")
print(str(earth) + "\n")

print("Sunrise/Sunset Times \
      \n====================")

home = Location("Ivybridge", -3.9413, 50.3921)
print(home)

sunrise, sunset = sun.sun_times(home)
print("""Sun times today in {}:
Sunrise today: {:%H:%M}
Sunset today: {:%H:%M}
""".format(home.name, sunrise, sunset))



print("Sleep Times \
      \n===========")

requirements = Requirements(min_duration=timedelta(hours=7),
                            min_rise=time(hour=6),
                            max_rise=time(hour=7))
print(requirements)

print("""Duration: {}
""".format(requirements.duration()))

print("""Alarms:
Got to bed: {:%H:%M}
Get up: {:%H:%M}
""".format(*alarms(home, requirements)))
