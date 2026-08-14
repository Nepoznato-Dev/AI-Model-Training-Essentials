<!--
---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
category: "Data Science and Analytics"
subcategory: "Mathematics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Estatística e Probabilidade
Probabilidade e estatística são os fundamentos matemáticos da ciência de dados, aprendizado de máquina e pesquisa científica. A probabilidade informa a probabilidade dos eventos; as estatísticas mostram como tirar conclusões dos dados. Juntos, eles transformam a incerteza em conhecimento quantificável e gerenciável.
---

## Teoria da Probabilidade
### Conceitos Básicos
| Conceito | Descrição | Exemplo |
|---------|-------------|---------|
| **Espaço de amostra** | Conjunto de todos os resultados possíveis | Lançando um dado: {1, 2, 3, 4, 5, 6} |
| **Evento** | Um subconjunto do espaço amostral | Lançando um número par: {2, 4, 6} |
| **Probabilidade** | Número entre 0 e 1 que mede a probabilidade | P(lançando 6) = 1/6 |
| **Probabilidade Condicional** | P(A|B): probabilidade de A dado B ter ocorrido | P(chuva | nublado) |
| **Independência** | Eventos onde um não afeta o outro | Os lançamentos de moedas são independentes |
### Regras de Probabilidade
| Regra | Fórmula | Caso de uso |
|------|---------|----------|
| **Regra de adição** | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) | Probabilidade de A ou B |
| **Regra de multiplicação** | P(A ∩ B) = P(A) × P(B|A) | Probabilidade de A e B |
| **Regra do complemento** | P(não A) = 1 − P(A) | Probabilidade de o evento não ocorrer |
| **Lei da Probabilidade Total** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Particionamento por eventos mutuamente exclusivos |
| **Teorema de Bayes** | P(A|B) = P(B|A) × P(A) / P(B) | Atualizando crenças com evidências |
### Distribuições de probabilidade
| Distribuição | Tipo | Parâmetros principais | Caso de uso |
|------------|------|----------------|----------|
| **Normal (Gaussiano)** | Contínuo | Média (μ), Desvio padrão (σ) | Fenômenos naturais, erros de medição |
| **Binômio** | Discreto | n (tentativas), p (probabilidade) | Contagens de sucesso/fracasso |
| **Poison** | Discreto | λ (taxa) | Eventos raros ao longo do tempo/espaço |
| **Exonencial** | Contínuo | λ (taxa) | Tempo entre eventos |
| **Uniforme** | Ambos | a, b (limites) | Resultados igualmente prováveis ​​|
| **Qui-Quadrado** | Contínuo | k (graus de liberdade) | Testes de adequação |
| **Distribuição t** | Contínuo | ν (graus de liberdade) | Inferência de pequenas amostras |
### Principais propriedades das distribuições
| Propriedade | Descrição |
|----------|------------|
| **Média (valor esperado)** | Centro de massa da distribuição: E[X] = Σ xᵢ × P(xᵢ) |
| **Variação** | Distribuído em torno da média: Var(X) = E[(X − μ)²] |
| **Desvio Padrão** | Raiz quadrada da variância; mesmas unidades que os dados |
| **Distorção** | Assimetria da distribuição |
| **Curtose** | "Tailedness" — quão pesadas são as caudas |
---

## Inferência Estatística
### Estatística Descritiva vs. Estatística Inferencial
| | Descritivo | Inferencial |
|---|-------------|---------|
| **Objetivo** | Resuma e descreva os dados | Tirar conclusões sobre uma população a partir de uma amostra |
| **Ferramentas** | Média, mediana, moda, desvio padrão, gráficos | Testes de hipóteses, intervalos de confiança, regressão |
| **Escopo** | Somente os dados que você possui | Generalizando além da sua amostra |
### Estrutura de teste de hipóteses
| Etapa | Descrição |
|------|-------------|
| 1. **Declarar hipóteses** | Hipótese nula (H₀): nenhum efeito; Alternativa (H₁): efeito existe |
| 2. **Escolha o nível de significância** | α = 0,05 (convencional) |
| 3. **Selecione teste** | Com base no tipo de dados, tamanho da amostra e suposições |
| 4. **Calcular estatística de teste** | Depende do teste escolhido |
| 5. **Encontre o valor p** | Probabilidade de observar os dados se H₀ for verdadeiro |
| 6. **Tome uma decisão** | Se p < α, rejeite H₀; caso contrário, não rejeite H₀ |
### Testes estatísticos comuns
| Teste | Quando usar | O que compara |
|------|-------------|-----------------|
| **teste t** | Compare médias de 1–2 grupos | Agrupar média(s) para um valor ou entre si |
| **Teste qui-quadrado** | Dados categóricos | Frequências observadas vs. esperadas |
| **ANOVA** | Compare médias de 3+ grupos | Variação entre grupos vs. variação dentro do grupo |
| **Mann-Whitney U** | Alternativa não paramétrica ao teste t | Distribuições de classificação de dois grupos |
| **Correlação de Pearson** | Relação linear entre duas variáveis ​​contínuas | valor de r de −1 a +1 |
| **Correlação de Spearman** | Relacionamento monotônico (baseado em classificação) | Valor de ρ para dados ordinais ou não normais |
### Intervalos de confiança
Um intervalo de confiança fornece uma gama de valores plausíveis para um parâmetro populacional:
- **IC 95% para média** (σ conhecido): x̄ ± 1,96 × (σ / √n)
- **Interpretação**: "Temos 95% de certeza de que a verdadeira média da população está dentro deste intervalo"
- **IC mais amplo** = mais incerteza (amostra menor, maior variabilidade ou maior nível de confiança)
---

