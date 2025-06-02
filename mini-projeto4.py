# flake8: noqa

from os import system
from time import sleep

i = '\033[3m'  # Itálico
r = '\033[0m'  # Resetar
B = '\033[34m'  # Azul

# =====[ Tempo ]=====
tempo_longo = 1.0
tempo_curto = 0.5


class Investimento():
    def __init__(self, percentual, aporte_inicial, recorrente):
        self.percentual = percentual
        self.aporte_inicial = aporte_inicial
        self.recorrente = recorrente

    def total_investido(self):
        if self.recorrente:
            # Vai lá Bruno
            pass
        else:
            return self.aporte_inicial

    def resgate(self):
        # Vai lá Bruno
        pass

    def __str__(self):
        return f'aporte = {self.aporte_inicial},  percentual = {self.percentual}, recorrente = {self.recorrente}, total = {self.total_investido()}'


primeira_resposta = ''

investimentos = []

print('[SIMULADOR DE INVESTIMENTOS RECORRENTES]')
sleep(tempo_longo)
print('')
print(f'{i}Bem vindo, vamos simular também investimentos recorrentes!')
print('Neste exercício vamos usar somente LCIs, sem cálculo de IR dessa vez')
sleep(tempo_longo)
print('')
print(f'Iniciando as simulações...{r}')
print('')
sleep(tempo_longo)

while True:
    primeira_resposta = input(
        f'Digite [{B}novo{r}] investimento, [{B}sair{r}] ou aperte [{B}enter{r}] para avançar em um mês: ')

    system('cls')

    if primeira_resposta.upper() == 'SAIR':
        system('cls')
        sleep(tempo_longo)
        print(f'{i}OK, finalizando o simulador.{r}')
        sleep(tempo_longo)
        break

    elif primeira_resposta.upper() == 'NOVO':

        percentual = int(input(f'Qual o percentual? ({B}% do CDI{r}) '))

        aporte_inicial = float(
            input(f'Qual o {B}valor{r} do aporte de entrada? '))

        serao_mensais = input(
            f'Serão depósitos mensalmente recorrentes? ({B}sim/não{r}) '
        )

        recorrente = False

        if serao_mensais.upper() == 'SIM':
            recorrente = True

        novo_investimento = Investimento(
            percentual, aporte_inicial, recorrente)

        investimentos.append(novo_investimento)

        sleep(tempo_longo)
        print('')
        print(f'{i}Investimento adicionado com sucesso{r}')
        sleep(tempo_longo)
        system('cls')

    elif primeira_resposta == '':
        # Vai lá Bruno
        print('Teste ENTER')


# Testando a classe
for investimento in investimentos:
    print(investimento)
