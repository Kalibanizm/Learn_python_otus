"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle

from homework_02 import exceptions


class Plane(Vehicle):
    cargo = 0
    max_cargo = 750

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, loaded_cargo):
        new_cargo = self.cargo + loaded_cargo
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before
