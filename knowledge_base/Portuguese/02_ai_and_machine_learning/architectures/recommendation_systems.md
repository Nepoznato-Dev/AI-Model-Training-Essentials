<!--
---
# Metadata
title: "Recommendation Systems"
description: "Collaborative filtering, content-based, hybrid, matrix factorisation"
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
tags: [recommendation, systems, ai-and-machine-learning]
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

-->
# Sistemas de recomendação
Os sistemas de recomendação prevêem o que um usuário desejará ver, comprar ou interagir em seguida. Eles alimentam os feeds de conteúdo nas redes sociais, sugestões de produtos em sites de comércio eletrônico, escolhas de filmes em plataformas de streaming e resultados de pesquisa. Apesar de serem invisíveis para a maioria dos usuários, eles estão entre os sistemas de IA com maior impacto comercial no mundo – a Netflix estima que seu mecanismo de recomendação economize mais de US$ 1 bilhão por ano ao reduzir a rotatividade de assinantes.
---

## Por que as recomendações são difíceis
| Desafio | Descrição |
|-----------|------------|
| **Escala** | Milhões de usuários × milhões de itens = bilhões de pares possíveis |
| **Disparidade** | Cada usuário interagiu com uma pequena fração dos itens disponíveis |
| **Início a frio** | Novos usuários e novos itens não possuem histórico de interação |
| **Preferências dinâmicas** | Os gostos dos usuários mudam com o tempo |
| **Além da precisão** | As recomendações também devem ser diversas, novas e fortuitas |
| **Metas de negócios** | Maximizando o envolvimento ≠ maximizando o bem-estar do usuário |
---

## Abordagens Básicas
### Filtragem Colaborativa
A ideia: se os usuários A e B concordaram no passado, provavelmente concordarão no futuro.
| Tipo | Como funciona | Exemplo |
|------|-------------|---------|
| **Baseado no usuário** | Encontre usuários semelhantes; recomende o que gostou | "Usuários que gostaram também gostaram..." |
| **Com base em item** | Encontre itens semelhantes ao que o usuário já gosta | "Porque você assistiu..." |
| **Fatoração de matrizes** | Decompor a matriz de interação usuário-item em fatores latentes | SVD, ALS (mínimos quadrados alternados) |
| Força | Fraqueza |
|----------|----------|
| Não há necessidade de entender os itens em si | Problema de inicialização a frio: não é possível recomendar novos itens |
| Captura preferências implícitas e complexas | Requer muitos dados de interação |
| Funciona em qualquer tipo de conteúdo | Viés de popularidade: recomenda itens já populares |
### Filtragem Baseada em Conteúdo
Recomende itens semelhantes aos que o usuário já gosta, com base nas características do item.
| Tipo de recurso | Exemplo |
|------------|---------|
| **Texto** | Gênero, descrição, palavras-chave, elenco |
| **Áudio** | Tempo, gênero, clima (para música) |
| **Visuais** | Paleta de cores, estilo (para imagens/moda) |
| **Metadados** | Preço, marca, categoria |
| Força | Fraqueza |
|----------|----------|
| Não há inicialização a frio para itens (recursos são conhecidos) | Não é possível recomendar itens fora do gosto do usuário |
| Funciona com menos dados de interação | Requer boa engenharia de recursos |
| Explicável ("recomendado porque é semelhante ao X") | Menos acaso |
### Abordagens Híbridas
A maioria dos sistemas de produção combina métodos colaborativos e baseados em conteúdo.
| Estratégia Híbrida | Descrição |
|----------------|------------|
| **Ponderada** | Combine pontuações de vários modelos |
| **Trocando** | Uso baseado em conteúdo para novos usuários, colaborativo para os já estabelecidos |
| **Cascata** | Use primeiro um modelo simples e depois refine com um modelo complexo |
| **Combinação de recursos** | Mesclar recursos colaborativos e de conteúdo em um único modelo |
| **Meta-aprendizagem** | Aprenda como combinar diferentes recomendadores |
---

