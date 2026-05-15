def processar_vendas():

  total_compra = 0.0

  itens_comprados = 0



  quantidades_tipos = int(input("Quantos produtos diferentes foram comprados?"))



  for i in range(quantidades_tipos):

    nome = input("Digite o nome do produto: ")

    preco = float(input("Preço unitário: "))

    qtd = int(input("Quantos itens comprados?"))



    if preco <= 0 or qtd <= 0:

      return "Erro: Valores inválidos para ", nome

    else:

      subtotal = preco *qtd

      total_compra += subtotal

      itens_comprados += 1



  if total_compra > 500:

    total_final = total_compra *0.90 # 10 % de desconto

    print("Desconto de 10% aplicado!")

  elif total_compra > 200:

    total_final = total_compra * 0.95 # 5 % de desconto

  else:

    total_final = total_compra



  print(f"Foram comprados: {itens_comprados} produtos\nTotal a pagar: R${total_final}")



processar_vendas()
