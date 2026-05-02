# -*- coding: utf-8 -*-

# Limite de segurança definido
limite_seguranca = 10000

# Função para analisar as vendas
def analisar_vendas():
    global limite_seguranca

    media = sum(vendas) / len(vendas)
    print(f"O valor medio das vendas é: {media:.2f}")
    print("-" * 40)

    if media > limite_seguranca:
        print("SISTEMA EM QUARENTENA")
        print("-" * 40)

    # laço para indicação de revisão manual (discrepancia detectada)
    for venda in vendas:
        if venda > 5 * media:
            print("DISCREPÂNCIA DETECTADA (Revisão manual indicada).")
            print("-" * 40)
            break

    # laço para edição dos valores
    for venda in vendas:
        if venda > limite_seguranca:
            novo_valor = input(
                f"A venda {venda:.2f} ultrapassou o limite de segurança. Deseja alterar o limite? (sim / nao): "
            ).lower()

            if novo_valor == "sim":
                n_limite = float(input("Digite o novo limite de segurança: "))
                limite_seguranca = n_limite
                print("Novo limite de segurança definido")
                print("-" * 40)
                break

            elif novo_valor == "nao":
                print("Usuário manteve o limite de segurança atual")
                print("-" * 40)
                break

            else:
                print("Erro, comando incorreto")
                print("-" * 40)

# Lista com os valores das 3 vendas
vendas = []

for i in range(3):
    valor = float(input(f"Digite o valor da venda {i + 1}: "))
    print("-" * 40)
    vendas.append(valor)

analisar_vendas()

for venda in vendas:
    print(f"Valor: {venda:.2f}\nTipo da variável: {type(venda)}")
