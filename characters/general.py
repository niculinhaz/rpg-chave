"""
For general info about the characters.
"""
from dataclasses import dataclass



gender_dict = { # Relates gendered nouns to classes
    "garota": {
        "warrior": "guerreira",
        "mage": "maga",
        "master": "mestra"
    },

    "garoto": {
        "warrior": "guerreiro",
        "mage": "mago",
        "master": "mestre"
    }
}



@dataclass
class Stats:
    health: int
    mana: int
    strength: int
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

    def __init__(
            self, 
            name,
            age,
            level,
            xp,
            gender,
            stats,
            char_class
        ):
        self.name = name
        self.age = age
        self.level = level
        self.xp = xp
        self.gender = gender
        self.stats = stats
        self.char_class = char_class
