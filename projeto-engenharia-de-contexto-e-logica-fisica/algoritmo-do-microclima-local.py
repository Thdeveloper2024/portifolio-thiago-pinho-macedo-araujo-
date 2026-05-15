def analisar_microclima():
    
    lugares = [
 
        ["parque dompedro", 29, 200, 97],  # nome | temp | qualidade do ar | umidade
    
        ["parque do carmo", 24, 70, 60],
    
        ["Aricanduva", 28, 160, 50]
    ]
 
    for linha in lugares:
    
        nota_temperatura = 0
    
        nota_ar = 0
    
        nota_umidade = 0
    
        for index_info, info in enumerate(linha, start=1):
    
            match index_info:
    
                case 2:
    
                    if info < 12 or info > 35:
    
                        nota_temperatura = 0
    
    
    
                    elif info < 18 or info > 30:
    
                        nota_temperatura = 4
    
    
    
                    elif info < 20 or info > 24:
    
                        nota_temperatura = 7
    
    
    
                    elif info >= 20 and info <= 23:
    
                        nota_temperatura = 10
    
                case 3:
    
                    if info < 50:
    
                        nota_ar = 10
    
    
    
                    elif info < 100:
    
                        nota_ar = 8
    
    
    
                    elif info < 150:
    
                        nota_ar = 6
    
    
    
                    elif info < 200:
    
                        nota_ar = 4
    
    
    
                    elif info < 300:
    
                        nota_ar = 2
    
    
    
                    elif info > 300:
    
                        nota_ar = 0
    
                case 4:
    
                    if info > 80 or info < 12:
    
                        nota_umidade = 0
    
    
    
                    elif info < 40 or info > 70:
    
                        nota_umidade = 3
    
    
    
                    elif info < 50 or info > 60:
    
                        nota_umidade = 7
    
    
    
                    elif info > 50 and info < 60:
    
                        nota_umidade = 10
    
        nota_final = (nota_ar + nota_umidade + nota_temperatura) / 3
    
        print('\n' + '=' * 40 + '\n')
    
        print(
            f"LUGAR: {linha[0]}\nNOTA DO AR: {nota_ar}\nNOTA DA UMIDADE: {nota_umidade}\nNOTA_TEMPERATURA: {nota_temperatura}\n\nNOTA FINAL: {nota_final:.2f}")
 
analisar_microclima()