def simulador_poupanca():

  saldo = float(input('Valor inicial do investimento: '))

  taxa = float(input('Taxa de juros mensal: '))

  meses = int(input('Número de meses da simulação: '))



  for i in range(meses):

    aporte = float(input(f'Quanto deseja depositar no {i + 1}° mês? '))



    saldo += aporte

    juros = saldo * (taxa/100)

    saldo += juros



    print(f'Mês {i + 1}: Saldo atualizado = R${saldo:.2f}')



    if saldo > 10000:

      print(f'Parabéns! Você atingiu a meta de 10k no mês {i}.')

    

  print(f'Resultado final após {meses} meses: R${saldo:.2f}')



simulador_poupanca()
