"""
Unreliable Car, derived from Car
"""

from random import randint
from Prac_08.car import Car


class UnreliableCar(Car):
    """An unreliable car."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
