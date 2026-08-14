---
# Metadata
title: "Graph Theory"
description: "Graph representations, trees, traversals, shortest paths, minimum spanning trees, network flows, and spectral graph theory"
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
    changes: "Initial deep-dive into graph theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [graph-theory, trees, traversals, shortest-paths, spanning-trees, network-flows, spectral-graph-theory]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Teoria dos Grafos
Um **gráfico** é uma estrutura matemática que consiste em vértices (nós) conectados por arestas (links). Relacionamentos de modelos de gráficos: redes sociais, roteiros, redes neurais, dependências, canais de comunicação. A teoria dos grafos – o estudo dessas estruturas – fornece algoritmos e teoremas que são centrais para a ciência da computação, pesquisa operacional e ciência de dados.
---

## Conceitos Fundamentais
### Definições
| Prazo | Definição | Notação |
|------|------------|----------|
| **Gráfico** | Um par G = (V, E) de vértices e arestas | G |
| **Vértice (nó)** | Um elemento de V | v, você, w |
| **Borda** | Uma conexão entre dois vértices | e = (u, v) ou {u, v} |
| **Encomenda** | Número de vértices | \|V\| = n |
| **Tamanho** | Número de arestas | \|E\| = m |
| **Graduação** | Número de arestas incidentes a um vértice | graus(v) |
| **Caminho** | Sequência de vértices distintos conectados por arestas | v₁, v₂, ..., vₖ |
| **Ciclo** | Um caminho que começa e termina no mesmo vértice | v₁ → v₂ → ... → vₖ → v₁ |
| **Conectado** | Existe um caminho entre cada par de vértices | — |
| **Componente** | Um subgrafo conectado máximo | — |
| **Subgrafo** | Um gráfico formado a partir de um subconjunto de V e E | H ⊆ G |
### Tipos de gráficos
| Tipo | Descrição | Exemplo |
|------|-------------|---------|
| **Não direcionado** | As arestas não têm direção | Rede de amizade |
| **Dirigido (dígrafo)** | As arestas têm direção (arcos) | Links de páginas da Web |
| **Ponderada** | As arestas carregam valores numéricos | Distâncias rodoviárias |
| **Não ponderado** | Todas as arestas são equivalentes | Conexões sociais |
| **Simples** | Sem loops, sem múltiplas arestas | A maioria dos gráficos de livros didáticos |
| **Multigrafo** | São permitidas múltiplas arestas entre os mesmos vértices | Rotas de voo (múltiplos voos entre cidades) |
| **Concluído** | Cada par de vértices está conectado | Kₙ tem n(n−1)/2 arestas |
| **Bipartido** | Os vértices são divididos em dois grupos; arestas apenas cruzam grupos | Matrizes de recomendação de itens de usuário |
| **Planar** | Pode ser desenhado sem cruzamentos de arestas | Layouts de placas de circuito |
| **Árvore** | Gráfico conectado e acíclico | Árvores de decisão, sistemas de arquivos |
| **DAG** | Dirigido, sem ciclos direcionados | Agendamento de tarefas, gráficos de dependência |
### O Lema do Aperto de Mão
A soma de todos os graus dos vértices é igual a duas vezes o número de arestas:
Σᵥ deg(v) = 2|E|
**Corolário:** Todo gráfico possui um número par de vértices de graus ímpares.
**Exemplo:** Em uma festa de 10 pessoas onde todos apertam a mão de exatamente 3 outras pessoas: Σ deg = 30, então |E| = 15 apertos de mão no total.
---

