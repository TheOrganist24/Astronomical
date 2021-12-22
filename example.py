from astronomical import sun

latitude = 50.392189
longitude = -3.941355

sunrise, sunset = sun.sun_times(latitude, longitude)

print("Sunrise today: {:%H:%M}\nSunset today: {:%H:%M}".format(sunrise, sunset))



