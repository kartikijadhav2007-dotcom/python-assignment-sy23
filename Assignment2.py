# Constants
EARTH = 9.8
MOON = 1.6

# Taking input from the user
mass = float(input("Enter mass of object (kg): "))

# Calculating weight
earth_weight = mass * EARTH
moon_weight = mass * MOON

# Displaying results
print("\nWeight on Earth =", earth_weight, "N")
print("Weight on Moon =", moon_weight, "N")

# Displaying details
print("\n--- Details ---")

print("Variable used: mass")
print("Data type of mass:", type(mass))

print("Data type of earth_weight:", type(earth_weight))
print("Data type of moon_weight:", type(moon_weight))

print("Constants used: EARTH, MOON")
print("Arithmetic operator used: *")