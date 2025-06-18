from empresas import Empresa, empresas
from pessoas import Pessoa, pessoas
import os

class Cores:
    RESET = '\033[0m'
    VERDE = '\033[92m'
    ROXO = '\033[95m'
    AZUL = '\033[94m'
    ITALICO = '\033[3m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

categorias = [
    "Moradia",
    "Alimentação",
    "Transporte",
    "Saúde",
    "Educação"
]

percentuais = [
    0.35, # Moradia
    0.25, # Alimentação
    0.10, # Transporte
    0.10, # Saúde
    0.10, # Educação
]

def get_price(empresa):
    return empresa.custo * (1 + empresa.margem)

def simular_empresa(empresa: Empresa):
    """Prepara a empresa para o novo mês: zera vendas e reabastece a oferta."""
    empresa.vendas = 0
    empresa.oferta += empresa.reposicao

def ajustar_estoque_e_preco(empresa: Empresa):
    """Ao final do mês, a empresa ajusta sua estratégia com base nas vendas."""
    
    if (empresa.vendas + empresa.oferta) > 0 and empresa.oferta == 0:
        empresa.reposicao += 1
        empresa.margem += 0.01
    
    elif empresa.oferta >= 10:
        empresa.reposicao = max(1, empresa.reposicao - 1)
        empresa.margem = max(0.01, empresa.margem - 0.01)

def simular_pessoa(pessoa: Pessoa, empresas: list, categorias: list, percentuais: list):
    """Simula as decisões de compra de uma pessoa para um mês."""
    pessoa.conforto = 0
    rendimento_mensal = pessoa.salario + (pessoa.patrimonio * 0.05) 
    pessoa.patrimonio += rendimento_mensal  

    for i in range(len(categorias)):
        categoria = categorias[i]
        percentual = percentuais[i]
        valor_para_compra = rendimento_mensal * percentual 

        
        produtos_acessiveis = [e for e in empresas if e.categoria == categoria and e.oferta > 0 and get_price(e) <= valor_para_compra]

        produto_a_comprar = None
        if produtos_acessiveis:
            produto_a_comprar = encontra_melhor_produto(produtos_acessiveis)
        else:
           
            estoque_na_categoria = [e for e in empresas if e.categoria == categoria and e.oferta > 0]
            if estoque_na_categoria:
                produto_a_comprar = min(estoque_na_categoria, key=get_price)
        
        
        if produto_a_comprar and pessoa.patrimonio >= get_price(produto_a_comprar):
            compra(produto_a_comprar, pessoa)

def compra(produto: Empresa, pessoa: Pessoa):
    """Processa a transação de compra e venda."""
    preco_pago = get_price(produto)
    produto.oferta -= 1
    produto.vendas += 1
    pessoa.patrimonio -= preco_pago
    pessoa.conforto += produto.qualidade

def encontra_melhor_produto(produtos_acessiveis: list):
    """Encontra o produto de maior qualidade em uma lista."""
    maior_qualidade = -1
    produto_ideal = None
    for produto in produtos_acessiveis:
        if produto.qualidade > maior_qualidade and produto.oferta > 0:
            maior_qualidade = produto.qualidade
            produto_ideal = produto
    return produto_ideal

def simular_mercado(pessoas, empresas, categorias, percentuais):
    """Executa um ciclo completo de simulação de mercado para um mês."""
    
    for empresa in empresas:
        simular_empresa(empresa)
    
    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais)
 
    for empresa in empresas:
        ajustar_estoque_e_preco(empresa)



