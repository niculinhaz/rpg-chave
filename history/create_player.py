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

    gendered_nouns = list(gender_dict[gender].values())
    ungendered_nouns = list(gender_dict[gender].keys())
    
    while True:
        player_race = input(f"Por favor, diga agora de que raça deseja ser.\n{gender_dict[gender]['human'].capitalize()}\n{gender_dict[gender]['elf'].capitalize()}\n")
        player_race = player_race.lower()

        if player_race not in gendered_nouns:
            print("Essa raça não existe!")
            continue
        else:
            break
    

    while True:
        player_class = input(f"\nAgora, escolha a sua classe.\n{gender_dict[gender]['warrior'].capitalize()}\n{gender_dict[gender]['mage'].capitalize()}\n")
        player_class = player_class.lower()

        if player_class not in gendered_nouns:
            print("Essa classe não existe!")
            continue
        else:
            break

    clean_class = ungendered_nouns[gendered_nouns.index(player_class)]
    clean_race = ungendered_nouns[gendered_nouns.index(player_race)]
    
    if clean_class == "mage":
        player = set_char(Character(name, age, 1, 0, gender, Stats(100, 20, 100, 15, 100, 5, 100, 15), clean_class, clean_race, weapon="sword"))
        save_char(player)
        print(f"Parabéns! Agora você é um(a) {gender_dict[gender]['master'].capitalize()} das artes místicas.. nerdkkkkk")
    elif clean_class == "warrior":
        player = set_char(Character(name, age, 1, 0, gender, Stats(100, 20, 100, 5, 100, 15, 100, 10), clean_class, clean_race, weapon="magic book"))
        save_char(player)
        print(f"Parabéns! Agora você é um(a) {gender_dict[gender]['warrior'].capitalize()} e vai conquistar o mundo com sua espada... kkkk")
    return player


def create_player():
    """
    Asks the player how their character is going to be.
    """
    while True:
        nome = input("Primeiro, me conte seu nome.\n")
        genderAccept = 0
        
        while(genderAccept == 0):
            genderInput = input(f"Agora, {nome}, me diga, qual o seu gênero?\n 1 - Garoto\n 2 - Garota\n 3 - Garote\n")
            match(genderInput):
                case '1':
                    genero = "garoto"
                    genderAccept = 1
                    break
                case '2':
                    genero = "garota"
                    genderAccept = 1
                    break
                case '3':
                    genero = "garote"
                    genderAccept = 1
                    break
                case _:
                    print("Selecione uma opção válida, por favor.")

        genero = genero.lower()
        AgeAccept = 0
        while(AgeAccept != 1):
            idade = input("E quantos anos você tem?\n")
            if not idade.isnumeric():
                print("Por favor, insira um valor numérico.")
                continue
            AgeAccept = 1
        resposta = input(f"Então seu nome é {nome}, você tem {idade} anos e é {genero}? Responda com sim ou não.\n")
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
