<!--
---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
category: "Data Science and Analytics"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [statistical, testing, experimentation, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teste estatístico e experimentação
A estatística é a gramática da ciência. Fornece as ferramentas para distinguir padrões reais de ruídos aleatórios, para medir se uma mudança realmente melhorou as coisas e para tomar decisões sob incerteza. Este arquivo cobre os conceitos básicos de teste de hipóteses, projeto experimental e as armadilhas comuns que enganam as pessoas.
---

## A estrutura de teste de hipóteses
Todo teste estatístico segue a mesma lógica:
1. **Indique a hipótese nula (H₀)**: Não há efeito/nenhuma diferença.
2. **Indique a hipótese alternativa (H₁)**: Há um efeito/uma diferença.
3. **Escolha um nível de significância (α)**: Geralmente 0,05 (5% de chance de falso positivo).
4. **Colete dados e calcule uma estatística de teste**.
5. **Calcule o valor p**: Probabilidade de observar este resultado (ou mais extremo) se H₀ for verdadeiro.
6. **Tome uma decisão**: Se p < α, rejeite H₀ (estatisticamente significativo). Caso contrário, não rejeite H₀.
### Conceitos-chave
| Conceito | Significado | Equívoco comum |
|--------|---------|---------------------|
| **valor p** | P(dados \| H₀ são verdadeiros) | NOT "a probabilidade de que H₀ seja verdadeiro" |
| **α (nível de significância)** | Limiar para rejeição de H₀ | Não é uma medida da importância do efeito |
| **Significância estatística** | Resultado improvável devido apenas ao acaso | NÃO significa praticamente significativo |
| **Tamanho do efeito** | Magnitude do efeito observado | Separado do valor p; um pequeno efeito pode ser significativo com N |
| **Poder** | Probabilidade de rejeitar corretamente um H₀ falso | Normalmente visam 80%+ |
| **Intervalo de confiança** | Gama de valores plausíveis para o parâmetro | Um IC de 95% não significa "95% de probabilidade de o valor verdadeiro estar neste intervalo" |
---

## Tipos de erros
| | H₀ é verdadeiro | H₀ é falso |
|---|-----------|-----------|
| **Rejeitar H₀** | Erro Tipo I (falso positivo) | ✅ Correto (verdadeiro positivo) |
| **Falha ao rejeitar H₀** | ✅ Correto (verdadeiro negativo) | Erro tipo II (falso negativo) |
| Erro | Símbolo | Significado |
|-------|--------|--------|
| **Tipo I** | α | Concluindo que há um efeito quando não há |
| **Tipo II** | β | Faltando um efeito real |
---

## Escolhendo o teste certo
| Cenário | Teste | Suposições |
|----------|------|------------|
| Compare médias de 2 grupos | **teste t** (independente) | Distribuição normal, variância igual |
| Compare médias de observações pareadas | **Teste t pareado** | As diferenças são normalmente distribuídas |
| Compare médias de 3+ grupos | **ANOVA** | Distribuição normal, variância igual |
| Compare distribuições categóricas | **Teste qui-quadrado** | Tamanho de amostra suficiente por célula |
| Comparar distribuições (não paramétricas) | **Mann-Whitney U** | Nenhuma suposição de normalidade |
| Compare 3+ grupos (não paramétrico) | **Kruskal-Wallis** | Nenhuma suposição de normalidade |
| Correlação de teste | **Pearson** (linear) ou **Spearman** (monotônico) | Pearson: normalidade; Spearman: baseado em classificação |
| Teste se os dados seguem uma distribuição | **Kolmogorov-Smirnov** | Dados contínuos |
### Paramétrico vs Não Paramétrico
| | Paramétrico | Não Paramétrico |
|---|-----------|---------------|
| **Suposições** | Os dados seguem uma distribuição específica (normalmente normal) | Nenhuma hipótese de distribuição |
| **Poder** | Maior quando os pressupostos são cumpridos | Menor, mas mais robusto |
| **Quando usar** | Amostras grandes, dados aproximadamente normais | Amostras pequenas, dados distorcidos, dados ordinais |
---

## Testes específicos em detalhes
### Teste t
Compara as médias de dois grupos.
| Variante | Caso de uso |
|--------|----------|
| **Teste t independente** | Dois grupos separados (tratamento vs controle) |
| **Teste t pareado** | O mesmo grupo medido duas vezes (antes vs depois) |
| **Teste t de uma amostra** | Compare uma média amostral com um valor conhecido |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Análise de Variância)
Compara médias em 3 ou mais grupos. Testa se pelo menos a média de um grupo difere dos demais.
| Tipo | Projeto |
|------|--------|
| **ANOVA unidirecional** | Uma variável independente com mais de 3 níveis |
| **ANOVA bidirecional** | Duas variáveis ​​independentes; testa efeitos de interação |
| **ANOVA de Medidas Repetidas** | Os mesmos assuntos medidos em condições diferentes |
Se a ANOVA for significativa, faça o acompanhamento com **testes post-hoc** (HSD de Tukey) para descobrir quais grupos específicos diferem.
### Teste Qui-Quadrado
Testa se duas variáveis ​​categóricas são independentes.
| Caso de uso | Exemplo |
|----------|---------|
| **Teste de independência** | O gênero está associado à preferência do produto? |
| **Bom ajuste** | O lançamento de um dado segue uma distribuição uniforme? |
**Regra geral**: cada célula deve ter uma contagem esperada de pelo menos 5.
---

