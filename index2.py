class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        # Polymorphism in action
        print(f"{self.name} soars through the sky at {self.flight_speed} mph using {self.power}!")
