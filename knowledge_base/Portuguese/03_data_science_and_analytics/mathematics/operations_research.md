---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Pesquisa Operacional
A pesquisa operacional (PO) é a aplicação de métodos matemáticos à tomada de decisões. Nascida durante a Segunda Guerra Mundial para a logística militar, agora otimiza cadeias de abastecimento, programa companhias aéreas, encaminha frotas de entrega, gerencia estoques e aloca recursos em todos os setores. OR fornece o kit de ferramentas matemáticas para tomar as melhores decisões possíveis sob restrições.
---

## Formulações de Programação Linear
### Formulário Padrão
Minimizar cᵀx
Sujeito a: Ax = b, x ≥ 0
### Formulações LP comuns
**Combinação de produtos:**
- Variáveis de decisão: xⱼ = quantidade do produto j a produzir
- Objetivo: maximizar o lucro Σ pⱼxⱼ
- Restrições: limites de recursos Σ aᵢⱼxⱼ ≤ bᵢ
**Problema de dieta:**
- Variáveis de decisão: xⱼ = quantidade de alimento j comprar
- Objetivo: minimizar custo Σ cⱼxⱼ
- Restrições: necessidades nutricionais Σ nᵢⱼxⱼ ≥ rᵢ
**Problema de mistura:**
- Variáveis de decisão: xⱼ = proporção do ingrediente j no blend
- Objetivo: minimizar custos
- Restrições: requisitos de qualidade (octanagem, resistência, etc.)
### Exemplo Resolvido: Planejamento de Produção
Uma fábrica fabrica os produtos A e B.
- A requer 2 horas de mão de obra, 1 kg de material; lucro $ 30
- B requer 1 hora de mão de obra, 3 kg de material; lucro $ 40
- Disponível: 40 horas de mão de obra, 30 kg de material
**Formulação:**
- Maximizar: 30x_A + 40x_B
- Sujeito a: 2x_A + x_B ≤ 40 (mão de obra)
- x_A + 3x_B ≤ 30 (material)
- x_A, x_B ≥ 0
**Solução:** Vértices da região viável: (0,0), (20,0), (18,4), (0,10)
- (0,0): lucro = 0
- (20,0): lucro = 600
- (18,4): lucro = 700 ← ótimo
- (0,10): lucro = 400
---

## Problema de transporte
Mover mercadorias de m fontes para n destinos a um custo mínimo.
### Formulação
- Variáveis de decisão: xᵢⱼ = quantidade embarcada da origem i ao destino j
- Objetivo: minimizar Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Sujeito a: Σⱼ xᵢⱼ = sᵢ (restrições de fornecimento)
- Σᵢ xᵢⱼ = dⱼ (restrições de demanda)
- xᵢⱼ ≥ 0
### Métodos de solução
| Método | Descrição | Qualidade da Solução Inicial |
|--------|-------------|---------------------------|
| **Canto Noroeste** | Comece no canto superior esquerdo, aloque avidamente | Viável, mas muitas vezes deficiente |
| **Aproximação de Vogel** | Considerar custos de penalização | Melhor solução inicial |
| **MODI/Trampolim** | Melhorar a solução inicial iterativamente | Encontra o ideal |
### Exemplo trabalhado
| | D1 | D2 | D3 | Fornecimento |
|---|----|----|----|--------|
| S1 | 2 | 3 | 1 | 50 |
| S2 | 4 | 1 | 5 | 30 |
| S3 | 3 | 2 | 4 | 20 |
| Demanda | 40 | 30 | 30 | 100 |
---

## Problema de Atribuição
Atribuir n trabalhadores a n empregos (um para um) para minimizar o custo total.
### Formulação
- Variáveis de decisão: xᵢⱼ ∈ {0, 1} (1 se o trabalhador i estiver atribuído ao trabalho j)
- Minimizar: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Sujeito a: Σⱼ xᵢⱼ = 1 (cada trabalhador consegue um emprego)
- Σᵢ xᵢⱼ = 1 (cada trabalho recebe um trabalhador)
### Algoritmo Húngaro
| Propriedade | Valor |
|----------|-------|
| Complexidade de tempo | O(n³) |
| Ideal? | Sim |
| Abordagem | Redução matricial + cobertura mínima |
**Etapas:**
1. Subtraia os mínimos das linhas de cada linha
2. Subtraia os mínimos das colunas de cada coluna
3. Cubra todos os zeros com um número mínimo de linhas
4. Se linhas = n, atribuição ótima encontrada entre zeros
5. Caso contrário, ajuste a matriz e repita
---

## Otimização do fluxo de rede
### Fluxo de Custo Mínimo
Dada uma rede com capacidades e custos nas bordas, encontre o fluxo que satisfaça as demandas com custo mínimo.
**Formulação:**
- Minimizar: Σ cᵢⱼxᵢⱼ
- Sujeito a: conservação do fluxo em cada nó
- Restrições de capacidade: 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Caminho mais curto como fluxo de rede
O problema do caminho mais curto é um caso especial de fluxo de custo mínimo (enviar 1 unidade de s para t).
### Aplicativos
| Aplicação | Modelo de Rede |
|------------|--------------|
| Cadeia de abastecimento | Nós = armazéns, arestas = rotas de navegação |
| Comunicação | Nós = roteadores, arestas = links com largura de banda |
| Tráfego | Nós = interseções, arestas = estradas com capacidade |
| Gestão de projetos | Redes CPM/PERT |
---

## Programação Dinâmica
**Programação dinâmica (DP)** resolve problemas complexos dividindo-os em subproblemas sobrepostos.
### Princípio de Otimização de Bellman
Uma política ótima tem a propriedade de que qualquer que seja o estado inicial e a decisão, as decisões restantes devem constituir uma política ótima para o estado resultante.
### Elementos-chave
| Elemento | Descrição |
|--------|-------------|
| **Palco** | Ponto de decisão (passo de tempo, índice de item) |
| **Estado** | Informações necessárias para tomar uma decisão |
| **Decisão** | Escolha feita em cada etapa |
| **Recorrência** | Valor ótimo na fase n em termos da fase n−1 |
### Problemas clássicos de DP
| Problema | Recorrência | Complexidade |
|---------|-----------|------------|
| **Fibonacci** | F(n) = F(n−1) + F(n−2) | O(n) com memorização |
| **Mochila** | V(i,w) = max(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **Caminho mais curto** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) ou O(E log V) |
| **Editar distância** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+custo) | O(mn) |
| **Subsequência comum mais longa** | L(i,j) = L(i−1,j−1)+1 se corresponder, caso contrário max(L(i−1,j), L(i,j−1)) | O(mn) |
| **Multiplicação em cadeia de matrizes** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |
### Exemplo Resolvido: Mochila 0/1
Itens: {peso: valor} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Capacidade W = 7.
V(i, w) = valor máximo usando os primeiros i itens com capacidade w
| eu\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |
Ótimo: V(4, 7) = 23 (itens 1 e 4: peso 2+5=7, valor 12+11=23).
---

## Teoria das Filas
A teoria das filas estuda as filas de espera – quanto tempo elas duram, quanto tempo você espera e como reduzir ambos.
### Notação de Kendall
A/B/c/K/N/D onde:
- A = processo de chegada (M = Markoviano/Poisson, D = determinístico, G = geral)
- B = processo de atendimento (mesmas opções)
- c = número de servidores
- K = capacidade (padrão ∞)
- N = população (padrão ∞)
- D = disciplina (FIFO, LIFO, Prioridade)
### Fila M/M/1 (servidor único)
| Métrica | Fórmula |
|--------|---------|
| Utilização | ρ = λ/μ |
| Número médio no sistema | eu = ρ/(1−ρ) |
| Tempo médio no sistema | W = 1/(μ−λ) |
| Número médio em fila | L_q = ρ²/(1−ρ) |
| Tempo médio de espera | W_q = ρ/(μ−λ) |
onde λ = taxa de chegada, μ = taxa de serviço, ρ = utilização.
### Fila M/M/c (vários servidores)
| Métrica | Fórmula |
|--------|---------|
| Utilização | ρ = λ/(cμ) |
| Probabilidade de espera (Erlang C) | P_w = fórmula complexa envolvendo ρ e c |
| Comprimento médio da fila | L_q = P_w · ρ/(1−ρ) |
### Lei de Little
L = λW (número médio no sistema = taxa de chegada × tempo médio)
Isto vale para QUALQUER sistema de filas, independentemente das distribuições de chegada/serviço.
### Exemplos de aplicação
| Cenário | Modelo de fila |
|----------|------------|
| Central de atendimento | M/M/c (agentes c) |
| Solicitações de servidor web | M/M/1 ou M/G/1 |
| Emergência hospitalar | M/G/c com prioridades |
| Linha de fabricação | Rede de filas |
| Agendamento de CPU do computador | Compartilhamento de processador M/M/1 |
---