## Representações gráficas
A maneira como você armazena um gráfico na memória determina a eficiência de cada algoritmo executado nele.
| Representação | Espaço | Pesquisa de borda | Iterar vizinhos | Melhor para |
|----------------|-------|-------------|-----------------------|----------|
| **Matriz de Adjacência** | O(n²) | O(1) | Sobre(n) | Gráficos densos, testes rápidos de arestas |
| **Lista de Adjacências** | O(n + m) | O(graus(v)) | O(graus(v)) | Gráficos esparsos, a maioria das redes do mundo real |
| **Lista de bordas** | O(m) | O(m) | O(m) | Algoritmos simples, MST de Kruskal |
| **Matriz de Incidência** | O(n·m) | O(m) | O(m) | Algoritmos especializados |
### Matriz de Adjacência
Uma matriz n × n A onde A[i][j] = 1 se a aresta (i,j) existir, 0 caso contrário. Para gráficos ponderados, A[i][j] = peso.
**Propriedades:**
- Simétrico para gráficos não direcionados
- Aᵏ[i][j] = número de caminhadas de comprimento k de i a j
- Autovalores de A revelam propriedades estruturais (ver Teoria dos Grafos Espectrais)
### Lista de Adjacências
Uma matriz (ou mapa hash) onde cada vértice v armazena uma lista de seus vizinhos.
```
Vertex 0: [1, 3]
Vertex 1: [0, 2, 3]
Vertex 2: [1, 3]
Vertex 3: [0, 1, 2]
```

Esta é a representação mais comum para gráficos do mundo real, que normalmente são esparsos (m ≪ n²).
---

## Árvores
Uma **árvore** é um gráfico conectado, acíclico e não direcionado. Uma **floresta** é uma união disjunta de árvores.
### Propriedades das árvores
Para uma árvore com n vértices:
- Tem exatamente n − 1 arestas
- Existe exatamente um caminho entre quaisquer dois vértices
- Remover qualquer borda o desconecta
- Adicionar qualquer aresta cria exatamente um ciclo
### Tipos de árvores
| Tipo | Descrição | Aplicação |
|------|-------------|-------------|
| **Árvore enraizada** | Um vértice designado como raiz | Sistemas de arquivos, organogramas |
| **Árvore binária** | Cada nó possui no máximo 2 filhos | BSTs, análise de expressão, árvores de decisão |
| **Árvore balanceada** | A altura é O(log n) | Árvores AVL, árvores rubro-negras (bancos de dados) |
| **Árvore abrangente** | Subgrafo que inclui todos os vértices e é uma árvore | Projeto de rede, algoritmos de aproximação |
| **Árvore geradora mínima** | Árvore geradora com peso total mínimo da aresta | Projeto de rede, clustering |
| **Gráfico estrela** | Um nó central conectado a todos os outros | Redes hub-and-spoke |
### Propriedades da árvore binária
| Propriedade | Fórmula |
|----------|---------|
| Máximo de nós na profundidade d | 2ᵈ |
| Máximo de nós na árvore de altura h | 2ʰ⁺¹ − 1 |
| Altura mínima para n nós | ⌊log₂(n)⌋ |
| Nós folha em árvore binária completa | Nós internos + 1 |
### Travessias em árvores
| Travessia | Encomendar | Caso de uso |
|----------|-------|----------|
| **Pré-encomenda** | Raiz → Esquerda → Direita | Copiando uma árvore, expressão de prefixo |
| **Em ordem** | Esquerda → Raiz → Direita | Saída classificada do BST |
| **Pós-encomenda** | Esquerda → Direita → Raiz | Excluindo uma árvore, expressão postfix |
| **Ordem de nível (BFS)** | Nível por nível, da esquerda para a direita | Caminho mais curto na árvore não ponderada |
---

