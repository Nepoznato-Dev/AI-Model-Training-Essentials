# System Architecture Design Skill

## Overview
The ability to design scalable, maintainable, and robust software systems that meet business requirements while considering technical constraints.

## Core Competencies

### 1. Architectural Patterns
- **Layered Architecture**: Separation of concerns (presentation, business, data)
- **Microservices**: Decomposed, independently deployable services
- **Event-Driven**: Asynchronous communication through events
- **Serverless**: Function-as-a-Service architectures
- **CQRS**: Command Query Responsibility Segregation
- **Hexagonal/Ports & Adapters**: Domain-centric design

### 2. Design Principles
- **SOLID**: Single responsibility, Open-closed, Liskov substitution, Interface segregation, Dependency inversion
- **DRY**: Don't Repeat Yourself
- **KISS**: Keep It Simple, Stupid
- **YAGNI**: You Ain't Gonna Need It
- **Separation of Concerns**: Distinct sections for distinct functionalities
- **Loose Coupling**: Minimize dependencies between components

### 3. Scalability Considerations
- **Horizontal vs Vertical Scaling**: Adding machines vs upgrading existing ones
- **Load Balancing**: Distributing traffic across servers
- **Caching Strategies**: Redis, CDN, browser caching
- **Database Sharding**: Partitioning data across databases
- **Replication**: Data redundancy for availability
- **Async Processing**: Message queues, background jobs

## Frameworks & Methods

### Architecture Decision Record (ADR)
```markdown
# ADR-001: [Title]

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
[What is the issue we're addressing?]

## Decision
[What change are we proposing?]

## Consequences
[What becomes easier or more difficult?]
- Positive impacts
- Negative impacts
- Risks and mitigations
```

### C4 Model for Documentation
1. **Context**: System and its users
2. **Container**: High-level technology choices
3. **Component**: Key components and their interactions
4. **Code**: Class diagrams and implementation details

## Practical Templates

### System Design Document Template
```markdown
## 1. Overview
- Purpose
- Scope
- Definitions and acronyms

## 2. System Description
- Architecture diagram
- Key components
- Technology stack

## 3. Data Design
- Database schema
- Data flow diagrams
- Data retention policies

## 4. Interface Design
- API specifications
- External integrations
- User interfaces

## 5. Security Design
- Authentication/Authorization
- Data encryption
- Compliance requirements

## 6. Performance Requirements
- Response time targets
- Throughput expectations
- Scalability plans

## 7. Deployment Architecture
- Infrastructure diagram
- CI/CD pipeline
- Monitoring strategy
```

### Trade-off Analysis Template
```markdown
## Decision: [What are we deciding?]

### Option A: [Name]
**Pros:**
- 
**Cons:**
- 
**Risks:**
- 

### Option B: [Name]
**Pros:**
- 
**Cons:**
- 
**Risks:**
- 

### Recommendation
[Which option and why?]
```

## Common Pitfalls

### ❌ What to Avoid
- Over-engineering simple problems
- Premature optimization
- Ignoring non-functional requirements
- Tight coupling between services
- No clear ownership boundaries
- Skipping documentation
- Not planning for failure

### ✅ Best Practices
- Start simple, evolve as needed
- Design for failure (circuit breakers, retries)
- Implement comprehensive monitoring
- Document architectural decisions
- Regular architecture reviews
- Consider operational complexity
- Plan for observability from day one

## Tools & Resources

### Diagramming Tools
- **Draw.io**: Free diagramming software
- **Lucidchart**: Collaborative diagrams
- **Excalidraw**: Hand-drawn style diagrams
- **PlantUML**: Text-based UML diagrams

### Architecture Frameworks
- TOGAF (The Open Group Architecture Framework)
- AWS Well-Architected Framework
- Azure Architecture Center
- Google Cloud Architecture Framework

## Example Application

### Scenario: Designing an E-commerce Platform
1. **Requirements Gathering**: Identify functional and non-functional needs
2. **High-Level Design**: Choose microservices architecture
3. **Service Decomposition**: Define bounded contexts (Catalog, Cart, Order, Payment)
4. **Data Strategy**: Polyglot persistence (SQL for orders, NoSQL for catalog)
5. **Integration Pattern**: Event-driven with message queue (Kafka/RabbitMQ)
6. **Security**: OAuth2, JWT, HTTPS everywhere
7. **Scalability**: Auto-scaling, CDN, database read replicas
8. **Observability**: Centralized logging, metrics, distributed tracing

## Success Indicators
- System meets performance SLAs
- Easy to add new features
- Minimal downtime during deployments
- Clear service ownership
- Effective incident response
- Cost-efficient infrastructure
- High developer productivity