## Análise de regressão
### Tipos de regressão
| Tipo | Variável Dependente | Caso de uso |
|------|-------------------|----------|
| **Regressão Linear** | Contínuo | Previsão de preços e vendas de casas |
| **Regressão Logística** | Binário (0/1) | Classificação: detecção de spam, diagnóstico de doenças |
| **Regressão Polinomial** | Contínuo (curvo) | Curvas de crescimento, tendências não lineares |
| **Regressão Múltipla** | Contínuo (2+ preditores) | Controle de fatores de confusão |
| **Cimeira/Laço** | Contínuo (regularizado) | Prevenindo overfitting, seleção de recursos |
### Noções básicas de regressão linear
O modelo: **y = β₀ + β₁x + ε**
| Componente | Significado |
|-----------|---------|
| β₀ (interceptação) | Valor de y quando x = 0 |
| β₁ (inclinação) | Mudança em y para uma mudança de uma unidade em x |
| ε (termo de erro) | Variação inexplicável |
**Métricas principais:**
- **R² (coeficiente de determinação)**: Proporção de variância explicada pelo modelo (0 a 1)
- **R² ajustado**: R² penalizado pelo número de preditores
- **RMSE**: raiz do erro quadrático médio — erro médio de previsão nas mesmas unidades de y
### Suposições de regressão linear
| Suposição | O que isso significa | Como verificar |
|-----------|--------------|--------------|
| **Linearidade** | A relação entre X e Y é linear | Gráficos de dispersão |
| **Independência** | As observações são independentes | Desenho do estudo |
| **Homoscedasticidade** | Variância constante dos resíduos | Parcelas residuais |
| **Normalidade** | Os resíduos são normalmente distribuídos | Gráfico Q-Q, teste de Shapiro-Wilk |
| **Sem multicolinearidade** | Os preditores não são altamente correlacionados | VIF (fator de inflação de variância) |
---

## Estatísticas Bayesianas
### Frequentista vs. Bayesiano
| | Frequentista | Bayesiano |
|---|-------------|----------|
| **Probabilidade significa** | Frequência de longo prazo | Grau de crença |
| **Os parâmetros são** | Corrigido, mas desconhecido | Variáveis ​​aleatórias com distribuições |
| **Usos** | valores p, intervalos de confiança | Distribuições posteriores, intervalos credíveis |
| **Fortes** | Objectivo, bem estabelecido | Incorpora conhecimento prévio, interpretação intuitiva |
### Teorema de Bayes na prática
**Posterior = (Probabilidade × Anterior) / Evidência**
Exemplo - exames médicos:
- Prevalência da doença: 1% (anterior)
- Sensibilidade do teste: 95% (taxa de verdadeiro positivo)
- Especificidade do teste: 90% (taxa de verdadeiro negativo)
- Se o teste for positivo: P(doença | positivo) = (0,95 × 0,01) / (0,95 × 0,01 + 0,10 × 0,99) ≈ 8,8%
Este resultado contraintuitivo – a maioria dos resultados positivos são falsos positivos quando a doença é rara – é a **falácia da taxa básica** e mostra por que o pensamento bayesiano é importante.
---

## Dicas Práticas
- **Sempre visualize seus dados** antes de executar qualquer teste estatístico
- **Verifique as suposições** — violações podem invalidar os resultados
- **O tamanho do efeito é importante** — um resultado estatisticamente significativo pode ser praticamente sem sentido
- **Correlação não é causalidade** — mesmo correlações fortes podem ter fatores de confusão
- **Comparações múltiplas** aumentam as taxas de falsos positivos – aplicam correções (Bonferroni, FDR)
- **Relatar intervalos de confiança**, não apenas valores-p
---

## Por que isso é importante
A estatística é a espinha dorsal da pesquisa científica, da análise de negócios e do aprendizado de máquina. Sem ele, não é possível diferenciar sinal de ruído, identificar efeitos reais de flutuações aleatórias ou fazer previsões com incerteza quantificada. Esteja você analisando testes A/B, treinando modelos de ML ou lendo artigos de pesquisa, o conhecimento estatístico é essencial.