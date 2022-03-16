from operator import truediv
import random

baralhoValores = {'A': [1,11] , '2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 }

# F = Ficar // C = Comprar // D = Dobrar // S = Dividir

def instrucoes():
    pass

def contagemPontosJogador(mãoAtualJogador):

    global baralhoValores
    sumPontos = 0

    for i in range(1,len(mãoAtualJogador)+1):
        mãoAtualJogador = sorted(mãoAtualJogador)
        if 'A' == mãoAtualJogador[i-1] and sumPontos > 10: sumPontos += int( baralhoValores[ mãoAtualJogador[i-1] ][0] )
        elif 'A' == mãoAtualJogador[i-1] and sumPontos <= 10: sumPontos += int( baralhoValores[ mãoAtualJogador[i-1] ][1] )
        else: sumPontos += int( baralhoValores[ mãoAtualJogador[i-1] ] )
    return sumPontos

def contagemPontosDealer(mãoAtualDealer):

    global baralhoValores
    sumPontos = 0

    for i in range(1,len(mãoAtualDealer)+1):
        mãoAtualDealer = sorted(mãoAtualDealer)
        if 'A' == mãoAtualDealer[i-1] and sumPontos > 10: sumPontos += int( baralhoValores[ mãoAtualDealer[i-1] ][0] )
        elif 'A' == mãoAtualDealer[i-1] and sumPontos <= 10: sumPontos += int( baralhoValores[ mãoAtualDealer[i-1] ][1] )
        else: sumPontos += int( baralhoValores[ mãoAtualDealer[i-1] ] )
    return sumPontos

def manter(mãoAtualDealer, mãoAtualJogador, baralhoCartas):
    
    global foiSeparado

    if foiSeparado == False:
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

    else:
        pontuaçãoJogador = []
        pontuaçãoDealer = contagemPontosDealer(mãoAtualDealer)
        pontuaçãoJogador.append(contagemPontosJogador(mãoAtualJogador[0]))
        pontuaçãoJogador.append(contagemPontosJogador(mãoAtualJogador[1]))

        
        print("Mão do Dealer: ", mãoAtualDealer, "( " , pontuaçãoDealer , " )")
        print("Sua mão: ", mãoAtualJogador, "( " , pontuaçãoJogador	, " )")
        input()
        
        while pontuaçãoDealer < 17 and (pontuaçãoJogador[0] > pontuaçãoDealer or pontuaçãoJogador[1] > pontuaçãoDealer) :
            cartaAtual = random.choice(baralhoCartas)
            baralhoCartas.remove(cartaAtual)
            mãoAtualDealer.append(cartaAtual)
            pontuaçãoDealer = contagemPontosDealer(mãoAtualDealer)
            print("Mão do Dealer: ", mãoAtualDealer, "( " , pontuaçãoDealer, " )")
            print("Sua mão: ", mãoAtualJogador, "( " , pontuaçãoJogador	, " )")
            input()
            
        ganhador(pontuaçãoDealer, pontuaçãoJogador)


def pedir(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas):
    global foiSeparado
    global baralhoValores

    cartaAtual = random.choice(baralhoCartas)
    baralhoCartas.remove(cartaAtual)
    mãoAtualJogador.append(cartaAtual)
    pontuaçãoJogador = contagemPontosJogador(mãoAtualJogador)
    if pontuaçãoJogador > 21 and foiSeparado == False: 
        print("Mão do Dealer: ", mãoAtualDealer, "( " , pontuaçãoDealer , " )")
        print("Sua mão: ", mãoAtualJogador, "( " , pontuaçãoJogador	, " )")
        ganhador(pontuaçãoDealer, pontuaçãoJogador)
    elif pontuaçãoJogador > 21 and foiSeparado == True:
        print("Mão do Dealer: ", mãoAtualDealer, "( " , pontuaçãoDealer , " )")
        print("Sua mão: ", mãoAtualJogador, "( " , pontuaçãoJogador	, " ) -> EXPLODIU")
        return
    else: opcoes(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas)

def dobrar():
    print("Dobrar")
    pass

def separar(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas):
    mãoAtualJogador = [ [ mãoAtualJogador[0] ] , [ mãoAtualJogador[1] ]  ]
    pontuaçãoJogador = []

    for i in range(0,2):
        cartaAtual = random.choice(baralhoCartas)
        baralhoCartas.remove(cartaAtual)
        mãoAtualJogador[i].append(cartaAtual)
        pontuaçãoJogador.append(contagemPontosJogador(mãoAtualJogador[i]))
    
    print("Sua mão: ", mãoAtualJogador, "( " , pontuaçãoJogador	, " )")
    print("_"*128)
    opcoes(pontuaçãoDealer, pontuaçãoJogador[0], mãoAtualDealer, mãoAtualJogador[0], baralhoCartas)
    opcoes(pontuaçãoDealer, pontuaçãoJogador[1], mãoAtualDealer, mãoAtualJogador[1], baralhoCartas)
    manter(mãoAtualDealer, mãoAtualJogador ,baralhoCartas)
    
def ganhador(pontuaçãoDealer, pontuaçãoJogador):
    global foiSeparado
    global jogadorNick

    if foiSeparado == False:
        if pontuaçãoDealer > 21: print(jogadorNick, " Wins!")
        elif pontuaçãoJogador > 21: print("Dealer Wins!")
        elif pontuaçãoJogador < pontuaçãoDealer: print("Dealer Wins!")
        elif pontuaçãoJogador > pontuaçãoDealer: print(jogadorNick," Wins!")
        else: print("Empate!")

    else:
        for i in range(0,2):
            if pontuaçãoJogador[i] > 21: print("Dealer Wins!")
            elif pontuaçãoDealer > 21: print(jogadorNick, " Wins!")
            elif pontuaçãoJogador[i] < pontuaçãoDealer: print("Dealer Wins!")
            elif pontuaçãoJogador[i] > pontuaçãoDealer: print(jogadorNick," Wins!")
            else: print("Empate!")

def opcoes(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas):    
    global baralhoValores
    global foiSeparado
    listaOpcao = { "M": "Manter" , "P": "Pedir" , "D": "Dobrar" }
    if mãoAtualJogador[0] == mãoAtualJogador[1]: listaOpcao = { "M": "Manter" , "P": "Pedir" , "D": "Dobrar", "S": "Separar" }
    
    print("Mão do Dealer: ", mãoAtualDealer[0], "( " , baralhoValores[ mãoAtualDealer[0] ] , " )")
    print("Sua mão: ", mãoAtualJogador, "( " , pontuaçãoJogador	, " )")
    opcaoEscolhida = input(print("O que deseja fazer?", listaOpcao))
    if opcaoEscolhida in listaOpcao.keys():
        if opcaoEscolhida == 'M' and foiSeparado == False: manter(mãoAtualDealer, mãoAtualJogador ,baralhoCartas)
        elif opcaoEscolhida == 'P': 
            pedir(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas)
            return
        elif opcaoEscolhida == 'D': dobrar()
        elif opcaoEscolhida == 'S': 
            foiSeparado = True
            separar(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas)
        else: return 0
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

    if pontuaçãoJogador < 21: opcoes(pontuaçãoDealer, pontuaçãoJogador, mãoAtualDealer, mãoAtualJogador, baralhoCartas)
    else: manter(mãoAtualDealer, mãoAtualJogador, baralhoCartas)

print("Bem vindo ao BlackJack21Game!")
jogadorNick = input("Para iniciarmos, informe seu nome:")
novamente = "S"

if input("Boas vindas %s gostaria de entender como se joga?" %jogadorNick) == 'Y': instrucoes()

while novamente == 'S':
    foiSeparado = False
    primeiraRodada()    
    print("Deseja jogar novamente ", jogadorNick, "? opções: S / N")
    novamente = input()