## Teste A/B
O teste A/B é a aplicação de testes de hipóteses às decisões de negócios – normalmente comparando um controle (A) com uma variante (B).
### Processo de projeto
| Etapa | Descrição |
|------|-------------|
| **1. Definir hipótese** | “Alterar a cor do botão de azul para verde aumentará a taxa de cliques” |
| **2. Escolha métrica** | Primário: taxa de cliques. Secundário: taxa de conversão, receita. |
| **3. Calcular o tamanho da amostra** | Com base no efeito mínimo detectável, poder (80%) e significância (5%) |
| **4. Randomizar** | Atribuir aleatoriamente usuários para controle e tratamento |
| **5. Execute o experimento** | Recolher dados até atingir o tamanho da amostra alvo |
| **6. Analisar** | Compare métricas usando testes estatísticos apropriados |
| **7. Decidir** | Implementar se for estatisticamente e praticamente significativo |
### Cálculo do tamanho da amostra
O tamanho da amostra que você precisa depende de:
| Fator | Efeito no tamanho da amostra |
|--------|-----------|
| **Efeito menor para detectar** | Precisa de mais amostras |
| **Maior potência** | Precisa de mais amostras |
| **Nível de significância mais baixo** | Precisa de mais amostras |
| **Maior variação** | Precisa de mais amostras |
### Erros comuns em testes A/B
| Erro | Por que está errado |
|--------|---------------|
| **Espiando cedo** | Verificação diária dos resultados inflaciona taxa de falsos positivos |
| **Múltiplas métricas sem correção** | Testando 20 métricas em α=0,05 → espera 1 falso positivo por acaso |
| **Parando antes do alvo N** | Teste de baixa potência não consegue detectar efeitos reais |
| **Ignorando a sazonalidade** | Executando um teste durante um período de férias versus semana normal |
| **Atribuição não aleatória** | Viés de seleção (por exemplo, atribuição de novos usuários ao tratamento) |
| **Confundindo significado com importância** | Um aumento de 0,1% pode ser estatisticamente significativo, mas não vale a pena enviar |
---

## Múltiplas Comparações
Quando você executa muitos testes simultaneamente, a chance de pelo menos um falso positivo aumenta dramaticamente.
| Número de testes | Probabilidade de ≥1 falso positivo (em α=0,05) |
|----------------|---------------------------------------------|
| 1 | 5% |
| 5 | 23% |
| 10 | 40% |
| 20 | 64% |
### Correções
| Método | Como funciona | Quando usar |
|--------|-------------|-------------|
| **Bonferroni** | Divida α pelo número de testes (α/n) | Conservador; algumas comparações |
| **Holm-Bonferroni** | Procedimento de redução; menos conservador | Uso geral |
| **Benjamini-Hochberg (FDR)** | Controla a taxa de falsas descobertas | Muitos testes; análise exploratória |
---

