# 🏥 Sistema de Triagem Automatizada (SUS)

## 📝 Descrição do Projeto
Este projeto consiste em um sistema de triagem automatizada desenvolvido para otimizar o atendimento no Sistema Único de Saúde (SUS). O objetivo é classificar pacientes com base em sintomas e sinais informados, priorizando casos mais urgentes e organizando o fluxo de atendimento médico.

O sistema foi modelado inicialmente por meio de um fluxograma estruturado, seguido da implementação de um pseudocódigo que representa a lógica de decisão aplicada durante a triagem. A abordagem permite padronizar o atendimento inicial e reduzir o tempo de espera em unidades de saúde.

![Fluxograma do Sistema](025a8a13-3c8a-4281-9aa5-0efcb8b8bf89.pdf)
*Figura 1: Fluxograma do sistema de triagem automatizada.*

![Pseudocódigo](IMG_1644.pdf)
*Figura 2: Pseudocódigo representando a lógica de decisão do sistema.*

## 🚀 Tecnologias Utilizadas
* **Modelagem:** Fluxograma
* **Lógica:** Pseudocódigo estruturado
* **Aplicação:** Sistema de triagem em saúde pública

## 📊 Resultados e Aprendizados
O desenvolvimento do sistema proporcionou uma visão prática sobre a criação de algoritmos voltados para problemas reais na área da saúde.
* **Organização de Fluxo:** Estruturação eficiente do atendimento.
* **Tomada de Decisão:** Aplicação de lógica condicional para classificação de pacientes.
* **Padronização:** Redução de inconsistências no processo de triagem.

## 🔧 Como Executar
1. Analise o fluxograma para entendimento da lógica geral.
2. Utilize o pseudocódigo como base para implementação em linguagem de programação.
3. Adapte conforme necessidade do ambiente de aplicação.

------------------------------------------------------------------------

## 📋 Questões e respostas

# Parte 1: Investigação e Descoberta (Antes do Código)

**Questão 01** Qual foi o maior desafio logístico encontrado ao tentar traduzir o problema do mundo real para uma estrutura de decisão binária (se/senão)

**Resposta:** O maior desafio foi conseguir transmitir ao sistema a ordem de preferência, e qual paciente tem que ser atendido pela ordem de prioridade.

**Questão 02** Com base no Teste de Mesa (Cenário C), qual modificação seria necessária para tornar seu algoritmo mais resiliente a falhas humanas ou de sensores?

**Resposta:** Com base nesse meu algoritmo a única entrada que seria necessário com urgência ser corrigido seria a entrada na pergunta onde o sistema faz ao profissional se ele tem algum risco de morte, e o profissional precisa responder sim/não, no caso preciso fazer um tratamento de erro caso seja digitado qualquer coisa que seja além disso, talvez um laço pedindo para que ele repita a pergunta e o profissional responda novamente.

---
[Voltar ao início](#-engenharia-de-solucoes-logicas)


