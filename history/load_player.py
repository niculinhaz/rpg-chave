"""

"""

import json

from characters import Warrior, Wizard

def setup_player(player_info: dict):
    """
    
    """

    data = player_info

    if data["class"] == "guerreiro":
        main_player = Warrior(
            data["name"],
            data["age"],
            data["level"],
            data["xp"],
            data["gender"],
            data["stats"],
            data["class"]
        )
        return main_player
    if data["class"] == "mago":
        main_player = Wizard(
            data["name"],
            data["age"],
            data["level"],
            data["xp"],
            data["gender"],
            data["stats"],
            data["class"]
        )
        return main_player

    return None

def load_player():
    """
    
    """

    with open("data/characters.json", "r", encoding="utf-8") as file:
        player_info = json.load(file)
        if player_info is None:
            return None
        
    setup_player(player_info)
    return player_info
