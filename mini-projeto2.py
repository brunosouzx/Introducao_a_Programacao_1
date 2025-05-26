from time import sleep

YELLOW = '\u001b[33m'
RESET = '\033[0m'
GREEN = '\033[32m'
BLUE = '\033[34m'


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


def escreva(texto):
    print(texto)
    sleep(0.7)


def pegue(texto):
    valor_do_input = input(texto)
    sleep(0.7)
    return valor_do_input


print('\n======================================\n')

escreva(f'Oi, pode me chamar de {BLUE}Dim{RESET}')
escreva("Sou seu assistente financeiro")
escreva(
    f'e eu vou te ajudar com as {YELLOW}contas{RESET} e os {YELLOW}objetivos{RESET}.\n')
escreva('''======================================
==========[ DADOS PESSOAIS ]==========
======================================\n''')
escreva("Primeiro, preciso de algumas informações")

nome = pegue(f'Me diz teu {YELLOW}nome{RESET}: ')
dia = int(pegue(f'O {YELLOW}dia{RESET} em que tu nasceu: '))
mes = int(pegue(f'Agora o {YELLOW}mês{RESET}: '))
ano = int(pegue(f'E o {YELLOW}ano{RESET}: '))

escreva("\n======================================\n")
escreva("Muito bem, então conferindo seus dados ,estou registrando aqui.")
escreva(f'{GREEN}{nome}{RESET}, nascido em {GREEN}{dia}/{mes}/{ano}{RESET} \n')
escreva('''======================================
=========[ DADOS FINANCEIROS ]========
======================================\n''')
escreva("Agora me informa por favor alguns dados financeiros")

patrimonio = int(pegue(
    f'Se você somar o dinheiro que tem guardado, me diz o total desse {YELLOW}patrimonio{RESET}: R$ '))
salario = int(pegue(f'Me diz teu {YELLOW}salário{RESET}: R$ '))
escreva("Sobre os seus gastos, me informa por partes por favor.")

aluguel = int(pegue(
    f'Quanto custa teu {YELLOW}aluguel{RESET}, (incluindo condominio e outras taxas): R$ '))
feira = int(pegue(
    f'Mais ou menos o quanto você gasta fazendo {YELLOW}feira{RESET} rodo mês: R$ '))
comida = int(
    pegue(f'E com {YELLOW}comida{RESET} fora de casa, em média dá quanto: R$ '))
transporte = int(pegue(
    f'Na mobilidade, quanto que gasta com {YELLOW}transporte{RESET} (onibus, uber, gasolina, etc): R$ '))
outros = int(pegue(
    f'Pra terminar, quanto você gasta com {YELLOW}outros{RESET} (lazer, roupas, etc): R$ '))

total = aluguel + feira + comida + transporte + outros

escreva("\n======================================\n")

escreva(f'''Obrigado {GREEN}{nome}{RESET}, resumindo as informações financeiras até agora.
Os seus gastos discriminados são:
{GREEN}Aluguel{RESET}: R$ {aluguel:.2f}
{GREEN}Feira{RESET}: R$ {feira:.2f}
{GREEN}Comida{RESET}: R$ {comida:.2f}
{GREEN}Transporte{RESET}: R$ {transporte:.2f}
{GREEN}Outros{RESET}: R$ {outros:.2f}
{GREEN}GASTOS TOTAIS{RESET}: R$ {total:.2f}''')

escreva("\n======================================\n")

escreva("Pra terminar, calculando o seu saldo mensal, com base em todos os gastos")
escreva(
    f'e no teu salário, o valor resultante é de {GREEN}R$ {(salario - total):.2f}{RESET}')
escreva("Desse valor, considere que qualquer investimento é válido,")

investimento = int(
    pegue(f'o quanto você conseguiria {YELLOW}investir{RESET} todo mês: R$ '))

escreva(
    f'OK, anotado, o valor do investimento mensal é {GREEN}R$ {investimento:.2f}{RESET}')
escreva("Acredito que coletei todas as informações necessarias")

nascimento = Data(dia, mes, ano)

gastos = Gastos(aluguel, feira, comida, transporte, outros)

financas = Financas(patrimonio=patrimonio, salario=salario,
                    gastos=gastos, investimento=investimento)

antonieta = Pessoa(nome, nascimento=nascimento, financas=financas)


gastos_totais = (
    antonieta.financas.gastos.aluguel +
    antonieta.financas.gastos.feira +
    antonieta.financas.gastos.comida +
    antonieta.financas.gastos.transporte +
    antonieta.financas.gastos.outros
)

escreva("\n======================================\n")

escreva('Agora organizei todos os seus dados '
        'de forma concentrada aqui no meu sistema')
escreva('Vou te mostrar como ficou: ')

escreva(f'{YELLOW}{antonieta.nome}{RESET}, \
nascimento em {YELLOW}{antonieta.nascimento.dia}\
/{antonieta.nascimento.mes}/{antonieta.nascimento.ano}{RESET}')
escreva(f'{YELLOW}{antonieta.nome}{RESET} tem {GREEN}{antonieta.financas.patrimonio:.2f}{RESET} de patrimônio')
escreva(f'{YELLOW}{antonieta.nome}{RESET} tem {GREEN}{antonieta.financas.salario:.2f}{RESET} de salário')
escreva(f'{YELLOW}{antonieta.nome}{RESET} tem {GREEN}{gastos_totais:.2f}{RESET} de gastos')
escreva(f'{YELLOW}{antonieta.nome}{RESET} tem {GREEN}{antonieta.financas.investimento:.2f}{RESET} \
de investimento\n')


# Parte 3


escreva('Agora sim, vamos pensar no futuro! Você tem um próximo objetivo'
        ' financeiro?')

escreva('Um desejo de adquirir ou realizar algo que você quer'
        ' e que precisa de investimento?')

escreva('Exemplo de objetivos assim são:')

escreva(f'Comprar uma {BLUE}moto{RESET} ou um {BLUE}carro{RESET}, fazer uma {BLUE}viagem{RESET}, comprar uma {BLUE}casa{RESET}, fazer um {BLUE}curso{RESET}, etc')

objetivo_financeiro = pegue(
    f'Qual seria esse seu próximo {YELLOW} objetivo {RESET} financeiro: '
)

vl_objetivo_financeiro = float(pegue(
    f'Qual seria o valor do {YELLOW} objetivo {RESET} financeiro: R$ '
))

escreva('Em uma conta que eu fiz aqui, sem considerar rendimentos ou inflação, ')

escreva(f'com base na sua capacidade de investimento mensal de: \
{GREEN}R$ {(antonieta.financas.investimento):.2f}{RESET}')

escreva(
    f'e o seu patrimônio atual de {GREEN}R$: {(antonieta.financas.patrimonio):.2f}\
        {RESET}'
)

escreva(f'Você conseguiria atingir o valor de {GREEN}\
R$ {vl_objetivo_financeiro:.2f}\
{RESET} em: ')

tempo_em_meses = (vl_objetivo_financeiro - antonieta.financas.patrimonio
                  )/antonieta.financas.investimento
escreva(f'{tempo_em_meses} meses')

tempo_em_anos = tempo_em_meses/12

escreva(f'{tempo_em_anos:.1f} anos')

escreva('Por hora é isso que tenho para te ajudar \n'
        'Espero que tenha sido útil')
