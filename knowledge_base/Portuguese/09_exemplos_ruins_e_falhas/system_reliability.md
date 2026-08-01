# Problemas de Confiabilidade de Sistema

## Vazamentos de memória

### Listeners esquecidos
### Recursos não fechados
### Referências circulares

```python
# Creating tree structure
# When deleting root, child keeps reference to root
# When deleting child, root keeps reference to child
# Neither can be garbage collected (in some languages)
```

## Condições de corrida

### Race condition de checar-antes-agir

```python
# VULNERABLE: check and act are not atomic
```

### Race condition de ler-modificar-escrever

```python
# VULNERABLE: Counter increment is not atomic
# Multiple threads calling increment() will lose updates
```

### Race condition de inicialização preguiçosa

```python
# VULNERABLE: Double-checked locking without proper synchronization
```

## Antipadrões de concorrência

### Deadlock
```text
# Thread 1:                    # Thread 2:
# DEADLOCK - both threads waiting forever
# Both threads:
# ... critical section ...
```

### Livelock
```text
# Two threads trying to be polite
```

### Starvation
```text
# High-priority tasks constantly preempt low-priority tasks
# Low-priority task never gets CPU time
```

## Problemas de performance

### Problema N+1 de consultas
```text
# Fetch all users
# N+1 queries: one query per user to get their orders
# Fetch all users
# Single query for all orders
# Group orders by user
```

### Loops ineficientes
```text
# O(n²) complexity
# O(n) complexity
```

## Resumo das melhores práticas

### Gerenciamento de memória
### Concorrência
### Performance

## Tópicos relacionados

## Padrões adicionais de confiabilidade

### Esgotamento de recursos
```text
# Unbounded connection creation
# Each request leaks a connection
# Eventually: "Too many open connections" error
```

### Falhas em cascata
### Pontos únicos de falha

## Monitoramento e observabilidade

### Health checks ausentes
```text
# No health check endpoint
# Load balancer can't detect unhealthy instances
# Traffic continues to broken servers
```

### Logging insuficiente
### Coleta de métricas ausente
```text
# No metrics exposed
# Operators are blind to:
# - Request rate
# - Error rate  
# - Latency distribution
# - Resource usage
```

## Desafios de sistemas distribuídos

### Problemas de clock skew
```text
# Assuming synchronized clocks across servers
# Server A: 10:00:00
# Server B: 10:00:05 (5 seconds ahead)
# Token expires at 10:00:02
# Server A says valid, Server B says expired = inconsistency
# Or use distributed tracing with consistent timestamps
```

### Tratamento de partições de rede
- assumir que a rede é sempre confiável é perigoso

## Princípios de chaos engineering

### Testando cenários de falha
```text
# Chaos Mesh experiment
```

### Game days

## Planejamento de capacidade

### Subprovisionamento
### Desperdício por overprovisioning

## Melhores práticas de resposta a incidentes

### Prevenção de burnout de plantão
### Qualidade de runbooks

## Consulta lenta de banco de dados

## Consulta lenta de banco de dados
### Sintomas
### Detecção
### Ações imediatas
### Escalonamento
### Pós-incidente
