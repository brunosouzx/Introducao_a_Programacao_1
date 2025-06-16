# flake8: noqa

class Pessoa:
    def __init__(self, patrimonio, salario):
        self.patrimonio = patrimonio
        self.conforto = 0.0
        self.salario = salario

    def __str__(self):
        return f'patrimônio: {self.patrimonio}'


pessoas = []


def add_pessoas(num_pessoas, patrimonio, salario, variacao=0.0):
    for i in range(num_pessoas):
        pessoas.append(
            Pessoa(patrimonio + i * variacao, salario + i * variacao))


add_pessoas(5,  patrimonio=20000000, salario=0,
            variacao=0)     # Herdeiros milionários
add_pessoas(10, patrimonio=200000,   salario=100000,
            variacao=-5000)  # Supersalários
add_pessoas(25, patrimonio=100000,   salario=30000,
            variacao=-1000)  # Faixa salarial média-alta
add_pessoas(50, patrimonio=10000,    salario=5000,
            variacao=-50)   # Faixa salarial baixa
add_pessoas(70, patrimonio=10000,    salario=1518,
            variacao=0)     # Salário mínimo
