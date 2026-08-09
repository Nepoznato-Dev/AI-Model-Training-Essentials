---
# Metadata
title: "Ensemble Methods"
description: "Bagging, boosting, stacking, voting, random forests, XGBoost"
category: "Data Science and Analytics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ensemble, methods, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Métodos de conjunto
Os métodos de conjunto combinam vários modelos de aprendizado de máquina para produzir melhores previsões do que qualquer modelo único poderia alcançar sozinho. A intuição é direta: se você tiver vários modelos que são um tanto precisos, mas cometem erros diferentes, a combinação de suas previsões cancelará erros individuais e produzirá um resultado mais robusto. Os conjuntos estão por trás das soluções de aprendizado de máquina mais competitivas e continuam sendo algumas das técnicas mais confiáveis ​​em sistemas de produção.
---

## Por que os conjuntos funcionam
| Princípio | Descrição |
|-----------|------------|
| **Sabedoria das multidões** | Múltiplas estimativas imperfeitas, calculadas em média, são melhores do que qualquer estimativa única |
| **Compensação entre polarização e variância** | Os conjuntos podem reduzir a variação (ensacar) ou o preconceito (aumentar) sem sacrificar o outro |
| **Diversidade de erros** | Se os modelos cometem erros diferentes, combiná-los anula erros individuais |
| **Suavização de limite de decisão** | Vários modelos criam uma superfície de decisão mais robusta do que um modelo |
---

## Bagging (agregação Bootstrap)
### Como funciona
| Etapa | Descrição |
|------|-------------|
| **1. Amostragem de bootstrap** | Extrair múltiplas amostras aleatórias (com reposição) dos dados de treinamento |
| **2. Modelos de base de trem** | Treinar um modelo em cada amostra de bootstrap (normalmente árvores de decisão) |
| **3. Agregado** | Para regressão: previsões médias. Para classificação: votação majoritária |
### Principais características
| Característica | Descrição |
|---------------|------------|
| **Reduz a variação** | A média suaviza as flutuações dos modelos individuais |
| **Treinamento paralelo** | Cada modelo básico é independente; podem ser treinados simultaneamente |
| **Avaliação imediata** | Cada amostra é deixada de fora de algumas amostras de bootstrap; use-os para validação |
| **Decorrelação** | A seleção aleatória de recursos em cada divisão reduz a correlação entre as árvores |
### Floresta Aleatória
| Aspecto | Descrição |
|--------|------------|
| **Aluno básico** | Árvores de decisão |
| **Adição de chave** | Em cada divisão, considere apenas um subconjunto aleatório de recursos (normalmente sqrt(n_features)) |
| **Por que funciona** | A seleção aleatória de características decorrelaciona as árvores, tornando o conjunto mais robusto |
| **Hiperparâmetros** | Número de árvores; profundidade máxima; min amostras por folha; recursos máximos |
| **Fortes** | Lida com dados de alta dimensão; robusto a valores discrepantes; fornece importância de recurso |
| **Fraquezas** | Menos interpretável que árvores isoladas; pode superajustar em tarefas de regressão barulhentas |
---

## Impulsionando
### Como funciona
| Etapa | Descrição |
|------|-------------|
| **1. Treine o primeiro modelo** | Treinar um modelo base (geralmente uma árvore/toco raso) nos dados |
| **2. Identificar erros** | Descubra quais instâncias o modelo errou |
| **3. Treine o próximo modelo** | Treinar um novo modelo focado nos erros (reponderado ou ajustado residualmente) |
| **4. Combinar sequencialmente** | Cada novo modelo corrige os erros acumulados de todos os modelos anteriores |
| **5. Repetir** | Continuar por um determinado número de rodadas |
### Impulsionando Algoritmos
| Algoritmo | Função de perda | Recurso principal |
|-----------|--------------|------------|
| **AdaBoost** | Exponencial | Repondera instâncias classificadas incorretamente; simples; sensível ao ruído |
| **Aumento de gradiente** | Qualquer perda diferenciável | Ajusta resíduos (gradiente de perda); mais flexível |
| **XGBoost** | Aumento de gradiente regularizado | Regularização L1/L2; gradientes de segunda ordem; otimização de hardware |
| **LightGBM** | Amostragem unilateral baseada em gradiente | Crescimento foliar; baseado em histograma; rápido em grandes conjuntos de dados |
| **CatBoost** | Impulso ordenado | Lida com recursos categóricos nativamente; reduz o sobreajuste |
### Boosting vs Ensacamento
| Dimensão | Ensacamento | Impulsionando |
|-----------|---------|----------|
| **Treinamento** | Paralelo | Sequencial |
| **Foco** | Reduz a variação | Reduz preconceito |
| **Modelos básicos** | Alta variância, baixo viés (árvores profundas) | Baixa variância, elevado viés (árvores/tocos rasos) |
| **Combinação** | Peso igual | Ponderado pelo desempenho |
| **Sobreajuste** | Menos propenso | Pode superajustar se houver muitas rodadas |
| **Sensibilidade ao ruído** | Robusto | Sensível a dados ruidosos |
---

