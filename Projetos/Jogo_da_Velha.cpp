#include <stdio.h>
#include <stdlib.h>

int FimDeJogo(char Resultado[0], char jogador[], char possibilidades[9]){

	system("cls");
	printf("|   %c   |   %c   |   %c   |\n", possibilidades[0], possibilidades[1], possibilidades[2] );    
    printf("-------------------------\n");
    printf("|   %c   |   %c   |   %c   |\n", possibilidades[3], possibilidades[4], possibilidades[5] );
    printf("-------------------------\n");
    printf("|   %c   |   %c   |   %c   |\n", possibilidades[6], possibilidades[7], possibilidades[8] );

    if (Resultado[0] == 'V') printf(" !! Fim do Jogo !! \n Vencedor: %s", jogador);
    else printf(" !! Fim do Jogo !! \n Não houveram vencedores");
	exit(0);
}

int verificador(char possibilidades[9], char jogador[]){
 	char Resultado[1] = {'F'};
 	
    //# Row winner #
    if ( ( ( possibilidades[0] == possibilidades[1] ) && ( possibilidades[1] == possibilidades[2] ) ) || ( ( possibilidades[3] == possibilidades[4] ) && ( possibilidades[4] == possibilidades[5] ) ) || ( ( possibilidades[6] == possibilidades[7] ) && ( possibilidades[7] == possibilidades[8] ) ) ){
		Resultado[0] = 'V';
		FimDeJogo(Resultado, jogador, possibilidades);
	}         
    //# Column winner #
    else if ( ( ( possibilidades[0] == possibilidades[3] ) && ( possibilidades[3] == possibilidades[6] ) ) || ( ( possibilidades[1] == possibilidades[4] ) && ( possibilidades[4] == possibilidades[7] ) ) || ( ( possibilidades[2] == possibilidades[5] ) && ( possibilidades[5] == possibilidades[8] ) ) ){ 
		Resultado[0] = 'V';
	    FimDeJogo(Resultado, jogador, possibilidades);
	}
    //# Diag winner #
    else if ( ( ( possibilidades[0] == possibilidades[4] ) && ( possibilidades[4] == possibilidades[8] ) ) || ( ( possibilidades[2] == possibilidades[4] ) && ( possibilidades[4] == possibilidades[6] ) ) ){
		Resultado[0] = 'V';
		FimDeJogo(Resultado, jogador, possibilidades);
	}         
	else
	{
	   	return 0 ;
	}

}
    	
int vsPlayer(){
	char nomeJogador1[15];
	char nomeJogador2[15];
	char possibilidades[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};	
	int contJogadas = 0;
	int jogadaEscolhida;

	system("cls");
    printf("Qual o nome do Jogador n 01 ( X ):\n");
    scanf("%s", &nomeJogador1);
    
	system("cls");
    printf("Qual o nome do Jogador n 02 ( O ):\n");
    scanf("%s", &nomeJogador2);	
        
    for (contJogadas = 0; contJogadas < 9; contJogadas++){
		system("cls");            
        printf("|   %c   |   %c   |   %c   |\n", possibilidades[0], possibilidades[1], possibilidades[2] );    
        printf("-------------------------\n");
        printf("|   %c   |   %c   |   %c   |\n", possibilidades[3], possibilidades[4], possibilidades[5] );
        printf("-------------------------\n");
        printf("|   %c   |   %c   |   %c   |\n", possibilidades[6], possibilidades[7], possibilidades[8] );

        if (contJogadas % 2 == 0){
        	printf("\n%s ( X ) escolha um dos numeros disponiveis acima: ", nomeJogador1);
			scanf("%d", &jogadaEscolhida);
            possibilidades[jogadaEscolhida-1] = 'X';
            verificador(possibilidades, nomeJogador1);
		}
        else{            
		   	printf("\n%s ( O ) escolha um dos numeros disponiveis acima: ", nomeJogador2);
			scanf("%d", &jogadaEscolhida);
            possibilidades[jogadaEscolhida-1] = 'O';
            verificador(possibilidades, nomeJogador2);
		}
	}
    return 0;
}
int vsIA(){
	system("cls");
    printf("vs I.A. are Coming Soon...");
	return 0;
}

int Instrucoes(){
	system("cls");
    printf("Instruções: Coming Soon...");
	return 0;
}
    
int main(){
	
	int selecaoMenu;
	    
	printf("#### Bem-vindo ao Jogo da Velha: ####\n");
    printf("|   1   |   2   |   3   |\n-------------------------\n|   4   |   5   |   6   |\n-------------------------\n|   7   |   8   |   9   |\n");
    printf("1. vs Player\n");
    printf("2. vs I.A.\n");
    printf("3. Como Jogar\n");

	scanf("%d", &selecaoMenu);
	switch(selecaoMenu){
		case 1:
			vsPlayer();
			break;
		case 2:
			vsIA();
			break;
		case 3:
			Instrucoes();
			break;
		default:
			return printf("Selecione um valor de 1 a 3");
			break;
	}
}