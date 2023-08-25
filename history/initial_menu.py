
# from emoji import emojize

from .create_player import create_player
from .load_player import load_player

def menu():
    """
    Initializes the game, and opens the menu.
    """
    print("\t\t BEM VINDO!\n")
    print("\tEsse é o fantástico mundo da Oakley!\n")
    input("\tPressione Enter para continuar.")
    player = load_player()
    if player is None:
        player = create_player()
        return player
    
    print(f"Jogador {player.name}, de nível {player.level} carregado!")
    input("Pressione enter para continuar.")
