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
print("Orbittal force on the {} from the {} is {:.2e}N".format(
    earth.name,
    the_sun.name,
    the_sun.orbittal_force(earth.name)))
print("Orbittal period of the {} round the {} is {}s".format(
    earth.name,
    the_sun.name,
    int(the_sun.orbittal_period(earth.name))))

print("\nSunrise/Sunset Times \
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