## Abordagens modernas de aprendizagem profunda
### Modelos de duas torres
A arquitetura dominante para recomendação em larga escala (usada pelo YouTube, Pinterest, Spotify).
| Componente | Função |
|-----------|------|
| **Torre do usuário** | Rede neural que codifica recursos e histórico do usuário em uma incorporação |
| **Torre de itens** | Rede neural que codifica recursos de itens em uma incorporação |
| **Similaridade** | Semelhança de produto escalar ou cosseno entre embeddings de usuário e item |
| Etapa | Descrição |
|------|-------------|
| 1 | Treinar ambas as torres para produzir embeddings semelhantes para pares de itens de usuário que interagem |
| 2 | Na hora de servir, pré-calcule os embeddings dos itens |
| 3 | Para uma solicitação de usuário, calcule a incorporação do usuário |
| 4 | Use a pesquisa do vizinho mais próximo aproximado (ANN) para encontrar os itens mais semelhantes |
### Modelos de sequência para recomendações
O comportamento do usuário é sequencial – o que você assistiu ontem influencia o que você assistirá hoje.
| Modelo | Abordagem |
|-------|----------|
| **GRU4Rec** | Modelo baseado em GRU para recomendações baseadas em sessão |
| **SASRec** | Recomendador sequencial baseado em autoatenção |
| **BERT4Rec** | Transformador Bidirecional para recomendações sequenciais |
| **DNN do YouTube** | Rede neural profunda tratando o histórico de exibição como uma sequência |
### Recuperação vs Classificação
Os sistemas modernos dividem as recomendações em duas etapas:
| Palco | Finalidade | Método |
|-------|---------|--------|
| **Recuperação (geração de candidatos)** | Limitar milhões de itens a aproximadamente 1.000 candidatos | Modelo de duas torres; Pesquisa de RNA; rápido, mas aproximado |
| **Classificação (pontuação)** | Pontue e ordene com precisão os candidatos | Modelo profundo com muitos recursos; mais lento, mas preciso |
| **Reclassificação** | Ajuste para diversidade, regras de negócios, atualização | Bandidos contextuais; otimização de restrições |
---

## Métricas de avaliação
| Métrica | O que mede | Quando usar |
|--------|-----------------|-------------|
| **Precisão@K** | Fração das principais recomendações K que são relevantes | Quando você se preocupa com a precisão das principais escolhas |
| **Recordar@K** | Fração de itens relevantes encontrados no top-K | Quando você se preocupa em não perder itens bons |
| **NDCG** (ganho cumulativo com desconto normalizado) | Qualidade de classificação; recompensas colocando itens relevantes em níveis mais elevados | Quando a ordem de classificação é importante |
| **MAP** (Precisão Média Média) | Precisão média entre todos os usuários | Qualidade geral da classificação |
| **Taxa de acerto@K** | Se pelo menos um item relevante aparece no top-K | Cenários de relevância binária |
| **Cobertura** | Fração de itens recomendados | Diversidade e justiça |
| **Serendipidade** | Recomendações inesperadas mas relevantes | Satisfação do usuário |
---

## O problema da partida a frio
| Cenário | Desafio | Soluções |
|----------|-----------|-----------|
| **Novo usuário** | Sem histórico de interação | Use dados demográficos; mostrar itens populares; usar sinais contextuais (localização, dispositivo, hora) |
| **Novo item** | Ninguém interagiu com isso ainda | Use recursos de conteúdo; estratégias explorar-explorar; algoritmos de bandidos |
| **Novo sistema** | Nenhum dado | Transferir aprendizagem de domínios semelhantes; curadoria de conteúdo inicial |
---

