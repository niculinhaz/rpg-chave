"""
For defining wizards information.
"""

from characters import Character

class Wizard(Character):
    """
    Class for Wizard data.
    """



class WizardActions:
    """
    Class containing wizard possible actions.
    """

    def __init__(self):
        self.wizard = Wizard()
    

    def basic_attack(target: Character):
        target.health = target.health - self.wizard.strenght
        return target.health


    def magic_attack(target: Character):
        target.health = target.health - (self.wizard.level * self.wizard.strenght / 2)
        self.wizard.mana = self.wizard.mana - (0.6 * self.wizard.mana)
        return target.health
    
    def cure(target: Character):
        target.health = target.health + (target.health * 0.5)
        return target.health
