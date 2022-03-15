from Python_Class.Projetos.blackjack.dealer import Dealer
from Python_Class.Projetos.blackjack.jogador import Jogador
from Python_Class.Projetos.blackjack.jogo import Jogo


print("Bem vindo ao BlackJack21Game!")

jogadorNick = input("Para iniciarmos, informe seu nome:")

jogador = Jogador(jogadorNick)
dealer = Dealer()
jogo = Jogo(jogador, dealer)

if input("Boas vindas %s gostaria de entender como se joga?" %jogador.nick) == 'Y': jogo.instrucoes()
else: jogo.iniciar()

print("Deseja jogar novamente ", jogador.nick, "? opções: S / N")
novamente = input()

while novamente == 'S':
    jogo.iniciar()
    print("Deseja jogar novamente ", jogador.nick, "? opções: S / N")
    novamente = input()