# flake8: noqa

# from miniprojeto5.empresas import empresas
# from miniprojeto5.pessoas import pessoas
from empresas import Empresa, empresas
from pessoas import Pessoa, pessoas

categorias = [
    "Moradia",
    "Alimentação",
    "Transporte",
    "Saúde",
    "Educação"
]
percentuais = [
    0.35,  # Moradia
    0.25,  # Alimentação
    0.10,  # Transporte
    0.10,  # Saúde
    0.10,  # Educação
]


def simular_empresa(empresa: Empresa):
    empresa.oferta += empresa.reposicao

    if empresa.oferta == 0:
        empresa.reposicao += 1
        empresa.margem += 0.01

    elif empresa.oferta >= 10:
        empresa.reposicao -= 1
        empresa.margem -= 0.01


def simular_pessoa(pessoa: Pessoa, empresas: list,
                   categorias: list, percentuais: list):

    rendimento_mensal = pessoa.salario + (pessoa.patrimonio * 0.05)

    # Para cada categoria, a pessoa tentará fazer UMA compra
    for i in range(len(categorias)):
        categoria = categorias[i]
        percentual = percentuais[i]
        valor_para_compra = rendimento_mensal * percentual

        produtos_acessiveis_para_escolha = []
        for empresa in empresas:
            if empresa.categoria == categoria and empresa.oferta > 0 and \
               empresa.custo <= valor_para_compra:
                produtos_acessiveis_para_escolha.append(empresa)

        if produtos_acessiveis_para_escolha:
            produto_ideal = encontra_melhor_produto(
                produtos_acessiveis_para_escolha)

            if produto_ideal and produto_ideal.oferta > 0:
                compra(produto_ideal, pessoa)

        else:
            empresas_na_categoria_com_estoque = [
                e for e in empresas if e.categoria == categoria and e.oferta > 0
            ]

            if empresas_na_categoria_com_estoque:
                produtos_baratos = sorted(
                    empresas_na_categoria_com_estoque, key=lambda e: e.custo, reverse=False
                )
                produto_mais_barato = produtos_baratos[0]

                if produto_mais_barato.oferta > 0 and pessoa.patrimonio >= produto_mais_barato.custo:
                    compra(produto_mais_barato, pessoa)


def compra(produto_ideal: Empresa, pessoa: Pessoa):
    # Print para teste
    print(f'{pessoa.patrimonio} comprou produto: {produto_ideal.nome} na categoria {produto_ideal.categoria}')
    produto_ideal.oferta -= 1
    produto_ideal.vendas += 1
    pessoa.patrimonio -= produto_ideal.custo


def encontra_melhor_produto(produtos_acessiveis: list):
    maior_qualidade = 0
    produto_ideal = None
    for produto in produtos_acessiveis:
        if produto.qualidade > maior_qualidade and produto.oferta > 0:
            maior_qualidade = produto.qualidade
            produto_ideal = produto

    return produto_ideal


def simular_mercado(pessoas, empresas, categorias, percentuais):
    # Atualização das empresas e produtos
    for empresa in empresas:
        simular_empresa(empresa)

    # Atualização das pessoas e seus patrimônios
    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais)


def main():
    # simular = True
    # while simular:
    #     clear()
    #     print("[SIMULADOR DE RELAÇÕES DE MERCADO]")
    #     print_pessoas(pessoas)
    #     print_empresas(empresas)

    #     # Aperte enter para avançar em 1 mês, digite um número para avançar N meses ou "sair" para encerrar
    #     resposta = input(
    #         "\nDigite um número para avançar N meses, 'enter' para avançar 1 mês ou 'sair' para encerrar: ")
    #     if resposta.isdigit():
    #         meses = int(resposta)
    #         for _ in range(meses):
    #             simular_mercado(pessoas, empresas, categorias, percentuais)
    #     elif resposta == "":
    #         simular_mercado(pessoas, empresas, categorias, percentuais)
    #     elif resposta == "sair":
    #         simular = False

    for empresa in empresas:
        print(empresa)

    for pessoa in pessoas:
        print(pessoa)

    simular_mercado(pessoas, empresas, categorias, percentuais)

    print('Depois da simulação\n')
    for empresa in empresas:
        print(empresa)

    for pessoa in pessoas:
        print(pessoa)


# Iniciar a simulação
if __name__ == "__main__":
    main()
