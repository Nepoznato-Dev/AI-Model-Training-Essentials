---
# Metadata
title: "Graph Neural Networks"
description: "GCNs, GATs, message passing, knowledge graphs, graph tasks"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [graph, neural, networks, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Redes Neurais de Gráfico
Redes Neurais de Grafos (GNNs) são redes neurais projetadas para operar em dados estruturados em grafos - redes de nós conectados por arestas. Enquanto as redes neurais tradicionais funcionam em grades (imagens) ou sequências (texto), as GNNs lidam com estruturas relacionais arbitrárias: redes sociais, gráficos moleculares, gráficos de conhecimento, redes rodoviárias, gráficos de recomendação e muito mais. Eles se tornaram essenciais para descoberta de medicamentos, detecção de fraudes, sistemas de recomendação e qualquer domínio onde o relacionamento entre entidades seja importante.
---

## O que é um gráfico?
| Componente | Descrição | Exemplo |
|-----------|-------------|---------|
| **Nó (vértice)** | Uma entidade | Uma pessoa, um átomo de uma molécula, uma cidade |
| **Borda** | Uma relação entre dois nós | Amizade, ligação química, estrada |
| **Peso da borda** | Força ou tipo de relacionamento | Distância, semelhança, capacidade |
| **Recursos do nó** | Atributos de cada nó | Idade, número atômico, população |
| **Recursos de borda** | Atributos de cada aresta | Tipo de relacionamento, distância |
| **Matriz de adjacência** | Matriz A onde A[i][j] = 1 se os nós i e j estiverem conectados | Codifica a estrutura do gráfico |
### Tipos de gráficos
| Tipo | Descrição | Exemplo |
|------|-------------|---------|
| **Não direcionado** | As arestas não têm direção | Rede de amizade |
| **Dirigido** | As arestas têm direção (A→B ≠ B→A) | Seguidores no Twitter |
| **Ponderada** | As arestas têm valores numéricos | Rede rodoviária com distâncias |
| **Heterogêneo** | Vários tipos de nós e arestas | Gráfico acadêmico (artigos, autores, locais) |
| **Dinâmico** | A estrutura do gráfico muda ao longo do tempo | Rede social evoluindo ao longo do tempo |
| **Bipartido** | Dois tipos de nós; arestas apenas entre tipos | Gráfico de recomendação de item do usuário |
---

## Por que não redes neurais regulares?
| Abordagem | Por que falha |
|----------|------------|
| **Rede feed-forward** | Requer entrada de tamanho fixo; gráficos variam em tamanho e estrutura |
| **CNN** | Assume estrutura de grade; gráficos não possuem grade regular |
| **RNN/Transformador** | Assume ordem sequencial; gráficos não têm ordenação natural |
As GNNs resolvem isso operando diretamente na estrutura do grafo, processando cada nó no contexto de seus vizinhos.
---

## Arquiteturas principais da GNN
### Estrutura de passagem de mensagens
A maioria das GNNs segue o mesmo padrão: cada nó coleta informações de seus vizinhos, combina-as e atualiza sua própria representação.
| Etapa | Descrição |
|------|-------------|
| **1. Mensagem** | Cada nó envia uma mensagem aos seus vizinhos (com base nas suas características atuais) |
| **2. Agregado** | Cada nó coleta e combina mensagens de todos os vizinhos |
| **3. Atualização** | Cada nó atualiza sua própria representação usando a mensagem agregada |
| **4. Repetir** | Faça isso para K camadas → cada nó captura informações de K saltos de distância |
### Principais modelos GNN
| Modelo | Método de agregação | Inovação Chave |
|-------|-------------------|----------------|
| **GCN** (Rede Convolucional de Gráficos) | Média das características vizinhas | Simples; eficaz; motivação espectral |
| **GraphSAGE** | Amostra e agregado; pode usar média, LSTM ou pooling | Indutivo (lida com nós invisíveis); escalável |
| **GAT** (Rede de Atenção Gráfica) | Agregação de vizinhos ponderada pela atenção | Aprende quais vizinhos são mais importantes |
| **GIN** (Rede de isomorfismo de grafos) | Soma das características vizinhas | Maximamente expressivo; consegue distinguir quaisquer gráficos distinguíveis pelo teste WL |
| **MPNN** (Rede Neural de Passagem de Mensagens) | Estrutura geral de passagem de mensagens | Unifica muitas variantes GNN |
### Como funciona o GCN (passo a passo)
```
For each layer:
  1. For each node, collect features from all neighbours
  2. Multiply by a learnable weight matrix W
  3. Normalise by node degree (so high-degree nodes don't dominate)
  4. Apply non-linearity (ReLU)
  5. This becomes the node's new representation
```

Após K camadas, a representação de cada nó codifica informações de K saltos no gráfico.
---

## Tarefas em nível de gráfico
| Tarefa | Descrição | Exemplo |
|------|-------------|---------|
| **Classificação de nós** | Preveja o rótulo de cada nó | Classifique os usuários como bots ou humanos |
| **Previsão de link** | Prever se uma aresta existe (ou existirá) | Prever relacionamentos perdidos; recomendar conexões |
| **Classificação gráfica** | Prever um rótulo para todo o gráfico | Classificar as moléculas como tóxicas ou não tóxicas |
| **Detecção de comunidade** | Encontre clusters de nós densamente conectados | Identificar grupos sociais |
| **Geração de gráfico** | Gere novos gráficos com propriedades desejadas | Projetar novas moléculas |
---

## Aplicativos
### Descoberta de medicamentos e previsão de propriedades moleculares
| Tarefa | Como as GNNs ajudam |
|------|-------------|
| **Predição de propriedades moleculares** | Representar moléculas como gráficos (átomos=nós, ligações=arestas); prever toxicidade, solubilidade, afinidade de ligação |
| **Interação medicamentosa** | Modelo de medicamentos e alvos como um gráfico; prever interações adversas |
| **Projeto de medicamento de novo** | Gere novos gráficos moleculares com propriedades desejadas |
### Sistemas de recomendação
| Abordagem | Descrição |
|----------|------------|
| **Gráfico de item do usuário** | Usuários e itens são nós; compras/visualizações são bordas |
| **Filtragem colaborativa baseada em gráficos** | GNNs propagam preferências através do gráfico |
| **Recomendações do gráfico de conhecimento** | Combine as preferências do usuário com o conhecimento dos itens (gêneros, atores, diretores) |
### Detecção de fraude
| Aplicação | Estrutura do gráfico |
|------------|----------------|
| **Fraude financeira** | As transações formam um gráfico; padrões fraudulentos emergem como estruturas de subgráficos |
| **Fraude em seguros** | Requerentes, provedores e apólices formam um gráfico; redes de fraudadores são detectadas |
| **Aquisições de contas** | Os padrões de login formam um gráfico; conexões anômalas sinalizam comprometimento |
### Gráficos de conhecimento
| Tarefa | Descrição |
|------|-------------|
| **Previsão de link** | Preveja fatos faltantes (por exemplo, "Paris é a capital de?") |
| **Resolução da entidade** | Determinar se duas menções referem-se à mesma entidade |
| **Resposta a perguntas** | Navegue no gráfico para encontrar respostas |
---

## Conceitos Avançados de GNN
### Suavização excessiva
| Problema | Descrição | Solução |
|--------|-------------|----------|
| **Suavização excessiva** | Depois de muitas camadas, todas as representações dos nós tornam-se semelhantes | Profundidade limite (2-4 camadas); use conexões residuais; usar conhecimento de salto |
### Esmagamento excessivo
| Problema | Descrição | Solução |
|--------|-------------|----------|
| **Esmagamento excessivo** | Informações de nós distantes são compactadas em vetores de tamanho fixo | Use transformadores gráficos; agrupamento hierárquico |
### Transformadores Gráficos
| Modelo | Recurso principal |
|-------|------------|
| **Transformador gráfico** | Aplicar atenção padrão do Transformer a todos os pares de nós |
| **GPS** (sistema de aviso gráfico) | Combine camadas GNN locais com camadas Transformer globais |
| **Grafógrafo** | Adicionar codificação posicional com base na estrutura do gráfico |
### Redes gráficas heterogêneas
| Modelo | Descrição |
|-------|------------|
| **R-GCN** | GCN Relacional; diferentes matrizes de peso para diferentes tipos de arestas |
| **HAN** | Rede Heterogênea de Atenção; atenção sobre diferentes tipos de nós e arestas |
| **HetGNN** | Rede Neural de Grafo Heterogêneo; lida com vários tipos de nós |
---

## Escalabilidade
| Desafio | Solução |
|-----------|----------|
| **Gráficos grandes** (milhões de nós) | Treinamento em minilote; amostragem de vizinhos |
| **Memória** | Particionamento de gráficos entre GPUs |
| **Velocidade** | Operações de matrizes esparsas; bibliotecas especializadas |
### Estratégias de Amostragem
| Estratégia | Descrição |
|----------|------------|
| **Amostragem de nós** | Amostra de um subconjunto de nós e suas vizinhanças K-hop |
| **Amostragem de bordas** | Amostras de arestas e os nós que elas conectam |
| **Amostragem por conglomerados** | Particione o gráfico em clusters; treinar em clusters |
| **Amostragem de passeio aleatório** | Amostra de nós por meio de passeios aleatórios a partir de nós de destino |
---

## Ferramentas e Estruturas
| Ferramenta | Finalidade |
|------|---------|
| **PyTorch Geométrico (PyG)** | Biblioteca GNN mais popular; rico conjunto de modelos e conjuntos de dados |
| **DGL** (Biblioteca de gráficos profundos) | Agnóstico em termos de estrutura; suporta PyTorch, TensorFlow, MXNet |
| **RedeX** | Algoritmos gráficos clássicos; manipulação de dados |
| **OGB** (referência de gráfico aberto) | Benchmarks e conjuntos de dados padrão para pesquisa da GNN |
| **CogDL** | Aprendizado profundo para gráficos; orientado para a investigação |
| **Espectral** | Biblioteca GNN para TensorFlow/Keras |
---

## Resumo
As redes neurais de grafos estendem o aprendizado profundo a dados relacionais - redes, moléculas, gráficos de conhecimento e qualquer sistema onde entidades estejam conectadas. Eles funcionam passando mensagens entre vizinhos, permitindo que cada nó aprenda com seu contexto local. As GNNs encontraram suas aplicações mais fortes na descoberta de medicamentos, sistemas de recomendação, detecção de fraudes e gráficos de conhecimento. O campo está evoluindo em direção a transformadores gráficos, gráficos heterogêneos e treinamento escalável para redes massivas do mundo real. Se seus dados tiverem relacionamentos, provavelmente vale a pena considerar os GNNs.