<!--
---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
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
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Teoria dos Jogos
A teoria dos jogos é a matemática da interação estratégica – situações em que o seu resultado depende não apenas das suas próprias escolhas, mas das escolhas dos outros. Das guerras de preços entre empresas às corridas ao armamento nuclear, dos leilões online à biologia evolutiva, a teoria dos jogos fornece as ferramentas para analisar o conflito e a cooperação. Tornou-se cada vez mais relevante para o aprendizado de máquina por meio do aprendizado por reforço multiagente, redes adversárias generativas (GANs) e design de mecanismos para plataformas online.
---

## Jogos de Forma Estratégica
### Definição
Um **jogo de forma estratégica (forma normal)** consiste em:
- Um conjunto de jogadores N = {1, 2, ..., n}
- Estratégia define S₁, S₂, ..., Sₙ para cada jogador
- Funções de retorno u₁, u₂, ..., uₙ mapeando perfis de estratégia para números reais
### Exemplo: Dilema do Prisioneiro
| | Cooperar (C) | Defeito (D) |
|---|---------------|-----------|
| **Cooperar (C)** | (−1, −1) | (−3, 0) |
| **Defeito (D)** | (0, −3) | (−2, −2) |
| Análise | Resultado |
|----------|--------|
| Estratégia dominante | Defeito (D domina C para ambos os jogadores) |
| Equilíbrio de Nash | (D, D) com retorno (−2, −2) |
| Ótimo social | (C, C) com retorno (−1, −1) |
| Dilema | A racionalidade individual leva à irracionalidade coletiva |
### Mais jogos clássicos
**Batalha dos Sexos:**
| | Ópera | Futebol |
|---|-------|----------|
| Ópera | (2, 1) | (0, 0) |
| Futebol | (0, 0) | (1, 2) |
Dois equilíbrios de Nash: (Ópera, Ópera) e (Futebol, Futebol).
**Frango (Pomba-Falcão):**
| | Falcão | Pomba |
|---|------|------|
| Falcão | (−10, −10) | (5, 0) |
| Pomba | (0, 5) | (1, 1) |
Dois equilíbrios de Nash: (Hawk, Dove) e (Dove, Hawk).
---

## Estratégias Dominantes
| Conceito | Definição |
|--------|------------|
| **Estritamente dominante** | Estratégia sᵢ oferece maior retorno do que qualquer outra estratégia, independentemente das escolhas dos oponentes |
| **Fracamente dominante** | A estratégia sᵢ oferece um retorno pelo menos tão alto quanto qualquer outro, e estritamente mais alto para alguns perfis de oponentes |
| **Estratégia dominada** | Uma estratégia que nunca é a melhor resposta |
**Eliminação iterada de estratégias dominadas:**
1. Remova quaisquer estratégias estritamente dominadas
2. Repita até que nada mais possa ser removido
3. Se permanecer um perfil de estratégia, será o equilíbrio único de Nash
---

## Equilíbrio de Nash
Um **equilíbrio de Nash** é um perfil de estratégia em que nenhum jogador pode melhorar seu retorno alterando unilateralmente sua estratégia.
### Definição
(s₁*, s₂*, ..., sₙ*) é um equilíbrio de Nash se para cada jogador i:
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) para todos sᵢ ∈ Sᵢ
### Encontrando o equilíbrio de Nash (jogos 2×2)
**Melhor método de resposta:**
1. Para cada coluna, sublinhe a melhor resposta do jogador 1
2. Para cada linha, sublinhe a melhor resposta do jogador 2
3. As células onde ambos estão sublinhados são equilíbrios de Nash
### Existência (Teorema de Nash)
Todo jogo finito possui pelo menos um equilíbrio de Nash (possivelmente em estratégias mistas).
### Estratégias Mistas
Uma **estratégia mista** é uma distribuição de probabilidade sobre estratégias puras.
| Conceito | Definição |
|--------|------------|
| Estratégia mista σᵢ | Distribuição de probabilidade sobre Sᵢ |
| Estratégia mista NE | Nenhum jogador pode melhorar o retorno esperado alterando a sua mistura |
| Suporte | Conjunto de estratégias puras jogadas com probabilidade positiva |
**Exemplo resolvido: centavos correspondentes**
| | Cabeças | Caudas |
|---|-------|-------|
| Cabeças | (1, −1) | (−1, 1) |
| Caudas | (−1, 1) | (1, −1) |
Nenhuma estratégia pura NE. NE misto: ambos jogam H e T com probabilidade ½ cada.
---