## Empilhamento
### Como funciona
| Etapa | Descrição |
|------|-------------|
| **1. Modelos de base de trem** | Treinar diversos modelos (por exemplo, floresta aleatória, SVM, rede neural, aumento de gradiente) |
| **2. Gerar previsões** | Use previsões fora do padrão (validação cruzada) como recursos de entrada |
| **3. Treinar metamodelo** | Treinar um modelo de segundo nível nas previsões dos modelos básicos |
| **4. Previsão final** | Os modelos básicos prevêem; meta-modelo combina suas previsões |
### Melhores práticas de empilhamento
| Prática | Razão |
|----------|--------|
| **Use diversos modelos básicos** | Algoritmos diferentes cometem erros diferentes; diversidade é o ponto principal |
| **Use validação cruzada para previsões básicas** | Impede que o metamodelo aprenda a explorar modelos básicos superajustados |
| **Mantenha o metamodelo simples** | Regressão logística ou árvore rasa; os modelos básicos fazem o trabalho pesado |
| **Incluir recursos brutos no metamodelo** | Às vezes é útil dar ao metamodelo acesso também aos recursos originais |
---

## Votação e média
### Votação Difícil (Classificação)
| Modelo | Previsão |
|-------|-----------|
| Modelo A | Classe 1 |
| Modelo B | Classe 0 |
| Modelo C | Classe 1 |
| **Votação majoritária** | **Classe 1** |
### Votação suave (classificação)
| Modelo | P(Classe 0) | P(Classe 1) |
|-------|-----------|-----------|
| Modelo A | 0,3 | 0,7 |
| Modelo B | 0,6 | 0,4 |
| Modelo C | 0,4 | 0,6 |
| **Média** | **0,43** | **0,57** |
| **Previsão** | | **Classe 1** |
### Média Ponderada
| Modelo | Peso | Previsão |
|-------|--------|-----------|
| Modelo A | 0,5 | 0,8 |
| Modelo B | 0,3 | 0,6 |
| Modelo C | 0,2 | 0,9 |
| **Média ponderada** | | 0,5×0,8 + 0,3×0,6 + 0,2×0,9 = 0,76 |
---

## Orientação Prática
### Quando usar qual conjunto
| Cenário | Método recomendado |
|----------|-------------------|
| **Linha de base rápida; dados tabulares** | Floresta Aleatória |
| **Precisão máxima; dados tabulares** | XGBoost/LightGBM/CatBoost |
| **Dados ruidosos** | Ensacamento (o aumento irá sobrecarregar o ruído) |
| **Interpretabilidade necessária** | Modelo único ou pequeno conjunto com importância especial |
| **Diversos tipos de modelos** | Empilhamento ou votação |
| **Aprendizagem on-line** | Métodos de conjunto de streaming; reforço adaptativo |
| **Dados desequilibrados** | Floresta Aleatória Equilibrada; reforço sensível ao custo |
### Estratégias de Diversidade do Ensemble
| Estratégia | Descrição |
|----------|------------|
| **Algoritmos diferentes** | Combine modelos baseados em árvore, lineares e neurais |
| **Recursos diferentes** | Treinar modelos em diferentes subconjuntos de recursos |
| **Diferentes subconjuntos de dados** | Ensacamento; subamostragem |
| **Diferentes hiperparâmetros** | Mesmo algoritmo com configurações variadas |
| **Períodos de tempo diferentes** | Treinar em diferentes janelas de tempo |
---

## Resumo
Os métodos de conjunto funcionam porque combinam vários modelos imperfeitos em um único preditor robusto. Bagging (florestas aleatórias) reduz a variância treinando modelos em paralelo em amostras de bootstrap e média. Boosting (XGBoost, LightGBM, CatBoost) reduz o viés treinando modelos sequencialmente, cada um corrigindo os erros anteriores. O empilhamento usa um metamodelo para combinar diversos modelos básicos. Votação e média são os conjuntos mais simples. O ponto comum é a diversidade: os conjuntos funcionam melhor quando seus modelos de componentes são individualmente razoáveis, mas cometem erros diferentes. Na prática, o aumento de gradiente em dados tabulares costuma ser a abordagem única de melhor desempenho, enquanto o empilhamento de diversos modelos aumenta ainda mais a precisão em competições e aplicações de alto risco.