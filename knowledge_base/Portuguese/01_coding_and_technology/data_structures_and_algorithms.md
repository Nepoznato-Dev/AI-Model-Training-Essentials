---
# Metadata
title: "Data Structures and Algorithms"
description: "Arrays, trees, graphs, sorting, searching, complexity"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, structures, algorithms, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Estruturas de dados e algoritmos
Estruturas de dados são as formas como organizamos os dados na memória para que as operações neles sejam eficientes. Algoritmos são procedimentos passo a passo para resolver problemas. Juntos, eles formam a base da ciência da computação – todos os programas que você já usou dependem deles. Escolher a estrutura de dados correta pode transformar um programa incrivelmente lento em um programa rápido, e conhecer o algoritmo certo pode transformar um problema insolúvel em um problema trivial.
---

## Estruturas de dados fundamentais
### Estruturas Lineares
| Estrutura | Acesso | Pesquisar | Inserir | Excluir | Caso de uso |
|-----------|--------|--------|--------|--------|----------|
| **Matriz** | O(1) por índice | Sobre(n) | Sobre(n) | Sobre(n) | Coleções de tamanho fixo; acesso aleatório |
| **Lista vinculada** | Sobre(n) | Sobre(n) | O(1) na cabeça | O(1) na cabeça | Tamanho dinâmico; inserções/exclusões |
| **Pilha** | Sobre(n) | Sobre(n) | O(1) empurrar/estalar | O(1) pop | Chamadas de função; desfazer; análise |
| **Fila** | Sobre(n) | Sobre(n) | O(1) enfileiramento | O(1) desenfileirar | Agendamento de tarefas; BFS; filas de mensagens |
| **Deque** | O(1) em ambas as extremidades | Sobre(n) | O(1) em ambas as extremidades | O(1) em ambas as extremidades | Janela deslizante; roubo de trabalho |
### Estruturas baseadas em hash
| Estrutura | Pesquisar | Inserir | Excluir | Caso de uso |
|-----------|--------|--------|--------|----------|
| **Tabela hash** | O(1) média | O(1) média | O(1) média | Pesquisas de valores-chave; esconderijos; conjuntos |
| **Conjunto de hash** | O(1) | O(1) | O(1) | Teste de adesão; desduplicação |
**Colisões de hash**: quando duas chaves fazem hash no mesmo slot, elas são armazenadas em uma lista vinculada (encadeamento) ou no próximo slot disponível (endereçamento aberto). Boas funções hash minimizam colisões.
### Estruturas de árvore
| Estrutura | Pesquisar | Inserir | Excluir | Caso de uso |
|-----------|--------|--------|--------|----------|
| **Árvore de pesquisa binária** | O(log n) média | O(logn) | O(logn) | Dados classificados; consultas de intervalo |
| **AVL / Árvore Vermelho-Preta** | O(log n) garantido | O(logn) | O(logn) | Autoequilíbrio; usado em mapas/conjuntos |
| **Árvore B / Árvore B+** | O(logn) | O(logn) | O(logn) | Índices de banco de dados; sistemas de arquivos |
| **Tentar** | O(k) onde k = comprimento da chave | OK (ok) | OK (ok) | Preenchimento automático; correspondência de prefixo |
| **Pilha (binário)** | Sobre(n) | O(logn) | O(logn) | Filas prioritárias; agendamento |
### Representações gráficas
| Representação | Espaço | Pesquisa de borda | Adicionar borda | Iterar vizinhos |
|---------------|-------|------------|----------|--------|
| **Matriz de adjacência** | O(V²) | O(1) | O(1) | O(V) |
| **Lista de adjacências** | O(V + E) | O(grau) | O(1) | O(grau) |
| **Lista de bordas** | O(E) | O(E) | O(1) | O(E) |
---

## Complexidade do algoritmo (Big-O)
A notação Big-O descreve como os requisitos de tempo ou espaço de um algoritmo aumentam à medida que o tamanho da entrada aumenta.
| Complexidade | Nome | Exemplo |
|-----------|------|--------|
| **O(1)** | Constante | Pesquisa de tabela hash; acesso ao array por índice |
| **O(logn)** | Logarítmico | Pesquisa binária; operações de árvores balanceadas |
| **O(n)** | Linear | Pesquisa linear; iterando uma matriz |
| **O(n log n)** | Linearítmico | Mesclar classificação; classificação de pilha; classificações de uso geral mais eficientes |
| **O(n²)** | Quadrático | Classificação por bolha; loops aninhados sobre os mesmos dados |
| **O(2^n)** | Exponencial | Geração de subconjuntos de força bruta; Fibonacci recursivo ingênuo |
| **O(n!)** | Fatorial | Caixeiro viajante (força bruta); permutações |
### Equívocos Comuns
| Equívoco | Realidade |
|-------------|---------|
| "O(n) é sempre mais rápido que O(n²)" | Para n pequeno, o fator constante é mais importante |
| "Lower Big-O é sempre melhor" | Existem compensações espaço-temporais; A pesquisa O(1) usa memória O(n) |
| "Big-O informa a velocidade exata" | Descreve a taxa de crescimento, não o tempo absoluto |
---

