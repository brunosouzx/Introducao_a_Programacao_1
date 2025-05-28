# flake8: noqa

import os  # importa a função que serve para limpar o terminal
from sys import exit  # importa a função que serve para encerrar o codigo
from time import sleep  # serve para dar intervalo de tempo para o cadigo

os.system("cls")


# =====[ CORES ]=====
R = '\033[31m'  # Vermelho
G = '\033[32m'  # Verde
B = '\033[34m'  # Azul
Y = '\033[33m'  # Amarelo
P = '\033[35m'  # Roxo
C = '\033[36m'  # Ciano
W = '\033[37m'  # Branco
i = '\033[3m'  # Itálico
n = '\033[7m'  # Negativo
r = '\033[0m'  # Resetar

# =====[ Tempo ]=====
tempo_longo = 1.0
tempo_curto = 0.5

# =====[ JUROS ]=====
IPCA = 5.53  # Ao ano (inflação)
CDI = 14.65  # Ao ano (juros)
POUPANCA = 6.00  # Ao ano

# INICIO DO WHILE COMO "MENU"
while True:

    print("SIMULADOR DE INVESTIMENTOS")
    sleep(tempo_longo)
    print(f'{i}Olá, vou te ajudar a simular as possibilidades de investimentos {r}\n')
    sleep(tempo_longo)
    print(
        f'Para começar, quero te dizer que as {B}taxas anuais{r} que estou utilizando são:')
    sleep(tempo_curto)

    print(f'{B}IPCA{r} (inflação): {P}{IPCA}%{r}')
    sleep(tempo_curto)
    print(f'{B}CDI{r} (juros):.... {P}{CDI}%{r}')
    sleep(tempo_curto)
    print(f'{B}Poupança{r}:....... {P}{POUPANCA}%{r}\n')
    sleep(tempo_longo)

    valor_investido = int(
        input(f'Agora me informa o valor em reais que você quer investir {G}R$ '))
    sleep(tempo_longo)
    print(f'{r}{i}Ok, registrei o valor do seu investimento.{r}\n')
    sleep(tempo_longo)

    while True:   # WHILE PARA TRATAR ERRO E FAZER O CODIGO NÃO PARAR E NEM DA ERRO
        os.system("cls")

        print("Essas são as opções de investimento que tenho disponíveis para você:")
        sleep(tempo_curto)
        print(
            f' {Y}[A]{r} {B}CDB{r} valendo 100% do CDI, taxa final de {P}14.65%{r}')
        sleep(tempo_curto)
        print(
            f' {Y}[B]{r} {B}CDB{r} valendo 110% do CDI, taxa final de {P}16.12%{r}')
        sleep(tempo_curto)
        print(
            f' {Y}[C]{r} {B}CDB{r} valendo 120% do CDI, taxa final de {P}17.58%{r}')
        sleep(tempo_curto)
        print(
            f' {Y}[D]{r} {B}LCA{r} valendo 95% do CDI, taxa final de {P}13.92%{r}\n')
        sleep(tempo_longo)
        print(
            'Obs: Lembre que o CDB retém IR na fonte, enquanto a LCA não.')
        sleep(tempo_longo)

        tipo_investimento = input(
            f'Qual o investimento que você quer fazer? ({Y}A{r}, {Y}B{r}, {Y}C{r} ou {Y}D{r}): ')

        if tipo_investimento.upper() == "A" or "B" or "C" or "D":
            break
        else:
            print(f"{R}OPÇÂO INVALIDA!{r}")
            sleep(tempo_longo*2)

    rendimento_anual = 0
    if tipo_investimento.upper() == "A":
        rendimento_anual = CDI
    elif tipo_investimento.upper() == "B":
        rendimento_anual = CDI * 1.1
    elif tipo_investimento.upper() == "C":
        rendimento_anual = CDI * 1.2
    else:
        rendimento_anual = CDI * 0.95

    rendimento_anual_decimal = rendimento_anual / 100

    rendimento_mensal_decimal = (rendimento_anual_decimal + 1) ** (1/12) - 1

    rendimento_mensal_porcentagem = rendimento_mensal_decimal * 100

    if tipo_investimento.upper() != "D":
        print(tipo_investimento)
        print(
            f"Como você escolheu {B}CDB{r} vou te lembrar as taxas regressivas de IR(Imposto de Renda):")
        sleep(tempo_curto)
        print(f'Até 6 meses:...... {P}22.50%{r}')
        sleep(tempo_curto)
        print(f'Até 12 meses:..... {P}20.00%{r}')
        sleep(tempo_curto)
        print(f'Até 23 meses:..... {P}17.50%{r}')
        sleep(tempo_curto)
        print(f'Acima de 24 meses: {P}15.00%{r}\n')
        sleep(tempo_longo)

    tempo_investimento = int(input(
        f'Quanto tempo você gostaria de esperar para resgatar esse investimento? (em meses){B} '))
    sleep(tempo_longo)
    print(f'{r}{i}Ok, registrei o tempo para o resgate.\n')
    sleep(tempo_longo)

    # ===== CALCULO =====

    #   imposto de renda
    if tipo_investimento.upper() != "D":
        if tempo_investimento < 6:
            valor_IR = 22.5
        elif tempo_investimento < 12:
            valor_IR = 20.0
        elif tempo_investimento < 24:
            valor_IR = 17.5
        else:
            valor_IR = 15.0
    else:
        valor_IR = 0

    print("TAXAS UTILIZADAS")
    sleep(tempo_curto)
    print(f'- Taxa de IR aplicada:...... {P}{valor_IR:.2f}%{r}')
    print(f'- Taxa de rendimento anual:. {P}{rendimento_anual:.2f}%{r}')
    print(
        f'- Taxa de rendimento mensal {P}{rendimento_mensal_porcentagem:.2f}%{r}'
    )
    print('\n')

    montante = valor_investido * \
        (1 + rendimento_mensal_decimal) ** tempo_investimento

    lucro_bruto = montante - valor_investido

    imposto_de_renda_deduzido = lucro_bruto * (valor_IR/100)

    resgate_liquido = montante - imposto_de_renda_deduzido

    lucro_total = resgate_liquido - valor_investido

    taxa_poupanca_mensal = (POUPANCA/100)/12

    montante_poupanca = valor_investido * \
        (1 + taxa_poupanca_mensal) ** tempo_investimento

    lucro_total_poupanca = montante_poupanca - valor_investido

    diferenca_lucro_poupanca = lucro_total - lucro_total_poupanca

    taxa_inflacao_anual = 5.53/100

    taxa_inflacao_mensal = taxa_inflacao_anual/12

    inflacao_acumulada = (1 + taxa_inflacao_mensal) ** tempo_investimento

    inflacao_acumulada_porcentagem = inflacao_acumulada*100

    valor_corrigido = valor_investido * inflacao_acumulada

    desvalorizacao = (1 / inflacao_acumulada) * 100

    resgate_proporcional = resgate_liquido / inflacao_acumulada

    poupanca_proporcional = montante_poupanca / inflacao_acumulada

    print("RESULTADO")
    sleep(tempo_curto)
    print(f'Valor investido:...... {G}R$ {valor_investido:.2f}{r}')
    sleep(tempo_curto)
    print(f'Remendo pelo tempo de: {B}{tempo_investimento} meses{r}')
    sleep(tempo_curto)
    print(f'Dedução de IR de:..... {P}{valor_IR:.2f}%{r}')
    sleep(tempo_curto)
    print(f'Valor deduzido é de:.. {G}R$ {imposto_de_renda_deduzido:.2f} {r}')
    sleep(tempo_curto)
    print(f'O resgate será de:.... {G}R$ {resgate_liquido:.2f} {r}')
    sleep(tempo_curto)
    print(f'O lucro total será:... {G}R$ {lucro_total:.2f} {r}')
    sleep(tempo_longo)

    analises_adicionais = input(
        f"{i}Você gostaria de ver algumas análises adicionais (sim/não)?{r} ")
    sleep(tempo_longo)

    if analises_adicionais.upper() == "NÃO":
        print('\n')
        print("RESUMO")
        sleep(tempo_curto)
        print(f'Valor investido:..... {G}R${valor_investido:.2f}{r}')
        sleep(tempo_curto)
        print(f'Valor resgatado:..... {G}R$ {resgate_liquido:.2f}{r}')
        sleep(tempo_curto)
        print(f'Se fosse na poupança: {G}R$ {montante_poupanca:.2f}{r}')
        sleep(tempo_curto)
        print(f'Correção da inflação: {G}R$ {valor_corrigido:.2f}{r}')
        sleep(tempo_longo)

        print('\n')
        print(f'{i}Espero ter ajudado!')
        break

    print('\n')
    print("ANÁLISES POUPANÇA")
    sleep(tempo_curto)
    print(f'Se você tivesse investido: {G}R${valor_investido:.2f}{r}')
    sleep(tempo_curto)
    print(f'na poupança, ao final dos: {B}{tempo_investimento} meses{r}')
    sleep(tempo_curto)
    print(f'o valor resgatado seria:.. {G}R$ {montante_poupanca:.2f}{r}')
    sleep(tempo_curto)
    print(f'e o lucro total:.......... {G}R$ {lucro_total_poupanca:.2f}{r}')
    sleep(tempo_curto)
    print(
        f'A diferença de lucro é de: {G}R$ {diferenca_lucro_poupanca:.2f}{r}')
    sleep(tempo_longo)

    print('\n')
    print("ANÁLISE DE INFLAÇÃO")
    sleep(tempo_curto)
    print(
        f'A inflação acumulada foi de:........................ {P}{inflacao_acumulada_porcentagem:.2f}%{r}'
    )
    sleep(tempo_curto)
    print(
        f'resultando em uma desvalorização de :................ {P}{desvalorizacao:.2f}%{r}')
    sleep(tempo_curto)
    print(
        f'Por exemplo, se você comprava algo por:............. {G}R$ {valor_investido:.2f}{r}')
    sleep(tempo_curto)
    print(
        f'o mesmo item custaria corrigido pela inflação será:. {G}R$ {valor_corrigido:.2f}{r}')
    sleep(tempo_curto)
    print(
        f'O resgate proporcionalmente ao valor corrigido fica: {G}R$ {resgate_proporcional:.2f}{r}')
    sleep(tempo_curto)
    print(
        f'Já na poupança o proporcional a essa correção seria: {G}R$ {poupanca_proporcional:.2f}{r}')
    sleep(tempo_longo)

    print('\n')
    print("RESUMO")
    sleep(tempo_curto)
    print(f'Valor investido:..... {G}R${valor_investido:.2f}{r}')
    sleep(tempo_curto)
    print(f'Valor resgatado:..... {G}R$ {resgate_liquido:.2f}{r}')
    sleep(tempo_curto)
    print(f'Se fosse na poupança: {G}R$ {montante_poupanca:.2f}{r}')
    sleep(tempo_curto)
    print(f'Correção da inflação: {G}R$ {valor_corrigido:.2f}{r}')
    sleep(tempo_longo)

    print(f'{i}Espero ter ajudado!')

    while True:  # WHILE PARA TRATAR ERRO E FAZER O CODIGO NÃO PARAR E NEM DA ERRO
        # E FAZER COM QUE REPITA SEM PRECISAR INICIAR O CODIGO NOVAMENTE
        print("deseja fazer uma nova simulação?")
        sleep(tempo_longo)
        continuar = input(f"digite {G}s{r}/{R}n{r}:  ")
        if continuar.upper() == "N":
            exit()
        elif continuar.upper() == "S":
            break
        else:
            print(f"{R}OPÇÂO INVALIDA!{r}")

    os.system("cls")