## Travessias de gráfico
Algoritmos de travessia visitam sistematicamente todos os vértices alcançáveis.
### Pesquisa em amplitude (BFS)
Explora vértices camada por camada, usando uma **fila**.
| Propriedade | Valor |
|----------|-------|
| Estrutura de dados | Fila (FIFO) |
| Complexidade de tempo | O(V + E) |
| Complexidade espacial | O(V) |
| Encontra o caminho mais curto? | Sim (gráficos não ponderados) |
| Completo? | Sim (explora todos os vértices acessíveis) |
**Algoritmo:**
1. Comece nos vértices de origem s. Mark foi visitado. Enfileirar s.
2. Enquanto a fila não estiver vazia: retire da fila o vértice u. Para cada vizinho não visitado v de u: marque v visitado, enfileire v.
**Aplicações:** caminho mais curto em gráficos não ponderados, componentes conectados, testes de bipartição, rastreamento da web.
### Pesquisa em profundidade (DFS)
Explora o mais profundamente possível antes de retroceder, usando uma **pilha** (ou recursão).
| Propriedade | Valor |
|----------|-------|
| Estrutura de dados | Pilha (LIFO) / recursão |
| Complexidade de tempo | O(V + E) |
| Complexidade espacial | O(V) |
| Encontra o caminho mais curto? | Não |
| Completo? | Sim (para gráficos finitos) |
**Algoritmo:**
1. Comece no vértice s. Mark foi visitado.
2. Para cada vizinho não visitado v de s: DFS recursivamente de v.
**DFS classifica arestas em:**
- **Bordas da árvore:** parte da árvore DFS
- **Bordas posteriores:** conecta um vértice ao seu ancestral (indica ciclos)
- **Arestas frontais:** conectam um vértice ao seu descendente
- **Bordas cruzadas:** conecta vértices em ramificações diferentes
**Aplicações:** classificação topológica, detecção de ciclo, componentes fortemente conectados, solução de labirintos.
### Comparação de BFS vs DFS
| Critério | BFS | DFS |
|-----------|-----|-----|
| Estratégia | Largo e profundo | Profundo e depois largo |
| Memória | Superior (fronteira de lojas) | Inferior (caminho das lojas) |
| Caminho mais curto (sem ponderação) | Garantido | Não garantido |
| Use quando a solução estiver próxima do início | Melhor | Pior |
| Use quando o gráfico for muito profundo | Pior | Melhor |
| Classificação topológica | Variante do algoritmo de Kahn | Abordagem padrão |
---

## Algoritmos de caminho mais curto
Encontrar o caminho mais curto entre vértices é um dos problemas gráficos mais importantes na prática.
### Algoritmo de Dijkstra
Encontra os caminhos mais curtos de uma única origem para todos os outros vértices em um gráfico com pesos de aresta **não negativos**.
| Propriedade | Valor |
|----------|-------|
| Pesos de borda | Deve ser ≥ 0 |
| Tempo (pilha binária) | O((V + E)log V) |
| Tempo (pilha de Fibonacci) | O(E + V log V) |
| Ambicioso? | Sim |
| Lida com pesos negativos? | Não |
**Algoritmo:**
1. Inicialize dist[s] = 0, dist[v] = ∞ para todos v ≠ s. Fila de prioridade Q com todos os vértices.
2. Enquanto Q não estiver vazio: extraia o vértice u com dist mínimo. Para cada vizinho v de u com peso de aresta w: se dist[u] + w < dist[v], atualize dist[v] = dist[u] + w.
**Exemplo resolvido:**```
Graph: A --1-- B --2-- C --1-- D
       A --4-- C
       B --1-- D

Shortest paths from A:
A → B: 1 (direct)
A → D: 2 (A→B→D)
A → C: 3 (A→B→C, NOT A→C=4)
```

### Algoritmo Bellman-Ford
Lida com pesos de aresta **negativos** e detecta ciclos negativos.
| Propriedade | Valor |
|----------|-------|
| Pesos de borda | Qualquer (detecta ciclos negativos) |
| Complexidade de tempo | O(V·E) |
| Complexidade espacial | O(V) |
| Lida com ciclos negativos? | Sim (detecta e reporta) |
**Algoritmo:**
1. Inicialize dist[s] = 0, dist[v] = ∞ para todos v ≠ s.
2. Repita V − 1 vezes: para cada aresta (u, v) com peso w: se dist[u] + w < dist[v], atualize dist[v].
3. Verifique se há ciclos negativos: se alguma aresta ainda puder ser relaxada, existe um ciclo negativo.
### Algoritmo Floyd-Warshall
Encontra os caminhos mais curtos entre **todos os pares** de vértices.
| Propriedade | Valor |
|----------|-------|
| Complexidade de tempo | O(V³) |
| Complexidade espacial | O(V²) |
| Lida com pesos negativos? | Sim (mas não ciclos negativos) |
| Abordagem | Programação dinâmica |
**Recorrência:** dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) para cada vértice intermediário k.
### Guia de seleção de algoritmo
| Cenário | Algoritmo |
|----------|-----------|
| Fonte única, pesos não negativos | Dijkstra |
| Fonte única, pesos negativos possíveis | Bellman-Ford |
| Todos os pares, gráfico denso | Floyd-Warshall |
| Todos os pares, gráfico esparso | Execute Dijkstra de cada vértice |
| Gráfico não ponderado | BFS |
| DAG (sem ciclos) | Ordenação topológica + relaxamento |
| A* (guiado por heurística) | Pesquisa A* (para pathfinding com boa heurística) |
---

## Árvores de abrangência mínima
Uma **árvore geradora mínima (MST)** conecta todos os vértices com peso total mínimo da aresta.
### Propriedades
- Um MST tem exatamente n − 1 arestas (para n vértices)
- Existe um MST se o gráfico estiver conectado
- Um gráfico com pesos de arestas distintos possui um MST único
- MST satisfaz a **propriedade de corte**: a aresta de peso mínimo que cruza qualquer corte pertence ao MST
- MST satisfaz a **propriedade do ciclo**: a aresta de peso máximo em qualquer ciclo não pertence ao MST
### Algoritmo de Kruskal
| Propriedade | Valor |
|----------|-------|
| Estratégia | Ganancioso - adicione bordas em ordem de peso |
| Estrutura de dados | Conjunto disjunto (localização de união) |
| Complexidade de tempo | O(E log E) |
| Melhor para | Gráficos esparsos |
**Algoritmo:**
1. Classifique todas as arestas por peso.
2. Para cada aresta (em ordem): se a adição não criar um ciclo (verifique com union-find), adicione-a ao MST.
3. Pare quando n − 1 arestas forem selecionadas.
### Algoritmo de Prim
| Propriedade | Valor |
|----------|-------|
| Estratégia | Ganancioso — crescer árvore a partir de um vértice inicial |
| Estrutura de dados | Fila de prioridade (min-heap) |
| Complexidade de tempo | O(E log V) com heap binário |
| Melhor para | Gráficos densos |
**Algoritmo:**
1. Comece em qualquer vértice. Marque-o como parte do MST.
2. Adicione repetidamente a aresta de peso mínimo conectando um vértice no MST a um vértice fora dele.
3. Pare quando todos os vértices estiverem incluídos.
### Aplicativos MST
| Aplicação | Como o MST ajuda |
|------------|---------------|
| Projeto de rede | Coloque o mínimo de cabo/tubo para conectar todos os locais |
| Agrupamento | Remova as k − 1 arestas MST mais longas para obter k clusters |
| Algoritmos de aproximação | 2-aproximação para TSP métrico |
| Segmentação de imagens | Agrupar pixels por MST de similaridade de cores |
| Eliminação de recursos | Remova recursos redundantes usando MST do gráfico de correlação |
---

## Fluxo de rede
Os problemas de fluxo de rede modelam a movimentação de recursos através de um sistema.
### Definição de Rede de Fluxo
Uma **rede de fluxo** é um gráfico direcionado com:
- Um vértice de **fonte** (produz fluxo)
- Um vértice **sink** t (consome fluxo)
- **Capacidades** c(u,v) ≥ 0 em cada aresta
- **Fluxo** f(u,v) satisfatório:
  - **Restrição de capacidade:** 0 ≤ f(u,v) ≤ c(u,v)
  - **Conservação de fluxo:** fluxo de entrada = fluxo de saída em todos os vértices, exceto s e t
### Problema de Fluxo Máximo
Encontre o fluxo total máximo de s a t.
**Método Ford-Fulkerson:**
1. Embora exista um caminho crescente de s para t no gráfico residual:
2. Encontre a capacidade do gargalo ao longo do caminho
3. Aumente o fluxo ao longo do caminho na quantidade de gargalo
4. Atualizar capacidades residuais
| Algoritmo | Complexidade do tempo | Notas |
|-----------|----------------|-------|
| Ford-Fulkerson (DFS) | O(m · f*) onde f* é fluxo máximo | Não pode terminar com capacidades irracionais |
| Edmonds-Karp (BFS) | O(V·E²) | Sempre termina, escolhe o caminho de aumento mais curto |
| Algoritmo de Dinic | O(V²·E) | Utiliza fluxos de bloqueio; O(V^(1/2) · E) para capacidades unitárias |
### Teorema do corte mínimo do fluxo máximo
O **fluxo máximo** de s para t é igual à capacidade de **corte mínimo** que separa s de t.
Um **corte** (S, T) particiona vértices em S (contendo s) e T (contendo t). A capacidade de corte é a soma das capacidades das arestas de S a T.
**Aplicações de fluxo máximo:**
- Correspondência bipartida (atribuir trabalhadores a empregos)
- Segmentação de imagens (separar o primeiro plano do fundo)
- Eliminação do beisebol (o time X ainda pode vencer?)
- Confiabilidade da rede (taxa máxima de transferência de dados)
### Correspondência bipartida via Max Flow
Dado um gráfico bipartido G = (L ∪ R, E):
1. Adicione fontes com arestas a todos os vértices em L (capacidade 1)
2. Adicione o coletor t com arestas de todos os vértices em R (capacidade 1)
3. Defina todas as capacidades de borda originais para 1
4. Fluxo máximo = correspondência máxima
---

## Teoria dos Grafos Espectrais
A teoria dos grafos espectrais estuda gráficos por meio dos autovalores e autovetores de matrizes associadas ao gráfico.
### Matrizes Chave
| Matriz | Definição | O que captura |
|--------|------------|------------------|
| **Matriz de adjacência** A | A[i][j] = 1 se a aresta (i,j) existir | Padrão de conectividade |
| **Matriz de graus** D | Diagonal; D[i][i] = grau(i) | Importância do vértice por grau |
| **Laplaciano** L = D − A | L[i][j] = −1 se aresta, deg(i) na diagonal | Suavidade de funções no gráfico |
| **Laplaciano normalizado** L_norm = D^(−1/2) L D^(−1/2) | Versão invariante à escala | Estrutura comunitária |
### Autovalores do Laplaciano
O Laplaciano L é positivo semidefinido, então todos os autovalores são ≥ 0.
| Autovalor | Significado |
|------------|---------|
| λ₁ = 0 | Sempre zero; autovetor é o vetor constante |
| λ₂ (conectividade algébrica) | > 0 se o gráfico estiver conectado; maior = melhor conectado |
| Número de autovalores zero | É igual ao número de componentes conectados |
| λₙ | Relacionado ao grau máximo e expansão do gráfico |
### Aplicações de Métodos Espectrais
| Aplicação | Método |
|------------|--------|
| **Particionamento de gráfico** | Use autovetores de L para dividir o gráfico em partes balanceadas |
| **Detecção de comunidade** | Clustering espectral: incorpore vértices usando autovetores inferiores e, em seguida, agrupe |
| **PáginaRank** | Autovetor da matriz de adjacência (ou matriz de transição) do grafo web |
| **Desenho gráfico** | Posicione vértices usando autovetores do Laplaciano |
| **Aprendizagem semissupervisionada** | Propague rótulos usando o gráfico Laplaciano (propagação de rótulos) |
| **Redes neurais gráficas** | Convoluções espectrais: filtrar sinais em gráficos usando autovetores de L |
### Desigualdade de Cheeger
Relaciona o segundo autovalor λ₂ à **expansão** do gráfico (quão bem conectado ele está):
λ₂ / 2 ≤ h(G) ≤ √(2λ₂)
onde h(G) é a constante de Cheeger (número isoperimétrico). Isso significa que λ₂ mede aproximadamente o quão difícil é cortar o gráfico em duas partes – um insight importante para agrupamento.
---

