# 📊 Sistema Multifuncional em Python

## 📝 Descrição do Projeto

Este projeto consiste em um conjunto de sistemas desenvolvidos em Python
com foco em lógica de programação, entrada de dados e tomada de decisão.
Ele reúne diferentes funcionalidades práticas que simulam situações do
dia a dia, como controle de vendas, análise climática, gestão de notas
escolares e simulação de investimentos.

O objetivo principal é exercitar conceitos fundamentais da programação,
como estruturas condicionais, loops, validação de dados e operações
matemáticas, proporcionando uma base sólida para o desenvolvimento de
sistemas mais complexos.

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

-   **Linguagem:** Python 3.x\
-   **Paradigma:** Programação estruturada\
-   **Execução:** Terminal / Console

------------------------------------------------------------------------

## 📊 Funcionalidades do Sistema

### 🛒 Processamento de Vendas

-   Cálculo automático de compras\
-   Aplicação de descontos progressivos\
-   Validação de dados

### 🌡️ Análise Climática

-   Média semanal\
-   Identificação de dias quentes\
-   Alertas climáticos

### 🎓 Sistema de Notas

-   Cálculo de média\
-   Classificação de alunos

### 💰 Simulador de Poupança

-   Juros compostos\
-   Aportes mensais\
-   Meta de investimento

------------------------------------------------------------------------

## 📚 Conceitos Importantes

### Tipagem

Entradas são strings e precisam ser convertidas com: - int() - float()

### Estruturas de Repetição

Uso de range(): - Começa em 0 - Final exclusivo

------------------------------------------------------------------------

## 🔧 Como Executar

``` bash
python arquivo.py
```

------------------------------------------------------------------------

## 📌 Observações

Projeto voltado para aprendizado e prática de lógica.

------------------------------------------------------------------------

## 📋 Questões e respostas


**Questão 01**

Sobre Tipagem: No Python, não precisamos declarar explicitamente se uma variável é Real ou Inteiro (como feito no pseudocódigo). No entanto, ao usar a função input(), o que acontece se você esquecer de usar as funções float() ou int() para envolver o input? Como isso afeta as operações matemáticas?

**Resposta:** Por padrão, as entradas do usuário são tratadas como strings. Sem a conversão explícita para tipos numéricos, as operações matemáticas resultam em comportamentos inesperados: no caso da adição, ocorre uma concatenação (ex: '1' + '2' resulta em '12'), enquanto outras operações aritméticas geram erros de execução por incompatibilidade de tipos.


**Questão 02**

Sobre Estruturas: No Pseudocódigo 1 e 4, utilizamos um laço PARA. No Python, a função range() é comumente usada para isso. Se quisermos que o laço conte de 1 até o número exato de meses (incluindo o último), como deve ficar a sintaxe do range()? Explique por que o Python se comporta de forma diferente do pseudocódigo tradicional neste aspecto.

**Resposta:** Na programação, a contagem geralmente começa em 0. Em muitas estruturas, precisamos ajustar manualmente o limite final, mas a função range() simplifica isso: ela já define o ponto de parada como exclusivo. Por exemplo, ao usar range(8), o contador inicia em 0 e para exatamente antes de chegar ao 8, percorrendo os números de 0 a 7.

------------------------------------------------------------------------

[Voltar ao início](#-sistema-multifuncional-em-python)
