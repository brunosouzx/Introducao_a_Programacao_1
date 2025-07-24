# flake8: noqa

import csv
import json
import os

# Códigos das cores de texto em Python
R = '\033[31m'  # vermelho
G = '\033[32m'  # verde
B = '\033[34m'  # azul
Y = '\033[33m'  # amarelo
P = '\033[35m'  # roxo
C = '\033[36m'  # ciano
W = '\033[37m'  # branco
i = '\033[3m'  # itálico
n = '\033[7m'  # negativo
r = '\033[0m'  # resetar
p = "\033[F"   # mover o cursor para o começo da linha anterior
u = "\033[A"   # mover o cursor para cima uma linha

# Parte 1, classe pessoa


class Pessoa:
    def __init__(self, nome, patrimonio, salario):
        self.nome = nome
        self.patrimonio = patrimonio
        self.conforto = 0.0
        self.salario = salario


class Empresa:
    def __init__(self, categoria, nome, produto, custo, qualidade):
        self.nome = nome
        self.categoria = categoria
        self.produto = produto
        self.custo = custo
        self.qualidade = qualidade
        self.margem = 0.05
        self.oferta = 0
        self.reposicao = 10
        self.vendas = 0


class Console():
    def limpar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_pessoas(self, pessoas, categorias):
        print()
        print("[PESSOAS]")

        # Imprimir em uma linha os percentuais dedicados à cada categoria
        print(f"{i}Divisão da renda mensal ", end="")
        for categoria, percentual in categorias.items():
            print(f"| {categoria} ", end="")
            print(f"{Y}{percentual * 100:3.1f}%{r}{i} ", end="")
        soma = sum(categorias.values())
        print(
            f"{i} | Totalizando {Y}{soma * 100:3.1f}%{r}{i} da renda mensal total.{r}")

        # Imprimir as pessoas e seus patrimônios
        max_renda_total = int(max(calc_renda_mensal(p) for p in pessoas))
        max_renda_total = 10000
        step = max_renda_total // 10

        print(f"{i}Gráfico de Barras | Legenda: {B}Conforto{r}{i}, {G}Salário{r}{i}, {P}Rendimentos{r}", end="")
        print(f"{i} | Cada traço = R${step:.2f}{r}{B}")

        for conforto in range(10, 1, -1):
            for pessoa in pessoas:
                char = " "
                if pessoa.conforto // len(categorias) >= conforto:
                    char = "|"
                print(char, end="")
            print()

        print(f"{r}", end="")
        for pessoa in pessoas:
            print("-", end="")
        print()

        for renda_total in range(step, max_renda_total, step):
            for pessoa in pessoas:
                char = " "
                if calc_renda_mensal(pessoa) >= renda_total:
                    if float(pessoa.salario) >= renda_total:
                        char = f"{G}|{r}"
                    else:
                        char = f"{P}|{r}"
                print(char, end="")
            print()
        print(f"{r}", end="")

    def mostrar_empresas(self, empresas):
        print()
        print("[EMPRESAS]")

        for empresa in empresas:
            print(f"|{empresa.categoria}| \t"
                  f"{empresa.nome}: {empresa.produto} "
                  f"{C}Q={empresa.qualidade}{r} Margem: {Y}{empresa.margem * 100:3.1f}%{r}\t"
                  f"Custo: {R}R$ {float(empresa.custo):.2f}{r}\t"
                  f"Preço: {G}R$ {calc_preco(empresa):.2f}{r}\t"
                  f"Lucro T.: {G}R$ {(empresa.vendas * empresa.custo * empresa.margem):.2f}{r}\t"
                  f"Vendas: ", end="")

            for i in range(empresa.vendas // 5):
                print(f"{G}${r}", end="")

            print()

    # def mostrar_categorias(self, categorias):
    #     for categoria in categorias.keys():
    #         print(categoria)

    def mostrar_categorias(self, categorias):
        print()
        print("[CATEGORIAS]")

        for categoria, percentual in categorias.items():
            print(f"{categoria} ", end="")
            # print(f"{Y}{percentual * 100:3.1f}%{r} ", end="")
        # soma = sum(categorias.values())
        # print(
        #     f"{i} | Totalizando {Y}{soma * 100:3.1f}%{r}{i} da renda mensal total.{r}"))


def calc_preco(empresa):
    return empresa.custo * (1 + empresa.margem)


def calc_disponibilidade(empresa):
    if empresa.oferta > 0:
        return True
    else:
        return False


def comprar(pessoa, empresa):
    empresa.vendas += 1
    empresa.oferta -= 1
    pessoa.patrimonio -= calc_preco(empresa)
    pessoa.conforto += empresa.qualidade

# Pesquisar melhor produto de uma categoria


def escolher_melhor(categoria, empresas, orcamento):
    melhor_empresa = None
    for empresa in empresas:
        if empresa.categoria == categoria and empresa.oferta > 0:
            preco = calc_preco(empresa)
            if preco <= orcamento:
                if melhor_empresa is None or empresa.qualidade > melhor_empresa.qualidade:
                    melhor_empresa = empresa
                elif empresa.qualidade == melhor_empresa.qualidade:
                    if calc_preco(empresa) < calc_preco(melhor_empresa):
                        melhor_empresa = empresa

    return melhor_empresa

# Pesquisar produto mais barato de uma categoria


def escolher_barato(categoria, empresas, orcamento):
    melhor_empresa = None
    for empresa in empresas:
        if empresa.categoria == categoria and empresa.oferta > 0:
            preco = calc_preco(empresa)
            if preco <= orcamento:
                if melhor_empresa is None or preco < calc_preco(melhor_empresa):
                    melhor_empresa = empresa

    return melhor_empresa

# Calcular a renda mensal total da pessoa, incluindo renda passiva


def calc_renda_mensal(pessoa):
    return float(pessoa.salario) + (float(pessoa.patrimonio) * 0.005)


def simular_empresa(empresa):
    # Se a oferta zerou quer dizer que a empresa vendeu tudo
    if empresa.oferta == 0:
        empresa.reposicao += 1
        empresa.margem += 0.01

    # Se a oferta está alta, quer dizer que as vendas foram aquém
    elif empresa.oferta > 10:
        empresa.reposicao = max(0, empresa.reposicao - 1)
        if (empresa.margem > 0.01):
            empresa.margem -= 0.01

    # Repor o estoque de produtos
    empresa.oferta += empresa.reposicao  # Exemplo de reposição de estoque
    empresa.vendas = 0  # Resetar vendas após reposição


def simular_pessoa(pessoa, empresas, categorias):
    # Reinicializar conforto da pessoa
    pessoa.conforto = 0.0

    # Fazer compras dentro do orçamento para cada categoria
    # e atualizar o conforto da pessoa

    # Renda passiva
    # Aplicar o percentual de rendimento no patrimônio da pessoa como renda passiva
    renda_total = calc_renda_mensal(pessoa)

    pessoa.patrimonio += renda_total  # Atualizar patrimônio com a renda total

    for categoria, percentual in categorias.items():
        # Comprar o produto de melhor qualidade
        # que caiba no orçamento da pessoa para aquela categoria
        orcamento = renda_total * percentual
        patrimonio = pessoa.patrimonio
        empresa = escolher_melhor(categoria, empresas, orcamento)
        if empresa is None:
            empresa = escolher_barato(categoria, empresas, patrimonio)

        # Se encontrou um produto, comprar e atualizar o conforto
        if empresa is not None:
            comprar(pessoa, empresa)


def simular_mercado(pessoas, empresas, categorias, percentuais):
    # Atualização das empresas e produtos
    for empresa in empresas:
        simular_empresa(empresa)

    # Atualização das pessoas e seus patrimônios
    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais)


