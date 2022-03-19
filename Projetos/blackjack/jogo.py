import random
from time import time
from jogador import Jogador

from dealer import Dealer


class Jogo:
    def __init__(self, jogador:Jogador):
        self.baralhoValores = {'A': [1,11] , '2': 2, '3': 3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10 }
        self.baralhoCartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
        self.jogador = jogador
        self.dealer = Dealer()

        self.jogador.setBaralho(self.baralhoCartas)
        self.dealer.setBaralho(self.baralhoCartas)
        

    def instrucoes():
        pass

    def verificarGanhador(self):
        if self.dealer.pontuacao > 21: print(self.jogador.nick, " Wins!")
        elif self.jogador.pontuacao > 21: print("Dealer Wins!")
        elif self.jogador.pontuacao < self.dealer.pontuacao: print("Dealer Wins!")
        elif self.jogador.pontuacao > self.dealer.pontuacao: print(self.jogador.nick," Wins!")
        else: print("Empate!")

    def iniciar(self):
        self.__distribuirCartas()

        self.opcoes()
        
    def opcoes(self): 
        listaOpcao = { "M": "Manter" , "P": "Pedir" , "D": "Dobrar" }
        if self.jogador.temCartasRepetidas(): listaOpcao.update({"S": "Separar" })

        print("Mão do Dealer: ", self.dealer.mao[0], "( " , self.baralhoValores[ self.dealer.mao[0] ] , " )")
        print("Sua mão: ",self.jogador.mao, "( " , self.jogador.pontuacao	, " )")
        opcaoEscolhida = input(print("O que deseja fazer?", listaOpcao))
        if opcaoEscolhida in listaOpcao.keys():
            if opcaoEscolhida == 'M': 
                self.dealer.jogar()
                self.baralho = self.dealer.getBaralho()
            elif opcaoEscolhida == 'P': 
                self.jogador.pedir(self.dealer.pontuacao, self.dealer.mao)
                self.baralho = self.jogador.getBaralho()
                self.opcoes(self)
            elif opcaoEscolhida == 'D': 
                self.jogador.dobrar()
            elif opcaoEscolhida == 'S': 
                self.jogador.separar()
        else: print("po cara ai n")
        
        self.verificarGanhador()


    def __distribuirCartas(self):
        for i in range(0,4):
            cartaAtual = random.choice(self.baralhoCartas)
            self.baralhoCartas.remove(cartaAtual)
            if i % 2 == 0: self.jogador.adicionarCarta(cartaAtual)
            else: self.dealer.adicionarCarta(cartaAtual)
    
    def contarPontos(self):
        sumPontos = 0
        self.jogador.pontuacao = self.jogador.contarPontos(sumPontos)
        self.dealer.pontuacao = self.dealer.contarPontos(sumPontos)
        return self.jogador.pontuacao, self.dealer.pontuacao
