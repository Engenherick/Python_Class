from dealer import Dealer
from jogador import Jogador
from jogo import Jogo

def run():
    print("Bem vindo ao BlackJack21Game!")

    jogadorNick = input("Para iniciarmos, informe seu nome:")

    jogador = Jogador(jogadorNick)
    jogo = Jogo(jogador)

    if input("Boas vindas %s gostaria de entender como se joga?" %jogador.nick) == 'Y': jogo.instrucoes()
    else: jogo.iniciar()

    print("Deseja jogar novamente ", jogador.nick, "? opções: S / N")
    novamente = input()

    while novamente == 'S':
        jogo.iniciar()
        print("Deseja jogar novamente ", jogador.nick, "? opções: S / N")
        novamente = input()

if __name__ == '__main__':
    run()