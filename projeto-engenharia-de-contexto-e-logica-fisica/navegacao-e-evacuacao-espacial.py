def saida_fuga():
    
    locais = ["laboratorio", "corredor", "escada um", "escada dois", "saida alfa", "saida fundo", "saida rua"]
 
    estado = ["porta trancada", "livre", "livre", "livre", "3 voltas", "4 voltas", "2 voltas"]
 
    posicao = 0
    inventario = []
    energia = 25
    voltas_dadas = 0
    fugiu = False
 
    print("=== SIMULADOR: BUSCA PELA SAÍDA EFICIENTE ===")
 
    while energia > 0 and not fugiu:
 
        local_atual = locais[posicao]
 
        condicao = estado[posicao]
 
        print(f"\nLocal: {local_atual} | Energia: {energia}")
 
        if condicao == "porta trancada":
 
            if "chave" in inventario:
 
                print("-> Porta aberta com a chave!")
 
                posicao += 1
 
            else:
 
                print("-> Procurando chave...")
 
                inventario.append("chave")
 
 
 
        elif condicao == "livre":
 
            print("-> Atravessando área livre...")
 
            posicao += 1
 
 
 
        elif "voltas" in condicao:
 
            limite_voltas = int(condicao.split()[0])
 
            if voltas_dadas < limite_voltas:
 
                voltas_dadas += 1
 
                print(f"-> Dando volta {voltas_dadas} de {limite_voltas} em {local_atual}...")
 
 
 
            else:
 
                print(f"-> {local_atual} concluída! Saindo para a rua...")
 
                voltas_dadas = 0
 
                fugiu = True
 
        energia -= 1
 
    if fugiu:
 
        print(f"\n[SUCESSO] O agente escapou pela {locais[posicao]}!")
 
    else:
 
        print("\n[FALHA] O agente exauriu suas forças.")
 
 
saida_fuga()