def print_empresas(empresas):
    print()
    print("[EMPRESAS]")

    for empresa in empresas:
        print(f"|{empresa.categoria}| \t"
              f"{empresa.nome}: {empresa.produto} "
              f"{C}Q={empresa.qualidade}{r} Margem: {Y}{empresa.margem * 100:3.1f}%{r}\t"
              f"Custo: {R}R$ {empresa.custo:.2f}{r}\t"
              f"Preço: {G}R$ {calc_preco(empresa):.2f}{r}\t"
              f"Lucro T.: {G}R$ {(empresa.vendas * empresa.custo * empresa.margem):.2f}{r}\t"
              f"Vendas: ", end="")

        for i in range(empresa.vendas // 5):
            print(f"{G}${r}", end="")

        print()


class Simulador:
    def simular_mercado(self, pessoas, empresas, categorias):
        # Atualização das empresas e produtos
        for empresa in empresas:
            simular_empresa(empresa)

        # Atualização das pessoas e seus patrimônios
        for pessoa in pessoas:
            simular_pessoa(pessoa, empresas, categorias)


class Leitor:
    def ler_pessoas(self, caminho='mini-projeto7/arquivos/pessoas.txt'):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        dados = [
            [campo.strip() for campo in linha.strip().split(',')]
            for linha in linhas[1:]
        ]

        pessoas = []
        for item in dados:
            nome = item[0]
            patrimonio = float(item[1])
            salario = float(item[2])

            pessoa = Pessoa(nome, patrimonio, salario)

            pessoas.append(pessoa)

        return pessoas

    def ler_empresas(self, caminho='mini-projeto7/arquivos/empresas.csv'):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor)

            empresas_leitura = []
            for linha in leitor:
                categoria = linha[0]
                empresa_nome = linha[1]
                produto = linha[2]
                custo = float(linha[3])
                qualidade = float(linha[4])

                empresa = Empresa(categoria, empresa_nome,
                                  produto, custo, qualidade)

                empresas_leitura.append(empresa)

            return empresas_leitura

    def ler_categorias(self, caminho='mini-projeto7/arquivos/categorias.json'):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            categorias = json.load(arquivo)

        return categorias


