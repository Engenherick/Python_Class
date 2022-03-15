from Python_Class.Projetos.blackjack.dealer import Dealer
from Python_Class.Projetos.blackjack.jogador import Jogador
from Python_Class.Projetos.blackjack.jogo import Jogo


jogador = Jogador("Jogador")
dealer = Dealer("Dealer")
jogo = Jogo(jogador, dealer)
