"""
Package containing information about the character creation.
"""
from emoji import emojize

from characters import Character

from .set_char import save_char, set_char

def define_class(name: str, age: int, gender: str):
    """
    Defines the class that the main character is going to be.
    
    Args:
    :name(str): The player's name.
    :age(int): The player's age.
    :gender(str): To talk to the player in the right gender.
    """
    if gender == "garota":
        player_class = input(emojize("\nAgora, escolha a sua classe.\nGuerreira :crossed_swords:\nMaga :fire:\n"))
        if player_class == "guerreira":
            player = set_char("guerreiro", Character(name, age, 1, 0, "F", 20, 5, 10, 15))
            save_char(player)
            print("Parabéns! Agora você é um guerreira e vai conquistar o mundo com sua espada... kkkk")
            return player
        if player_class == "maga":
            player = set_char("mago", Character(name, age, 1, 0, "F", 20, 15, 5, 10))
            save_char(player)
            print("Parabéns! Agora você é uma mestra das artes místicas.. nerdkkkkk")
            return player
    if gender == "garoto":
        player_class = input(emojize("\nAgora, escolha a sua classe.\nGuerreiro :crossed_swords:\nMago :fire:\n"))    
        player_class = player_class.lower()
        if player_class == "guerreiro":
            player = set_char("guerreiro", Character(name, age, 1, 0, "M", 20, 5, 10, 15))
            save_char(player)
            print("Parabéns! Agora você é um guerreiro e vai conquistar o mundo com sua espada... kkkk")
            return player
        if player_class == "mago":
            player = set_char("mago", Character(name, age, 1, 0, "M", 20, 15, 5, 10))
            save_char(player)
            print("Parabéns! Agora você é um mestre das artes místicas.. nerdkkkkk")
            return player

def create_player():
    """
    Asks the player how their character is going to be.
    """
    loop_control = True
    resposta = ""
    while loop_control:
        nome = input("Primeiro, me conte seu nome.\n")
        genero = input(f"Agora, {nome}, me diga, você é um garoto ou uma garota?\n")
        genero = genero.lower()
        idade = int(input("E quantos anos você tem?\n"))
        resposta = input(f"Então seu nome é {nome}, você tem {idade} anos e é um/uma {genero}? Responda com sim ou não.\n")
        resposta = resposta.lower()
        if resposta == "sim":
            player = define_class(nome, idade, genero)
            loop_control = False
            return player
        if resposta == "nao" or resposta == "não":
            print("Então vamos começar de novo.")
            continue
