"""
For defining warriors information.
"""

from characters import Character

class Warrior(Character):
    """
    Class for Warrior data.
    """

    def __init__(self, name, age, level, xp, gender, stats, char_class):
        super().__init__(name, age, level, xp, gender, stats, char_class)



class WarriorActions:
    """
    Class containing warrior possible actions.
    """

    def __init__(self, warrior: Warrior):
        self.warrior = warrior    

    def light_attack(self, target: Character):
        target.health = target.health - self.warrior.stats.strenght
        return target.health


    def heavy_attack(self, target: Character):
        target.health = target.health - (self.warrior.level * self.warrior.stats.strenght / 2)
        self.warrior.mana = self.warrior.mana - (0.6 * self.warrior.mana)
        return target.health
    
    def defend(self, attack):
        self.warrior.health = attack - (self.warrior.stats.defense * 0.75)
        return self.warrior.health
