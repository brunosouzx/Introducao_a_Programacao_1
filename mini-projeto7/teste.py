import csv
import json


class Pessoa:
    def __init__(self, nome, patrimonio, salario):
        self.nome = nome
        self.patrimonio = patrimonio
        self.conforto = 0.0
        self.salario = salario


def ler_pessoas(caminho='mini-projeto7/arquivos/pessoas.txt'):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    dados = [
        [campo.strip() for campo in linha.strip().split(',')]
        for linha in linhas[1:]
    ]

    pessoas = []
    for item in dados:
        nome = item[0]
        patrimonio = item[1]
        salario = item[2]

        pessoa = Pessoa(nome, patrimonio, salario)

        pessoas.append(pessoa)


# ler_pessoas()


def ler_empresas(caminho='mini-projeto7/arquivos/empresas.csv'):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        dados = []
        for linha in leitor:
            dados.append(linha)

    print(dados)


# ler_empresas()


def ler_categorias(caminho='mini-projeto7/arquivos/categorias.json'):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        categorias = json.load(arquivo)

    print(categorias)
    return categorias


ler_categorias()
