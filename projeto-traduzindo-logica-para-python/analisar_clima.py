def analisar_clima():

  soma_temperaturas = 0.0

  dias_quentes = 0

  alerta_extremo = False



  for dia in range(7):

    temp = float(input(f"Digite a temperatura do {dia +1}° dia: "))

    soma_temperaturas += temp



    if temp > 35.0:

      dias_quentes = dias_quentes + 1



    if temp < 45.0 or temp < -5.0:

      alerta_extremo = True





  media = soma_temperaturas / 7

  print("Media semanal: ",media)

  print("Dias acima de 35°C: ", dias_quentes)



  if alerta_extremo:

    print("CUIDADO: Condições climáticas perigosas detectadas!")



  else:

    print("Clima dentro da normalidade operacional.")



analisar_clima()



