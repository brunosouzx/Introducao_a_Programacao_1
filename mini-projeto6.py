import string

import numpy as np


def menu():
    print('Menu:')
    print('1. Definir Jogador X')
    print('2. Definir Jogador O')
    print('3. Definir tamanho do tabuleiro')
    print('4. Definir tamanho da sequência')
    print('5. Mostrar Placar')
    print('6. Iniciar novo jogo')
    print('7. Sair do jogo')
    opcao = int(input('Ecolha uma opcão: '))

    return opcao


def iniciar_novo_jogo(jogador_x='Jogador X',
                      jogador_o='Jogador O',
                      tamanho_matriz=3,
                      tamanho_sequencia=3
                      ):
    tabuleiro = np.full((tamanho_matriz, tamanho_matriz), '   ', dtype='<U3')

    imprimir_matriz(tabuleiro, tamanho_matriz)

    vencedor = False

    # while not vencedor:
    #     pass


def imprimir_matriz(tabuleiro, tamanho_matriz):
    cabecalho_numerico = "   " + \
        " | ".join([str(i) for i in range(tamanho_matriz)]
                   )
    print(cabecalho_numerico)

    linha_divisoria = "  +" + "---+" * tamanho_matriz
    print(linha_divisoria)

    for i, linha in enumerate(tabuleiro):
        letra_linha = string.ascii_uppercase[i]
        conteudo_linha = "|".join(linha)

        print(f" {letra_linha}|{conteudo_linha}|")
        print(linha_divisoria)

# opcao_escolhida = menu()


iniciar_novo_jogo()
# while opcao_escolhida != 7:
#     if opcao_escolhida < 1 or opcao_escolhida > 7:
#         print('Escolha uma opção válida!')
#         opcao_escolhida = menu()

#     elif opcao_escolhida == 1:
#         jogador_x = input('Digite o nome do Jogador X: ')

#     elif opcao_escolhida == 2:
#         jogador_o = input('Digite o número do Jogador O')

#     elif opcao_escolhida == 3:
#         tamanho = int(input('Digite o tamanho da matriz: '))

#     elif opcao_escolhida == 4:
#         tamanho_sequencia = int(input('Digite a sequência para vencer: '))

#     elif opcao_escolhida == 5:
#         pass

#     elif opcao_escolhida == 6:
#         iniciar_novo_jogo()
