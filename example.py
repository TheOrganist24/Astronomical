from datetime import timedelta, time
from astronomical.globals import CelestialBody, earth
from astronomical import sun
from astronomical.location import Location
from astronomical.sleep import Requirements, alarms

print("""TheOrganist24: Astronomical
Library of utilities related to astronomical movements
""")

home = Location("Ivybridge", -3.9413, 50.3921)
print(home)

print("Heavenly Bodies \
      \n===============")
the_sun = CelestialBody("Sun", 1.9885*10**30)
print(the_sun)

the_sun.add_daughters(earth, 149.598*10**9)
print("Orbital daughters of the {}:".format(the_sun.name))
for daughter, details in the_sun.daughters.items():
    print(f" - {details}")
print(f"Current orbittal declination for {earth.name} " \
      f"is {the_sun.declination(earth.name):.2f} degrees")
print(f"Current elevation to {the_sun.name} from {earth.name} " \
      f"is {the_sun.elevation(earth.name, home):.2f} degrees")

print("\nSunrise/Sunset Times \
       \n====================")

sunrise, sunset = sun.sun_times(home)
print(f"Sun times today in {home.name}: \n" \
      f"Sunrise today: {sunrise:%H:%M} \n" \
      f"Sunset today: {sunset:%H:%M} \n")


print("Sleep Times \
      \n===========")

requirements = Requirements(min_duration=timedelta(hours=7),
                            min_rise=time(hour=6),
                            max_rise=time(hour=7))
print(requirements)

print(f"Duration: {requirements.duration()}")

print("""Alarms:
Got to bed: {:%H:%M}
Get up: {:%H:%M}
""".format(*alarms(home, requirements)))
