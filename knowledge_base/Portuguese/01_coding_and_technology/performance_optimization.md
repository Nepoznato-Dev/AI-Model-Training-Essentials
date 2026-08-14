---
# Metadata
title: "Performance Optimisation"
description: "Profiling, caching, CDN, query optimisation, front-end perf"
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
tags: [performance, optimization, coding-and-technology]
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
# Otimização de desempenho
A otimização de desempenho é a prática de tornar o software mais rápido — reduzindo os tempos de resposta, aumentando o rendimento, diminuindo o uso de memória e eliminando gargalos. É uma das habilidades mais impactantes que um desenvolvedor pode ter, porque software lento perde usuários, desperdiça recursos e frustra a todos. Mas também é um dos erros mais comuns, com os desenvolvedores otimizando as coisas erradas com base na intuição e não em evidências.
---

## A Regra de Ouro
> **Meça primeiro, otimize depois.** Nunca otimize com base em suposições. Crie um perfil do código, encontre o gargalo real e corrija-o.
| Antipadrão | Por que é ruim |
|------------|------------|
| **Otimização prematura** | Gastar tempo acelerando código que não é lento |
| **Otimização sem medição** | Corrigindo o gargalo errado; não há como verificar a melhoria |
| **Sacrificando a legibilidade pela velocidade** | Código ilegível custa mais que ganho de desempenho |
| **Armazenando tudo em cache** | Dados obsoletos, excesso de memória, complexidade |
---

## Perfil
Antes de fazer algo mais rápido, você precisa saber *onde* o tempo está sendo gasto.
| Tipo de ferramenta | O que mede | Exemplos |
|-----------|-----------------|----------|
| **Criador de perfil de CPU** | Quais funções consomem mais tempo de CPU | cProfile (Python), perf (Linux), Chrome DevTools (JS) |
| **Perfilador de memória** | Alocação de memória e vazamentos | tracemalloc (Python), Valgrind, heaptrack |
| **Criador de perfil de E/S** | Gargalos de E/S de disco e rede | iotop, strace, Wireshark |
| **APM (Monitoramento de desempenho de aplicativos)** | Tempo de solicitação ponta a ponta | Nova Relíquia, Datadog, Jaeger |
| **DevTools do navegador** | Renderização de frontend, execução de JavaScript, rede | Chrome DevTools, perfil do Firefox |
### Fluxo de trabalho de criação de perfil
| Etapa | Descrição |
|------|-------------|
| 1. Identifique a operação lenta | Os usuários relatam carregamento lento da página; monitoramento mostra alta latência |
| 2. Crie um perfil do caminho completo | Descubra qual componente leva mais tempo |
| 3. Detalhamento | Crie o perfil desse componente específico para encontrar a função quente |
| 4. Corrija o gargalo | Aplique a otimização apropriada |
| 5. Meça novamente | Verifique a melhoria; verifique se há regressões |
---

## Otimização Algorítmica
Os maiores ganhos de desempenho vêm da escolha de algoritmos melhores, não de microotimizações.
| Alterar | Melhoria |
|--------|------------|
| Pesquisa linear O(n) → Pesquisa de tabela hash O(1) | 100x+ para grandes conjuntos de dados |
| Loop aninhado O(n²) → Classificar + pesquisa binária O(n log n) | Ordens de grandeza para n grandes |
| Cálculo repetido → Memoização / cache | Elimina trabalho redundante |
| Concatenação de strings em loop → Builder / join | Evita cópia quadrática de strings |
| Dados não classificados → Dados classificados com pesquisa binária | O(log n) em vez de O(n) por pesquisa |
---

