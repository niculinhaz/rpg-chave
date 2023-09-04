
from characters import Stats
from characters.races import Race
import json

class Enemy:
    def __init__(self, race_in: str, stats_in: dict) -> None:
        race = Race(race_in)
        stats = Stats(
            stats_in["max_health"],
            stats_in["max_health"],
            stats_in["max_mana"],
            stats_in["max_mana"],
            stats_in["max_strength"],
            stats_in["max_strength"],
            stats_in["max_defense"],
            stats_in["max_defense"],
        )
        

def load_enemy(area: str, race: str) -> Enemy:
    try:
        with open("characters/enemies/enemies.json", "r") as file:
            json_enemies = json.load(file)
            try:
                stats = json_enemies[area][race]["stats"]
            except KeyError:
                print("A área ou o inimigo indicados não existem.")
                return None
            
            return Enemy(race, stats)
            
    except FileNotFoundError:
        print("O arquivo de inimigos não existe. Impossível prosseguir.")
        return None
