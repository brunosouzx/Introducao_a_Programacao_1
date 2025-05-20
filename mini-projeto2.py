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