## Estratégias de cache
O cache armazena resultados computados para que não precisem ser recalculados.
| Tipo de cache | Localização | Velocidade | Vitalício |
|----------|----------|-------|----------|
| **Cache da CPU** | L1/L2/L3 | ~1 ns | Automático |
| **Na memória** | RAM do aplicativo (dict, HashMap) | ~100ns | Até ser liberado ou despejado |
| **Cache distribuído** | Redis, Memcached | ~1ms | TTL configurável |
| **CDN** | Servidores de borda em todo o mundo | ~10-50ms | TTL configurável |
| **Cache do navegador** | Navegador do usuário | ~1ms | Cabeçalhos de cache HTTP |
| **Cache de consulta de banco de dados** | Nível de banco de dados ou ORM | ~1-10ms | Até que os dados sejam alterados |
### Padrões de cache
| Padrão | Descrição | Quando usar |
|---------|-------------|-------------|
| **Cache à parte** | O aplicativo verifica o cache; cargas do banco de dados em caso de falha; armazena em cache | Mais comum; simples |
| **Escrever** | Grave no cache e no banco de dados simultaneamente | Quando lê >> escreve; consistência importante |
| **Escrever atrás** | Escreva no cache; gravar de forma assíncrona no banco de dados | Alto rendimento de gravação; algum risco de perda de dados |
| **TTL (Hora de Viver)** | As entradas de cache expiram após um tempo definido | Quando os dados mudam periodicamente |
| **Invalidação** | Remover explicitamente entradas de cache obsoletas | Quando você sabe exatamente quando os dados mudam |
### Invalidação de cache
Os dois problemas mais difíceis da ciência da computação: invalidação de cache, nomenclatura de coisas e erros isolados.
| Estratégia | Descrição |
|----------|------------|
| **Baseado em TTL** | As entradas expiram após N segundos; simples, mas pode servir dados obsoletos |
| **Orientado por eventos** | Invalidar quando os dados forem alterados; mais complexo, mas preciso |
| **Baseado em versão** | Inclua um número de versão; incremento nas mudanças |
| **Com base em tags** | Entradas de cache relacionadas a tags; invalidar todas as entradas com uma tag |
---

## Otimização de banco de dados
Os bancos de dados costumam ser o maior gargalo em aplicações web.
| Técnica | Descrição | Impacto |
|-----------|-------------|--------|
| **Indexação** | Adicione índices nas colunas usadas em WHERE, JOIN, ORDER BY | Consultas 10-1000x mais rápidas |
| **Otimização de consulta** | Evite SELECT *; use EXPLAIN para analisar consultas | Reduza E/S |
| **Pooling de conexões** | Reutilizar conexões de banco de dados em vez de criar novas | Elimine sobrecarga de conexão |
| **Ler réplicas** | Rotear consultas de leitura para bancos de dados de réplica | Distribuir carga de leitura |
| **Particionamento** | Divida tabelas grandes em partições menores | Consultas mais rápidas em grandes conjuntos de dados |
| **Desnormalização** | Adicione dados redundantes para evitar junções | Leituras mais rápidas; gravações mais lentas |
| **Visualizações materializadas** | Resultados da consulta pré-calculados | Consultas complexas instantâneas |
| **Prevenção N+1** | Use JOINs, carregamento antecipado ou consultas em lote | Elimine milhares de consultas |
---

## Simultaneidade e Paralelismo
| Conceito | Descrição | Quando usar |
|---------|-------------|-------------|
| **Rodeamento** | Vários threads em um único processo | Tarefas vinculadas a E/S (rede, disco) |
| **Multiprocessamento** | Vários processos (ignora GIL em Python) | Tarefas vinculadas à CPU |
| **Assíncrono/aguarda** | Multitarefa cooperativa; fio único | E/S de alta simultaneidade (servidores web) |
| **Computação GPU** | Milhares de núcleos paralelos | Operações matriciais; processamento de imagens; AM |
### Assíncrono vs Threading
| Aspecto | Assíncrono/Aguarda | Rosqueamento |
|--------|------------|-----------|
| **Modelo** | Cooperativa (controle de rendimento de tarefas) | Preemptivo (sistema operacional alterna threads) |
| **Despesas gerais** | Muito baixo (sem mudança de contexto) | Superior (criação de threads, troca de contexto) |
| **Complexidade** | Raciocínio mais simples (thread único) | Condições de corrida, impasses, bloqueios |
| **Melhor para** | Muitas operações de E/S simultâneas | Bloqueio de operações que não podem ser assíncronas |
| **Limitação** | Não é possível usar código vinculado à CPU sem bloquear | GIL em Python limita o verdadeiro paralelismo |
---

