# Pipeline de ETL Tratamento de Dados - Olist - Mini Projeto 1 SCTECH

Este repositório contém um pipeline de **ETL (Extract, Transform, Load)** desenvolvido em Python nativo para a higienização, tratamento e análise exploratória de bases de dados de e-commerce da Olist (datasets de produtos e pedidos). O projeto foi construído sem o auxílio de bibliotecas externas de análise de dados (como Pandas), utilizando estruturas de dados puras.


### O Problema:
Bases de dados brutas de grandes ecossistemas de e-commerce frequentemente sofrem com falhas de preenchimento, dados nulos e falta de padronização textual (ex: nomes de categorias com caracteres especiais e delimitadores). Se esses dados forem consumidos diretamente por sistemas de Inteligência Artificial podem causar falhas em modelos preditivos (*Garbage In, Garbage Out*).

## Descrição do Projeto

O objetivo principal deste script é solucionar inconsistências estruturais e dados ausentes nos registros da Olist antes que essas informações sejam consumidas por  modelos preditivos. 


O pipeline executa as seguintes etapas de limpeza:
* **Limpeza de Categorias:** Padronização dos nomes de categorias para letras minúsculas, remoção de caracteres especiais/pontuações via Expressões Regulares (Regex), substituição de delimitadores (`_`) por espaços legíveis e tratamento de valores nulos para a constante `"sem categoria"`.
* **Tratamento de Dimensões Físicas:** Identificação de registros com dados de peso ou dimensões ausentes. Foi aplicada a estratégia de **descarte por exclusão**, eliminando os registros incompletos após constatar que a inconsistência afetava apenas 2 produtos (8 campos nulos no total), representando um impacto mínimo na base.
* **Análise de Hipótese Logística:** Verificação de uma hipótese de negócio da diretoria sobre pedidos sem data de entrega. O pipeline separa e contabiliza esses pedidos por status, validando ou invalidando a suposição inicial com dados concretos.
* **Relatório Completo em .txt:** Além do relatório resumido no terminal, também foi incluído um relatório completo exportado em .txt


## Guia de Execução

Para rodar o pipeline de dados localmente, siga os passos abaixo:

### 1 - Pré-requisitos
Certifique-se de ter o Python 3.x instalado em sua máquina.

### 2 - Estrutura de Pastas
Os arquivos CSV originais da Olist devem ser posicionados em um diretório chamado `dataset/` na raiz do projeto:

mini_projeto_1_sctech/
├── dataset/
│   ├── olist_products_dataset.csv
│   └── olist_orders_dataset.csv
├── funcoes.py
├── main.py
└── README.md

### 3 - Como Executar

1. **Abra o terminal** (Prompt de Comando, PowerShell ou terminal do WSL) na pasta raiz do projeto.
2. **Execute o script principal** utilizando o Python 3 com o seguinte comando:

   python main.py

## Reflexões Qualidade de Dados e Machine Learning

No desenvolvimento e treinamento de modelos baseados em Inteligência Artificial, o sucesso de um modelo preditivo está diretamente ligado à qualidade
dos dados de entrada, princípio do **Garbage In, Garbage Out**. A aplicação de uma lógica de programação na etapa de ETL é o que garante a integridade desses dados.
Ao mapear inconsistências e tratar valores nulos, o fornecimento de dados fica mais limpo e consistente melhorando a qualidade dos modelos preditivos.

Essa limpeza é necessária pois ajuda a mitigar problemas como o Overfitting, quando o modelo se ajusta excessivamente aos dados de treinamento, memorizando 
não apenas os padrões reais mas também suas inconsistências, então o modelo acaba não aprendendo apenas decorando se tornando inútil para predições futuras.

