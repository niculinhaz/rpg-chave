
def menu():
    print("\t\t BEM VINDO!\n")
    print("\t Esse é o fantástico mundo da Oakley!\n")
    input("\tPressione Enter para continuar.")
    print("\n\nPrimeiro, escolha a categoria de seu personagem.")
    boneco = input("\nGuerreiro (espadinha fiun)\nMago (uuu fogo)\n")
    boneco = boneco.lower()
    if(boneco == "guerreiro"):
        print("Parabéns! Agora você é um guerreiro muito forte!")
    if(boneco == "mago"):
        print("Parabéns! Agora você é um mestre das artes místicas..")
        print("doutor esquisito kkkklklkklkllklk")