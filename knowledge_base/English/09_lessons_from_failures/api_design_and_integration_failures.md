<!--
---
# Metadata
title: "API Design and Integration Failures"
description: "API anti-patterns, breaking changes, versioning failures, cascading failures"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [api, design, integration, failures, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# API Design and Integration Failures

APIs (Application Programming Interfaces) are the connective tissue of modern software — they let services communicate, let third parties integrate, and let teams work independently. When API design goes wrong, the consequences ripple across every system that depends on it: broken integrations, security vulnerabilities, developer frustration, and costly rewrites. Integration failures — where systems can't communicate reliably — are among the most common sources of production incidents.

---

## Common API Design Failures

### Design Mistakes

| Mistake | Description | Consequence |
|---------|-------------|-------------|
| **Inconsistent naming** | `/getUsers` vs `/list_users` vs `/fetch-users` | Confusion; errors; slow development |
| **Overloaded endpoints** | One endpoint that does 10 different things based on parameters | Hard to understand; hard to test; hard to change |
| **Under-fetching** | Client needs to make 5 API calls to get related data | Slow; wasteful; complex client code |
| **Over-fetching** | API returns all fields when client only needs 2 | Wasted bandwidth; slow on mobile; security risk (exposing unnecessary data) |
| **No versioning** | Breaking changes deployed without warning | Clients break; angry developers |
| **Vague error messages** | "Error 500: Internal Server Error" with no details | Impossible to debug; slow resolution |
| **Missing pagination** | Endpoint returns all records (could be millions) | Timeouts; memory exhaustion; crashed clients |
| **Inconsistent status codes** | 200 OK for errors; 500 for client mistakes | Clients can't distinguish success from failure |

### REST API Anti-Patterns

| Anti-Pattern | Description | Better Approach |
|-------------|-------------|-----------------|
| **Using GET for mutations** | `GET /delete-user?id=5` | Use DELETE method |
| **Using POST for everything** | `POST /get-users`; `POST /update-user` | Use appropriate HTTP methods (GET, POST, PUT, PATCH, DELETE) |
| **Returning HTML from API** | API returns HTML fragments | Return JSON; let the client render |
| **Business logic in URLs** | `/users/active/premium/from-2023` | Use query parameters or request body for complex filters |
| **Exposing database schema** | `/api/table_name/column` | Design API around resources and domain concepts, not tables |
| **No HATEOAS / links** | Client hardcodes all URLs | Include links to related resources in responses |

---

## Security Failures

### Common API Vulnerabilities

| Vulnerability | Description | Example |
|--------------|-------------|---------|
| **Broken authentication** | API doesn't properly verify identity | Missing token validation; expired tokens accepted |
| **Excessive data exposure** | API returns more data than client needs | User endpoint returns password hashes and internal IDs |
| **Mass assignment** | Client can set fields they shouldn't | `PATCH /user` allows setting `role: "admin"` |
| **Injection** | User input interpreted as code | SQL injection; NoSQL injection; command injection |
| **IDOR** (Insecure Direct Object Reference) | Accessing resources by changing ID in URL | `/api/users/5` → change to `/api/users/6` to see someone else's data |
| **Rate limiting missing** | No limit on API calls | Brute force; denial of service; scraping |
| **CORS misconfiguration** | Overly permissive cross-origin access | `Access-Control-Allow-Origin: *` on authenticated endpoints |

### Authentication and Authorisation Failures

| Failure | Description | Impact |
|---------|-------------|--------|
| **Hardcoded credentials** | API keys or passwords in source code | Leaked through version control; accessible to all developers |
| **No token expiry** | Tokens never expire | Stolen token gives permanent access |
| **Weak secret keys** | Short or predictable signing keys | Tokens can be forged |
| **No scope / permissions** | All tokens have full access | Compromised token = full system access |
| **Logging sensitive data** | Tokens or passwords in logs | Accessible to anyone with log access |
| **Inconsistent authorisation** | Some endpoints check permissions; others don't | Unauthorised access through unguarded endpoints |

---

## Integration Failures

### Distributed System Integration Issues

| Failure | Description | Example |
|---------|-------------|---------|
| **Tight coupling** | Services depend on internal implementation details of each other | Changing one service's database breaks three others |
| **Synchronous chains** | Service A calls B calls C calls D; latency accumulates | 200ms + 300ms + 500ms = 1 second response time |
| **No circuit breaker** | Failing service causes cascading failures | Service D is slow; all upstream services exhaust their threads waiting |
| **No retry logic** | Transient failures become permanent | Network blip = failed transaction; user has to retry manually |
| **Excessive retries** | Retries without backoff overwhelm recovering services | Thundering herd problem |
| **No idempotency** | Retrying a non-idempotent operation creates duplicates | Payment charged twice; order created twice |
| **Eventual consistency surprises** | Client reads stale data after a write | User updates profile; refreshes page; old data still shown |

### Third-Party Integration Failures

| Failure | Description | Mitigation |
|---------|-------------|------------|
| **Vendor API changes** | Third-party changes their API without notice | Version pinning; abstraction layer; monitoring vendor changelogs |
| **Rate limiting** | Third-party throttles your requests | Caching; request queuing; negotiating higher limits |
| **Vendor downtime** | Third-party service is unavailable | Circuit breakers; fallback behaviour; multi-vendor strategy |
| **Data format changes** | Third-party changes response format | Schema validation; transformation layer; alerts on format changes |
| **Deprecation without migration path** | Vendor deprecates endpoint with no equivalent | Stay informed; maintain abstraction; plan migrations early |

---

## Case Studies

### Case Study 1: The API That Returned Everything

| Aspect | Description |
|--------|-------------|
| **Scenario** | A SaaS company's user API returned all user fields including internal metadata |
| **What went wrong** | No field filtering; response included password hashes, internal notes, and admin flags |
| **Impact** | Security researchers discovered the exposure; public disclosure; GDPR investigation |
| **Root cause** | API serialised the entire database model without filtering |
| **Fix** | Explicit response models; field-level access control; security review of all endpoints |
| **Lesson** | Never expose your database model directly through an API; use DTOs (Data Transfer Objects) |

### Case Study 2: The Cascading Failure

| Aspect | Description |
|--------|-------------|
| **Scenario** | A microservices architecture with synchronous inter-service communication |
| **What went wrong** | One service experienced a database slowdown; upstream services waited for responses; thread pools exhausted |
| **Impact** | Complete system outage for 45 minutes; all services affected |
| **Root cause** | No circuit breakers; no timeouts; synchronous dependency chain |
| **Fix** | Circuit breakers; timeouts; async communication where possible; bulkheads |
| **Lesson** | Synchronous calls between services create fragile chains; design for failure |

---

## Best Practices

### API Design Checklist

| Area | Practice |
|------|----------|
| **Naming** | Use nouns for resources; HTTP methods for actions; consistent naming convention |
| **Versioning** | Version from day one; use URL versioning (`/v1/`) or header versioning |
| **Pagination** | Always paginate list endpoints; use cursor-based pagination for large datasets |
| **Error handling** | Consistent error format; include error codes; provide actionable messages |
| **Rate limiting** | Implement rate limits; return 429 with retry-after header |
| **Idempotency** | Support idempotency keys for mutation endpoints |
| **Documentation** | OpenAPI / Swagger spec; keep it updated; provide examples |
| **Testing** | Contract tests; integration tests; consumer-driven contract tests |
| **Monitoring** | Track latency; error rates; throughput; dependency health |
| **Deprecation** | Announce deprecations well in advance; provide migration guides |

---

## Summary

API design failures range from cosmetic (inconsistent naming) to catastrophic (security vulnerabilities, cascading failures). The most common design mistakes — overloaded endpoints, over-fetching, missing pagination, vague errors — make APIs hard to use and maintain. Security failures — broken authentication, IDOR, mass assignment, excessive data exposure — expose systems to attack. Integration failures — tight coupling, synchronous chains, missing circuit breakers, no idempotency — create fragile systems where one failure cascades across services. Third-party integrations add external risk: API changes, rate limiting, and vendor downtime. The prevention strategies are well-established: use explicit response models; version from day one; implement circuit breakers and timeouts; design for idempotency; validate and sanitise all inputs; monitor everything; and treat API contracts as binding agreements that require coordination to change. The best APIs are boring — predictable, consistent, well-documented, and resilient to failure.
