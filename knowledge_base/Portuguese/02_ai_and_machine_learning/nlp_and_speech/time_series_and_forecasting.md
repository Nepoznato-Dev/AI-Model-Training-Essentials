<!--
---
# Metadata
title: "Time Series and Forecasting"
description: "ARIMA, Prophet, LSTMs, seasonality, anomaly detection"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [time, series, forecasting, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Séries Temporais e Previsão
Os dados de série temporal são quaisquer dados coletados ao longo do tempo: preços de ações, leituras de temperatura, tráfego do site, números de vendas, monitores de frequência cardíaca, consumo de energia. Previsão significa prever valores futuros com base em padrões passados. É uma das aplicações mais valiosas em termos práticos da ciência de dados — e uma das mais difíceis, porque o futuro é genuinamente incerto e as séries temporais do mundo real estão cheias de ruído, sazonalidade e quebras estruturais.
---

## Características das séries temporais
| Componente | Descrição | Exemplo |
|-----------|-------------|---------|
| **Tendência** | Aumento ou diminuição a longo prazo | Temperaturas globais aumentando ao longo de décadas |
| **Sazonalidade** | Padrões regulares e previsíveis em intervalos fixos | As vendas no varejo aumentam todo mês de dezembro |
| **Ciclicidade** | Flutuações em intervalos não fixos (frequentemente económicos) | Recessões a cada 5-10 anos |
| **Ruído (residual)** | Variação aleatória que não pode ser explicada | Movimentos diários dos preços das ações |
| **Autocorrelação** | Os valores atuais dependem de valores passados ​​| A temperatura de hoje é semelhante à de ontem |
### Estacionaridade
Uma série temporal é **estacionária** se suas propriedades estatísticas (média, variância) não mudam ao longo do tempo. A maioria dos métodos de previsão assume estacionariedade.
| Teste | Finalidade |
|------|---------|
| **Dickey-Fuller Aumentado (ADF)** | Testa se uma raiz unitária está presente (não estacionária) |
| **Teste KPSS** | Testa se a série é estacionária em tendência |
| Transformação | Quando usar |
|---------------|------------|
| **Diferenciação** | Remover tendência: y'(t) = y(t) - y(t-1) |
| **Transformação de log** | Estabilizar a variância (para crescimento exponencial) |
| **Diferenciação sazonal** | Remova a sazonalidade: y'(t) = y(t) - y(t-s) onde s é a duração da temporada |
---

## Métodos Clássicos de Previsão
### Médias Móveis
| Método | Descrição | Melhor para |
|--------|-------------|----------|
| **Média Móvel Simples (SMA)** | Média das últimas N observações | Suavização de dados ruidosos |
| **Média Móvel Ponderada** | Observações mais recentes ganham maior peso | Quando os dados recentes são mais importantes |
| **Média Móvel Exponencial (EMA)** | Pesos decrescentes exponencialmente | Acompanhando tendências com menos atraso |
### Suavização Exponencial
| Método | Componentes | Caso de uso |
|--------|-----------|----------|
| **Simples (SES)** | Somente nível | Sem tendência, sem sazonalidade |
| **Holt's (Duplo)** | Nível + tendência | Dados com tendência mas sem sazonalidade |
| **Holt-Winters (Triplo)** | Nível + tendência + sazonalidade | Dados com tendência e sazonalidade |
### ARIMA e variantes
ARIMA (AutoRegressive Integrated Moving Average) é o carro-chefe da previsão clássica de séries temporais.
| Componente | Significado | Parâmetro |
|-----------|---------|-----------|
| **AR(p)** | Regredir nos valores de p anteriores | Quantos valores anteriores usar |
| **Eu (d)** | Número de passos diferenciais para tornar estacionário | Quantas vezes a diferença |
| **MA(q)** | Modelar o erro como uma combinação de erros passados ​​| Quantos erros anteriores usar |
| Variante | Extensão | Caso de uso |
|--------|-----------|----------|
| **SARIMA** | Adiciona componentes sazonais (P, D, Q, s) | Dados com forte sazonalidade |
| **ARIMAX** | Adiciona variáveis ​​externas | Quando você souber sobre os próximos eventos |
| **VAR** | ARIMA multivariada; múltiplas séries interdependentes | Quando as variáveis ​​afetam umas às outras |
---

## Abordagens modernas de ML
### Modelos baseados em LSTM e RNN
| Modelo | Arquitetura | Vantagem |
|-------|------------|-----------|
| **LSTM** | Rede de memória de longo e curto prazo | Captura dependências temporais de longo alcance |
| **GRU** | Unidade Recorrente Fechada (LSTM mais simples) | Treinamento mais rápido; desempenho semelhante |
| **Seq2Seq** | Codificador-decodificador para séries temporais | Comprimentos flexíveis de entrada/saída |
| **Rede Convolucional Temporal (TCN)** | Convoluções causais dilatadas | Treinamento paralelo; campo receptivo longo |
### Profeta (Meta)
Uma ferramenta prática de previsão projetada para séries temporais de negócios.
| Recurso | Descrição |
|--------|-------------|
| **Decomposição** | Tendência + sazonalidade + feriados |
| **Flexível** | Lida com dados ausentes, valores discrepantes e quebras estruturais |
| **Interpretável** | Os componentes são legíveis por humanos |
| **Automático** | Padrões razoáveis; ajuste mínimo necessário |
| Força | Limitação |
|----------|------------|
| Ótimo para métricas de negócios (vendas, usuários) | Não é ideal para dados de frequência muito alta |
| Lida com feriados e eventos especiais | Assume sazonalidade aditiva ou multiplicativa |
| Robusto para valores discrepantes | Menos preciso que o aprendizado profundo para padrões complexos |
### Modelos baseados em transformadores
| Modelo | Recurso principal |
|-------|------------|
| **Informante** | ProbSparse atenção para sequências longas |
| **Autoformador** | Mecanismo de autocorrelação para decomposição em série |
| **PatchTST** | Corrige a série temporal; independente de canal |
| **TimesFM** (Google) | Modelo de base para séries temporais; pré-treinado em dados diversos |
| **Chronos** (Amazonas) | Tokeniza séries temporais; usa arquitetura estilo LLM |
---

## Detecção de anomalias em séries temporais
Detectar padrões incomuns que se desviam do comportamento esperado.
| Método | Abordagem | Caso de uso |
|--------|----------|----------|
| **Estatística** | Z-score, AIQ, cartas de controle | Simples, bem compreendido |
| **Floresta de Isolamento** | Baseado em árvore; isola anomalias por particionamento aleatório | Detecção multivariada de anomalias |
| **LOF** (fator atípico local) | Baseado em densidade; compara densidade local com vizinhos | Quando as anomalias estão em regiões de baixa densidade |
| **Autocodificadores** | Erro de reconstrução; erro alto = anomalia | Padrões complexos e não lineares |
| **Baseado em LSTM** | Preveja o próximo passo; grande erro de previsão = anomalia | Anomalias sequenciais |
### Aplicativos
| Domínio | O que significam anomalias |
|--------|-------------------|
| **Finanças** | Fraude, quebras de mercado, quebras repentinas |
| **Saúde** | Frequência cardíaca anormal, início de convulsões |
| **Fabricação** | Falha de equipamento, defeitos de qualidade |
| **Segurança cibernética** | Tentativas de intrusão, ataques DDoS |
| **Infraestrutura** | Sobrecarga de servidor, falhas de rede |
---

## Métricas de avaliação
| Métrica | Fórmula (conceitual) | Quando usar |
|--------|----------|------------|
| **MAE** (erro médio absoluto) | Média de erros absolutos | Interpretável; mesmas unidades que os dados |
| **RMSE** (raiz do erro quadrático médio) | Raiz quadrada dos erros quadráticos médios | Penaliza mais erros grandes |
| **MAPE** (erro percentual médio absoluto) | Média de erros percentuais absolutos | Quando o erro relativo é importante |
| **SMAPE** (MAPE Simétrico) | Versão simétrica do MAPE | Lida melhor com valores próximos de zero |
| **MASE** (erro médio absoluto em escala) | MAE relativamente a uma previsão ingénua | Comparando entre diferentes séries |
---

## Fluxo de trabalho prático
| Etapa | Descrição |
|------|-------------|
| **1. Explorar** | Trace a série; identificar tendência, sazonalidade, valores discrepantes |
| **2. Decompor** | Separar em componentes de tendência, sazonais e residuais |
| **3. Estacionar** | Aplicar diferenciação ou transformações, se necessário |
| **4. Divisão** | Divisão baseada no tempo (nunca divisão aleatória para séries temporais) |
| **5. Linha de base** | Comece com uma previsão ingênua (último valor, ingênua sazonal) |
| **6. Modelo** | Experimente métodos clássicos (ARIMA, Profeta) e depois métodos de ML |
| **7. Avaliar** | Use métricas apropriadas; comparar com a linha de base |
| **8. Iterar** | Adicione recursos, experimente modelos diferentes, ajuste hiperparâmetros |
---

## Ferramentas e bibliotecas
| Ferramenta | Finalidade |
|------|---------|
| **modelos de estatísticas** | Séries temporais clássicas (ARIMA, ETS, decomposição) |
| **Profeta** (Meta) | Previsão de séries temporais de negócios |
| **hora** | Interface unificada de ML para séries temporais |
| **Dardos** | Biblioteca abrangente de previsões (aprendizado clássico + profundo) |
| **GluonTS** (Amazônia) | Modelagem probabilística de séries temporais |
| **NeuralProfeta** | Profeta com componentes de rede neural |
| **tsfresco** | Extração automática de recursos de série temporal |
| **pandas** | Manipulação e reamostragem de séries temporais |
---

## Resumo
A previsão de séries temporais combina estatísticas clássicas com aprendizado de máquina moderno. Os métodos clássicos (ARIMA, suavização exponencial, Profeta) são interpretáveis, rápidos e frequentemente precisos. Métodos de aprendizagem profunda (LSTM, Transformers) capturam padrões complexos, mas requerem mais dados e ajustes. Os princípios-chave permanecem os mesmos, independentemente do método: compreender a estrutura dos seus dados (tendência, sazonalidade, ruído), comparar com uma linha de base simples, avaliar com métricas apropriadas e levar em conta o fato de que o futuro não replicará exatamente o passado.