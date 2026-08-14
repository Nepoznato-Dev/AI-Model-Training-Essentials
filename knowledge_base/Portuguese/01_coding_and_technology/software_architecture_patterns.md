---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
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
tags: [software, architecture, patterns, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Padrões de arquitetura de software
Arquitetura é o conjunto de decisões estruturais sobre como um sistema é organizado – quais componentes ele possui, como eles se comunicam e onde estão as responsabilidades. Uma boa arquitetura torna um sistema fácil de entender, modificar e dimensionar. A arquitetura ruim torna cada mudança uma luta. Este arquivo cobre os principais padrões, quando usar cada um e as compensações envolvidas.
---

## Monolith vs Microsserviços
Esta é a decisão arquitetônica mais fundamental e vale a pena acertar.
| Aspecto | Monólito | Microsserviços |
|--------|----------|---------------|
| **Estrutura** | Unidade única implantável | Muitos serviços pequenos e implementáveis ​​de forma independente |
| **Dados** | Banco de dados compartilhado | Cada serviço possui seus dados |
| **Comunicação** | Chamadas de função em processo | Chamadas de rede (HTTP, gRPC, mensagens) |
| **Escalonamento** | Dimensione todo o aplicativo | Dimensionar serviços individuais |
| **Implantação** | Ciclo de lançamento único | Implantações independentes |
| **Complexidade** | Mais simples de desenvolver inicialmente | Complexidade operacional (ligação em rede, monitorização) |
| **Melhor para** | Equipes pequenas, produtos em estágio inicial | Equipes grandes, domínios complexos, grande escala |
### Quando começar com um monólito
A maioria dos aplicativos deve começar como um monólito. É mais simples construir, testar, implantar e depurar. Você sempre pode extrair serviços mais tarde, quando tiver uma imagem mais clara dos limites do seu domínio. Isso às vezes é chamado de “monólito modular” – um monólito com limites internos limpos que facilitam a extração posterior.
### Quando adotar microsserviços
Considere microsserviços quando:
- As equipes são grandes o suficiente para que a coordenação se torne um gargalo.
- Diferentes partes do sistema têm requisitos de escala muito diferentes.
- Você precisa de implantação independente de componentes.
- Seu domínio tem contextos claramente delimitados (veja DDD abaixo).
---

## Arquitetura em camadas (N-Tier)
O padrão de arquitetura mais comum. O código é organizado em camadas, cada uma com uma responsabilidade específica.
```
â”Œ─────────────────────────┐
│   Presentation Layer    │  ← UI, controllers, API endpoints
├─────────────────────────┤
│   Application Layer     │  ← Use cases, orchestration
├─────────────────────────┤
│   Domain Layer          │  ← Business logic, entities
├─────────────────────────┤
│   Infrastructure Layer  │  ← Database, external services, file I/O
└─────────────────────────┘
```

| Camada | Responsabilidade | Regra |
|-------|---------------|------|
| **Apresentação** | Lidar com solicitações de usuário/HTTP | Pode chamar apenas a camada de aplicativo |
| **Inscrição** | Orquestrar casos de uso | Pode chamar a camada de domínio |
| **Domínio** | Lógica de negócios central | Não deve depender de outras camadas |
| **Infraestrutura** | Preocupações técnicas | Implementa interfaces definidas em Domínio |
**Regra principal**: as dependências apontam para dentro. A camada Domínio não conhece o banco de dados ou a estrutura da web.
---

## Arquitetura Orientada a Eventos
Os componentes se comunicam emitindo e reagindo a **eventos** — coisas que aconteceram.
| Padrão | Descrição |
|--------|-------------|
| **Notificação de evento** | O serviço A emite "OrderPlaced"; serviços B, C, D reagem |
| **Fornecimento de Eventos** | Armazene todas as alterações de estado como uma sequência de eventos (não apenas o estado atual) |
| **CQRS** | Separar modelo de leitura (consultas) do modelo de gravação (comandos) |
### Fonte de eventos
Em vez de armazenar o "estado atual" em um banco de dados, armazene cada mudança de estado como um evento:
```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Benefícios: trilha de auditoria completa, capacidade de reconstruir qualquer estado passado, consumidores dissociados. Desafios: evolução do esquema de eventos, consistência eventual, complexidade de depuração.
### CQRS (segregação de responsabilidade de consulta de comando)
| Lado | Finalidade | Banco de dados |
|------|---------|----------|
| **Comando (Escrita)** | Lidar com mutações; aplicar regras de negócios | Otimizado para gravações (normalizado) |
| **Consulta (Ler)** | Atender solicitações de leitura | Otimizado para leituras (desnormalizadas) |
O CQRS combina naturalmente com o Event Sourcing: os eventos do lado da gravação são projetados em visualizações otimizadas para leitura.
---

## Filas de mensagens e corretores de eventos
Quando os serviços precisam se comunicar de forma assíncrona, as filas de mensagens são a espinha dorsal.
| Ferramenta | Tipo | Melhor para |
|------|------|----------|
| **Apache Kafka** | Log de eventos distribuídos | Streaming de eventos de alto rendimento, fornecimento de eventos |
| **CoelhoMQ** | Corretor de mensagens com roteamento | Filas de tarefas, padrões de roteamento complexos |
| **AWS SQS** | Fila gerenciada | Enfileiramento simples e nativo da AWS |
| **AWS SNS** | Notificação de publicação/assinatura | Distribuir para vários assinantes |
| **Google Pub/Sub** | Publicação/assinatura gerenciada | Streaming de eventos nativos do GCP |
| **Transmissões Redis** | Fluxo leve | Registro de eventos simples, casos de uso de cache |
### Padrões de mensagens
| Padrão | Descrição |
|--------|-------------|
| **Ponto a Ponto** | Um produtor, um consumidor por mensagem |
| **Publicar/Assinar** | Um produtor, vários assinantes |
| **Solicitação/Responder** | Estilo síncrono sobre transporte assíncrono |
| **Fila de cartas mortas** | Mensagens que falham no processamento vão para uma fila separada para inspeção |
---

## Design Orientado a Domínio (DDD)
DDD é uma abordagem estratégica para design de software que centraliza o código em torno de conceitos de negócios, e não de preocupações técnicas.
### Conceitos-chave
| Conceito | Descrição |
|--------|-------------|
| **Contexto limitado** | Um limite dentro do qual um modelo de domínio é consistente (por exemplo, "Pedido", "Envio", "Faturamento") |
| **Linguagem onipresente** | Vocabulário compartilhado entre desenvolvedores e especialistas de domínio |
| **Agregados** | Clusters de entidades relacionadas tratadas como uma unidade única para alterações de dados |
| **Entidades** | Objetos com identidade (por exemplo, um usuário com user_id) |
| **Objetos de valor** | Objetos sem identidade; definidos pelos seus atributos (por exemplo, Dinheiro, Endereço) |
| **Eventos de domínio** | Algo que aconteceu no domínio (por exemplo, OrderPlaced) |
| **Camada Anticorrupção** | Camada de tradução entre seu domínio e sistemas externos |
### Quando DDD ajuda
O DDD é mais valioso quando o domínio de negócios é complexo – pense em comércio eletrônico, logística, serviços financeiros, saúde. Se o seu domínio for simples (um blog, um aplicativo de tarefas), DDD é um exagero.
---

## Estratégias de cache
O cache é uma das maneiras mais eficazes de melhorar o desempenho, mas introduz complexidade em torno da consistência.
| Estratégia | Descrição | Troca |
|----------|-------------|-----------|
| **Cache-Aside** | O aplicativo verifica primeiro o cache; carrega do banco de dados em caso de falha | Simples; consistência eventual |
| **Escrever** | Grave no cache e no banco de dados simultaneamente | Consistente; gravações mais lentas |
| **Escrever atrás** | Escreva no cache; gravação assíncrona no banco de dados | Gravações rápidas; risco de perda de dados |
| **Leitura** | Cargas de cache do banco de dados em caso de falha de forma transparente | Mais simples do que colocar em cache |
### O que armazenar em cache
| Camada | O que | Ferramentas |
|-------|------|-------|
| **CDN** | Ativos estáticos, respostas de API | CloudFront, Cloudflare |
| **Inscrição** | Resultados calculados, dados da sessão | Redis, Memcached |
| **Banco de dados** | Resultados da consulta, linhas acessadas com frequência | Cache de consulta, visualizações materializadas |
**A invalidação de cache** é notoriamente difícil. Estratégias comuns: TTL (time-to-live), invalidação orientada a eventos (limpar cache na alteração de dados) e remoção de LRU (menos usado recentemente).
---

## Padrões de Projeto
### Princípios SÓLIDOS
| Princípio | O que isso significa |
|-----------|--------------|
| **S** — Responsabilidade Única | Uma classe deve ter um motivo para mudar |
| **O** — Aberto/Fechado | Aberto para ampliação, fechado para modificação |
| **L** — Substituição de Liskov | Os subtipos devem ser substituíveis pelos seus tipos base |
| **I** — Segregação de interface | Muitas interfaces específicas > uma interface de uso geral |
| **D** — Inversão de Dependência | Dependa de abstrações e não de concreções |
### Padrões Comuns
| Padrão | Intenção | Exemplo |
|--------|--------|---------|
| **Singleton** | Certifique-se de que uma classe tenha apenas uma instância | Conjunto de conexões de banco de dados |
| **Fábrica** | Crie objetos sem especificar a classe exata | `UserFactory.create(type="admin")`|
| **Observador** | Notificar dependentes quando houver mudança de estado | Ouvintes de eventos, pub/sub |
| **Estratégia** | Trocar algoritmos em tempo de execução | Estratégia de pagamento: cartão de crédito, PayPal, criptografia |
| **Repositório** | Acesso abstrato a dados por trás de uma interface limpa | `UserRepository.find_by_id(123)`|
| **Decorador** | Adicionar comportamento dinamicamente | Registrando decorador em torno de um serviço |
| **Adaptador** | Faça interfaces incompatíveis funcionarem juntas | Adaptador de API legado |
---

## Escolhendo a arquitetura certa
Não existe uma arquitetura universalmente "melhor". A escolha certa depende de:
| Fator | Favoreça o monólito quando... | Favoreça microsserviços quando... |
|--------|-------------|-------------------------------------------|
| **Tamanho da equipe** | < 10 developers | >20 desenvolvedores, múltiplas equipes |
| **Complexidade do domínio** | Simples ou bem compreendido | Contextos complexos e com muitos limites |
| **Requisitos de escala** | Necessidades de escala uniforme | Componentes diferentes precisam de escalas diferentes |
| **Cadência de implantação** | Ciclo de lançamento único | São necessárias implantações independentes |
| **Diversidade tecnológica** | Uma pilha está bem | Serviços diferentes precisam de tecnologia diferente |
**Conselhos práticos**: comece com um monólito modular. Extraia serviços somente quando você tiver uma necessidade clara e limites de domínio claros. Microsserviços prematuros são um dos erros arquitetônicos mais comuns no setor.