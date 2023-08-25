"""

"""

import json

from characters import Warrior, Wizard

def load_player():
    """
    
    """

    with open("data/characters.json", "r", "utf-8") as file:
        player_info = json.load(file)
    
    return player_info

def setup_player(player_info: dict):
    """
    
    """

    if player_info[
 