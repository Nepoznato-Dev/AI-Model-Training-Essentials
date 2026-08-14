---
# Metadata
title: "Stochastic Processes"
description: "Random variables review, Markov chains, random walks, Brownian motion, Poisson processes, martingales, Monte Carlo methods, and MCMC"
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
    changes: "Initial deep-dive into stochastic processes"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [stochastic-processes, markov-chains, random-walks, brownian-motion, poisson-processes, martingales, monte-carlo, mcmc]
difficulty_level: "advanced"
prerequisites:
  - "statistics_and_probability.md"
  - "real_analysis.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Processos Estocásticos
Um **processo estocástico** é uma coleção de variáveis ​​aleatórias indexadas por tempo (ou espaço). Enquanto a teoria da probabilidade estuda eventos aleatórios individuais, os processos estocásticos estudam como a aleatoriedade evolui ao longo do tempo. Eles modelam preços de ações, comprimento de filas, propagação de doenças, geração de linguagem e dinâmica de treinamento de modelos de aprendizado de máquina.
---

## Fundações
### Definição
Um processo estocástico {X_t : t ∈ T} é uma família de variáveis ​​aleatórias definidas em um espaço de probabilidade comum. T é o **conjunto de índices** (tempo):
- **Tempo discreto:** T = {0, 1, 2, ...}
- **Tempo contínuo:** T = [0, ∞)
O **espaço de estados** S é o conjunto de valores possíveis que X_t pode assumir.
### Principais Propriedades
| Propriedade | Definição |
|----------|------------|
| **Estacionaridade** | Distribuição conjunta de (X_{t₁}, ..., X_{tₖ}) igual a (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Independência** | X_t independente de X_s para t ≠ s |
| **Ergodicidade** | As médias temporais convergem para as médias do conjunto |
| **Propriedade Markov** | O futuro depende apenas do presente, não do passado |
| **Martingale** | O valor futuro esperado é igual ao valor atual |
---

## Cadeias de Markov
Uma **cadeia de Markov** é um processo estocástico onde o estado futuro depende apenas do estado atual (propriedade sem memória).
### Cadeias de Markov em Tempo Discreto (DTMC)
P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}
A **matriz de transição** P possui entradas p_{ij} = P(vá para j | atualmente em i).
| Propriedade | Declaração |
|----------|-----------|
| Somas de linha | Cada linha soma 1: Σⱼ p_{ij} = 1 |
| transição em n etapas | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Distribuição estacionária | πP = π (vetor próprio esquerdo com autovalor 1) |
### Classificação dos Estados
| Prazo | Definição |
|------|------------|
| **Recorrente** | Cadeia retorna ao estado i com probabilidade 1 |
| **Transitório** | Probabilidade diferente de zero de nunca mais retornar |
| **Absorvente** | p_{ii} = 1 (uma vez inserido, nunca mais sai) |
| **Período** | GCD dos tempos de retorno; período 1 = aperiódico |
| **Comunicação** | Os estados i e j podem se alcançar |
### Distribuição Estacionária
Para uma cadeia de Markov recorrente positiva e irredutível, a distribuição estacionária π existe, é única e satisfaz:
πP = π, Σᵢ πᵢ = 1
**Interpretação:** πᵢ = proporção de tempo gasto no estado i no longo prazo.
**Exemplo resolvido:** Modelo meteorológico com estados {Ensolarado, Chuvoso}.
P = [[0,9, 0,1], [0,5, 0,5]] (linhas: de ensolarado, de chuvoso)
Distribuição estacionária: πP = π
- π₁ = 0,9π₁ + 0,5π₂
- π₂ = 0,1π₁ + 0,5π₂
- π₁ + π₂ = 1
- Resolvendo: π₁ = 5/6 ≈ 0,833, π₂ = 1/6 ≈ 0,167
### Convergência para Estacionaridade
Para uma cadeia recorrente positiva, irredutível e aperiódica:
- Pⁿ → Π (matriz com todas as linhas iguais a π) como n → ∞
- **Tempo de mistura:** Número de etapas até a distribuição estar próxima de π
- **Lacuna espectral:** 1 − |λ₂| (onde λ₂ é o segundo maior autovalor) determina a velocidade de mistura
### Cadeias de Markov em Tempo Contínuo (CTMC)
As transições ocorrem em momentos aleatórios governados por distribuições exponenciais.
| Conceito | Descrição |
|--------|-------------|
| **Matriz de taxas Q** | q_{ij} ≥ 0 para i ≠ j; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Probabilidades de transição** | P(t) = e^{Qt} (matriz exponencial) |
| **Distribuição estacionária** | πQ = 0 |
| **Tempo de espera** | O tempo no estado i é Exp(−q_{ii}) |
---

