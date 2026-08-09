---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
category: "Coding and Technology"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Software Architecture Patterns

Architecture is the set of structural decisions about how a system is organised — what components it has, how they communicate, and where responsibilities lie. Good architecture makes a system easy to understand, modify, and scale. Bad architecture makes every change a struggle. This file covers the major patterns, when to use each, and the trade-offs involved.

---

## Monolith vs Microservices

This is the most fundamental architectural decision, and it's worth getting right.

| Aspect | Monolith | Microservices |
|--------|----------|---------------|
| **Structure** | Single deployable unit | Many small, independently deployable services |
| **Data** | Shared database | Each service owns its data |
| **Communication** | In-process function calls | Network calls (HTTP, gRPC, messaging) |
| **Scaling** | Scale the whole application | Scale individual services |
| **Deployment** | Single release cycle | Independent deployments |
| **Complexity** | Simpler to develop initially | Operational complexity (networking, monitoring) |
| **Best For** | Small teams, early-stage products | Large teams, complex domains, high scale |

### When to Start with a Monolith

Most applications should start as a monolith. It's simpler to build, test, deploy, and debug. You can always extract services later when you have a clearer picture of your domain boundaries. This is sometimes called the "modular monolith" — a monolith with clean internal boundaries that make extraction easy later.

### When to Go Microservices

Consider microservices when:
- Teams are large enough that coordination becomes a bottleneck.
- Different parts of the system have very different scaling requirements.
- You need independent deployment of components.
- Your domain has clear bounded contexts (see DDD below).

---

## Layered Architecture (N-Tier)

The most common architecture pattern. Code is organised into layers, each with a specific responsibility.

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

| Layer | Responsibility | Rule |
|-------|---------------|------|
| **Presentation** | Handle user/HTTP requests | Can call Application layer only |
| **Application** | Orchestrate use cases | Can call Domain layer |
| **Domain** | Core business logic | Should not depend on other layers |
| **Infrastructure** | Technical concerns | Implements interfaces defined in Domain |

**Key rule**: dependencies point inward. The Domain layer doesn't know about the database or the web framework.

---

## Event-Driven Architecture

Components communicate by emitting and reacting to **events** — things that have happened.

| Pattern | Description |
|---------|-------------|
| **Event Notification** | Service A emits "OrderPlaced"; services B, C, D react |
| **Event Sourcing** | Store all state changes as a sequence of events (not just current state) |
| **CQRS** | Separate read model (queries) from write model (commands) |

### Event Sourcing

Instead of storing "current state" in a database, store every state change as an event:

```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Benefits: complete audit trail, ability to reconstruct any past state, decoupled consumers. Challenges: event schema evolution, eventual consistency, debugging complexity.

### CQRS (Command Query Responsibility Segregation)

| Side | Purpose | Database |
|------|---------|----------|
| **Command (Write)** | Handle mutations; enforce business rules | Optimised for writes (normalised) |
| **Query (Read)** | Serve read requests | Optimised for reads (denormalised) |

CQRS pairs naturally with Event Sourcing: events from the write side are projected into read-optimised views.

---

## Message Queues and Event Brokers

When services need to communicate asynchronously, message queues are the backbone.

| Tool | Type | Best For |
|------|------|----------|
| **Apache Kafka** | Distributed event log | High-throughput event streaming, event sourcing |
| **RabbitMQ** | Message broker with routing | Task queues, complex routing patterns |
| **AWS SQS** | Managed queue | AWS-native, simple queuing |
| **AWS SNS** | Pub/sub notification | Fan-out to multiple subscribers |
| **Google Pub/Sub** | Managed pub/sub | GCP-native event streaming |
| **Redis Streams** | Lightweight stream | Simple event logging, caching use cases |

### Messaging Patterns

| Pattern | Description |
|---------|-------------|
| **Point-to-Point** | One producer, one consumer per message |
| **Publish/Subscribe** | One producer, multiple subscribers |
| **Request/Reply** | Synchronous-style over async transport |
| **Dead Letter Queue** | Messages that fail processing go to a separate queue for inspection |

---

## Domain-Driven Design (DDD)

DDD is a strategic approach to software design that centres the code around business concepts rather than technical concerns.

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Bounded Context** | A boundary within which a domain model is consistent (e.g., "Ordering", "Shipping", "Billing") |
| **Ubiquitous Language** | Shared vocabulary between developers and domain experts |
| **Aggregates** | Clusters of related entities treated as a single unit for data changes |
| **Entities** | Objects with identity (e.g., a User with a user_id) |
| **Value Objects** | Objects without identity; defined by their attributes (e.g., Money, Address) |
| **Domain Events** | Something that happened in the domain (e.g., OrderPlaced) |
| **Anti-Corruption Layer** | Translation layer between your domain and external systems |

### When DDD Helps

DDD is most valuable when the business domain is complex — think e-commerce, logistics, financial services, healthcare. If your domain is simple (a blog, a todo app), DDD is overkill.

---

## Caching Strategies

Caching is one of the most effective ways to improve performance, but it introduces complexity around consistency.

| Strategy | Description | Trade-off |
|----------|-------------|-----------|
| **Cache-Aside** | Application checks cache first; loads from DB on miss | Simple; eventual consistency |
| **Write-Through** | Write to cache and DB simultaneously | Consistent; slower writes |
| **Write-Behind** | Write to cache; async write to DB | Fast writes; risk of data loss |
| **Read-Through** | Cache loads from DB on miss transparently | Simpler than cache-aside |

### What to Cache

| Layer | What | Tools |
|-------|------|-------|
| **CDN** | Static assets, API responses | CloudFront, Cloudflare |
| **Application** | Computed results, session data | Redis, Memcached |
| **Database** | Query results, frequently accessed rows | Query cache, materialised views |

**Cache invalidation** is notoriously hard. Common strategies: TTL (time-to-live), event-driven invalidation (clear cache on data change), and LRU (least recently used) eviction.

---

## Design Patterns

### SOLID Principles

| Principle | What It Means |
|-----------|--------------|
| **S** — Single Responsibility | A class should have one reason to change |
| **O** — Open/Closed | Open for extension, closed for modification |
| **L** — Liskov Substitution | Subtypes should be substitutable for their base types |
| **I** — Interface Segregation | Many specific interfaces > one general-purpose interface |
| **D** — Dependency Inversion | Depend on abstractions, not concretions |

### Common Patterns

| Pattern | Intent | Example |
|---------|--------|---------|
| **Singleton** | Ensure a class has only one instance | Database connection pool |
| **Factory** | Create objects without specifying exact class | `UserFactory.create(type="admin")` |
| **Observer** | Notify dependents when state changes | Event listeners, pub/sub |
| **Strategy** | Swap algorithms at runtime | PaymentStrategy: CreditCard, PayPal, Crypto |
| **Repository** | Abstract data access behind a clean interface | `UserRepository.find_by_id(123)` |
| **Decorator** | Add behaviour dynamically | Logging decorator around a service |
| **Adapter** | Make incompatible interfaces work together | Legacy API adapter |

---

## Choosing the Right Architecture

There's no universally "best" architecture. The right choice depends on:

| Factor | Favour Monolith When... | Favour Microservices When... |
|--------|------------------------|------------------------------|
| **Team size** | < 10 developers | > 20 developers, multiple teams |
| **Domain complexity** | Simple or well-understood | Complex, many bounded contexts |
| **Scale requirements** | Uniform scaling needs | Different components need different scale |
| **Deployment cadence** | Single release cycle | Independent deployments needed |
| **Technology diversity** | One stack is fine | Different services need different tech |

**Practical advice**: start with a modular monolith. Extract services only when you have a clear need and clear domain boundaries. Premature microservices are one of the most common architectural mistakes in the industry.
