"""
CP1404/CP5632 Practical
Unreliable car class
"""
import random

from car import Car

class UnreliableCar(Car):
    """Represents a unreliable car object"""

    def __init__(self, name, fuel, reliability):
        """Initialise a unreliable Car instance.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometre
        reliability: reliability of the car
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance, if allowed by reliability chance"""
        if random.randrange(0,101) < self.reliability:
            super().drive(distance)
        else:
            return 0
