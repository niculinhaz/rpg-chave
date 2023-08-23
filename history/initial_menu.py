
# from emoji import emojize
from .set_char import save_char, set_char
from characters import Character

def menu():
    print("\t\t BEM VINDO!\n")
    print("\t Esse é o fantástico mundo da Oakley!\n")
    input("\tPressione Enter para continuar.")
    i = 0
    while i != 1:
        nome = input("Primeiro, me conte seu nome.\n")
        genero = input(f"Agora, {nome}, me diga, você é um garoto ou uma garota?\n")
        genero = genero.lower()
        idade = input("E quantos anos você tem?\n")
        conf = input(f"Então seu nome é {nome}, você tem {idade} anos e é um/uma {genero}? Responda com sim ou não.\n")
        conf == conf.lower()
        if conf == "sim":
            if genero == "garota":
                boneco = input("\nAgora, escolha a sua classe.\nGuerreira\nMaga\n")
                if boneco == "guerreira":
                    player = set_char("guerreiro", Character(nome, 1, 0, genero, 20, 5, 10, 15))
                    save_char(player)
                    print("Parabéns! Agora você é um guerreira e vai conquistar o mundo com sua espada... kkkk")
                    return player
                if boneco == "maga":
                    player = set_char("mago", Character(nome, 1, 0, genero, 20, 15, 5, 10))
                    save_char(player)
                    print("Parabéns! Agora você é uma mestra das artes místicas.. nerdkkkkk")
                    return player
            if genero == "garoto":
                boneco = input("\nAgora, escolha a sua classe.\nGuerreiro :crossed_swords:\nMago :fire:\n")    
                boneco = boneco.lower()
                if boneco == "guerreiro":
                    player = set_char("guerreiro", Character(nome, 1, 0, genero, 20, 5, 10, 15))
                    save_char(player)
                    print("Parabéns! Agora você é um guerreiro e vai conquistar o mundo com sua espada... kkkk")
                    return player
                if boneco == "mago":
                    player = set_char("mago", Character(nome, 1, 0, genero, 20, 15, 5, 10))
                    save_char(player)
                    print("Parabéns! Agora você é um mestre das artes místicas.. nerdkkkkk")
                    return player
        if conf == "nao" or conf == "não":
            print("Então vamos começar de novo.")
            continue
