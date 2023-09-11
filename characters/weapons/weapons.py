"""
Module containing weapons basic information.
"""

from dataclasses import dataclass

weapon_types = ["dagger", "bow", "stick", "club", "sword", "spear", "magic book", "axe"]
weapon_range = ["short", "medium", "long"]


@dataclass
class Weapon:
    name: str
    type: weapon_types
    range: weapon_range
    durability: int
    power: int
