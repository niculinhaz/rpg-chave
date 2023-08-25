"""
For defining wizards information.
"""

from characters import Character

class Wizard(Character):
    """
    Class for Wizard data.
    """

    def __init__(self, name, age, level, xp, gender, stats, char_class):
        super().__init__(name, age, level, xp, gender, stats, char_class)


class WizardActions:
    """
    Class containing wizard possible actions.
    """

    def __init__(self):
        self.wizard = Wizard
    

    def basic_attack(self, target: Character):
        target.health = target.health - self.wizard.stats.strenght
        return target.health


    def magic_attack(self, target: Character):
        target.health = target.health - (self.wizard.level * self.wizard.stats.strenght / 2)
        self.wizard.mana = self.wizard.stats.mana - (0.6 * self.wizard.stats.mana)
        return target.health
    
    def cure(self, target: Character):
        target.health = target.health + (target.health * 0.5)
        return target.health
