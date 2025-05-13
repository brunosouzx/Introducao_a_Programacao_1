
print("=====================================")
print("")

#DESAFIO 1

nome_completo = 'Antonieta da Silva'
dia_nascimento = 16
mes_nascimento = 5
ano_nascimento = 1998

print(f'{nome_completo}, nascida em {dia_nascimento}/{mes_nascimento}/{ano_nascimento}')

dias_ano = 365
anos_vividos = 2025 - ano_nascimento
dias_totais = (anos_vividos * dias_ano) - 2

idade_atual = dias_totais//dias_ano

print(f'{nome_completo} tem {dias_totais} dias de vida')
print(f'{nome_completo} tem {idade_atual} anos de idade')

print("")
print("\n=====================================\n")
print("")

#DESAFIO 2

patrimonio = 2000
recebimentos_mensais = 1518.00
gastos = 1077.0
investimentos_mensais = 150

salario_minimo = 1518.00
equivalente_salario_minimo = recebimentos_mensais/salario_minimo

gasto_por_renda = (gastos/recebimentos_mensais)*100


RENDIMENTO_MES = 0.005

rendimento = patrimonio * RENDIMENTO_MES

patrimonio_total= patrimonio + rendimento + investimentos_mensais

saldo_final = recebimentos_mensais - investimentos_mensais - gastos

print(f'{nome_completo}, recebe mensalmente : R$ {recebimentos_mensais}')
print(f'Os recebimentos equivalem a {equivalente_salario_minimo} salário(s) mínimo(s)')
print(f'{nome_completo}, tem patrimônio de : R$ {patrimonio}')
print(f'{nome_completo}, gasta: R$ {gastos}')
print(f'Os gastos equivalem a {gasto_por_renda}% da sua renda') #gosto por roenda
print(f'{nome_completo}, investe mensalmente :R$ {investimentos_mensais}')
print(f'{nome_completo} após 1 mês etsá com o patrimonio de R${patrimonio_total}')  #apos um mes ela ta com  patrimonio
print(f' O saldo de dinheiro livre no mês foi de R${saldo_final}')

print("")
print("=====================================")
print("")

#DESAFIO 3

patrimonio_12_meses=patrimonio*(1+RENDIMENTO_MES)**12
rendimento_total = patrimonio_12_meses - patrimonio

print(f'Se {nome_completo} não investir nada, após 12 meses o seu patrimônio terá rendido R${rendimento_total} e será R${patrimonio_12_meses}')




