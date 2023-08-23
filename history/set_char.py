"""

"""

import json


from characters import Character, Warrior, Wizard


def save_char(pick: Wizard | Warrior):
    boneco = {
        "nome" : pick.name,
        "gender" : pick.gender,
        "level" : pick.level,
        "xp" : pick.xp,
        "health" : pick.health,
        "strenght" : pick.strenght,
        "mana" : pick.mana,
        "defense" : pick.defense,
    }

    json_object = json.dumps(boneco, indent= 4)
    with open("data/characters.json", "w", encoding= "UTF-8") as file:
        file.write(json_object)


def set_char(type: str, ch: Character):
    """
    Set the player as the chosen class.
    """
    if type == "guerreiro":
        principal = Warrior(
            ch.name,
            ch.level,
            ch.xp,
            ch.gender,
            ch.health,
            ch.mana,
            ch.strenght,
            ch.defense
        )
    if type == "mago":
        principal = Wizard(
            ch.name,
            ch.level,
            ch.xp,
            ch.gender,
            ch.health,
            ch.mana,
            ch.strenght,
            ch.defense
        )
    
    return principal