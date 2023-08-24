"""

"""

import json


from characters import Character, Warrior, Wizard


def save_char(pick: Wizard | Warrior):
    """
    Saves the created character into the database.
    Args:
    :pick: The player character.
    """

    boneco = {
        "nome" : pick.name,
        "age" : pick.age,
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


def set_char(chosen_class: str, character: Character):
    """
    Set the player as the chosen class.
    args:
    :type(str): The chosen class.
    :character: The information about the character.
    """
    if chosen_class == "guerreiro":
        principal = Warrior(
            character.name,
            character.age,
            character.level,
            character.xp,
            character.gender,
            character.health,
            character.mana,
            character.strenght,
            character.defense
        )
    if chosen_class == "mago":
        principal = Wizard(
            character.name,
            character.age,
            character.level,
            character.xp,
            character.gender,
            character.health,
            character.mana,
            character.strenght,
            character.defense
        )
    
    return principal