def FimDeJogo(Resultado, jogador):
    if Resultado == 'Vitoria': print(" !! Fim do Jogo !! \n Vencedor: %s" %jogador)
    else: print(" !! Fim do Jogo !! \n Não houveram vencedores")
    input()
    menu()

def verificador(possibilidades, jogador):
        
    # Row winner #
    if ( possibilidades[0] == possibilidades[1] ) and ( possibilidades[1] == possibilidades[2] ) or ( possibilidades[3] == possibilidades[4] ) and ( possibilidades[4] == possibilidades[5] ) or ( possibilidades[6] == possibilidades[7] ) and ( possibilidades[7] == possibilidades[8] ): 
        Resultado = "Vitoria"
        FimDeJogo(Resultado, jogador)
    # Column winner #
    elif ( possibilidades[0] == possibilidades[3] ) and ( possibilidades[3] == possibilidades[6] ) or ( possibilidades[1] == possibilidades[4] ) and ( possibilidades[4] == possibilidades[7] ) or ( possibilidades[2] == possibilidades[5] ) and ( possibilidades[5] == possibilidades[8] ): 
        Resultado = 'Vitoria'
        FimDeJogo(Resultado, jogador)
    # Diag winner #
    elif ( possibilidades[0] == possibilidades[4] ) and ( possibilidades[4] == possibilidades[8] ) or ( possibilidades[2] == possibilidades[4] ) and ( possibilidades[4] == possibilidades[6] ): 
        Resultado = "Vitoria"
        FimDeJogo(Resultado, jogador)
    else: pass

def vsPlayer():
    nomeJogador1 = input(print('Qual o nome do Jogador nº 01 ( X ):'))
    nomeJogador2 = input(print('Qual o nome do Jogador nº 02 ( O ):'))

    possibilidades = list(range(1,10,1))
    
    for contJogadas in range(0,9):
            
        print('|   %s   |   %s   |   %s   |' % ( possibilidades[0] , possibilidades[1] , possibilidades[2] ) )    
        print('-------------------------')
        print('|   %s   |   %s   |   %s   |' % ( possibilidades[3] , possibilidades[4] , possibilidades[5] ) )
        print('-------------------------')
        print('|   %s   |   %s   |   %s   |' % ( possibilidades[6] , possibilidades[7] , possibilidades[8] ) )

        if contJogadas % 2 == 0:
            jogadaEscolhida = int(input(print('\n%s ( X ) escolha um dos números disponíveis acima:' %nomeJogador1)))
            possibilidades[jogadaEscolhida-1] = 'X'
            verificador(possibilidades, nomeJogador1)
        else:            
            jogadaEscolhida = int(input(print('\n%s ( O ) escolha um dos números disponíveis acima:' %nomeJogador2)))
            possibilidades[jogadaEscolhida-1] = 'O'
            verificador(possibilidades, nomeJogador2)
    pass

def vsIA():
    print('vs I.A. are Coming Soon...')
    pass

def Instrucoes():
    print('Instruções: Coming Soon...')
    pass

def menu():
    print('#### Bem-vindo ao Jogo da Velha: ####\n')
    print('|   0   |   1   |   2   |\n-------------------------\n|   4   |   5   |   6   |\n-------------------------\n|   7   |   8   |   9   |\n')
    print('1. vs Player')
    print('2. vs I.A.')
    print('3. Como Jogar')

    selecaoMenu = int(input())

    if selecaoMenu not in range(1,4): return print('Selecione um valor de 1 a 3')
    elif selecaoMenu == 1: vsPlayer()
    elif selecaoMenu == 2: vsIA()
    else: Instrucoes()

menu()


    


