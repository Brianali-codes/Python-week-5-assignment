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
