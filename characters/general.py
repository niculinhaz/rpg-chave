"""
For general info about the characters.
"""
from dataclasses import dataclass



gender_dict = { # Relates gendered nouns to classes and races
    "garota": {
        "warrior": "guerreira",
        "mage": "maga",
        "master": "mestra",
        "human": "humana",
        "elf": "elfa"
    },

    "garoto": {
        "warrior": "guerreiro",
        "mage": "mago",
        "master": "mestre",
        "human": "humano",
        "elf": "elfo"
    },
    
    "garote": {
        "warrior": "guerreire",
        "mage": "mague",
        "master": "mestre",
        "human": "humane",
        "elf": "elfe"
    }
}



@dataclass
class Stats:
    max_health: int
    current_health: int
    max_mana: int
    current_mana: int
    max_strength: int
    current_strength: int
    max_defense: int
    current_defense: int


@dataclass
class Character:
    name: str
    age: int
    level: int
    xp: float
    gender: str
    stats: Stats
    char_class: str
    race: str

    def __init__(
            self, 
            name,
            age,
            level,
            xp,
            gender,
            stats,
            char_class,
            race
        ):
        self.name = name
        self.age = age
        self.level = level
        self.xp = xp
        self.gender = gender
        self.stats = stats
        self.char_class = char_class
        self.race = race
