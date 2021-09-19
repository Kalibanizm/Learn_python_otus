"""
создайте класс `Plane`, наследник `Vehicle`


from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, add_cargo):
        if self.max_cargo >= self.cargo + add_cargo:
            self.cargo += add_cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo_before = self.cargo
        self.cargo = 0
        return cargo_before
"""
from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):

    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, cargo, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if cargo + self.cargo > self.max_cargo:
            raise CargoOverload('There is cargo overload')
        self.cargo += cargo
        return f'The plane was loaded with {self.cargo}'

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo