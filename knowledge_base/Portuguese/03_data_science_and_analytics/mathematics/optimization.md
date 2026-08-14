<!--
---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
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
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Otimização
Otimização é a matemática de encontrar a melhor solução a partir de um conjunto de soluções viáveis. Ele pergunta: dada uma função e restrições, qual entrada minimiza (ou maximiza) a saída? A otimização é o motor do aprendizado de máquina – treinar um modelo significa minimizar uma função de perda. Ele aparece em pesquisa operacional, economia, projeto de engenharia e praticamente em todos os campos quantitativos.
---

## Formulação do problema
Um **problema de otimização** geral tem a forma:
Minimize f(x)
Sujeito a: gᵢ(x) ≤ 0 (restrições de desigualdade), hⱼ(x) = 0 (restrições de igualdade)
| Prazo | Significado |
|------|---------|
| **Função objetivo** f(x) | A quantidade a minimizar (ou maximizar) |
| **Variáveis ​​de decisão** x | Os valores que podemos controlar |
| **Região viável** | Conjunto de todos x satisfazendo todas as restrições |
| **Mínimo global** | Viável x* com f(x*) ≤ f(x) para todo x viável |
| **Mínimo local** | Viável x* com f(x*) ≤ f(x) para todo x viável em alguma vizinhança |
| **Problema convexo** | f é convexa, a região viável é um conjunto convexo (min local = min global) |
---

## Programação Linear (LP)
Quando o objetivo e todas as restrições são **lineares**, o problema é um programa linear.
### Formulário Padrão
Minimizar cᵀx
Sujeito a: Machado ≤ b, x ≥ 0
onde c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.
### Propriedades
| Propriedade | Declaração |
|----------|-----------|
| Convexidade | LP é sempre um problema convexo |
| Solução ideal | Sempre em um vértice (ponto de canto) do politopo viável |
| Existência | Se a região viável for limitada e não vazia, existe solução ótima |
| Vários ótimos | Se dois vértices são ótimos, cada ponto na aresta entre eles também é ótimo |
### O Método Simplex
O **método simplex** (Dantzig, 1947) move-se ao longo das arestas do politopo viável de vértice a vértice, sempre melhorando o objetivo, até atingir o ótimo.
| Propriedade | Valor |
|----------|-------|
| Momento do pior caso | O(2ⁿ) (exponencial — raro na prática) |
| Tempo médio do caso | Polinômio para a maioria dos problemas práticos |
| Ideia chave | Mover para vértice adjacente com melhor valor objetivo |
**Algoritmo (visão geral):**
1. Comece com uma solução básica viável (vértice do politopo)
2. Escolha uma variável de entrada (uma que melhore o objetivo)
3. Escolha uma variável de saída (mantenha a viabilidade)
4. Pivô: vá para o novo vértice
5. Repita até que não exista nenhuma direção de melhoria
### Métodos de pontos internos
Alternativa ao simplex: aproximar o ótimo de dentro da região viável.
| Propriedade | Valor |
|----------|-------|
| Momento do pior caso | Polinômio (O(n³·⁵) para algumas variantes) |
| Desempenho prático | Competitivo com simplex em grandes problemas |
| Ideia chave | Seguir um “caminho central” pelo interior |
### Exemplo de LP trabalhado
**Problema:** Uma fábrica produz cadeiras (x₁) e mesas (x₂).
- Lucro: $ 30 por cadeira, $ 50 por mesa
- Madeira: 2x₁ + 4x₂ ≤ 100 (pés de tábua disponíveis)
- Mão de obra: x₁ + 3x₂ ≤ 60 (horas disponíveis)
- Maximizar: 30x₁ + 50x₂
**Solução (método gráfico para 2 variáveis):**
- Vértices da região viável: (0,0), (30,0), (40,10), (0,20)
- Avalie o objetivo em cada vértice:
  - (0,0): lucro = 0
  - (30,0): lucro = 900
  - (40,10): lucro = 1700 ← ótimo
  - (0,20): lucro = 1000
- **Ótimo:** x₁ = 40 cadeiras, x₂ = 10 mesas, lucro = $ 1.700
---

## Otimização Convexa
Um problema é **convexo** se a função objetivo for convexa e a região viável for um conjunto convexo.
### Conjuntos e funções convexas
| Conceito | Definição |
|--------|------------|
| **Conjunto convexo** | Para qualquer x, y no conjunto e t ∈ [0,1]: tx + (1−t)y também está no conjunto |
| **Função convexa** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) para todo t ∈ [0,1] |
| **Estritamente convexo** | A desigualdade é estrita para t ∈ (0,1) ex ≠ y |
**Propriedade chave:** Para otimização convexa, todo mínimo local é um mínimo global.
### Funções Convexas Comuns
| Função | Convexo? | Onde |
|----------|------------|-------|
| machado + b (linear) | Sim (e côncavo) | Em todos os lugares |
| x² | Sim | ℝ |
| eˣ | Sim | ℝ |
| −log(x) | Sim | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Sim | ℝⁿ |
| max(f₁, f₂) se f₁, f₂ convexo | Sim | Intersecção de domínios |
### Gradiente Descendente
O algoritmo de otimização mais fundamental em aprendizado de máquina.
**Regra de atualização:** x_{k+1} = x_k − α∇f(x_k)
onde α > 0 é a **taxa de aprendizagem** (tamanho do passo).
| Variante | Regra de atualização | Vantagem |
|--------|-------------|-----------|
| **Lote GD** | x ← x − α∇f(x) | Convergência estável |
| **GD Estocástico (SGD)** | x ← x − α∇fᵢ(x) (uma amostra) | Rápido por iteração, escapa dos mínimos locais |
| **Mini-lote SGD** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Balanço entre lote e estocástico |
| **Momentum** | v ← βv − α∇f(x); x ← x + v | Acelera em regiões planas |
| **Adão** | Taxas de aprendizagem adaptativa por parâmetro | Funciona bem imediatamente para aprendizado profundo |
| **RMSprop** | Dimensione a taxa de aprendizagem calculando a média da magnitude do gradiente | Bom para RNNs |
### Taxas de convergência
| Método | Convexo f | Fortemente convexo f |
|-------|----------|-------------------|
| Descida gradiente | O(1/k) | O((1−μ/L)ᵏ) (linear) |
| DGD | O(1/√k) | O(1/k) |
| GD acelerado (Nesterov) | O(1/k²) | O((1−√(μ/L))ᵏ) |
onde k = contagem de iterações, μ = parâmetro de convexidade forte, L = constante de Lipschitz.
### Escolhendo a taxa de aprendizagem
| Estratégia | Descrição |
|----------|------------|
| α fixo | Simples, mas pode divergir (muito grande) ou convergir lentamente (muito pequeno) |
| Pesquisa de linha | Encontre α que minimize f(x − α∇f(x)) ao longo da direção do gradiente |
| Cronogramas de decaimento | α_t = α₀ / (1 + βt) ou α_t = α₀ · βᵗ |
| Aquecimento | Comece pequeno, aumente e depois diminua (comum no treinamento de transformadores) |
| Adaptativo (Adão) | Taxas de aprendizagem por parâmetro baseadas em estatísticas de gradiente |
---

## Otimização restrita
### Multiplicadores de Lagrange
Para o problema: minimize f(x) sujeito a h(x) = 0.
**Lagrangiano:** L(x, λ) = f(x) + λh(x)
No ideal: ∇ₓL = 0 e ∇_λL = 0 (o que dá h(x) = 0).
**Exemplo resolvido:** Minimize f(x,y) = x² + y² sujeito a x + y = 1.
- L = x² + y² + λ(x + y − 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Restrição: x + y = 1 → −λ = 1 → λ = −1
- Solução: x = 1/2, y = 1/2, f = 1/2
### Condições KKT
As **condições de Karush-Kuhn-Tucker (KKT)** generalizam os multiplicadores de Lagrange para restrições de desigualdade.
Para: minimizar f(x) sujeito a gᵢ(x) ≤ 0, hⱼ(x) = 0.
**Lagrangiano:** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)
**Condições KKT** (necessárias para otimização):
| Condição | Equação |
|-----------|----------|
| Estacionaridade | ∇ₓL = 0 |
| Viabilidade primária | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| Viabilidade dupla | λᵢ ≥ 0 |
| Frouxidão complementar | λᵢgᵢ(x) = 0 para todo i |
**Frouxidão complementar** significa: se a restrição gᵢ não estiver ativa (gᵢ(x) < 0), então λᵢ = 0 (a restrição não afeta a solução).
Para problemas convexos que satisfazem a condição de Slater, as condições KKT são necessárias e suficientes.
---

## Dualidade
Todo problema de otimização (o **primal**) tem um problema **dual** associado.
### Dualidade Fraca e Forte
| Conceito | Declaração |
|--------|-----------|
| **Função dupla** | g(λ, ν) = infₓ L(x, λ, ν) |
| **Problema duplo** | Maximize g(λ, ν) sujeito a λ ≥ 0 |
| **Dualidade fraca** | Ótimo duplo ≤ Ótimo primordial (sempre válido) |
| **Forte dualidade** | Ótimo duplo = Ótimo primal (válido para problemas convexos com a condição de Slater) |
| **Lacuna de dualidade** | Primal Optimal - Dual Optimal (zero sob dualidade forte) |
### Por que a dualidade é importante
| Aplicação | Como a dualidade ajuda |
|------------|--------|
| Limites inferiores | Dual dá um certificado de quão boa é a solução primária |
| SVM | O duplo problema do SVM leva ao truque do kernel |
| Análise de sensibilidade | Variáveis ​​duais medem o quanto o ótimo muda se as restrições forem relaxadas |
| Decomposição | Grandes problemas podem ser divididos em subproblemas menores por meio do dual |
---

## Programação Inteira
Quando algumas ou todas as variáveis ​​devem ser **inteiras**, o problema se torna muito mais difícil (NP-difícil em geral).
### Tipos
| Tipo | Descrição |
|------|-------------|
| IP puro | Todas as variáveis ​​devem ser números inteiros |
| IP misto (MIP) | Algumas variáveis ​​inteiras, algumas contínuas |
| IP binário | Variáveis ​​restritas a {0, 1} |
### Métodos de solução
| Método | Idéia |
|--------|------|
| **Filial e destino** | Dividir em subproblemas, resolver relaxamentos LP, podar |
| **Planos de corte** | Adicionar restrições lineares para reforçar o relaxamento LP |
| **Galho e corte** | Combine branch-and-bound com planos de corte |
| **Heurísticas** | Busca local gananciosa, recozimento simulado para soluções aproximadas |
---

## Métodos Heurísticos e Metaheurísticos
Quando a otimização exata é intratável, a heurística encontra boas soluções (não necessariamente ótimas).
| Método | Ideia-chave | Melhor para |
|--------|----------|----------|
| **Descida gradiente** | Siga a descida mais íngreme | Funções suaves e diferenciáveis ​​|
| **Método de Newton** | Use informações de segunda ordem (curvatura) | Problemas suaves e bem condicionados |
| **Recozimento simulado** | Aceitar soluções piores com probabilidade decrescente | Otimização global, combinatória |
| **Algoritmos genéticos** | Evoluir uma população usando seleção, cruzamento, mutação | Multiobjetivo, não diferenciável |
| **Enxame de partículas** | Agentes exploram o espaço, influenciados por posições mais conhecidas | Contínuo, não convexo |
| **Otimização Bayesiana** | Construir modelo substituto, usar função de aquisição | Funções caras de caixa preta (ajuste de hiperparâmetros) |
### Método de Newton para Otimização
**Regra de atualização:** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)
onde H é a matriz Hessiana (matriz de segundas derivadas).
| Propriedade | Valor |
|----------|-------|
| Taxa de convergência | Quadrático (quase ótimo) |
| Custo por iteração | O(n³) para inversão Hessiana |
| Requer | Duas vezes diferenciável, Hessiano definido positivo |
| Quase Newton (BFGS) | Hessian aproximado de gradientes | O(n²) por iteração |
---

## Relevância para aprendizado de máquina e ciência de dados
| Conceito de Otimização | Aplicação |
|----------|-------------|
| Descida gradiente | Treinamento de redes neurais, regressão logística, qualquer modelo diferenciável |
| SGD e variantes | ML em larga escala (treinamento em minilotes), aprendizagem online |
| Adam, RMSprop | Otimizadores padrão para aprendizado profundo |
| Otimização convexa | SVMs, regressão logística, LASSO, Ridge (ótimo global garantido) |
| Multiplicadores de Lagrange | Aprendizagem restrita, ML justo, alocação de recursos |
| Condições KKT | Derivando SVM dual, entendendo a atividade de restrição |
| Dualidade | Truque do kernel SVM, análise de sensibilidade, métodos de decomposição |
| Programação linear | Alocação de recursos, otimização de portfólio, fluxo de rede |
| Programação inteira | Seleção de recursos (binários), escalonamento, problemas combinatórios |
| Otimização Bayesiana | Ajuste de hiperparâmetros (Optuna, Hyperopt) |
| Newton/quase-Newton | Métodos de segunda ordem para problemas de pequeno a médio porte (L-BFGS) |
---

## Resumo
| Método | Tipo de problema | Garantias | Escala |
|--------|------------|------------|-------|
| Simplexo | Programação linear | Ótimo exato | Milhões de variáveis ​​|
| Ponto interior | Convexo (LP, QP, SOCP) | Ótimo exato | Grande escala |
| Descida gradiente | Suave sem restrições | Converge para min local | Muito grande (aprendizado profundo) |
| DGD | Risco empírico em grande escala | Converge (com decadência) | Conjuntos de dados massivos |
| Newton/BFGS | Suave, duas vezes diferenciável | Convergência quadrática | Pequeno a médio |
| KKT/Lagrange | Restrito (convexo) | Exato sob condições | Médio |
| Filial e destino | Programação inteira | Ótimo exato | Pequeno a médio |
| Heurísticas | Qualquer (não convexo, combinatório) | Sem garantia | Varia |
A otimização é sem dúvida a ferramenta matemática mais importante no aprendizado de máquina. Cada modelo que você treina — desde regressão linear até grandes modelos de linguagem — envolve a solução de um problema de otimização. Compreender quando um problema é convexo (ótimo global garantido), quando a descida do gradiente convergirá e como lidar com restrições fornece a base teórica para projetar, depurar e melhorar algoritmos de aprendizagem.