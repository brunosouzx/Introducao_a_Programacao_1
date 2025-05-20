class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


class Gastos:
    def __init__(self, aluguel, feira, comida, transporte, outros):
        self.aluguel = aluguel
        self.feira = feira
        self.comida = comida
        self.transporte = transporte
        self.outros = outros


class Financas:
    def __init__(self, patrimonio, salario, gastos, investimento):
        self.patrimonio = patrimonio
        self.salario = salario
        self.gastos = gastos
        self.investimento = investimento


class Pessoa:
    def __init__(self, nome, nascimento, financas):
        self.nome = nome
        self.nascimento = nascimento
        self.financas = financas


dia = 1
mes = 11
ano = 2001

aluguel = 700
feira = 900
comida = 500
transporte = 400
outros = 289

patrimonio = 2000

salario = 8000

investimento = 800

nascimento = Data(dia, mes, ano)


gastos = Gastos(aluguel, feira, comida, transporte, outros)


financas = Financas(patrimonio=patrimonio, salario=salario,
                    gastos=gastos, investimento=800)

antonieta = Pessoa('Antonieta da Silva',
                   nascimento=nascimento, financas=financas)


gastos_totais = (
    antonieta.financas.gastos.aluguel +
    antonieta.financas.gastos.feira +
    antonieta.financas.gastos.comida +
    antonieta.financas.gastos.transporte +
    antonieta.financas.gastos.outros
)

print('\n---\n')

print('Agora organizei todos os seus dados'
      'de forma concentrada aqui no meu sistema')
print('Vou te mostrar como ficou: ')

print(f'{antonieta.nome}, \
nascimento em {antonieta.nascimento.dia}\
/{antonieta.nascimento.mes}/{antonieta.nascimento.ano}')
print(f'{antonieta.nome} tem {antonieta.financas.patrimonio} de patrimônio')
print(f'{antonieta.nome} tem {antonieta.financas.salario} de salário')
print(f'{antonieta.nome} tem {gastos_totais} de gastos')
print(f'{antonieta.nome} tem {antonieta.financas.investimento} \
de investimento')


# Parte 3

YELLOW = '\u001b[33m'
RESET = '\033[0m'
GREEN = '\033[32m'

print('Agora sim, vamos pensar no futuro! Você tem um próximo objetivo'
      ' financeiro?')

print('Um desejo de adquirir ou realizar algo que você quer'
      ' e que precisa de investimento?')

print('Exemplo de objetivos assim são:')

print('Comprar uma moto ou um carro, fazer uma viagem, comprar uma casa, '
      'fazer um curso, etc')

objetivo_financeiro = input(
    f'Qual seria esse seu próximo {YELLOW} objetivo {RESET} financeiro: '
)

vl_objetivo_financeiro = float(input(
    f'Qual seria o valor do {YELLOW} objetivo {RESET} financeiro: R$ '
))

print('Em uma conta que eu fiz aqui, sem considerar rendimentos ou inflação, ')

print(f'com base na sua capacidade de investimento mensal de: \
{GREEN}R$ {antonieta.financas.investimento}{RESET}')

print(
    f'e o seu patrimônio atual de {GREEN}R$: {antonieta.financas.patrimonio}\
        {RESET}'
)

print(f'Você conseguiria atingir o valor de {GREEN}\
R$ {vl_objetivo_financeiro}\
{RESET} em: ')

tempo_em_meses = (vl_objetivo_financeiro - antonieta.financas.patrimonio
                  )/antonieta.financas.investimento
print(f'{tempo_em_meses} meses')

tempo_em_anos = tempo_em_meses/12

print(f'{tempo_em_anos} anos')

print('Por hora é isso que tenho para te ajudar \n'
      'Espero que tenha sido útil')
