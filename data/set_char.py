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
        "name" : pick.name,
        "age" : pick.age,
        "gender" : pick.gender,
        "level" : pick.level,
        "xp" : pick.xp,
        "stats" : {
            "max_health" : pick.stats.max_health,
            "health" : pick.stats.current_health,
            "max_mana" : pick.stats.max_mana,
            "mana" : pick.stats.current_mana,
            "max_strength" : pick.stats.max_strength,
            "strength": pick.stats.current_strength,
            "max_defense" : pick.stats.max_defense,
            "defense": pick.stats.current_defense,
        },
        "class" : pick.char_class,
        "race" : pick.race,
        "weapon" : pick.weapon
    }

    json_object = json.dumps(boneco, indent=4)
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
            character.stats.max_health,
            character.stats.current_health,
            character.stats.max_mana,
            character.stats.current_mana,
            character.stats.max_strength,
            character.stats.current_strength,
            character.stats.max_defense,
            character.stats.current_defense
            ),
            character.char_class,
            character.race,
            character.weapon
        )
    if character.char_class == "mage":
        main_player = Wizard(
            character.name,
            character.age,
            character.level,
            character.xp,
            character.gender,
            Stats(
            character.stats.max_health,
            character.stats.current_health,
            character.stats.max_mana,
            character.stats.current_mana,
            character.stats.max_strength,
            character.stats.current_strength,
            character.stats.max_defense,
            character.stats.current_defense
            ),
            character.char_class,
            character.race,
            character.weapon
        )
        
    return main_player