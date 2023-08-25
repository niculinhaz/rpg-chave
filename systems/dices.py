"""
Module containing the simulation of a dice system.
"""

import random

class Dice:
    """
    Class containing all the dices and their rolls.
    """
    def __init__(self):
        self.four_dice = [1,2,3,4]
        self.six_dice = [1,2,3,4,5,6]
        self.eight_dice = [1,2,3,4,5,6,7,8]
        self.twelve_dice = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.twenty_dice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        
    def roll_dice(self, dice: list[int]):
        """
        Simulates a dice roll.
        """
        face = random.choice(dice)
        return face
