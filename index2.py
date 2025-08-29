# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving...")

# Subclasses with different behaviors
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")
