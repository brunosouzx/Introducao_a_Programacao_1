# flake8:noqa

import string
import numpy as np
import os

# --- Variáveis Globais ---

# Dicionário global para armazenar o placar
placar = {'X': 0, 'O': 0, 'Empates': 0}

# Definições padrão do jogo
jogador_x = 'Jogador X'
jogador_o = 'Jogador O'
tamanho_matriz = 3
tamanho_sequencia = 3


# --- Funções Auxiliares ---

def limpar_tela():
    """Limpa o terminal para uma melhor visualização."""
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    """Exibe o menu principal e retorna a opção escolhida pelo usuário."""
    limpar_tela()
    print("==========================")
    print("  JOGO DA VELHA AVANÇADO  ")
    print("==========================")
    print('Menu:')
    print('1. Definir Jogador X')
    print('2. Definir Jogador O')
    print('3. Definir tamanho do tabuleiro')
    print('4. Definir tamanho da sequência para vitória')
    print('5. Mostrar Placar')
    print('6. Iniciar Novo Jogo')
    print('7. Sair do Jogo')

    while True:
        try:
            opcao = int(input('Escolha uma opção: '))
            if 1 <= opcao <= 7:
                return opcao
            else:
                print('Opção inválida! Escolha um número entre 1 e 7.')
        except ValueError:
            print('Entrada inválida! Por favor, digite um número.')


def mostrar_placar():
    """Exibe o placar atual do jogo."""
    limpar_tela()
    print("--- PLACAR GERAL ---")
    print(f"| {jogador_x} ('X'): {placar['X']} vitórias")
    print(f"| {jogador_o} ('O'): {placar['O']} vitórias")
    print(f"| Empates:              {placar['Empates']}     ")
    print("--------------------")
    input("\nPressione Enter para voltar ao menu...")


# --- Funções de Lógica do Jogo ---

def imprimir_matriz(tabuleiro, tamanho_matriz):
    """Imprime o tabuleiro formatado no console com letras e números."""
    limpar_tela()

    cabecalho_numerico = "   |" + "|".join([f"{i:^3}" for i in range(tamanho_matriz)])
    print(cabecalho_numerico)

    linha_divisoria = "   +" + "---+" * tamanho_matriz
    print(linha_divisoria)

    for i, linha in enumerate(tabuleiro):
        letra_linha = string.ascii_uppercase[i]
        conteudo_linha = "|".join(linha)

        print(f" {letra_linha} |{conteudo_linha}|")
        print(linha_divisoria)


def checar_vitoria(tabuleiro, jogador, tamanho_sequencia):
    """
    Verifica se o jogador atual venceu no tabuleiro numpy.
    A função foi adaptada para verificar strings com espaços (' X ' ou ' O ').
    """
    tamanho = len(tabuleiro)
    # A sequência a ser encontrada, ex: (' X ', ' X ', ' X ')
    sequencia_ganhadora = tuple([f' {jogador} '] * tamanho_sequencia)

    # Itera sobre cada célula como um ponto de partida potencial
    for r in range(tamanho):
        for c in range(tamanho):
            # Checagem Horizontal 
            if c <= tamanho - tamanho_sequencia:
                linha_horizontal = tuple(tabuleiro[r, c + i] for i in range(tamanho_sequencia))
                if linha_horizontal == sequencia_ganhadora:
                    return True

            # Checagem Vertical 
            if r <= tamanho - tamanho_sequencia:
                linha_vertical = tuple(tabuleiro[r + i, c] for i in range(tamanho_sequencia))
                if linha_vertical == sequencia_ganhadora:
                    return True

            # Checagem Diagonal (Direita-Baixo \)
            if r <= tamanho - tamanho_sequencia and c <= tamanho - tamanho_sequencia:
                diagonal_1 = tuple(tabuleiro[r + i, c + i] for i in range(tamanho_sequencia))
                if diagonal_1 == sequencia_ganhadora:
                    return True

            # Checagem Diagonal (Esquerda-Baixo /)
            if r <= tamanho - tamanho_sequencia and c >= tamanho_sequencia - 1:
                diagonal_2 = tuple(tabuleiro[r + i, c - i] for i in range(tamanho_sequencia))
                if diagonal_2 == sequencia_ganhadora:
                    return True

    return False


