""" """

from . import Weapon

class MagicBook(Weapon):
    def __init__(self, name, type, range, durability, power):
        super().__init__(self, name, type, range, durability, power)

