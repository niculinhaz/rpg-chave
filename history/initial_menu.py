
# from emoji import emojize

from .create_player import create_player

def menu():
    """
    Initializes the game, and opens the menu.
    """
    print("\t\t BEM VINDO!\n")
    print("\tEsse é o fantástico mundo da Oakley!\n")
    input("\tPressione Enter para continuar.")
    player = create_player()
    return player