def print_pessoas(pessoas):
    print("\n[PESSOAS]")
    print(f"{Cores.ITALICO}Divisão da renda mensal | Moradia {Cores.AMARELO}35.0%{Cores.RESET}{Cores.ITALICO} | Alimentação {Cores.AMARELO}25.0%{Cores.RESET}{Cores.ITALICO} | Transporte {Cores.AMARELO}10.0%{Cores.RESET}{Cores.ITALICO} | Saúde {Cores.AMARELO}10.0%{Cores.RESET}{Cores.ITALICO} | Educação {Cores.AMARELO}10.0%{Cores.RESET}{Cores.ITALICO} | Totalizando {Cores.AMARELO}90.0%{Cores.RESET}{Cores.ITALICO} da renda mensal total.")
    print(f"Gráfico de Barras | Legenda: {Cores.AZUL}Conforto{Cores.RESET}, {Cores.VERDE}Salário{Cores.RESET}, {Cores.ROXO}Rendimentos{Cores.RESET}{Cores.ITALICO} | Cada traço = R$1000.00{Cores.RESET}")

    max_barras = 10
    colunas_conforto = []
    colunas_renda = []

    for pessoa in pessoas:
        # ---- Barras de Conforto (acima da linha) ----
        media_conforto = pessoa.conforto / len(categorias) if categorias else 0
        barras_conforto = min(max_barras, int(media_conforto))
        coluna_conforto = [' '] * (max_barras - barras_conforto) + [f"{Cores.AZUL}|{Cores.RESET}"] * barras_conforto
        colunas_conforto.append(coluna_conforto)

        # ---- Barras de Rendimento (abaixo da linha) ----
        rendimento_mensal = pessoa.salario + pessoa.patrimonio * 0.05
        total_barras_renda = min(max_barras, int(rendimento_mensal / 1000))

        barras_salario = min(total_barras_renda, int(pessoa.salario / 1000))
        barras_patrimonio = total_barras_renda - barras_salario

        coluna_renda = (
            [f"{Cores.VERDE}|{Cores.RESET}"] * barras_salario +
            [f"{Cores.ROXO}|{Cores.RESET}"] * barras_patrimonio +
            [' '] * (max_barras - total_barras_renda)
        )
        colunas_renda.append(coluna_renda)

    # ---- Parte de cima (Conforto - de cima pra baixo) ----
    for i in range(max_barras):
        linha = ''.join(coluna[i] for coluna in colunas_conforto)
        print(linha)

    # ---- Linha divisória ----
    print('-' * len(pessoas))

    # ---- Parte de baixo (Renda - de cima pra baixo também) ----
    for i in range(max_barras):
        linha = ''.join(coluna[i] for coluna in colunas_renda)
        print(linha)






def print_empresas(empresas):
    print("\n[EMPRESAS]")
    for empresa in empresas:
        preco = get_price(empresa)
        lucro_total = empresa.vendas * (preco - empresa.custo)

        vendas_barras = '$' * (empresa.vendas // 5)

        print(f"{empresa.categoria:<12} {empresa.nome.strip():<15}: {empresa.produto.strip():<15} {Cores.AZUL}Q={empresa.qualidade:<2}{Cores.RESET}\
              Margem:{Cores.AMARELO} {empresa.margem*100:<4.1f}%{Cores.RESET}\t\
              Custo:{Cores.VERMELHO} R$ {empresa.custo:<8.2f}{Cores.RESET}\t\
              Preço: R$ {Cores.VERDE}{preco:<8.2f}{Cores.RESET}\t\
              Lucro T.: R$ {Cores.VERDE}{lucro_total:<10.2f}{Cores.RESET}\t Vendas: {Cores.VERDE}{vendas_barras}{Cores.RESET}")

def main():
    simular = True
    
    while simular:
        clear()
        print("[SIMULADOR DE RELAÇÕES DE MERCADO]")
        print_pessoas(pessoas)
        print_empresas(empresas)
        
        resposta = input("\nDigite um número para avançar N meses, 'enter' para avançar 1 mês ou 'sair' para encerrar: ")
        
        if resposta.lower() == 'sair':
            simular = False
        elif resposta.isdigit() and int(resposta) > 0:
            meses = int(resposta)
            for _ in range(meses):
                simular_mercado(pessoas, empresas, categorias, percentuais)
        elif resposta == "":
            simular_mercado(pessoas, empresas, categorias, percentuais)

if __name__ == "__main__":
    main()