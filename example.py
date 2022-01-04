from datetime import timedelta, time
from astronomical.globals import CelestialBody, earth
from astronomical import sun
from astronomical.location import Location
from astronomical.sleep import Requirements, alarms

print("""TheOrganist24: Astronomical
Library of utilities related to astronomical movements
""")

print("Heavenly Bodies \
      \n===============")
the_sun = CelestialBody("Sun", 1.989*10**30)
print(the_sun)

the_sun.add_daughters(earth, 147.1*10**9)
print("Orbital daughters of the {}:".format(the_sun.name))
for daughter, details in the_sun.daughters.items():
    print(f" - {details}")
print(f"Orbittal force on the {earth.name} " \
      f"from the {the_sun.name} " \
      f"is {the_sun.orbittal_force(earth.name):.2e}N")
print(f"Orbittal period of the {earth.name} " \
      f"round the {the_sun.name} " \
      f"is {int(the_sun.orbittal_period(earth.name))}s")

print("\nSunrise/Sunset Times \
      \n====================")

home = Location("Ivybridge", -3.9413, 50.3921)
print(home)

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
