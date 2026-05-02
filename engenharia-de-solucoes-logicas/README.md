# 🛡️ Sistema de Monitoramento de Vendas

## 📝 Descrição do Projeto

Este projeto consiste em um sistema de análise de vendas com foco em
detecção de anomalias e segurança financeira. O objetivo principal é
monitorar valores de vendas, identificar discrepâncias e aplicar regras
de validação baseadas em limites definidos pelo usuário.

Desenvolvido como prática de lógica de programação, o sistema realiza
cálculos automáticos, verifica padrões suspeitos e permite ajustes
dinâmicos no limite de segurança, garantindo maior controle sobre os
dados inseridos.

http://googleusercontent.com/image_generation_content/0 *Figura 1:
Execução do sistema exibindo análise de vendas e alertas de segurança.*

## 🚀 Tecnologias Utilizadas

-   **Linguagem:** Python 3.x
-   **Paradigma:** Programação estruturada
-   **Execução:** Terminal / Console

## 📊 Resultados e Aprendizados

O projeto demonstrou a importância da validação de dados e análise de
padrões em sistemas simples: \* **Detecção de discrepâncias:**
Identificação de valores muito acima da média. \* **Controle dinâmico:**
Ajuste do limite de segurança em tempo de execução. \* **Validação de
entradas:** Prevenção de decisões com base em dados inconsistentes.

## 🔧 Como Executar

1.  Clone o repositório.
2.  Certifique-se de ter o Python instalado.
3.  Execute o comando: `python main.py`.
4.  Insira os valores das vendas conforme solicitado no terminal.

------------------------------------------------------------------------

## 📋 Questões e respostas

# Parte 1: Investigação e Descoberta (Antes do Código)

**Questão 01** O que é Discrepância de Dados (Outliers): Como um único valor muito alto ou muito baixo pode "mentir" sobre a média de um grupo?

**Resposta:** São valores que fogem muito do padrão de um conjunto de dados sendo muito maiores ou menores que os outros, a média é calculada somando tudo e dividindo pela quantidade, o problema é que um valor extremo pode puxar a média muito para cima ou muito para baixo.

**Questão 02** Por que em análise de dados muitas vezes ignoramos os valores extremos (o maior e o menor) para obter um resultado mais fiel?

**Resposta:** É um jeito de ajustar ou tratar os dados para que eles representem melhor a realidade, sem puxar o resultado par longe do comum.

**Questão 03** Lógica de Negócio: Pesquise o que é uma "Margem de Tolerância" em auditorias financeiras.

**Resposta:** É um limite aceitável de erro ou diferença em dados financeiros sem que isso seja considerado um problema relevante.

# Parte 3: Análise de Compreensão e Metacognição

**Questão 01** O Teste de Estresse (Análise): Realize um Teste de Mesa manual com os valores: Venda 1 = 100, Venda 2 = 200, Venda 3 = 5000. O que aconteceu com a média? O seu código tomou a decisão que você esperava? Se não, qual linha de lógica você precisou alterar?

**Resposta:** A média ficou muito alta no valor de 1766,67. Sim, na média simples ficou correto matematicamente, mais se for seguir no padrão das venda não ficou. precisei ignorar o valor da venda 3 e fazer a média com o valor da venda 1 e 2 para obter um resultado mais realista.

**Questão 02** Aplicação Real: Se este código fosse usado em um banco real, qual o perigo de usar uma variável global para o limite de segurança em vez de uma variável protegida?

**Resposta:** Por que na variável global ela pode ser acessada e alterada por qualquer parte do sistema, já na variável protegida nem todo mundo pode alterar.

**Questão 03** A Experiência Individual: "Descreva o erro de indentação ou de digitação (SyntaxError/NameError) mais frustrante que você cometeu durante a elaboração deste código específico. Como a sua intuição te ajudou a encontrar o erro antes mesmo de ler a mensagem de erro do Python? Explique a diferença entre o que você achava que o computador estava lendo e o que ele realmente estava lendo naquela linha."

**Resposta:** Ter criado ( print(venda_total) ) sem nunca ter criado essa variável. A intuição me ajudou a ver que não tinha determinado a venda total, o que eu achava " venda_total deve ser o valor das vendas" o que ele estava lendo "essa variável não existe".

------------------------------------------------------------------------


[Voltar ao início](#-sistema-de-monitoramento-de-vendas)