## Desempenho de front-end
| Técnica | Descrição | Impacto |
|-----------|-------------|--------|
| **Minificação** | Remova os espaços em branco e reduza os nomes das variáveis ​​| Arquivos 20-40% menores |
| **Agregação** | Combine vários arquivos em menos solicitações | Menos solicitações HTTP |
| **Divisão de código** | Carregue apenas o código necessário para a página atual | Carregamento inicial mais rápido |
| **Carregamento lento** | Carregue imagens e componentes quando necessário | Renderização inicial mais rápida |
| **Árvore tremendo** | Remova o código não utilizado dos pacotes | Pacotes menores |
| **Otimização de imagem** | Usar WebP/AVIF; imagens responsivas; carregamento lento | Imagens 50-80% menores |
| **CDN** | Servir ativos estáticos de servidores de borda | Menor latência globalmente |
| **HTTP/2 e HTTP/3** | Multiplexação; compactação de cabeçalho; 0-RTT | Sobrecarga de protocolo mais rápida |
| **Trabalhadores de serviços** | Ativos de cache para uso offline; notificações push | Visitas repetidas mais rápidas |
---

## Otimização de memória
| Técnica | Descrição |
|-----------|------------|
| **Pooling de objetos** | Reutilizar objetos em vez de criar novos |
| **Transmissão** | Processar dados em pedaços em vez de carregar tudo na memória |
| **Geradores/iteradores** | Rendimento valores um de cada vez em vez de construir listas |
| **Arquivos mapeados na memória** | Acesse arquivos grandes sem carregá-los completamente |
| **Ajuste da coleta de lixo** | Ajuste os parâmetros do GC para sua carga de trabalho |
| **Escolha da estrutura de dados** | Use matrizes em vez de listas vinculadas para localidade de cache; usar conjuntos para testes de adesão |
---

## Otimização de rede
| Técnica | Descrição |
|-----------|------------|
| **Compressão** | gzip, brotli para respostas HTTP |
| **Reutilização de conexão** | Conexões que mantêm vivas; Multiplexação HTTP/2 |
| **Solicitar lote** | Combine várias chamadas de API em uma |
| **Paginação** | Carregar dados em páginas em vez de todos de uma vez |
| **Compressão em repouso** | Compactar dados em bancos de dados e caches |
| **Escolha do protocolo** | gRPC (binário, eficiente) vs REST (legível por humanos) |
---

## Monitoramento e alertas
| Métrica | O que isso lhe diz |
|--------|------------------|
| **Latência P50/P95/P99** | Tempo de resposta em vários percentis |
| **Rendimento** | Solicitações por segundo |
| **Taxa de erro** | Percentagem de pedidos falhados |
| **Utilização da CPU** | Qual a capacidade de processamento utilizada |
| **Uso de memória** | Consumo de RAM; aproximando-se dos limites? |
| **Tempo de consulta ao banco de dados** | Consultas lentas que precisam de otimização |
---

## Resumo
A otimização do desempenho é um processo sistemático: medir, identificar o gargalo, corrigi-lo, medir novamente. As maiores vitórias vêm de melhorias algorítmicas e da eliminação de trabalho desnecessário – não de micro-otimizações. Cache, indexação de banco de dados e simultaneidade são as ferramentas mais poderosas. O desempenho do front-end depende da minimização do tamanho da carga útil e das viagens de ida e volta. E a regra mais importante é sempre a mesma: não adivinhe – perfile.