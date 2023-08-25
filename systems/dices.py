"""
Module containing the simulation of a dice system.
"""

import random

class Dice:
    """
    Class containing all the dices and their rolls.
    """
    def __init__(self, faces):
        self.faces = faces
        
    def roll_dice(self):
        """
        Simulates a dice roll.
        """
        return random.randint(1, self.faces)
