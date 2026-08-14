---
# Metadata
title: "Information Theory"
description: "Shannon entropy, differential entropy, joint and mutual information, KL divergence, cross-entropy, channel capacity, source coding, compression, and connections to machine learning loss functions"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into information theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [information-theory, entropy, kl-divergence, cross-entropy, mutual-information, channel-capacity, compression, machine-learning]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Teoria da Informação
A teoria da informação, fundada por Claude Shannon em 1948, quantifica a própria informação. Quanto uma mensagem lhe diz? Quanto você pode compactar dados? Quão rápido você consegue se comunicar em um canal barulhento? Essas perguntas têm respostas matemáticas precisas. Além da comunicação, a teoria da informação tornou-se fundamental para o aprendizado de máquina – a entropia cruzada é a função de perda padrão para classificação, a divergência KL mede a similaridade de distribuição e a informação mútua impulsiona a seleção de recursos.
---

## Entropia
**Entropia** mede a incerteza média ou "surpresa" de uma variável aleatória.
### Entropia de Shannon (discreta)
Para uma variável aleatória discreta X com função de massa de probabilidade p(x):
H(X) = −Σₓ p(x) log₂ p(x)
Unidades: **bits** (ao usar log₂) ou **nats** (ao usar ln).
| Distribuição | Entropia | Intuição |
|------------|---------|-----------|
| Moeda justa (p = 0,5, 0,5) | 1 bit | Incerteza máxima para resultado binário |
| Moeda tendenciosa (p = 0,9, 0,1) | 0,469 bits | Menos surpreendente – principalmente cabeças |
| Determinístico (p = 1, 0) | 0 bits | Nenhuma incerteza |
| Dado justo (6 lados) | 2.585 bits | Mais resultados = mais incerteza |
| Uniforme em n resultados | log₂(n) bits | Entropia máxima para n resultados |
### Propriedades da Entropia
| Propriedade | Declaração |
|----------|-----------|
| Não-negatividade | H(X) ≥ 0 |
| Máximo | H(X) ≤ log₂(\|X\|) com igualdade para distribuição uniforme |
| Regra da cadeia | H(X, Y) = H(X) + H(Y \| X) |
| O condicionamento reduz | H(X \| Y) ≤ H(X) |
| Concavidade | H é uma função côncava da distribuição de probabilidade |
### Entropia Diferencial (Contínua)
Para uma variável aleatória contínua X com densidade p(x):
h(X) = −∫ p(x) log p(x) dx
Ao contrário da entropia discreta, a entropia diferencial pode ser **negativa**.
| Distribuição | Entropia Diferencial |
|------------|----------|
| Uniforme em [a,b] | log(b − a) |
| Normal N(μ, σ²) | (1/2) log(2πeσ²) |
| Exponencial(λ) | 1 − ln(λ) |
---

## Informações conjuntas, condicionais e mútuas
### Entropia Conjunta
H(X, Y) = −Σₓ Σᵧ p(x, y) log p(x, y)
Mede a incerteza total do par (X, Y).
### Entropia Condicional
H(Y | X) = −Σₓ Σᵧ p(x, y) log p(y | x) = H(X, Y) − H(X)
Mede a incerteza restante sobre Y após observar X.
### Informação Mútua
I(X; Y) = Σₓ Σᵧ p(x, y) log [p(x, y) / (p(x)p(y))]
Mede o quanto o conhecimento de X lhe diz sobre Y (e vice-versa).
| Propriedade | Declaração |
|----------|-----------|
| Não-negatividade | eu(X; Y) ≥ 0 |
| Simetria | eu(X; Y) = eu(Y; X) |
| Relação com a entropia | Eu(X; Y) = H(X) − H(X \| Y) = H(Y) − H(Y \| X) |
| Relação com a articulação | eu(X; Y) = H(X) + H(Y) − H(X, Y) |
| Independência | I(X; Y) = 0 se X e Y forem independentes |
| Autoinformação | Eu(X; X) = H(X) |
### Visual: O Diagrama de Entropia
```
┌─────────────────────────────────────────┐
│            H(X, Y)                      │
│  ┌──────────────┐  ┌──────────────┐    │
│  │   H(X|Y)     │  │   H(Y|X)     │    │
│  │              │I │              │    │
│  │              │( │              │    │
│  │   H(X)−I    │X │   H(Y)−I    │    │
│  │              │; │              │    │
│  │              │Y │              │    │
│  └──────────────┘  └──────────────┘    │
│         H(X)              H(Y)          │
└─────────────────────────────────────────┘
```

