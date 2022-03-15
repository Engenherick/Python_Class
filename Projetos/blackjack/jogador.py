import random

class Jogador:
    def __init__(self, nick):
        self.nick = nick
        self.pontuacao = 0
        self.mao = []

    def setBaralho(self, baralho):
        self.baralho = baralho

    def getBaralho(self):
        return self.baralho

    def adicionarCarta(self, carta):
        self.mao.append(carta)
    
    def manter(self):
        pass

    def pedir(self, pontuaçãoDealer, maoAtualDealer):
        cartaAtual = random.choice(self.baralhoCartas)
        self.baralhoCartas.remove(cartaAtual)
        self.adicionarCarta(cartaAtual)
        self.pontuacao = self.contarPontos(self.mao)

    def contarPontos(self, sumPontos):
        for i in range(0,len(self.jogador.mao)):
            self.jogador.mao = sorted(self.jogador.mao)
            if 'A' in self.jogador.mao[i-1] and sumPontos > 10: sumPontos += int( self.baralhoValores[ self.jogador.mao[i-1] ][0] )
            elif 'A' in self.jogador.mao[i-1] and sumPontos <= 10: sumPontos += int( self.baralhoValores[ self.jogador.mao[i-1] ][1] )
            else: sumPontos += int( self.baralhoValores[ self.jogador.mao[i-1] ] )
        return sumPontos

    def dobrar(self):
        print("Dobrar")
        pass

    def separar(self):
        print("Separar")
        pass

    def temCartasRepetidas(self):
        self.mao[0] == self.mao[1]