## Algoritmos de classificação
| Algoritmo | Melhor | Média | Pior | Espaço | Estável | No local |
|-----------|------|--------|-------|-------|--------|----------|
| **Classificação por bolha** | Sobre(n) | O(n²) | O(n²) | O(1) | Sim | Sim |
| **Classificação por inserção** | Sobre(n) | O(n²) | O(n²) | O(1) | Sim | Sim |
| **Classificação por seleção** | O(n²) | O(n²) | O(n²) | O(1) | Não | Sim |
| **Mesclar classificação** | O(n log n) | O(n log n) | O(n log n) | Sobre(n) | Sim | Não |
| **Classificação rápida** | O(n log n) | O(n log n) | O(n²) | O(logn) | Não | Sim |
| **Classificação de pilha** | O(n log n) | O(n log n) | O(n log n) | O(1) | Não | Sim |
| **Tim Sort** | Sobre(n) | O(n log n) | O(n log n) | Sobre(n) | Sim | Não |
**Conselhos práticos**: use a classificação integrada da sua linguagem (`sorted()` do Python,`Array.sort()`do JavaScript). Eles usam algoritmos altamente otimizados (Tim Sort, Introsort) que lidam com todos os casos extremos.
---

## Pesquisando Algoritmos
| Algoritmo | Estrutura de dados | Complexidade | Requisito |
|-----------|---------------|-----------|------------|
| **Pesquisa linear** | Qualquer | Sobre(n) | Nenhum |
| **Pesquisa binária** | Matriz ordenada | O(logn) | Os dados devem ser classificados |
| **Pesquisa de tabela hash** | Tabela hash | O(1) média | Boa função hash |
| **BFS** (Pesquisa em amplitude) | Gráfico/árvore | O(V + E) | Caminho mais curto não ponderado |
| **DFS** (pesquisa em profundidade) | Gráfico/árvore | O(V + E) | Localização de caminhos; detecção de ciclo |
| **Dijkstra** | Gráfico ponderado | O((V + E)log V) | Pesos não negativos; caminho mais curto |
| **Uma* Pesquisa** | Gráfico ponderado | O((V + E)log V) | Guiado por heurística; ótimo com heurística admissível |
---

## Principais padrões de algoritmo
| Padrão | Descrição | Exemplos de problemas |
|--------|-------------|-----------------|
| **Dividir e conquistar** | Dividir o problema em subproblemas; resolver recursivamente; combinar | Mesclar classificação; classificação rápida; pesquisa binária |
| **Programação dinâmica** | Divida em subproblemas sobrepostos; resultados de cache | Fibonacci; mochila; subsequência comum mais longa |
| **Ganancioso** | Faça a escolha localmente ideal em cada etapa | Dijkstra; Codificação de Huffman; seleção de atividades |
| **Retrocesso** | Experimente possibilidades; desfazer escolhas erradas; tente alternativas | Solucionador de Sudoku; N-rainhas; permutações |
| **Janela deslizante** | Manter uma janela de elementos; deslize-o pelos dados | Submatriz de soma máxima de tamanho K; substring mais longa sem repetições |
| **Duas dicas** | Use dois ponteiros movendo-se um em direção ao outro ou na mesma direção | Soma do par em array classificado; remover duplicatas |
| **Pesquisa binária na resposta** | Pesquisa binária no espaço de resposta | Alocar páginas mínimas; vacas agressivas |
---

## Quando usar o quê
| Problema | Estrutura de dados | Algoritmo |
|---------|---------------|-----------|
| Pesquisa rápida de valor-chave | Tabela hash/dicionário | Hashing |
| Manter a ordem ordenada | BST balanceado (TreeMap, std::set) | Operações de árvores |
| Processamento baseado em prioridades | Fila de heap/prioridade | Operações de pilha |
| Caminho mais curto (sem ponderação) | Gráfico (lista de adjacências) | BFS |
| Caminho mais curto (ponderado) | Gráfico (lista de adjacências) | Dijkstra's / A* |
| Teste de adesão | Conjunto de hash/filtro Bloom | Hashing |
| Correspondência de prefixo | Experimente | Tente percorrer |
| Consultas de intervalo | Árvore de segmento / árvore Fenwick | Operações de árvores |
| Cache LRU | Mapa hash + lista duplamente vinculada | Operações combinadas |
| Componentes conectados | União de conjunto disjunto (Union-Find) | União e Encontrar |
---

## Resumo
Estruturas de dados e algoritmos não são apenas tópicos de entrevista – eles são os blocos de construção de um software eficiente. Matrizes e tabelas hash atendem à maioria das necessidades diárias. Árvores e gráficos lidam com dados hierárquicos e relacionais. Classificar e pesquisar são problemas resolvidos em bibliotecas padrão. Os padrões algorítmicos – dividir e conquistar, programação dinâmica, ganancioso, retrocesso – são estratégias reutilizáveis ​​para lidar com novos problemas. A habilidade principal não é memorizar algoritmos; é reconhecer qual padrão se adapta a um determinado problema e escolher a estrutura de dados correta para o trabalho.