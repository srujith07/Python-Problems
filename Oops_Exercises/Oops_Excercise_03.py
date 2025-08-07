# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Given:

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

obj_Bus = Bus("Volvo", 90,15)

print(obj_Bus.name, obj_Bus.max_speed, obj_Bus.mileage)