# Parte 3, simulação de mercado
# Enquanto não for digitado "sair", simular o mercado

leitor = Leitor()
console = Console()
simulador = Simulador()


def main():
    console.limpar()
    categorias = leitor.ler_categorias()
    pessoas = leitor.ler_pessoas()
    empresas = leitor.ler_empresas()
    simular = True
    while simular:
        console.limpar()
        print("[SIMULADOR DE RELAÇÕES DE MERCADO]")
        console.mostrar_categorias(categorias)
        console.mostrar_pessoas(pessoas, categorias)
        console.mostrar_empresas(empresas)
        resposta = input(
            "\nDigite um número para avançar N meses, 'enter' para 1 mês ou 'sair': ").strip().lower()
        if resposta.isdigit():
            meses = int(resposta)
            for _ in range(meses):
                simulador.simular_mercado(pessoas, empresas, categorias)
        elif resposta == "":
            simulador.simular_mercado(pessoas, empresas, categorias)
        elif resposta == "sair":
            simular = False


if __name__ == "__main__":
    main()


# Desconsiderar daqui para baixo, é só um exemplo de código comentado

# # ----------------------------------------------

# # Parte 1, classes com métodos de impressão e atualização

# class Data:
#     def __init__(self, dia, mes, ano):
#         self.dia = dia
#         self.mes = mes
#         self.ano = ano
#         self.meses = ["janeiro",  "fevereiro",
#                       "março",    "abril",
#                       "maio",     "junho",
#                       "julho",    "agosto",
#                       "setembro", "outubro",
#                       "novembro", "dezembro"]

#     def __str__(self):
#         return f"{self. dia} de {self.meses[self.mes - 1]} de {self.ano}"

# data = Data(1, 5, 2025)
# print(data)  # Saída: 1 de maio de 2025


# # Coletar nome
# def coletar_nome():
#     nome = input("Digite seu nome: ")
#     return nome

# # Coletar data de nascimento
# def coletar_data_nascimento():
#     dia = int(input("Digite o dia do seu nascimento: "))
#     mes = int(input("Digite o mês do seu nascimento: "))
#     ano = int(input("Digite o ano do seu nascimento: "))
#     return Data(dia, mes, ano)

# # Coletar dados do usuário
# def coletar_dados():
#     nome = coletar_nome()
#     data_nascimento = coletar_data_nascimento()
#     return nome, data_nascimento

# class Investimento:
#     def __init__(self,
#                  aporte,
#                  percentual = 0.95,
#                  recorrente = False):
#         self.tipo = "LCI"
#         self.indexador = "CDI"
#         self.percentual = percentual
#         self.aporte = aporte
#         self.investido = aporte
#         self.recorrente = recorrente
#         self.resgate = aporte

#     def __str__(self):
#         recorrente_str = 'U'
#         if self.recorrente:
#             recorrente_str = 'R'
#         return (f"[{recorrente_str}]"
#                 f"[{self.tipo} de "
#                 f"{self.percentual:.2f} do {self.indexador}% "
#                 f"{Y}R${self.investido:.2f}{r}, "
#                 f"{G}R${self.resgate:.2f}{r}]")

