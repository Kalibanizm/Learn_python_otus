from abc import ABC

import exceptions


class Vehicle(ABC):

    weight = 2500
    started = False
    fuel = 100
    fuel_consumption = 1

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started == 0 and self.fuel > 0:
            self.started = 1
            return self.started
        else:
            raise exceptions.LowFuelError

    def move(self, journey):
        need_fuel = self.fuel_consumption * journey
        if self.fuel > need_fuel:
            self.fuel -= need_fuel
            return self.fuel
        else:
            raise exceptions.NotEnoughFuel
