from datetime import timedelta
from astronomical import sun
from astronomical.location import Location
from astronomical.sleep import Requirements, duration, alarms

print("""TheOrganist24: Astronomical
Library of utilities related to astronomical movements
""")

print("Sunrise/Sunset Times \
      \n====================")

home = Location("Ivybridge", -3.941355, 50.392189)
print(home)

sunrise, sunset = sun.sun_times(home)
print("""Sun times today in {}:
Sunrise today: {:%H:%M}
Sunset today: {:%H:%M}
""".format(home.name, sunrise, sunset))



print("Sleep Times \
      \n===========")

requirements = Requirements(duration=timedelta(hours=7),
                            min_rise=timedelta(hours=6),
                            max_rise=timedelta(hours=7))
print(requirements)

print("""Duration: {}
""".format(duration(requirements)))

print("""Alarms:
Got to bed: {}
Get up: {}
""".format(*alarms(home, requirements)))
