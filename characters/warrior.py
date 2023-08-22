"""
For defining warriors information.
"""

from characters import Character

class Warrior(Character):
    """
    Class for Warrior data.
    """



class WarriorActions:
    """
    Class containing warrior possible actions.
    """

    def __init__(self):
        self.warrior = Warrior()
    

    def light_attack(target: Character):
        target.health = target.health - self.warrior.strenght
        return target.health


    def heavy_attack(target: Character):
        target.health = target.health - (self.warrior.level * self.warrior.strenght / 2)
        self.warrior.mana = self.warrior.mana - (0.6 * self.wizard.mana)
        return target.health
    
    def defend(attack):
        self.warrior.health = attack - (self.warrior.defense * 0.75)
        return self.warrior.health

