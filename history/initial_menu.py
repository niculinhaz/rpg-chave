
# from emoji import emojize

from .create_player import create_player
from data import load_player

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
    
    if player.gender == "garoto":
        print(f"Jogador {player.name.capitalize()}, de nível {player.level}, carregado!")
        input("Pressione enter para continuar.")
    if player.gender == "garota":
        print(f"Jogadora {player.name.capitalize()}, de nível {player.level}, carregada!")
        input("Pressione enter para continuar.")
    if player.gender == "garote":
        print(f"Jogadore {player.name.capitalize()}, de nível {player.level}, carregade!")
        input("Pressione enter para continuar.")
