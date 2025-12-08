print("The following questions will be used to determine the weight of a hypothetical object on a chosen planet in the solar system.")

# We use the weight of the object on Earth to determine the weight on other planets using the ratio of the strength of gravity between the two.

earth_weight_pounds = input("How much does your object weigh on Earth in pounds? ")
if earth_weight_pounds == "?":
    earth_weight_kilos = float(input("How much does your object weigh in kg? "))
    earth_weight_pounds = float(earth_weight_kilos) * 2.2
earth_weight_kilos = float(earth_weight_pounds) / 2.2

astronomical_body = input("What astronomical body is the object on? ")

# We measure the force of gravity by m/s^2.

gravity = 0.0

if astronomical_body in ("the sun", "The sun", "The Sun", "the Sun", "sun", "Sun"):
    astronomical_body = "the Sun"
    gravity = 274

elif astronomical_body in ("Mercury", "mercury"):
    astronomical_body = "Mercury"
    gravity = 3.7

elif astronomical_body in ("Venus", "venus"):
    astronomical_body = "Venus"
    gravity = 8.9

elif astronomical_body in ("Earth", "earth"):
    astronomical_body = "Earth"
    gravity = 9.81

elif astronomical_body in ("the moon", "The moon", "The Moon", "the Moon", "moon", "Moon"):
    astronomical_body = "the Moon"
    gravity = 1.62

elif astronomical_body in ("Mars", "mars"):
    astronomical_body = "Mars"
    gravity = 3.7

elif astronomical_body in ("Jupiter", "jupiter"):
    astronomical_body = "Jupiter"
    gravity = 24.79

elif astronomical_body in ("Saturn", "saturn"):
    astronomical_body = "Saturn"
    gravity = 10.44

elif astronomical_body in ("Uranus", "uranus"):
    astronomical_body = "Uranus"
    gravity = 8.69

elif astronomical_body in ("Neptune", "neptune"):
    astronomical_body = "Neptune"
    gravity = 11.15

elif astronomical_body in ("Pluto", "pluto"):
    astronomical_body = "Pluto"
    gravity = 0.62

else:
    print("Astronomical body not recognized.")

weight_on_planet_kilos = float(earth_weight_kilos) * (gravity / 9.81)
weight_on_planet_lb = weight_on_planet_kilos * 2.2

print("Your object weighs " + str(round(weight_on_planet_kilos, 4)) +
      " kilograms and " + str(round(weight_on_planet_lb, 4)) + " pounds on " + astronomical_body)
