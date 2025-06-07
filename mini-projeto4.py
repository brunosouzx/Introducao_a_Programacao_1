# flake8: noqa

from os import system
from time import sleep

i = '\033[3m'  # Itálico
r = '\033[0m'  # Resetar
G = '\033[32m'  # Verde
B = '\033[34m'  # Azul
Y = '\033[33m'  # Amarelo
P = '\033[35m'  # Roxo

CDI = 14.65
# =====[ Tempo ]=====
tempo_longo = 1.0
tempo_curto = 0.5

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

mes_atual = 3
ano_atual = 2025

class Investimento():
    def __init__(self, percentual, aporte_inicial, recorrente):
        self.percentual = percentual
        self.aporte_inicial = aporte_inicial
        self.recorrente = recorrente
        self.investido = 0.0
        self.total = 0.0

    def total_investido(self):
        if self.recorrente:
            self.investido += self.aporte_inicial
        else:
            self.investido = self.aporte_inicial
        
        taxa_anual = (CDI*(self.percentual/100))/100
        taxa_mensal = (taxa_anual + 1) ** (1/12) - 1

        if self.recorrente :
            
            if self.total ==0.0:
                rendimento_bruto = self.aporte_inicial * taxa_mensal
                valor_final = self.aporte_inicial + rendimento_bruto
                self.total=valor_final
            else:
                periodo_novo=self.aporte_inicial+self.total
                rendimento_bruto = periodo_novo * taxa_mensal
                valor_final = periodo_novo + rendimento_bruto
                self.total=valor_final
        else:    
            if self.total ==0.0:
                rendimento_bruto = self.aporte_inicial * taxa_mensal
                valor_final = self.aporte_inicial + rendimento_bruto
                self.total=valor_final
            else:
                rendimento_bruto = self.total * taxa_mensal
                valor_final = self.total + rendimento_bruto
                self.total=valor_final
            


    def __str__(self):
        tipo = "[R]" if self.recorrente else "[U]"
        cifroes = int(self.total // 1000)
        return f'{tipo}[LCI de {self.percentual:.2f} do CDI% {Y}R${self.investido:.2f}{r}, {G}R$ {self.total:.2f}{r}]   \t\t{G}{"$"*cifroes}{r}'
        
def avancar_mes():
    global ano_atual 
    global mes_atual
    mes_atual += 1
    if mes_atual == 12:
        ano_atual += 1
        mes_atual = 0

system('cls')

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
        
        for investimento in investimentos:
            investimento.total_investido()
            print(investimento)
        avancar_mes()

        


        print(f'resumo da simulação em {P}{meses[mes_atual]} de {ano_atual}{r}')
        print("\n...\n")
