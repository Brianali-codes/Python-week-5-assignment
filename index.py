# Base class: Superhero
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self._origin = origin  # Encapsulated (private-like attribute)

    def introduce(self):
        print(f"I am {self.name} from {self._origin}, and I have the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def get_origin(self):
        return self._origin


# inheritance
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        # Polymorphism in action
        print(f"{self.name} soars through the sky at {self.flight_speed} mph using {self.power}!")
