"""

"""

import json

from characters import Character

def load_player():
    """
    
    """

    with open("data/characters.json", "r", "utf-8") as file:
        player_info = json.load(file)
    
    return player_info
 