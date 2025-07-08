# flake8:noqa

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


def iniciar_novo_jogo(jogador_x,
                      jogador_o,
                      tamanho_matriz,
                      tamanho_sequencia
                      ):
    tabuleiro = np.full((tamanho_matriz, tamanho_matriz), '   ', dtype='<U3')

    imprimir_matriz(tabuleiro, tamanho_matriz)

    vencedor = False
    vez_jogador = 'X'

    while not vencedor:
        nome_turno = jogador_x if vez_jogador == 'X' else jogador_o

        print(f'Turno do {nome_turno}')

        jogada = input(
            f'{nome_turno}, escolha sua jogada (letra e número separados por espaço): '
        )

        jogada_tuple = tuple(jogada.upper().split(' '))

        linha = ord(jogada_tuple[0]) - ord('A')
        coluna = int(jogada_tuple[1])

        # Fazer algumas validações sobre os valores passados

        tabuleiro[linha, coluna] = f' {vez_jogador} '

        # Função para verificar se é vencedor
        # is_vencedor()

        imprimir_matriz(tabuleiro, tamanho_matriz)

        vez_jogador = 'O' if vez_jogador == 'X' else 'X'


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


opcao_escolhida = menu()


jogador_x = 'Jogador X'
jogador_o = 'Jogador O'
tamanho_matriz = 3
tamanho_sequencia = 3


# iniciar_novo_jogo()
while opcao_escolhida != 7:
    if opcao_escolhida < 1 or opcao_escolhida > 7:
        print('Escolha uma opção válida!')
        opcao_escolhida = menu()

    elif opcao_escolhida == 1:
        jogador_x = input('Digite o nome do Jogador X: ')
        opcao_escolhida = menu()

    elif opcao_escolhida == 2:
        jogador_o = input('Digite o número do Jogador O: ')
        opcao_escolhida = menu()

    elif opcao_escolhida == 3:
        tamanho_matriz = int(input('Digite o tamanho da matriz: '))
        opcao_escolhida = menu()

    elif opcao_escolhida == 4:
        tamanho_sequencia = int(input('Digite a sequência para vencer: '))
        opcao_escolhida = menu()

    elif opcao_escolhida == 5:
        pass

    elif opcao_escolhida == 6:
        iniciar_novo_jogo(jogador_x, jogador_o,
                          tamanho_matriz, tamanho_sequencia)