---

## Divergência KL
A **divergência de Kullback-Leibler (KL)** mede a diferença entre uma distribuição e outra.
D_KL(P || Q) = Σₓ P(x) log [P(x) / Q(x)]
| Propriedade | Declaração |
|----------|-----------|
| Não-negatividade | D_KL(P \|\| Q) ≥ 0 (desigualdade de Gibbs) |
| Identidade | D_KL(P \|\| Q) = 0 se P = Q |
| Assimetria | D_KL(P \|\| Q) ≠ D_KL(Q \|\| P) em geral |
| Não é uma métrica | Falha na simetria e na desigualdade triangular |
**Interpretação:** D_KL(P || Q) é o número extra de bits necessários para codificar dados de P usando um código otimizado para Q.
### Relação com outras quantidades
| Relacionamento | Fórmula |
|------------|---------|
| Entropia cruzada | H(P, Q) = H(P) + D_KL(P \|\| Q) |
| Informação mútua | Eu(X; Y) = D_KL(P(X,Y) \|\| P(X)P(Y)) |
| KL condicional | D_KL(P(Y\|X) \|\| Q(Y\|X)) média sobre X |
---

## Entropia Cruzada
**Entropia cruzada** entre distribuições P e Q:
H(P, Q) = −Σₓ P(x) log Q(x) = H(P) + D_KL(P || Q)
### Entropia Cruzada como Função de Perda
Na classificação, P é a distribuição verdadeira (rótulo codificado one-hot) e Q é a distribuição prevista do modelo.
**Entropia cruzada binária (BCE):**
L = −[y log(ŷ) + (1−y) log(1−ŷ)]
**Entropia cruzada categórica:**
L = −Σᵢ yᵢ log(ŷᵢ)
| Cenário | e (verdadeiro) | ŷ (previsto) | Perda |
|----------|----------|---------------|------|
| Correto, confiante | 1 | 0,95 | 0,051 |
| Correto, incerto | 1 | 0,55 | 0,598 |
| Errado, confiante | 1 | 0,05 | 2.996 |
| Errado, incerto | 1 | 0,45 | 0,799 |
Minimizar a entropia cruzada equivale a minimizar a divergência KL da verdadeira distribuição – e é por isso que funciona tão bem como uma função de perda.
---

## Capacidade do canal
### Modelo de canal de comunicação
```
X → [Channel] → Y
```

- X: variável aleatória de entrada
- Y: variável aleatória de saída
- Canal: definido por probabilidades condicionais p(y|x)
### Teorema de codificação de canal barulhento de Shannon
Para um canal com capacidade C, se a taxa de transmissão R< C, there exists a coding scheme that achieves arbitrarily small error probability. If R >C, a comunicação confiável é impossível.
**Capacidade do canal:**
C = máx_{p(x)} I(X; Y)
### Exemplos importantes de canais
| Canal | Descrição | Capacidade |
|--------|-------------|----------|
| **Binário simétrico (BSC)** | Inverte cada bit com probabilidade p | 1 − H(p) bits |
| **Apagamento binário (BEC)** | Apaga cada bit com probabilidade ε | 1 − ε bits |
| **Gaussiano (AWGN)** | Y = X + Z, Z ~ N(0, σ²) | (1/2) log (1 + SNR) bits |
| **Binário silencioso** | Transmissão perfeita | 1 bit |
---

## Codificação Fonte e Compressão
### Teorema da codificação fonte
O número médio de bits necessários para codificar uma fonte é limitado abaixo pela sua entropia:
eu ≥ H(X)
Um código ideal atinge L ≈ H(X).
### Codificação Huffman
Um código **sem prefixo** que atribui códigos mais curtos a símbolos mais prováveis.
| Símbolo | Probabilidade | Código Huffman | Comprimento |
|--------|------------|-------------|--------|
| Um | 0,5 | 0 | 1 |
| B | 0,25 | 10 | 2 |
| C | 0,125 | 110 | 3 |
| D | 0,125 | 111 | 3 |
Comprimento médio: 0,5(1) + 0,25(2) + 0,125(3) + 0,125(3) = 1,75 bits/símbolo
Entropia: H = 1,75 bits/símbolo (ideal neste caso!)
### Compressão sem perdas vs. Compressão com perdas
| Tipo | Princípio | Exemplos | Limite |
|------|-----------|----------|-------|
| **Sem perdas** | Remover redundância estatística | ZIP, PNG, FLAC | Taxa de entropia H(X) |
| **Com perdas** | Remover informações perceptualmente irrelevantes | JPEG, MP3, H.264 | Função de distorção de taxa R(D) |
**Teoria da distorção de taxa:** Para compressão com perdas com distorção máxima D, a taxa mínima é R(D) = min I(X; X̂) sujeita a E[d(X, X̂)] ≤ D.
---