## Passeios aleatórios
Um **passeio aleatório** é um caminho formado por etapas aleatórias sucessivas.
### Passeio Aleatório Simples
X_n = X_{n-1} + Z_n, onde Z_n ∈ {+1, −1} com probabilidades p, q = 1−p.
| Propriedade | p = 1/2 (simétrico) | p ≠ 1/2 (tendencioso) |
|----------|---------------------|-------------------|
| E[X_n] | 0 | n(2p−1) |
| Var[X_n] | n | 4npq |
| Retorna à origem? | Sim (com probabilidade 1) | Não (afasta-se) |
| Recorrente? | Sim (em 1D e 2D) | Não |
### Passeio Aleatório em Dimensões Superiores
| Dimensão | Recorrente? | Intuição |
|-----------|------------|-----------|
| 1D | Sim | “Um homem bêbado sempre encontra o caminho de casa” |
| 2D | Sim | “Um pássaro bêbado sempre encontra o caminho de casa” |
| 3D+ | Não | “Um pardal bêbado nunca encontra o caminho de casa” |
### Conexão com o Movimento Browniano
Escalando um passeio aleatório: seja S_n = ΣZ_i. Então como tamanho do passo → 0 e passos → ∞:
S_{⌊nt⌋} / √n → B(t) (movimento browniano, pelo teorema de Donsker)
---

## Movimento Browniano
**Movimento browniano** (processo de Wiener) B(t) é o limite de tempo contínuo de um passeio aleatório.
### Definição
B(t) satisfaz:
1. B(0) = 0
2. B(t) tem caminhos contínuos
3. Incrementos independentes: B(t) − B(s) é independente de B(s) − B(r) para r < s < t
4. B(t) − B(s) ~ N(0, t − s) (incrementos gaussianos)
### Principais Propriedades
| Propriedade | Declaração |
|----------|-----------|
| E[B(t)] | = 0 |
| Var[B(t)] | = t |
| Cov[B(s), B(t)] | = min(s, t) |
| Em nenhum lugar diferenciável | Os caminhos são contínuos, mas não possuem derivada |
| Dimensão fractal | Gráfico tem dimensão Hausdorff 3/2 |
| Propriedade de Markov | O futuro depende apenas da posição atual |
| Martingale | E[B(t) | F_s] = B(s) para s < t |
### Movimento Browniano Geométrico
S(t) = S(0) exp((μ − σ²/2)t + σB(t))
Este é o modelo padrão para preços de ações na estrutura Black-Scholes.
- μ: deriva (retorno esperado)
- σ: volatilidade
---

## Processos de Poisson
Um **processo Poisson** N(t) conta o número de eventos que ocorrem em [0, t].
### Definição
N(t) ~ Poisson(λt), onde λ é a taxa (eventos por unidade de tempo).
| Propriedade | Declaração |
|----------|-----------|
| N(0) = 0 | — |
| Incrementos independentes | Eventos em intervalos disjuntos são independentes |
| Incrementos estacionários | N(t+s) − N(s) ~ Poisson(λt) |
| E[N(t)] | =λt |
| Var[N(t)] | =λt |
| Horários entre chegadas | Distribuído exponencialmente: T_i ~ Exp(λ) |
### Generalizações
| Variante | Descrição |
|--------|-------------|
| **Não homogêneo** | Taxa λ(t) varia com o tempo |
| **Composto Poisson** | Cada evento tem um tamanho aleatório: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Medida aleatória de Poisson** | Pontos no espaço-tempo, não apenas no tempo |
| **Multivariado** | Vários tipos de eventos com possíveis interações |
---

##Martingales
Um **martingale** é um jogo justo: o valor futuro esperado, dadas todas as informações atuais, é igual ao valor atual.
### Definição
{X_n} é um martingale em relação à filtragem {F_n} se:
1. X_n é mensurável por F_n (adaptado)
2. E[|X_n|] < ∞ (integrável)
3. E[X_{n+1} | F_n] = X_n (jogo justo)
| Variante | Condição | Interpretação |
|--------|-----------|----------------|
| **Martingale** | E[X_{n+1} | F_n] = X_n | Jogo justo |
| **Submartingale** | E[X_{n+1} | F_n] ≥ X_n | Jogo favorável (tendência de alta) |
| **Supermartingale** | E[X_{n+1} | F_n] ≤ X_n | Jogo desfavorável (tendência de queda) |
### Teoremas Chave
| Teorema | Declaração |
|--------|-----------|
| **Parada opcional** | Sob condições, E[X_T] = E[X_0] para um tempo de parada T |
| **Convergência** | Um martingale limitado converge quase certamente |
| **Desigualdade máxima** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob) |
---