## Modelos de inventário
### Quantidade Econômica do Pedido (EOQ)
A quantidade ideal do pedido que minimiza os custos totais de estoque.
Q* = √(2DS/H)
| Variável | Significado |
|----------|---------|
| D | Procura anual |
| S | Custo de encomenda por encomenda |
| H | Custo de manutenção por unidade e por ano |
| P* | Quantidade ideal de pedido |
**Custo total em Q*:** TC = √(2DSH)
### Extensões
| Modelo | Extensão |
|-------|-----------|
| **EOQ com descontos** | Descontos por quantidade alteram a função de custo |
| **Quantidade da ordem de produção** | Itens produzidos gradativamente, não entregues de uma só vez |
| **(s, Q) modelo** | Reordenar unidades Q quando o estoque cair para o nível s |
| **(s, S) modelo** | Encomende até S quando o estoque cair para s |
| **Modelo de fornecedor de notícias** | Demanda incerta e de período único |
### Modelo de fornecedor de notícias
Quantidade ideal de pedido para estoque perecível de período único:
P(D ≤ Q*) = c_u / (c_u + c_o)
onde c_u = custo menor (lucro cessante) e c_o = custo excedente (desperdício).
---

## Agendamento
### Agendamento de Job Shop
| Notação | Significado |
|----------|---------|
| n/m/J/C_max | n empregos, m máquinas, job shop, minimizar o makepan |
| Loja de fluxo | Todos os trabalhos visitam as máquinas na mesma ordem |
| Loja de empregos | Cada trabalho possui sua própria sequência de máquina |
| Loja aberta | Sem restrições de pedido |
### Regras de Prioridade
| Regra | Descrição | Efeito |
|------|------------|--------|
| FCFS | Primeiro a chegar, primeiro a ser servido | Justo, mas não ideal |
| SPT | Menor tempo de processamento primeiro | Minimiza a conclusão média |
| EDD | Data de vencimento mais antiga primeiro | Minimiza o atraso máximo |
| CR | Rácio crítico (prazo restante/tempo de processamento) | Equilibrado |
| LPT | Maior tempo de processamento primeiro | Bom para makespan em máquinas paralelas |
### Algoritmo de Johnson (Flow Shop de 2 Máquinas)
Para n jobs em 2 máquinas, minimizando o makepan:
1. Encontre o trabalho com menor tempo de processamento
2. Se estiver na máquina 1, agende primeiro; se estiver na máquina 2, agende por último
3. Remova esse trabalho e repita
Ideal para 2 máquinas; NP-difícil para 3+ máquinas.
---

## Relevância para aprendizado de máquina e ciência de dados
| OU Conceito | Aplicação |
|-----------|------------|
| Programação linear | Alocação de recursos, otimização de portfólio, alocação de orçamento publicitário |
| Transporte/atribuição | Logística, correspondência de transporte compartilhado, atribuição de tarefas |
| Fluxo de rede | Otimização da cadeia de suprimentos, roteamento de tráfego de data center |
| Programação dinâmica | Alinhamento de sequências (bioinformática), algoritmo de Viterbi (HMMs), RL (equação de Bellman) |
| Teoria das filas | Planejamento de capacidade de servidor, modelagem de latência, alocação de recursos em nuvem |
| Modelos de inventário | Integração de previsão de demanda, ML da cadeia de suprimentos |
| Agendamento | Orquestração de pipeline de ML, agendamento de tarefas de GPU, agendamento de pesquisa de hiperparâmetros |
| Programação inteira | Seleção de recursos (binário), seleção de modelo, projeto de rede |
---

## Resumo
| Tópico | Problema Central | Método Chave |
|-------|------------|------------|
| Formulações LP | Otimizar objetivo linear com restrições | Simplex, ponto interior |
| Transporte | Enviar mercadorias a um custo mínimo | MODI, trampolim |
| Atribuição | Combine trabalhadores com empregos | Algoritmo húngaro |
| Fluxo de rede | Fluxo de rota através de uma rede | Algoritmos de fluxo de custo mínimo |
| Programação Dinâmica | Subproblemas sobrepostos | Princípio de Bellman, memorização |
| Teoria das Filas | Análise de fila de espera | M/M/1, lei de Little |
| Inventário | Quando e quanto pedir | EOQ, fornecedor de notícias |
| Agendamento | Sequenciar trabalhos em máquinas | Regras de prioridade, algoritmo de Johnson |
A pesquisa operacional transforma a tomada de decisões de arte em ciência. Ao formular matematicamente problemas do mundo real, OR fornece soluções comprovadamente ótimas (ou quase ótimas) para problemas de logística, programação, alocação de recursos e planejamento que afetam todos os setores. Para os cientistas de dados, os métodos OR complementam o aprendizado de máquina: enquanto o ML prevê, o OR prescreve — e juntos, eles formam a base de sistemas de decisão inteligentes.