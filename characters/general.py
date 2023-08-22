"""
For general info about the characters.
"""

from dataclasses import dataclass

@dataclass
class Character:
    name: str
    level: int
    xp: float
    gender: int
    health: int
    mana: int
    strenght: int
    defense: int
    