## Métodos de Monte Carlo
**Métodos de Monte Carlo** usam amostragem aleatória para estimar quantidades determinísticas.
### Ideia Básica
Para estimar E[f(X)] onde X ~ P:
1. Extraia N amostras: x₁, x₂, ..., x_N de P
2. Calcule: Î = (1/N) Σᵢ f(xᵢ)
3. Pela lei dos grandes números: Î → E[f(X)] como N → ∞
**Erro:** Erro padrão = σ_f / √N, onde σ_f² = Var[f(X)]
### Técnicas de redução de variância
| Técnica | Idéia | Aceleração |
|-----------|------|--------|
| **Amostragem de importância** | Amostra de Q em vez de P, peso por P/Q | Pode ser dramático |
| **Variações antitéticas** | Use pares (x, −x) para cancelar a variância | ~2x |
| **O controle varia** | Subtraia a função de expectativa conhecida correlacionada com f | Varia |
| **Amostragem estratificada** | Dividir domínio, amostrar cada estrato | Reduz a variação |
| **Rao-Blackwell** | Condição de estatísticas suficientes | Sempre ajuda |
---

## Cadeia de Markov Monte Carlo (MCMC)
MCMC constrói uma cadeia de Markov cuja distribuição estacionária é a distribuição alvo. Após um período de "burn-in", as amostras aproximam-se do alvo.
### Algoritmo Metropolis-Hastings
| Etapa | Ação |
|------|--------|
| 1 | Estado atual: x_t |
| 2 | Propor: x* ~ q(x* \| x_t) (distribuição da proposta) |
| 3 | Razão de aceitação: α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4 | Aceitar com probabilidade α: x_{t+1} = x* (aceitar) ou x_t (rejeitar) |
**Caso especial — Algoritmo Metropolis:** Proposta simétrica q(x*|x) = q(x|x*), então α = min(1, π(x*)/π(x_t)).
### Amostragem de Gibbs
Um caso especial de Metropolis-Hastings onde cada variável é atualizada a partir de sua distribuição condicional completa.
Para alvo π(x₁, x₂, ..., xₖ):
1. Amostra x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Amostra x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Continue para todas as variáveis
4. Repita
| Propriedade | Declaração |
|----------|-----------|
| Sempre aceita | α = 1 (sem etapa de rejeição) |
| Requer | Capacidade de extrair amostras de cada condicional completa |
| Convergência | Garantido para cadeias irredutíveis e aperiódicas |
### Diagnóstico MCMC
| Diagnóstico | Finalidade |
|-----------|---------|
| **Traçado gráfico** | Verificação visual de mistura e estacionariedade |
| **Autocorrelação** | Mede a dependência da amostra (quer baixa autocorrelação) |
| **Gelman-Rubin (R̂)** | Compare várias cadeias; R̂ < 1,05 sugere convergência |
| **Tamanho efetivo da amostra** | N_eff = N/(1 + 2Σρₖ); contas para autocorrelação |
| **Queimadura** | Descartar as amostras iniciais antes que a cadeia atinja a estacionariedade |
---

## Relevância para aprendizado de máquina e ciência de dados
| Processo Estocástico | Aplicação |
|-------------------|-------------|
| Cadeias de Markov | PageRank (passeio aleatório no gráfico da web), geração de texto (modelos de n-gramas), MCMC |
| Passeios aleatórios | Node2Vec e DeepWalk (embeddings de gráficos), exploração em RL |
| Movimento browniano | Modelagem de preços de ações, modelos de difusão em IA generativa |
| Processos de Poisson | Modelagem de chegadas de eventos (cliques, falhas), teoria das filas |
| Martingais | Matemática financeira, comprovando a convergência do SGD (aproximação estocástica) |
| Monte Carlo | Estimativa de valores esperados, inferência bayesiana, aprendizagem por reforço (avaliação de políticas) |
| MCMC (Metrópole-Hastings) | Amostragem posterior bayesiana, programação probabilística (Stan, PyMC) |
| Amostragem de Gibbs | Modelos de tópicos (LDA), redes Bayesianas, remoção de ruído de imagens |
| Diagnóstico MCMC | Garantir inferências fiáveis ​​a partir de modelos probabilísticos |
---

## Resumo
| Processo | Espaço de Estado | Tempo | Propriedade chave |
|---------|---------|------|-------------|
| Cadeia de Markov | Discreto/contínuo | Discreto/contínuo | Sem memória (propriedade de Markov) |
| Passeio aleatório | ℤᵈ | Discreto | Soma de i.i.d. etapas |
| Movimento browniano | ℝ | Contínuo | Incrementos gaussianos, caminhos contínuos |
| Processo de Poisson | ℕ | Contínuo | Processo de contagem com lacunas exponenciais |
| Martingale | ℝ | Discreto/contínuo | Jogo justo (E[X_{t+1}|F_t] = X_t) |
Os processos estocásticos são a matemática da aleatoriedade ao longo do tempo. Eles sustentam a inferência bayesiana moderna (MCMC), a aprendizagem por reforço (processos de decisão de Markov), a modelagem generativa (modelos de difusão), a matemática financeira e a teoria das filas. A compreensão desses processos fornece as ferramentas para modelar a incerteza de forma dinâmica — não apenas como um instantâneo, mas à medida que ela evolui.