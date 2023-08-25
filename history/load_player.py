"""

"""

import json

from characters import Warrior, Wizard

def setup_player(player_info: dict):
    """
    
    """

    data = player_info

    if data["class"] == "Guerreiro":
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
    if data["class"] == "Mago":
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
        try:
            player_info = json.load(file)
        
            player_info = setup_player(player_info)
            return player_info

        except json.decoder.JSONDecodeError:
            return None