---
# Metadata
title: "Performance Optimisation"
description: "Profiling, caching, CDN, query optimisation, front-end perf"
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

# Performance Optimisation

Performance optimisation is the practice of making software faster — reducing response times, increasing throughput, lowering memory usage, and eliminating bottlenecks. It's one of the most impactful skills a developer can have, because slow software loses users, wastes resources, and frustrates everyone. But it's also one of the most commonly done wrong, with developers optimising the wrong things based on intuition rather than evidence.

---

## The Golden Rule

> **Measure first, optimise second.** Never optimise based on assumptions. Profile the code, find the actual bottleneck, and fix that.

| Anti-pattern | Why It's Bad |
|-------------|-------------|
| **Premature optimisation** | Spending time speeding up code that isn't slow |
| **Optimising without measurement** | Fixing the wrong bottleneck; no way to verify improvement |
| **Sacrificing readability for speed** | Unreadable code costs more than the performance gain |
| **Caching everything** | Stale data, memory bloat, complexity |

---

## Profiling

Before you can make something faster, you need to know *where* the time is being spent.

| Tool Type | What It Measures | Examples |
|-----------|-----------------|----------|
| **CPU profiler** | Which functions consume the most CPU time | cProfile (Python), perf (Linux), Chrome DevTools (JS) |
| **Memory profiler** | Memory allocation and leaks | tracemalloc (Python), Valgrind, heaptrack |
| **I/O profiler** | Disk and network I/O bottlenecks | iotop, strace, Wireshark |
| **APM (Application Performance Monitoring)** | End-to-end request timing | New Relic, Datadog, Jaeger |
| **Browser DevTools** | Frontend rendering, JavaScript execution, network | Chrome DevTools, Firefox Profiler |

### Profiling Workflow

| Step | Description |
|------|-------------|
| 1. Identify the slow operation | Users report slow page load; monitoring shows high latency |
| 2. Profile the full path | Find which component takes the most time |
| 3. Drill down | Profile that specific component to find the hot function |
| 4. Fix the bottleneck | Apply the appropriate optimisation |
| 5. Measure again | Verify the improvement; check for regressions |

---

## Algorithmic Optimisation

The biggest performance gains come from choosing better algorithms, not from micro-optimisations.

| Change | Improvement |
|--------|------------|
| Linear search O(n) → Hash table lookup O(1) | 100x+ for large datasets |
| Nested loop O(n²) → Sort + binary search O(n log n) | Orders of magnitude for large n |
| Repeated computation → Memoisation / caching | Eliminates redundant work |
| String concatenation in a loop → Builder / join | Avoids quadratic string copying |
| Unsorted data → Sorted data with binary search | O(log n) instead of O(n) per lookup |

---

## Caching Strategies

Caching stores computed results so they don't need to be recomputed.

| Cache Type | Location | Speed | Lifetime |
|-----------|----------|-------|----------|
| **CPU cache** | L1/L2/L3 | ~1 ns | Automatic |
| **In-memory** | Application RAM (dict, HashMap) | ~100 ns | Until cleared or evicted |
| **Distributed cache** | Redis, Memcached | ~1 ms | Configurable TTL |
| **CDN** | Edge servers worldwide | ~10-50 ms | Configurable TTL |
| **Browser cache** | User's browser | ~1 ms | HTTP cache headers |
| **Database query cache** | Database or ORM level | ~1-10 ms | Until data changes |

### Caching Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Cache-aside** | Application checks cache; loads from DB on miss; stores in cache | Most common; simple |
| **Write-through** | Write to cache and DB simultaneously | When reads >> writes; consistency important |
| **Write-behind** | Write to cache; asynchronously write to DB | High write throughput; some data loss risk |
| **TTL (Time to Live)** | Cache entries expire after a set time | When data changes periodically |
| **Invalidation** | Explicitly remove stale cache entries | When you know exactly when data changes |

### Cache Invalidation

The two hardest problems in computer science: cache invalidation, naming things, and off-by-one errors.

| Strategy | Description |
|----------|-------------|
| **TTL-based** | Entries expire after N seconds; simple but may serve stale data |
| **Event-driven** | Invalidate when data changes; more complex but accurate |
| **Version-based** | Include a version number; increment on changes |
| **Tag-based** | Tag related cache entries; invalidate all entries with a tag |

---

## Database Optimisation

Databases are often the biggest bottleneck in web applications.

