"""
For general info about the characters.
"""
from dataclasses import dataclass



@dataclass
class Stats:
    health: int
    mana: int
    strenght: int
    defense: int


@dataclass
class Character:
    name: str
    age: int
    level: int
    xp: float
    gender: str
    stats: Stats
    char_class: str