## Teorema Minimax
### Jogos de soma zero
Em um **jogo de soma zero**, o ganho de um jogador é exatamente a perda do outro: u₁ + u₂ = 0.
### Teorema Minimax de Von Neumann
Para cada jogo finito de soma zero para dois jogadores:
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
O **maximin** (melhor pior caso para o jogador 1) é igual ao **minimax** (melhor pior caso para o jogador 2). Este valor comum é o **valor do jogo**.
### Resolvendo jogos de soma zero
Para um jogo de soma zero 2×2 com matriz:
| | eu | R |
|---|---|---|
| T | uma | b |
| B | c | e |
Estratégia mista ideal do jogador 1: jogar T com probabilidade p = (d−c)/((a−b)+(d−c))
Valor do jogo: v = (ad−bc)/((a−b)+(d−c))
---

## Jogos de formato extensivo
Jogos com movimentos sequenciais são representados como **árvores de jogo**.
### Conceitos-chave
| Conceito | Definição |
|--------|------------|
| **Árvore de jogo** | Árvore mostrando todas as sequências possíveis de movimentos |
| **Conjunto de informações** | Conjunto de nós que um jogador não consegue distinguir |
| **Informação perfeita** | Cada conjunto de informações é um singleton (todos os movimentos observáveis) |
| **Subjogo perfeito NE** | Equilíbrio de Nash em todos os subjogos |
| **Indução reversa** | Resolva do final da árvore para trás |
### Teorema de Zermelo
Em jogos de dois jogadores com informação finita e perfeita, sem chance: ou um jogador tem uma estratégia vencedora ou ambos podem forçar um empate (por exemplo, xadrez).
---

## Jogos Cooperativos
Em **jogos cooperativos**, os jogadores podem formar acordos e coalizões vinculativos.
### Função Característica
Um jogo cooperativo é definido por uma **função característica** v: 2^N → ℝ, onde v(S) é o valor que a coalizão S pode alcançar.
| Propriedade | Definição |
|----------|------------|
| **Superaditivo** | v(S ∪ T) ≥ v(S) + v(T) para S, T disjuntos |
| **Convexo** | v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) para S ⊂ T |
### O Núcleo
O **núcleo** é o conjunto de alocações onde nenhuma coalizão pode melhorar rompendo:
Núcleo = {x ∈ ℝⁿ: Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) para todos S ⊂ N}
O núcleo pode estar vazio — nesse caso, não existe alocação estável.
### Valor Shapley
O **valor Shapley** fornece uma alocação justa única com base em contribuições marginais:
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]
| Propriedade | Declaração |
|----------|-----------|
| Eficiência | Σ φᵢ = v(N) (todos os valores são distribuídos) |
| Simetria | Contribuintes iguais recebem pagamentos iguais |
| Jogador fictício | Não contribuintes ganham zero |
| Aditividade | φ(v + w) = φ(v) + φ(w) |
**Interpretação:** O valor Shapley de cada jogador é sua contribuição marginal média em todas as ordenações possíveis de formação de coalizão.
### Exemplo trabalhado
Três jogadores: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.
| Jogador | Contribuições marginais (média das encomendas) | Valor Shapley |
|--------|-------------------------------------------------|---------------|
| 1 | (100+50+70+70+50+0)/6 = 56,7 | 37,5 |
| 2 | (100+50+60+60+50+0)/6 | 27,5 |
| 3 | (100+70+60+70+60+0)/6 | 35,0 |
(Calculado precisamente usando a fórmula de Shapley para cada permutação.)
---