## Exploração vs Exploração
| Estratégia | Descrição | Compensação |
|----------|-------------|-----------|
| **ε-ganancioso** | Mostrar itens aleatórios com probabilidade ε | Simples, mas ineficiente |
| **Amostragem Thompson** | Amostra da distribuição posterior da qualidade dos itens | Princípio; boas propriedades teóricas |
| **Limite superior de confiança (UCB)** | Prefira itens com alta incerteza | Bom equilíbrio entre exploração e aproveitamento |
| **Bandidos contextuais** | Exploração condicionada ao contexto do usuário | Mais eficiente que a exploração cega |
| **Injeção de diversidade** | Incluir deliberadamente itens diversos ou novos | Simples; pode reduzir o envolvimento a curto prazo |
---

## Preconceito e justiça
| Tipo de polarização | Descrição | Impacto |
|-----------|-------------|--------|
| **Viés de popularidade** | Itens populares são mais recomendados, tornando-se mais populares | Itens de cauda longa são mal atendidos |
| **Viés de seleção** | Os modelos aprendem com as interações observadas, nem todas as possíveis | Orientado para usuários ativos |
| **Viés de posição** | Itens mostrados em posições mais altas recebem mais cliques independentemente da qualidade | Reforça posições de topo |
| **Viés de exposição** | Itens mostrados recebem mais sinal de treinamento | Ciclo de feedback |
| **Viés demográfico** | As recomendações diferem entre os grupos demográficos de forma injusta | Discriminação; experiência ruim para alguns grupos |
### Estratégias de Mitigação
| Estratégia | Descrição |
|----------|------------|
| **Ponderação de propensão inversa** | Itens populares para baixo peso no treinamento |
| **Remoção de camadas** | Adicionar um componente de redução de polarização ao modelo |
| **Restrições de justiça** | Adicionar restrições para garantir um tratamento equitativo |
| **Recomendações diversas** | Otimize explicitamente a diversidade junto com a relevância |
| **Auditoria e monitoramento** | Verifique regularmente as recomendações quanto a preconceitos entre grupos |
---

## Exemplos da indústria
| Empresa | Sistema | Abordagem |
|--------|--------|----------|
| **Netflix** | Recomendações de filmes/TV | Recuperação de duas torres + classificação profunda + bandidos contextuais para obras de arte |
| **YouTube** | Recomendações de vídeo | Rede neural profunda para geração de candidatos; modelo de classificação separado |
| **Spotify** | Recomendações musicais | Filtragem colaborativa + PNL em playlists + análise de áudio |
| **Amazônia** | Recomendações de produtos | Filtragem colaborativa item a item; personalizado em escala |
| **TikTok** | Feed de vídeo curto | Aprendizagem por reforço; forte ênfase na exploração |
| **Pinterest** | Recomendações visuais | Modelo de duas torres; semelhança visual |
---

## Ferramentas e Estruturas
| Ferramenta | Finalidade |
|------|---------|
| **Recomendadores do TensorFlow (TFRS)** | Modelos de duas torres, recuperação, classificação |
| **RecSys PyTorch** | Modelos de recomendação orientados para a investigação |
| **Surpresa** | Filtragem colaborativa clássica (SVD, NMF, KNN) |
| **Implícito** | Filtragem colaborativa rápida para feedback implícito (ALS, BPR) |
| **Faiss** (Meta) | Pesquisa aproximada do vizinho mais próximo em escala |
| **Milvus / Pinha / Weaviate** | Bancos de dados vetoriais para pesquisa de similaridade |
| **Recorde** | Biblioteca abrangente de pesquisa de recomendações |
| **Merlin** (NVIDIA) | Pipeline de recomendação acelerado por GPU |
---

## Resumo
Os sistemas de recomendação estão entre as aplicações de IA de maior impacto na indústria. O campo evoluiu de uma simples filtragem colaborativa para arquiteturas de aprendizagem profunda que combinam histórico do usuário, conteúdo de itens, sinais contextuais e objetivos de negócios. Os sistemas modernos usam um pipeline de recuperação, classificação e reclassificação, com modelos de duas torres para geração rápida de candidatos e modelos profundos para pontuação precisa. Os desafios – partida a frio, preconceito, exploração e equilíbrio entre a satisfação do usuário e as metas de negócios – continuam sendo áreas ativas de pesquisa e engenharia.