def iniciar_novo_jogo(jogador_x, jogador_o, tamanho_matriz, tamanho_sequencia):
    """Função principal que executa uma partida do jogo."""
    tabuleiro = np.full((tamanho_matriz, tamanho_matriz), '   ', dtype='<U3')

    vencedor = None
    vez_jogador = 'X'
    jogadas_feitas = 0
    total_jogadas_possiveis = tamanho_matriz * tamanho_matriz

    while not vencedor and jogadas_feitas < total_jogadas_possiveis:
        imprimir_matriz(tabuleiro, tamanho_matriz)
        nome_turno = jogador_x if vez_jogador == 'X' else jogador_o
        print(f"\nTurno de {nome_turno} ('{vez_jogador}')")

        # --- Obter e validar a jogada do jogador ---
        while True:
            jogada = input(
                f'{nome_turno}, escolha sua jogada (letra e número separados por espaço, ex: A 0): '
            )
            try:
                jogada_split = jogada.upper().split(' ')
                if len(jogada_split) != 2:
                    print("Formato inválido. Use letra e número separados por espaço.")
                    continue

                letra, numero = jogada_split
                linha = ord(letra) - ord('A')
                coluna = int(numero)

                if not (0 <= linha < tamanho_matriz and 0 <= coluna < tamanho_matriz):
                    print(f"Jogada inválida. Letra deve ser de A-{string.ascii_uppercase[tamanho_matriz-1]} e número de 0-{tamanho_matriz-1}.")
                elif tabuleiro[linha, coluna] != '   ':
                    print("Este espaço já está ocupado. Tente outro.")
                else:
                    break  # Jogada válida, sai do loop de input

            except (ValueError, IndexError):
                print("Entrada inválida. Use o formato 'Letra Numero', por exemplo: A 0")

        # --- Atualizar o Jogo ---
        tabuleiro[linha, coluna] = f' {vez_jogador} '
        jogadas_feitas += 1

        # --- Checar Condição de Fim de Jogo ---
        if checar_vitoria(tabuleiro, vez_jogador, tamanho_sequencia):
            vencedor = vez_jogador
        else:
            # Troca o jogador
            vez_jogador = 'O' if vez_jogador == 'X' else 'X'

    # --- Fim da Partida ---
    imprimir_matriz(tabuleiro, tamanho_matriz)
    if vencedor:
        nome_vencedor = jogador_x if vencedor == 'X' else jogador_o
        print(f"\n--- FIM DE JOGO! O JOGADOR '{nome_vencedor}' ({vencedor}) VENCEU! ---")
        placar[vencedor] += 1
    else:
        print("\n--- FIM DE JOGO! DEU EMPATE! ---")
        placar['Empates'] += 1

    input("\nPressione Enter para continuar...")


# --- Loop Principal do Programa ---

if __name__ == "__main__":
    opcao_escolhida = menu()

    while opcao_escolhida != 7:
        if opcao_escolhida == 1:
            jogador_x = input('Digite o nome do Jogador X: ')
            if not jogador_x: jogador_x = "Jogador X"

        elif opcao_escolhida == 2:
            jogador_o = input('Digite o nome do Jogador O: ')
            if not jogador_o: jogador_o = "Jogador O"

        elif opcao_escolhida == 3:
            try:
                novo_tamanho = int(input('Digite o tamanho do tabuleiro (mínimo 3): '))
                if novo_tamanho >= 3:
                    tamanho_matriz = novo_tamanho
                    # Ajusta a sequência se ela for maior que o novo tabuleiro
                    if tamanho_sequencia > tamanho_matriz:
                        tamanho_sequencia = tamanho_matriz
                else:
                    print("O tamanho mínimo é 3.")
                    input("Pressione Enter para continuar...")
            except ValueError:
                print("Por favor, digite um número inteiro.")
                input("Pressione Enter para continuar...")


        elif opcao_escolhida == 4:
            try:
                nova_sequencia = int(input(f'Digite a sequência para vencer (entre 3 e {tamanho_matriz}): '))
                if 3 <= nova_sequencia <= tamanho_matriz:
                    tamanho_sequencia = nova_sequencia
                else:
                    print(f"A sequência deve estar entre 3 e o tamanho do tabuleiro ({tamanho_matriz}).")
                    input("Pressione Enter para continuar...")
            except ValueError:
                print("Por favor, digite um número inteiro.")
                input("Pressione Enter para continuar...")


        elif opcao_escolhida == 5:
            mostrar_placar()

        elif opcao_escolhida == 6:
            iniciar_novo_jogo(jogador_x, jogador_o, tamanho_matriz, tamanho_sequencia)

        opcao_escolhida = menu()

    limpar_tela()
    print("Obrigado por jogar! Até a próxima.\n")