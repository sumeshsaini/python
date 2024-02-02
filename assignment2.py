def calculate(mass, velocity):
    momentum = mass * velocity**2
    return momentum
mass = float(input("Enter the mass of the object in kilograms : "))
velocity = float(input("Enter the velocity of the object in meters per second : "))
momentum = calculate(mass, velocity)
print(f"The momentum of the object is: {momentum} kgm/s")