| Technique | Description | Impact |
|-----------|-------------|--------|
| **Indexing** | Add indexes on columns used in WHERE, JOIN, ORDER BY | 10-1000x faster queries |
| **Query optimisation** | Avoid SELECT *; use EXPLAIN to analyse queries | Reduce I/O |
| **Connection pooling** | Reuse database connections instead of creating new ones | Eliminate connection overhead |
| **Read replicas** | Route read queries to replica databases | Distribute read load |
| **Partitioning** | Split large tables into smaller partitions | Faster queries on large datasets |
| **Denormalisation** | Add redundant data to avoid joins | Faster reads; slower writes |
| **Materialised views** | Pre-computed query results | Instant complex queries |
| **N+1 prevention** | Use JOINs, eager loading, or batch queries | Eliminate thousands of queries |

---

## Concurrency and Parallelism

| Concept | Description | When to Use |
|---------|-------------|-------------|
| **Threading** | Multiple threads within a single process | I/O-bound tasks (network, disk) |
| **Multiprocessing** | Multiple processes (bypasses GIL in Python) | CPU-bound tasks |
| **Async/await** | Cooperative multitasking; single thread | High-concurrency I/O (web servers) |
| **GPU computing** | Thousands of parallel cores | Matrix operations; image processing; ML |

### Async vs Threading

| Aspect | Async/Await | Threading |
|--------|------------|-----------|
| **Model** | Cooperative (tasks yield control) | Preemptive (OS switches threads) |
| **Overhead** | Very low (no context switching) | Higher (thread creation, context switching) |
| **Complexity** | Simpler reasoning (single thread) | Race conditions, deadlocks, locks |
| **Best for** | Many concurrent I/O operations | Blocking operations that can't be made async |
| **Limitation** | Can't use CPU-bound code without blocking | GIL in Python limits true parallelism |

---

## Frontend Performance

| Technique | Description | Impact |
|-----------|-------------|--------|
| **Minification** | Remove whitespace and shorten variable names | 20-40% smaller files |
| **Bundling** | Combine multiple files into fewer requests | Fewer HTTP requests |
| **Code splitting** | Load only the code needed for the current page | Faster initial load |
| **Lazy loading** | Load images and components when they're needed | Faster initial render |
| **Tree shaking** | Remove unused code from bundles | Smaller bundles |
| **Image optimisation** | Use WebP/AVIF; responsive images; lazy loading | 50-80% smaller images |
| **CDN** | Serve static assets from edge servers | Lower latency globally |
| **HTTP/2 and HTTP/3** | Multiplexing; header compression; 0-RTT | Faster protocol overhead |
| **Service workers** | Cache assets for offline use; push notifications | Faster repeat visits |

---

## Memory Optimisation

| Technique | Description |
|-----------|-------------|
| **Object pooling** | Reuse objects instead of creating new ones |
| **Streaming** | Process data in chunks instead of loading everything into memory |
| **Generators / iterators** | Yield values one at a time instead of building lists |
| **Memory-mapped files** | Access large files without loading them entirely |
| **Garbage collection tuning** | Adjust GC parameters for your workload |
| **Data structure choice** | Use arrays instead of linked lists for cache locality; use sets for membership testing |

---

## Network Optimisation

| Technique | Description |
|-----------|-------------|
| **Compression** | gzip, brotli for HTTP responses |
| **Connection reuse** | Keep-alive connections; HTTP/2 multiplexing |
| **Request batching** | Combine multiple API calls into one |
| **Pagination** | Load data in pages instead of all at once |
| **Compression at rest** | Compress data in databases and caches |
| **Protocol choice** | gRPC (binary, efficient) vs REST (human-readable) |

---

## Monitoring and Alerting

| Metric | What It Tells You |
|--------|------------------|
| **P50 / P95 / P99 latency** | Response time at various percentiles |
| **Throughput** | Requests per second |
| **Error rate** | Percentage of failed requests |
| **CPU utilisation** | How much processing capacity is used |
| **Memory usage** | RAM consumption; approaching limits? |
| **Database query time** | Slow queries that need optimisation |

---

## Summary

Performance optimisation is a systematic process: measure, identify the bottleneck, fix it, measure again. The biggest wins come from algorithmic improvements and eliminating unnecessary work — not from micro-optimisations. Caching, database indexing, and concurrency are the most powerful tools. Frontend performance depends on minimising payload size and round trips. And the most important rule is always the same: don't guess — profile.
