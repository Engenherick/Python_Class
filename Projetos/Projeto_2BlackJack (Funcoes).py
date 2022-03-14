import random

baralhoValores = {'A': [1,10] , '2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 }

# F = Ficar // C = Comprar // D = Dobrar // S = Dividir

def instrucoes():
    pass

def contagemPontosJogador(mãoAtualJogador):

    global baralhoValores
    sumPontos = 0

    for i in range(0,len(mãoAtualJogador)):
        mãoAtualJogador = sorted(mãoAtualJogador)
        if 'A' in mãoAtualJogador[i-1] and sumPontos > 10: sumPontos += int( baralhoValores[ mãoAtualJogador[i-1] ][0] )
        elif 'A' in mãoAtualJogador[i-1] and sumPontos <= 10: sumPontos += int( baralhoValores[ mãoAtualJogador[i-1] ][1] )
        else: sumPontos += int( baralhoValores[ mãoAtualJogador[i-1] ] )
    return sumPontos

def contagemPontosDealer(mãoAtualDealer):

    global baralhoValores

    sumPontos = 0

    for i in range(0,len(mãoAtualDealer)):
        mãoAtualDealer = sorted(mãoAtualDealer)
        if 'A' in mãoAtualDealer[i-1] and sumPontos > 10: sumPontos += int( baralhoValores[ mãoAtualDealer[i-1] ][0] )
        elif 'A' in mãoAtualDealer[i-1] and sumPontos <= 10: sumPontos += int( baralhoValores[ mãoAtualDealer[i-1] ][1] )
        else: sumPontos += int( baralhoValores[ mãoAtualDealer[i-1] ] )
    return sumPontos

def manter(mãoAtualDealer, mãoAtualJogador, baralhoCartas):
    
    pontuaçãoDealer = contagemPontosDealer(mãoAtualDealer)
    pontuaçãoJogador = contagemPontosJogador(mãoAtualJogador)
    
    print("Mão do Dealer: ", mãoAtualDealer, "( " , pontuaçãoDealer , " )")
    print("Sua mão: ", mãoAtualJogador, "( " , pontuaçãoJogador	, " )")
    input()

    while pontuaçãoDealer < 17 and pontuaçãoJogador > pontuaçãoDealer:
        cartaAtual = random.choice(baralhoCartas)
        baralhoCartas.remove(cartaAtual)
        mãoAtualDealer.append(cartaAtual)
        pontuaçãoDealer = contagemPontosDealer(mãoAtualDealer)
        print("Mão do Dealer: ", mãoAtualDealer, "( " , pontuaçãoDealer, " )")
        print("Sua mão: ", mãoAtualJogador, "( " , pontuaçãoJogador	, " )")
        input()
        
    ganhador(pontuaçãoDealer, pontuaçãoJogador)
    pass

def pedir(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas):

    global baralhoValores

    cartaAtual = random.choice(baralhoCartas)
    baralhoCartas.remove(cartaAtual)
    mãoAtualJogador.append(cartaAtual)
    pontuaçãoJogador = contagemPontosDealer(mãoAtualJogador)
    if pontuaçãoJogador > 21: 
        print("Mão do Dealer: ", mãoAtualDealer, "( " , pontuaçãoDealer , " )")
        print("Sua mão: ", mãoAtualJogador, "( " , pontuaçãoJogador	, " )")
        ganhador(pontuaçãoDealer, pontuaçãoJogador)
    else: opcoes(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas)

def dobrar():
    print("Dobrar")
    pass

def separar():
    print("Separar")
    pass

def ganhador(pontuaçãoDealer, pontuaçãoJogador):

    global jogadorNick
    if pontuaçãoDealer > 21: print(jogadorNick, " Wins!")
    elif pontuaçãoJogador > 21: print("Dealer Wins!")
    elif pontuaçãoJogador < pontuaçãoDealer: print("Dealer Wins!")
    elif pontuaçãoJogador > pontuaçãoDealer: print(jogadorNick," Wins!")
    else: print("Empate!")

def opcoes(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas):
    
    global baralhoValores

    listaOpcao = { "M": "Manter" , "P": "Pedir" , "D": "Dobrar" }

    if mãoAtualJogador[0] == mãoAtualJogador[1]: listaOpcao = { "M": "Manter" , "P": "Pedir" , "D": "Dobrar", "S": "Separar" }

    print("Mão do Dealer: ", mãoAtualDealer[0], "( " , baralhoValores[ mãoAtualDealer[0] ] , " )")
    print("Sua mão: ", mãoAtualJogador, "( " , pontuaçãoJogador	, " )")
    opcaoEscolhida = input(print("O que deseja fazer?", listaOpcao))
    if opcaoEscolhida in listaOpcao.keys():
        if opcaoEscolhida == 'M': manter(mãoAtualDealer, mãoAtualJogador ,baralhoCartas)
        elif opcaoEscolhida == 'P': pedir(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas)
        elif opcaoEscolhida == 'D': dobrar()
        elif opcaoEscolhida == 'S': separar()
    else: print("po cara ai n")

    return 0

def primeiraRodada():
    pontuaçãoDealer = 0
    pontuaçãoJogador = 0

    mãoAtualJogador = []
    mãoAtualDealer = []
    baralhoCartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    
    for i in range(0,4):
        cartaAtual = random.choice(baralhoCartas)
        baralhoCartas.remove(cartaAtual)
        if i % 2 == 0: mãoAtualJogador.append(cartaAtual)
        else: mãoAtualDealer.append(cartaAtual)

    pontuaçãoJogador = contagemPontosJogador(mãoAtualJogador)
    pontuaçãoDealer = contagemPontosDealer(mãoAtualDealer)

    opcoes(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas)

    return 0

print("Bem vindo ao BlackJack21Game!")
jogadorNick = input("Para iniciarmos, informe seu nome:")

if input("Boas vindas %s gostaria de entender como se joga?" %jogadorNick) == 'Y': instrucoes()
else: primeiraRodada()

print("Deseja jogar novamente ", jogadorNick, "? opções: S / N")
novamente = input()

while novamente == 'S':
    primeiraRodada()
    print("Deseja jogar novamente ", jogadorNick, "? opções: S / N")
    novamente = input()