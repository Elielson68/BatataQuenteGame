import random
print ("Bem-vindo ao jogo Quente ou Frio, para jogar basta 'chutar' um número, digitando um entre 1 a 20, a máquina sorteou aleatoriamente um número entre esses valores\ne sempre que o valor do seu chute se aproximar do valor que a máquina escolheu ela irá responder que está ficando mais quente\ne caso o valor comece a se distanciar do valor, ela irá responder que está ficando frio. Boa sorte, e desculpe pelo linguajar de nossa máquina.")
maquina = random.randrange(1,20)
jogador = 9999
tentativas = 0
while jogador != maquina:
    try:
        jogador = int(input("Chute: "))
        if (jogador < 0):
            print("\nMáquina: Meu amigo...Use números positivos, pode ser?")
            pass
        result = jogador - maquina
        if (jogador>=1) and (result < 0):
            result = result * (-1)
        #if (jogador - maquina < 0):
            #print("Conversão: ", jogador)
        if (result >= 5) and (result < 10):
            print("\nMáquina: Está ficando frio")
            tentativas += 1
        if (result >= 10) and (result < 15):
            print("\nMáquina: Está começando a congelar!")
            tentativas += 1
        if (result >= 15) and (result <= 20):
            print("\nMáquina: ESTAMOS NA ERA DO GELO, AMIGO!")
            tentativas += 1
        if (result == 4 ):
            print("\nMáquina: Está esquentando!")
            tentativas += 1
        if (result == 3 ):
            print("\nMáquina: Ta QUENTE!")
            tentativas += 1
        if (result == 2 ):
            print("\nMáquina: COMEÇOU A QUEIMAR!")
            tentativas += 1
        if (result == 1 ):
            print("\nMáquina: TA PEGANDO FOGO, BIXO!")
            tentativas += 1
        elif (int(jogador) == maquina) and (tentativas == int(0)):
            print("\nMaquina: Porra! de primeira? Namoral? Acordou com a bunda virada pra lua hoje hein")
            print("Quero ver fazer isso de novo, quer jogar novamente?\nDigite '1' para Sim.\nDigite '2' para Não.")
            resposta = input("Resposta: ")

            if (resposta == str(1)):
                print("____________Novo jogo____________\n")
                jogador = 9999
                maquina = random.randrange(1, 20)
                tentativas = 0
            elif (resposta == str(2)):
                print("____________FIM DE JOGO____________\n")
                jogador = maquina
        elif (int(jogador) == maquina):
            print("\nMáquina: Acertou, desgraçado. Tu errou " + str(tentativas) + " vezes até acertar essa porra.")
            print("Deseja jogar novamente?\nDigite '1' para Sim.\nDigite '2' para Não.")
            resposta = input("Resposta: ")

            if (resposta == str(1)):
                print("____________Novo jogo____________\n")
                jogador = 9999
                maquina = random.randrange(1, 20)
                tentativas = 0
            elif (resposta == str(2)):
                print("____________FIM DE JOGO____________\n")
                jogador = maquina
    except ValueError:
        print("\nMáquina: Opa! Isso não é um número inteiro. Digite um número válido.")




