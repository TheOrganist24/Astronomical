from astronomical import sun
from astronomical.location import Location

print("""TheOrganist24: Astronomical
Library of utilities related to astronomical movements
""")

home = Location("Ivybridge", -3.941355, 50.392189)

latitude = 50.392189
longitude = -3.941355

sunrise, sunset = sun.sun_times(*home.location)

print("""Sun times today in {}:
Sunrise today: {:%H:%M}
Sunset today: {:%H:%M}
""".format(home.name, sunrise, sunset))

