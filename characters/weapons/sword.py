""" """

from . import Weapon

class Sword(Weapon):
    def __init__(self, name, type, durability, range, power):
        super().__init__(self, name, type, durability, range, power)

