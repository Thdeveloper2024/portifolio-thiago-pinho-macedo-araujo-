# 🏢 Auditoria de Orçamentos Corporativos (Python)
 
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-concluído-brightgreen.svg)]()
 
## 📖 Sobre o Projeto
Este projeto foi desenvolvido como parte da disciplina de programação de computadores do curso de Engenharia de Software. O objetivo do script é processar e calcular o orçamento de uma estrutura organizacional complexa (dicionários aninhados) de uma multinacional, aplicando regras de negócio dinâmicas e auditoria de execução.
 
A solução foi arquitetada utilizando conceitos avançados de Python para garantir flexibilidade, performance e rastreabilidade.
 
## 🚀 Funcionalidades
- **Cálculo Hierárquico:** Varredura completa da estrutura corporativa, independentemente do nível de profundidade.
- **Filtros Dinâmicos:** Capacidade de ignorar setores específicos e todos os seus subsetores na hora do cálculo financeiro.
- **Conversão de Câmbio:** Suporte a parâmetros opcionais para conversão de moedas em tempo de execução.
- **Sistema de Auditoria:** Monitoramento automatizado de tempo de execução e registro (logging) dos parâmetros utilizados na transação financeira.
 
## 🛠️ Tecnologias e Conceitos Aplicados
Este projeto foi construído utilizando Python puro (Standard Library), com foco nos seguintes paradigmas e recursos:
* **Funções Recursivas (Recursion):** Utilizadas para a navegação na árvore de dados (dicionários aninhados).
* **Decorators:** Implementação do `@auditor` para injetar comportamentos de log e cronometragem sem modificar a lógica de negócios.
* **Empacotamento de Argumentos (`*args` e `**kwargs`):** Utilizados tanto no decorator quanto na função principal para permitir a passagem dinâmica de departamentos a serem ignorados e taxas de câmbio.
 
## ⚙️ Como Executar
 
### Pré-requisitos
* Python 3.8 ou superior instalado.

### Passo a Passo
1. Clone este repositório:
   ```bash
   git clone https://github.com/Thdeveloper2024/portfolio-thiago-pinho-macedo-araujo.git
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd sistema_auditoria_recursos_corporativos
   ```
3. Execute o script principal:
   ```bash
   empresa_nacional.py
   ```
 
## 🧠 Lógica e Estrutura do Código
Breve explicação de como o código foi organizado:
* Este programa foi desenvolvido com o objetivo de simular o controle financeiro de uma empresa nacional localizada em São Paulo, utilizando conceitos básicos da linguagem Python aprendidos durante o primeiro semestre do curso de Análise e Desenvolvimento de Sistemas da Universidade Cidade de São Paulo.

O sistema trabalha com uma estrutura de dados organizada em dicionários, representando os setores da empresa, como Tecnologia, RH, Financeiro e Comercial. Dentro de cada departamento existem subdivisões e valores de orçamento, permitindo uma organização mais próxima de um ambiente empresarial real.

Durante o desenvolvimento do código, foram utilizados conceitos importantes da programação, como funções, recursividade, decorators, parâmetros especiais (**args** e **kwargs**) e manipulação de estruturas de dados. A função principal percorre automaticamente todos os departamentos da empresa para realizar o cálculo total do orçamento, inclusive acessando setores internos de forma recursiva.

Além disso, o programa também permite ignorar determinados departamentos durante o cálculo financeiro, simulando análises estratégicas de custos. Outro recurso implementado foi a conversão monetária, permitindo visualizar o orçamento em outra moeda utilizando taxa de câmbio.

O objetivo principal do projeto foi praticar lógica de programação e organização de sistemas empresariais, aproximando os conteúdos aprendidos em sala de aula de situações que podem ocorrer no mercado de tecnologia e gestão corporativa.

* **Dados:** Os dados utilizados no programa representam a estrutura organizacional e financeira de uma empresa nacional fictícia localizada em São Paulo. Essas informações foram organizadas utilizando dicionários em Python, permitindo separar cada setor da empresa de maneira hierárquica e organizada.
## 👤 Autor
 
* **Thiago Pinho Macedo Araujo** * LinkedIn: linkedin.com/in/thiago-macedo-094695362
* E-mail: thiagomacedo1213@gmail.com
 
---
*Projeto acadêmico com foco na aplicação prática de conceitos avançados da linguagem Python.*
