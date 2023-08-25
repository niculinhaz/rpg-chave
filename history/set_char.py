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
            "strength": pick.stats.strength,
            "defense": pick.stats.defense,
        },
        "class" : pick.char_class
    }

    json_object = json.dumps(boneco, indent= 4)
    with open("data/characters.json", "w", encoding= "UTF-8") as file:
        file.write(json_object)


def set_char(character: Character):
    """
    Set the player as the chosen class.
    args:
    :type(str): The chosen class.
    :character: The information about the character.
    """


    if character.char_class == "warrior":
        main_player = Warrior(
            character.name,
            character.age,
            character.level,
            character.xp,
            character.gender,
            Stats(
            character.stats.health,
            character.stats.mana,
            character.stats.strength,
            character.stats.defense
            ),
            character.char_class
        )
    if character.char_class == "mage":
        main_player = Wizard(
        character.name,
        character.age,
        character.level,
        character.xp,
        character.gender,
        Stats(
        character.stats.health,
        character.stats.mana,
        character.stats.strength,
        character.stats.defense
        ),
        character.char_class
    )
        
    return main_player