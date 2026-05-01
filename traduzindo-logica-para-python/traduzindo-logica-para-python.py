"""
Definições de siglas:

    if = se
    elif = se não, se
    else = se não
    return = retornar um valor e encerrar a função
    for = para (laço de repetição)
    in = em (usado para iterar sobre uma sequência)
    range = intervalo (usado para gerar uma sequência de números)
    int = número inteiro
    float = número decimal (número real)
    input = entrada de dados (função para ler dados do usuário)
    print = imprimir (função para exibir informações na tela)
    def = definir uma função
    or = ou (operador lógico)
    and = e (operador lógico)
    para fechar uma função basta digitar nome função()
    
"""


# 1. Função: processar_vendas

def processar_vendas():
    total_compra = 0.0
    itens_comprados = 0
    
    quantidade_tipos = int(input("Quantos produtos diferentes foram comprados?"))

    for i in range(quantidade_tipos):
        
        #(nome) serve como uma variavel.
        nome = input("Digite o nome do produto:")
        
        # float/numero real, para aceitar valores decimais   
        preco = float(input("Digite o preço do produto:"))
        
        # int/numero inteiro, para aceitar valores inteiros SEM .
        qtd = int(input("Digite a quantidade deste produto:"))
        
        if preco <= 0 or qtd <= 0:
            return "Preço e quantidade devem ser maiores que zero,{nome}" 
        
        else:
            subtotal = preco * qtd
            total_compra = total_compra + subtotal
            itens_comprados = itens_comprados + qtd
            
        if total_compra > 500:
            total_final = total_compra * 0.90 # 10% de desconto
            print("Desconto de 10% aplicado!")
        elif total_compra > 200:
            total_final = total_compra * 0.95 # 5% de desconto
            print("Desconto de 5% aplicado!")
        else:
            total_final = total_compra
            print("Resumo:", itens_comprados, "itens, total a pagar: R$", total_final)
             
processar_vendas()
            
# 2. Função: analisar_clima        
     
def analisar_clima():
    soma_temperaturas = 0.0
    dias_quentes = 0
    alerta_extremo = False
         
    for dia in range(1, 8):
        temp = float(input(f"Digite a temperatura do dia {dia}: "))
        soma_temperaturas = soma_temperaturas + temp
        
        if temp > 35:
            dias_quentes = dias_quentes + 1
            
        if temp > 45 or temp < -5:
            alerta_extremo = True
            
            media = soma_temperaturas / 7
            print("Média das temperaturas:", media)
            print("Número de dias com temperatura acima de 35°C:", dias_quentes)
            
        if alerta_extremo == True:
            print("CUIDADO: Condições climáticas perigosas detectadas!")
        else:
            print("Clima dentro da normalidade operacional.")
            
            
analisar_clima()
                   
                
                           
         
            


        
        
        
        
    
    