## Projeto de Mecanismo
**Design de mecanismo** é a “teoria dos jogos inversos” – em vez de analisar determinados jogos, projete jogos que produzam os resultados desejados.
### O Princípio da Revelação
Qualquer mecanismo que alcance um resultado desejado pode ser substituído por um **mecanismo de revelação direta** onde dizer a verdade é um equilíbrio de Nash.
### Teoria do Leilão
| Tipo de leilão | Regras | Equivalência de receitas |
|------------|-------|---------------------|
| **Oferta selada de primeiro preço** | O licitante com lance mais alto vence e paga seu lance | Todos os leilões padrão geram a mesma receita esperada |
| **Oferta selada de segundo preço (Vickrey)** | O licitante com lance mais alto vence e paga o segundo lance mais alto | (sob valores privados independentes) |
| **Inglês (ascendente)** | Aumentos de preços; primeiro a aceitar vitórias | — |
| **Holandês (descendente)** | O preço cai; primeiro a aceitar vitórias | — |
### Leilão Vickrey (segundo preço)
**Estratégia dominante:** Dê lances pelo seu verdadeiro valor.
| Propriedade | Declaração |
|----------|-----------|
| Licitação verdadeira | Estratégia fracamente dominante |
| Eficiência | Item vai para licitante de maior valor |
| Receita | Mesma receita esperada que o primeiro preço (Teorema da Equivalência de Receita) |
### Design de leilão ideal (Myerson)
O leilão que maximiza a receita:
- Aloca para o licitante com maior **avaliação virtual**
- Define um preço de reserva
- Avaliação virtual: ψ(v) = v − (1−F(v))/f(v)
---

## Conexões com aprendizado de máquina
### Redes Adversariais Gerativas (GANs)
GANs são um jogo para dois jogadores entre um gerador G e um discriminador D:
min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]
| Conceito de Teoria dos Jogos | Equivalente a GAN |
|--------------------|-----------------|
| Jogo de soma zero para dois jogadores | Gerador vs discriminador |
| Equilíbrio de Nash | G gera dados reais, D gera ½ em todos os lugares |
| Mínimo | A função objetivo GAN |
| Colapso do modo | Incapacidade de atingir o equilíbrio |
### Aprendizado por Reforço Multiagente (MARL)
| Conceito | Aplicação MARL |
|--------|-----------------|
| Equilíbrio de Nash | Políticas estáveis ​​em ambientes multiagentes |
| Mínimo | Políticas robustas contra adversários adversários |
| Jogos cooperativos | Formação de coalizão, alocação de tarefas |
| Valor Shapley | Cessão de crédito (qual agente contribuiu com o quê?) |
| Projeto de mecanismo | Projetando incentivos em sistemas multiagentes |
| Peça fictícia | Algoritmo de aprendizagem convergindo para o equilíbrio de Nash |
### Outras conexões de ML
| Aplicação | Ferramenta de Teoria dos Jogos |
|------------|-----------------|
| Design de leilão de anúncios (Google, Facebook) | Projeto de mecanismo, teoria do leilão |
| Design de mercado (Uber, Airbnb) | Teoria da correspondência, projeto de mecanismo |
| Robustez adversária | Jogos de soma zero entre atacante e defensor |
| Divisão justa | Valor Shapley, alocação sem inveja |
| Aprendizagem federada | Teoria dos jogos cooperativos para medição de contribuição |
| Sistemas de recomendação | Projeto de mecanismo para elicitação de preferências verdadeiras |
---

## Resumo
| Conceito | Ideia Central | Resultado chave |
|---------|-----------|------------|
| Jogos de forma estratégica | Jogadores, estratégias, recompensas | Representação da matriz do jogo |
| Estratégias dominantes | Melhor independentemente dos outros | Eliminação iterada |
| Equilíbrio de Nash | Nenhum desvio unilateral rentável | Existe em todos os jogos finitos |
| Estratégias mistas | Randomizar as ações | Teorema da existência de Nash |
| Mínimo | Melhor pior caso (soma zero) | Teorema minimax de Von Neumann |
| Forma extensiva | Movimentos sequenciais | Indução retroativa, perfeição de subjogo |
| Jogos cooperativos | Coligações vinculativas | Núcleo, valor Shapley |
| Projeto de mecanismo | Projete jogos para resultados | Princípio da revelação, leilões ótimos |
| Teoria do leilão | Venda via concorrência | Equivalência de receitas, leilão de Vickrey |
A teoria dos jogos é a matemática do pensamento estratégico. Num mundo cada vez mais povoado pela interação de agentes de IA, mercados automatizados e sistemas adversários, a teoria dos jogos fornece o conjunto de ferramentas essencial para prever comportamentos, conceber mecanismos e construir sistemas multiagentes robustos. Para cientistas de dados, explica como funcionam as GANs, como os leilões online geram bilhões em receitas e como construir sistemas de IA com bom desempenho em ambientes competitivos.