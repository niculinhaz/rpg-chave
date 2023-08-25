"""

"""

import json


from characters import Character, Stats, Warrior, Wizard


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
        "stats" : {
            "health" : pick.stats.health,
            "mana" : pick.stats.mana,
            "strenght": pick.stats.strenght,
            "defense": pick.stats.defense,
        },
        "class" : pick.char_class
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
        main_player = Warrior(
            character.name,
            character.age,
            character.level,
            character.xp,
            character.gender,
            Stats(
            character.stats.health,
            character.stats.mana,
            character.stats.strenght,
            character.stats.defense
            ),
            character.char_class
        )
    if chosen_class == "mago":
        main_player = Wizard(
        character.name,
        character.age,
        character.level,
        character.xp,
        character.gender,
        Stats(
        character.stats.health,
        character.stats.mana,
        character.stats.strenght,
        character.stats.defense
        ),
        character.char_class
    )
        
    return main_player