## Tamanho do efeito
Os valores P informam *se* existe um efeito. O tamanho do efeito informa *quão grande* ele é.
| Medir | Para | Interpretação |
|--------|-----|---------------|
| **D** de Cohen | Diferença entre duas médias | 0,2 = pequeno, 0,5 = médio, 0,8 = grande |
| **R** de Pearson | Correlação | 0,1 = pequeno, 0,3 = médio, 0,5 = grande |
| **η² (eta-quadrado)** | ANOVA | 0,01 = pequeno, 0,06 = médio, 0,14 = grande |
| **Proporção de probabilidades** | Resultados categóricos | 1,0 = sem efeito; >1 ou <1 = efeito |
**Sempre relate o tamanho do efeito junto com os valores p.** Um resultado pode ser estatisticamente significativo, mas praticamente sem sentido.
---

## Bayesiano vs Frequentista
| Aspecto | Frequentista | Bayesiano |
|--------|------------|----------|
| **Probabilidade** | Frequência dos acontecimentos a longo prazo | Grau de crença |
| **Parâmetros** | Corrigido, mas desconhecido | Variáveis ​​aleatórias com distribuições |
| **Usos** | valores de p, intervalos de confiança, testes de hipóteses | Distribuições posteriores, intervalos credíveis |
| **Anterior** | Nenhuma crença anterior incorporada | Distribuição prévia explícita |
| **Interpretação** | "Se repetíssemos esta experiência muitas vezes..." | "Dados os dados, a probabilidade de..." |
| **Fortes** | Objetivo, bem estabelecido, simples | Interpretação intuitiva, incorpora conhecimentos prévios |
| **Fraquezas** | valores p amplamente incompreendidos | A escolha do anterior pode ser subjetiva |
---

## Noções básicas de inferência causal
Correlação não é causalidade. Mas às vezes você precisa saber *se X causou Y*, e não apenas se eles estão associados.
| Método | Descrição | Quando usar |
|--------|-------------|-------------|
| **Experimentos randomizados** | Padrão ouro; atribuição aleatória elimina fatores de confusão | Quando você pode randomizar |
| **Diferença em diferenças (DiD)** | Compare as mudanças ao longo do tempo entre o tratamento e o controle | Mudanças políticas, experiências naturais |
| **Descontinuidade de regressão (RDD)** | Explorar um limite de corte | Bolsas de estudo, limites de elegibilidade |
| **Variáveis ​​Instrumentais (IV)** | Utilizar um instrumento que afete o tratamento, mas não diretamente o resultado | Quando a randomização não é possível |
| **Correspondência de pontuação de propensão** | Combinar unidades tratadas e de controle com base nas características observadas | Estudos observacionais |
---

## Erros estatísticos comuns
| Erro | Descrição |
|--------|-------------|
| **p-hacking** | Tentando muitas análises até encontrar p < 0,05 |
| **HARKing** | Hipotetização após os resultados serem conhecidos |
| **Viés de sobrevivência** | Olhando apenas para os sucessos (por exemplo, empresas de sucesso) |
| **Paradoxo de Simpson** | A tendência se inverte quando os dados são agregados ou divididos por grupo |
| **Negligência da taxa básica** | Ignorando a probabilidade anterior ao interpretar os resultados |
| **Falácia ecológica** | Inferindo o comportamento individual a partir de dados em nível de grupo |
| **Confundido** | Uma terceira variável explica a relação observada |
| **Sobreajuste** | Modelo captura ruído, não sinal |
---

## Resumo
Os testes estatísticos tratam de tomar decisões sob incerteza com honestidade intelectual. Sempre estabeleça suas hipóteses antes de coletar dados. Escolha o teste certo para o seu tipo de dados. Relate os tamanhos dos efeitos, não apenas os valores p. Correto para múltiplas comparações. E lembre-se: significância estatística não é o mesmo que significância prática.