# # ----------------------------------------------

# # Parte 2, funções de controle do programa

# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def intro():
#     clear()
#     print(f"[SIMULADOR DE INVESTIMENTOS RECORRENTES]"); time.sleep(delay_longo)
#     print()
#     print(f"{i}Bem vindo, vamos simular também investimentos recorrentes!{r}"); time.sleep(delay_curto)
#     print(f"{i}Neste exercício vamos usar somente LCIs, sem cálculo de IR dessa vez{r}"); time.sleep(delay_curto)
#     print()
#     time.sleep(delay_longo)
#     print(f"{i}Iniciando as simulações...{r}"); time.sleep(delay_longo)
#     print()
#     time.sleep(delay_longo)

# def menu():
#     resposta = input(f"Digite [{B}novo{r}] investimento, [{B}sair{r}] ou aperte [{B}enter{r}] para avançar em um mês: ")
#     clear()

#     return resposta

# def avancar_mes(data):
#     data.mes += 1
#     if data.mes > 12:
#         data.mes = 1
#         data.ano += 1

# def add_investimento(investimentos):
#     print()
#     percentual = float(input(f"Qual o percentual? ({B}% do CDI{r}) "))
#     aporte = float(input(f"Qual o {B}valor{r} do aporte de entrada? "))
#     recorrente = input(f"Serão depósitos mensalmente recorrentes? ({B}sim/não{r}) ").strip().lower() == "sim"

#     inv = Investimento(aporte, percentual, recorrente)
#     investimentos.append(inv)

#     time.sleep(delay_curto)
#     print(f"\n{i}Investimento adicionado com sucesso!{r}")
#     time.sleep(delay_longo)
#     time.sleep(delay_longo)
#     clear()

# def print_data(data):
#     print(f"{i}resumo da simulação em {P}{data}{r}")
#     print("\n...\n")

# def print_investimento(inv, max_resgate):
#     print(inv, end ='  \t')
#     print_barra(inv, max_resgate, char="$", color=G)

# def print_barra(inv, max_resgate, char="$", color=G):
#     unidades = 0
#     max_unidades = 50
#     valor_unidade = 1000

#     if max_resgate < max_unidades * valor_unidade:
#         unidades = int(inv.resgate // valor_unidade)
#     else:
#         unidades = int(50 * inv.resgate / max_resgate)

#     print(f"{color}", end="")
#     for _ in range(unidades):
#         print(char, end="")
#     print(f"{r}")

# def calc_taxa_mensal(inv, indexador):
#     taxa_mensal = (1 + (inv.percentual / 100.0) * indexador) ** (1/12)
#     return taxa_mensal

# def atualizar_investimento(inv, indexador):
#     taxa_mensal = calc_taxa_mensal(inv, indexador)
#     inv.resgate = inv.resgate * taxa_mensal

#     # Se for recorrente, adicionar o valor de entrada mensal
#     if inv.recorrente:
#         inv.investido += inv.aporte
#         inv.resgate += inv.aporte

# def encontrar_resgate_maximo(investimentos):
#     max_resgate = 0.0
#     for inv in investimentos:
#         if inv.resgate > max_resgate:
#             max_resgate = inv.resgate
#     return max_resgate

# def simular_mes(investimentos, data, indexador):
#     print("[SIMULAÇÃO]\n")

#     max_resgate = encontrar_resgate_maximo(investimentos)

#     for inv in investimentos:
#         print_investimento(inv, max_resgate)
#         atualizar_investimento(inv, indexador)

#     print_data(data)
#     avancar_mes(data)

# def sair():
#     time.sleep(delay_curto)
#     print(f"{i}Ok, finalizando a simulação.{r}")
#     time.sleep(delay_longo)
#     print()
#     clear()
#     return False

# # ----------------------------------------------

# # Parte 3, controle do fluxo do programa
# cdi  = 0.1465
# data = Data(1, 5, 2025)
# investimentos = []

# clear()
# intro()

# simular = True
# while simular:

#     resposta = menu()

#     if resposta == "novo":
#         add_investimento(investimentos)

#     elif resposta == "":
#         simular_mes(investimentos, data, cdi)

#     elif resposta == "sair":
#         simular = sair()