## Estruturas gráficas especiais
| Gráfico | Vértices | Bordas | Propriedades |
|-------|----------|-------|------------|
| Conclua Kₙ | n | n(n−1)/2 | Cada par conectado; diâmetro 1 |
| Ciclo Cₙ | n | n | 2-regular; conectado |
| Caminho Pₙ | n | n−1 | Árvore; diâmetro n−1 |
| Hipercubo Qₖ | 2ᵏ | k·2ᵏ⁻¹ | k-regular; diâmetro k; bipartido |
| Bipartido completo K_{m,n} | m+n | m·n | Cada vértice em uma parte se conecta a todos os outros |
| Gráfico de Petersen | 10 | 15 | 3-regular; diâmetro 2; não plano; sem ciclo hamiltoniano |
---

## Relevância para aprendizado de máquina e ciência de dados
| Conceito de gráfico | Aplicação |
|---------------|------------|
| BFS/DFS | Rastreamento da Web, análise de redes sociais, rotulagem de componentes conectados |
| Dijkstra / A* | Planejamento de rotas, descoberta de caminhos de IA de jogos, navegação robótica |
| Árvore geradora mínima | Clustering (ligação única), seleção de recursos, projeto de rede |
| Fluxo máximo/corte mínimo | Segmentação de imagens, correspondência bipartida, atribuição de recomendação |
| Métodos espectrais | Agrupamento espectral, redes neurais de grafos, redução de dimensionalidade (automapas laplacianos) |
| Classificação de página | Ranking em buscadores, análise de influência nas redes sociais |
| DAG | Redes bayesianas, inferência causal, agendamento de tarefas, gráficos computacionais em aprendizagem profunda |
| Gráficos bipartidos | Matrizes de itens de usuário em sistemas de recomendação, mercados bilaterais |
| Estruturas de árvores | Árvores de decisão, florestas aleatórias, agrupamento hierárquico, navegação em sistemas de arquivos |
| Representações gráficas | Gráficos de conhecimento (Wikidata, DBpedia), gráficos moleculares (descoberta de medicamentos), redes de citação |
---

## Resumo
| Tópico | Ideia Central | Algoritmo Chave/Resultado |
|-------|-----------|-----------|
| Fundamentos | Vértices, arestas, graus, caminhos | Lema do aperto de mão |
| Representações | Como armazenar gráficos | Matriz de adjacência vs lista de adjacência |
| Árvores | Gráficos acíclicos conectados | n vértices → n−1 arestas |
| Travessias | Exploração sistemática de vértices | BFS (caminho mais curto), DFS (exploração profunda) |
| Caminhos mais curtos | Rotas de peso mínimo | Dijkstra, Bellman-Ford, Floyd-Warshall |
| Árvore de abrangência mínima | Maneira mais barata de conectar todos os vértices | Kruskal, Prim |
| Fluxo de rede | Rendimento máximo | Ford-Fulkerson, teorema do corte mínimo do fluxo máximo |
| Teoria Espectral | Autovalores revelam estrutura | Autovalores Laplacianos, agrupamento espectral |
A teoria dos grafos é indiscutivelmente o ramo da matemática mais diretamente aplicável à moderna ciência de dados. Redes sociais, gráficos de conhecimento, estruturas moleculares, gráficos de computação em estruturas de aprendizagem profunda, resolução de dependências, sistemas de recomendação – todos são fundamentalmente problemas gráficos. Os algoritmos abordados aqui não são apenas teóricos; eles são executados em escala em sistemas de produção todos os dias.