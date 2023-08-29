"""
Package containing information about the character creation.
"""

from characters import Character, Stats, gender_dict

from data import save_char, set_char

def define_class(name: str, age: int, gender: str):
    """
    Defines the class that the main character is going to be.
    
    Args:
    :name(str): The player's name.
    :age(int): The player's age.
    :gender(str): To talk to the player in the right gender.
    """
    
    while True:
        player_class = input(f"\nAgora, escolha a sua classe.\n{gender_dict[gender]['warrior'].capitalize()}\n{gender_dict[gender]['mage'].capitalize()}\n")
        player_class = player_class.lower()

        gendered_classes = list(gender_dict[gender].values())
        base_classes = list(gender_dict[gender].keys())

        if player_class in gendered_classes:

            clean_class = base_classes[gendered_classes.index(player_class)]

            player = set_char(Character(name, age, 1, 0, gender, Stats(20, 5, 10, 15), char_class=clean_class))
            save_char(player)
            if player.char_class == "mage":
                print(f"Parabéns! Agora você é um {gender_dict[gender]['mage'].capitalize()} das artes místicas.. nerdkkkkk")
            elif player.char_class == "warrior":
                print(f"Parabéns! Agora você é um {gender_dict[gender]['warrior'].capitalize()} e vai conquistar o mundo com sua espada... kkkk")
            return player
        else:
            print("Essa classe não existe!")


def create_player():
    """
    Asks the player how their character is going to be.
    """
    while True:
        nome = input("Primeiro, me conte seu nome.\n")
        genero = input(f"Agora, {nome}, me diga, você é um garoto ou uma garota?\n")
        genero = genero.lower()
        idade = int(input("E quantos anos você tem?\n"))
        resposta = input(f"Então seu nome é {nome}, você tem {idade} anos e é um/uma {genero}? Responda com sim ou não.\n")
        resposta = resposta.lower()
        if resposta == "sim":
            player = define_class(nome, idade, genero)
            return player
        elif resposta == "nao" or resposta == "não":
            print("Então vamos começar de novo.")
            continue
        else:
            print("Por favor, responda apenas com 'sim' ou 'não'!")
            continue
