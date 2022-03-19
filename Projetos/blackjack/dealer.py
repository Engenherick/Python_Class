import random
import time


class Dealer:
    def __init__(self):
        self.name = "Agnaldo"
        self.pontuacao = 0
        self.mao = []

    def adicionarCarta(self, carta):
        self.mao.append(carta)
    
    def setBaralho(self, baralho):
        self.baralho = baralho

    def getBaralho(self):
        return self.baralho

    def jogar(self):
        print("Mão do Dealer: ", self.dealer.mao, "( " , self.dealer.pontuacao , " )")
        print("Sua mão: ", self.jogador.mao, "( " , self.jogador.pontuacao	, " )")
        time.sleep(1000)
        while self.dealer.pontuacao < 17 and self.jogador.pontuacao > self.dealer.pontuacao:
            cartaAtual = random.choice(self.baralhoCartas)
            self.baralhoCartas.remove(cartaAtual)
            self.dealer.adicionarCarta(cartaAtual)
            self.dealer.pontuacao = self.__contagemPontosDealer()
            print("Mão do Dealer: ", self.dealer.mao, "( " , self.dealer.pontuacao, " )")
            print("Sua mão: ", self.jogador.mao, "( " , self.jogador.pontuacao	, " )")
            time.sleep(1000)

        return self.baralho
    
    def contarPontos(self, sumPontos):
        for i in range(0,len(self.jogador.mao)):
            self.jogador.mao = sorted(self.jogador.mao)
            if 'A' in self.jogador.mao[i-1] and sumPontos > 10: sumPontos += int( self.baralhoValores[ self.jogador.mao[i-1] ][0] )
            elif 'A' in self.jogador.mao[i-1] and sumPontos <= 10: sumPontos += int( self.baralhoValores[ self.jogador.mao[i-1] ][1] )
            else: sumPontos += int( self.baralhoValores[ self.jogador.mao[i-1] ] )
        return sumPontos
    
        