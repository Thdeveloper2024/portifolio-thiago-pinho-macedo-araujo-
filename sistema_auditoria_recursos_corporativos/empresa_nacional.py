```python

# EMPRESA NACIONAL - SÃO PAULO
# Sistema de Controle Orçamentário


# ESTRUTURA DE DADOS DA EMPRESA
empresa_data = {

    "Matriz_SP": {

        "InformacoesEmpresa": {
            "Nome": "TechNova Soluções",
            "Cidade": "São Paulo",
            "Tipo": "Empresa Nacional",
            "Funcionarios": 185
        },

        "Tecnologia": {

            "Infraestrutura": {
                "Servidores": 18000,
                "Seguranca": 12000,
                "Backup": 6000,
                "Cloud": 15000
            },

            "Desenvolvimento": {
                "Frontend": 10000,
                "Backend": 12000,
                "DevOps": 7000,
                "QA": 5000,

                "Mobile": {
                    "Android": 4000,
                    "iOS": 4500
                }
            },

            "Suporte": {
                "HelpDesk": 3500,
                "Monitoramento": 2500
            }
        },

        "RH": {

            "Recrutamento": 5000,
            "Treinamento": 4500,

            "Cultura": {
                "Eventos": 2500,
                "Brindes": 1200,
                "Campanhas": 1800
            }
        },

        "Financeiro": {
            "Auditoria": 7000,
            "Contabilidade": 9000,
            "FolhaPagamento": 35000
        },

        "Comercial": {

            "Marketing": {
                "Publicidade": 10000,
                "RedesSociais": 4000
            },

            "Vendas": {
                "Comissoes": 12000,
                "CRM": 3500
            }
        }
    }
}



# BIBLIOTECA TIME


import time



# DECORATOR DE AUDITORIA


def auditor(func):

    def wrapper(*args, **kwargs):

        print("\n===== AUDITORIA FINANCEIRA =====")
        print("Iniciando análise orçamentária...\n")

        print(f"Departamentos ignorados (*args): {args[1:]}")
        print(f"Parâmetros financeiros (**kwargs): {kwargs}")

        inicio = time.time()

        resultado = func(*args, **kwargs)

        fim = time.time()

        print(f"\nTempo total de execução: {fim - inicio:.6f} segundos")
        print("===== FIM DA AUDITORIA =====\n")

        return resultado

    return wrapper

# FUNÇÃO RECURSIVA

@auditor
def calcular_orcamento(
        estrutura,
        *departamentos_ignorados,
        moeda_destino="BRL",
        taxa_cambio=1.0):

    total = 0

    # Percorre todo o dicionário
    for chave, valor in estrutura.items():

        # Ignora departamentos
        if chave in departamentos_ignorados:
            print(f"\nDepartamento ignorado: {chave}")
            continue

        # Se for outro dicionário -> recursão
        if isinstance(valor, dict):

            total += calcular_orcamento(
                valor,
                *departamentos_ignorados,
                moeda_destino=moeda_destino,
                taxa_cambio=1.0
            )

        # Soma apenas valores numéricos
        elif isinstance(valor, (int, float)):

            total += valor

    # Conversão financeira
    total_convertido = total * taxa_cambio

    return total_convertido


# ORÇAMENTO COMPLETO

print("===== ORÇAMENTO COMPLETO =====")

orcamento_total = calcular_orcamento(
    empresa_data,
    moeda_destino="BRL",
    taxa_cambio=1.0
)

print(f"\nOrçamento total da empresa: R$ {orcamento_total:,.2f}")



# ORÇAMENTO FILTRADO

print("\n===== ORÇAMENTO FILTRADO =====")

orcamento_filtrado = calcular_orcamento(
    empresa_data,
    "RH",
    "Comercial",
    moeda_destino="USD",
    taxa_cambio=0.18
)

print(f"\nOrçamento convertido: US$ {orcamento_filtrado:,.2f}")
```