## Conexões com outros campos
### Teoria da Informação e Termodinâmica
| Conceito | Teoria da Informação | Termodinâmica |
|--------|-------------------|----------------|
| Entropia | Entropia de Shannon H(X) | Entropia de Boltzmann S = k_B ln W |
| Entropia máxima | Distribuição uniforme | Equilíbrio térmico |
| Divergência KL | Diferença de distribuição | Diferença de energia livre |
| Informação mútua | Informações compartilhadas | Correlações em sistemas físicos |
As formas matemáticas são idênticas – Shannon tomou emprestado deliberadamente o termo “entropia” da mecânica estatística.
### Teoria da Informação e Estatística
| Conceito | Aplicação |
|--------|-------------|
| Probabilidade máxima | Equivalente a minimizar a divergência KL da distribuição empírica para a distribuição do modelo |
| Informações sobre Pescador | Curvatura da divergência KL; limite inferior da variância do estimador (Cramér-Rao) |
| Comprimento mínimo da descrição (MDL) | Seleção de modelo minimizando o comprimento total de codificação |
| AIC/BIC | Critérios aproximados de seleção de modelos baseados em KL |
---

## Relevância para aprendizado de máquina e ciência de dados
| Conceito de TI | Aplicativo de ML |
|-----------|----------------|
| Perda de entropia cruzada | Perda de classificação padrão (binária e multiclasse) |
| Divergência KL | Perda de VAE (prazo de regularização), correspondência de distribuição, destilação |
| Informação mútua | Seleção de recursos (MIFS), aprendizagem de representação (InfoMax), desemaranhamento |
| Entropia | Critério de divisão da árvore de decisão (ganho de informação), exploração em RL (entropia máxima RL) |
| Capacidade do canal | Complexidade da comunicação, compreensão dos limites de generalização |
| Codificação fonte | Compressão de dados para armazenamento e transmissão, codificação eficiente |
| Entropia máxima | Classificadores MaxEnt, seleção prévia na inferência Bayesiana |
| Distorção de taxa | Compreendendo as compensações na compressão com perdas e quantização em redes neurais |
| Informações sobre Pescador | Descida gradiente natural, entendendo a sensibilidade dos parâmetros |
| MDL/AIC/BIC | Seleção de modelo, evitando overfitting |
---

## Resumo
| Quantidade | Fórmula (discreta) | Significado |
|----------|-------------------|--------|
| Entropia H(X) | −Σ p(x) log p(x) | Incerteza média |
| Entropia conjunta H(X,Y) | −Σ p(x,y) log p(x,y) | Incerteza total do par |
| Entropia condicional H(Y\|X) | H(X,Y) − H(X) | Incerteza restante sobre Y dado X |
| Informação mútua I(X;Y) | H(X) − H(X\|Y) | Informação partilhada entre X e Y |
| Divergência KL D_KL(P\|\|Q) | Σ P(x)log(P(x)/Q(x)) | “Distância” entre distribuições |
| Entropia cruzada H(P,Q) | −Σ P(x)log Q(x) | Codificação de custos usando distribuição errada |
| Capacidade do canal C | máximo I(X;Y) | Taxa máxima de comunicação confiável |
A teoria da informação fornece os limites fundamentais do que pode ser aprendido, compactado e comunicado. Para os profissionais de aprendizagem automática, explica porque é que a entropia cruzada funciona como uma função de perda, como medir a qualidade das representações aprendidas e como pensar sobre o compromisso entre a complexidade do modelo e o ajuste dos dados. Os insights de Shannon de 1948 permanecem tão relevantes para a IA moderna quanto para as telecomunicações.