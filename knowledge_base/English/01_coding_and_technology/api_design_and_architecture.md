<!--
---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
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
tags: [api, design, architecture, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# API Design and Architecture

An API (Application Programming Interface) is how software components talk to each other. A well-designed API is intuitive, consistent, and a pleasure to work with. A poorly designed one causes confusion, bugs, and frustration. This file covers the principles, patterns, and practices for building APIs that developers actually want to use.

---

## REST API Principles

REST (Representational State Transfer) is the dominant architectural style for web APIs. It treats data as **resources** identified by URLs, and uses HTTP methods to operate on them.

### Core Principles

| Principle | Description |
|-----------|-------------|
| **Resources** | Everything is a resource with a URI (`/users/123`, `/orders/456`) |
| **HTTP Methods** | GET (read), POST (create), PUT (replace), PATCH (partial update), DELETE (remove) |
| **Statelessness** | Each request contains all information needed; no server-side session state |
| **Uniform Interface** | Consistent resource naming, standard methods, standard status codes |
| **Representation** | Resources can be represented in multiple formats (JSON, XML) |

### Resource Naming Conventions

| Do | Don't |
|----|-------|
| `/users` (plural noun) | `/user` (singular) |
| `/users/123/orders` (nested) | `/getOrdersForUser?id=123` |
| `/products?category=electronics` (query params for filtering) | `/productsByCategory/electronics` |
| Use hyphens: `/user-profiles` | Use underscores: `/user_profiles` |

### HTTP Methods and Idempotency

| Method | Purpose | Idempotent? | Safe? |
|--------|---------|-------------|-------|
| **GET** | Read a resource | ✅ Yes | ✅ Yes |
| **POST** | Create a resource | ❌ No | ❌ No |
| **PUT** | Replace a resource entirely | ✅ Yes | ❌ No |
| **PATCH** | Partially update a resource | ❌ No* | ❌ No |
| **DELETE** | Remove a resource | ✅ Yes | ❌ No |

*PATCH can be made idempotent with careful design.

### HTTP Status Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| **200** | OK | Successful GET, PUT, PATCH, DELETE |
| **201** | Created | Successful POST (resource created) |
| **204** | No Content | Successful DELETE (nothing to return) |
| **400** | Bad Request | Invalid input or malformed request |
| **401** | Unauthorized | Missing or invalid authentication |
| **403** | Forbidden | Authenticated but not authorised |
| **404** | Not Found | Resource doesn't exist |
| **409** | Conflict | Duplicate resource or state conflict |
| **422** | Unprocessable Entity | Valid JSON but semantic errors |
| **429** | Too Many Requests | Rate limit exceeded |
| **500** | Internal Server Error | Unexpected server error |
| **502** | Bad Gateway | Upstream service failure |
| **503** | Service Unavailable | Temporary overload or maintenance |

---

## API Versioning

APIs evolve. When you need to make breaking changes, versioning lets existing clients keep working.

| Strategy | Example | Pros | Cons |
|----------|---------|------|------|
| **URL path** | `/v1/users`, `/v2/users` | Simple, explicit | URL changes per version |
| **Query parameter** | `/users?version=2` | Flexible | Easy to forget |
| **Header** | `Accept: application/vnd.myapi.v2+json` | Clean URLs | Less discoverable |
| **No versioning** | Schema evolution only | Simplest | Breaking changes affect everyone |

**Best practice**: use URL path versioning (`/v1/`) for clarity. Support at least one previous version. Deprecate old versions with clear timelines.

---

## Authentication Methods

| Method | How It Works | Best For |
|--------|-------------|----------|
| **API Keys** | Secret key in header (`X-API-Key: abc123`) | Server-to-server, simple integrations |
| **OAuth2** | Token-based delegation with scopes | Third-party access, user-authorised apps |
| **JWT** | Self-contained token with claims | Stateless authentication across services |
| **Basic Auth** | Base64-encoded username:password | Development only — never production without TLS |
| **Session cookies** | Server-side session ID in HTTP-only cookie | Traditional web applications |

### OAuth2 Flow (Simplified)

1. Client redirects user to authorisation server.
2. User logs in and grants permission.
3. Authorisation server returns an authorisation code.
4. Client exchanges code for access token (and optionally refresh token).
5. Client uses access token to call the API.
6. When access token expires, use refresh token to get a new one.

---

## API Styles: REST vs GraphQL vs gRPC

| Feature | REST | GraphQL | gRPC |
|---------|------|---------|------|
| **Data Format** | JSON (typically) | JSON | Protobuf (binary) |
| **Endpoints** | Multiple (one per resource) | Single endpoint | Defined by .proto file |
| **Over-fetching** | Common (get more than needed) | None (client specifies fields) | None (schema-defined) |
| **Under-fetching** | Requires multiple calls | None (get exactly what's needed) | None |
| **Real-time** | WebSockets needed | Subscriptions built-in | Streaming built-in |
| **Caching** | HTTP caching works naturally | Harder to cache | Limited |
| **Learning Curve** | Low | Medium | Medium–High |
| **Best For** | Public APIs, CRUD apps | Complex UIs, mobile apps | Internal microservices, high-performance |

---

## Pagination, Filtering, and Sorting

For endpoints that return lists:

| Technique | Example | When to Use |
|-----------|---------|-------------|
| **Offset/Limit** | `?offset=20&limit=10` | Simple; works for small datasets |
| **Cursor-based** | `?cursor=abc123&limit=10` | Large datasets; consistent results |
| **Keyset** | `?created_after=2024-01-01&limit=10` | Very efficient; requires unique key |

```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Rate Limiting

Protect your API from abuse and ensure fair usage.

| Strategy | How It Works |
|----------|-------------|
| **Fixed window** | N requests per time window (e.g., 100/hour) |
| **Sliding window** | More granular; counts requests in rolling window |
| **Token bucket** | Tokens added at fixed rate; each request consumes a token |

Return `429 Too Many Requests` with headers:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Error Handling

Consistent error responses make APIs much easier to work with:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**Principles**: use consistent error structure, include actionable messages, use standard HTTP status codes, log errors server-side with correlation IDs, and never expose stack traces or internal details.

---

## API Documentation

| Tool | Description |
|------|-------------|
| **OpenAPI (Swagger)** | Industry standard for REST API documentation |
| **Swagger UI** | Interactive API documentation from OpenAPI spec |
| **Postman** | API testing, documentation, and collection sharing |
| **Redoc** | Beautiful API reference docs from OpenAPI spec |
| **GraphQL Playground / GraphiQL** | Interactive GraphQL exploration |

**Best practice**: write the OpenAPI spec first (spec-driven development), then generate documentation and client SDKs from it.

---

## API Gateway Patterns

An API gateway sits between clients and backend services, providing a single entry point.

| Responsibility | Description |
|---------------|-------------|
| **Routing** | Direct requests to appropriate backend services |
| **Authentication** | Validate tokens at the gateway level |
| **Rate Limiting** | Apply global or per-client limits |
| **Transformation** | Convert between protocols (REST ↔ gRPC) |
| **Caching** | Cache common responses |
| **Monitoring** | Centralised logging and metrics |
| **Load Balancing** | Distribute traffic across service instances |

| Tool | Type |
|------|------|
| **Kong** | Open-source API gateway (Nginx-based) |
| **AWS API Gateway** | Fully managed, integrated with AWS |
| **Azure API Management** | Managed gateway with developer portal |
| **Envoy / Istio** | Service mesh with API gateway capabilities |
| **Traefik** | Auto-discovery, Let's Encrypt integration |

---

## Webhooks

Webhooks let your API push events to clients in real-time, rather than making clients poll for changes.

| Aspect | Best Practice |
|--------|--------------|
| **Delivery** | POST request with JSON payload to client's URL |
| **Security** | Sign payloads with HMAC; client verifies signature |
| **Reliability** | Retry failed deliveries with exponential backoff |
| **Idempotency** | Include unique event ID; client handles duplicates |
| **Versioning** | Include API version in webhook payload |

---

## Design Checklist

- [ ] Resources are plural nouns (`/users`, not `/getUser`)
- [ ] HTTP methods used correctly (GET for reads, POST for creates, etc.)
- [ ] Consistent error response format
- [ ] Pagination for all list endpoints
- [ ] Rate limiting with clear headers
- [ ] API versioning strategy defined
- [ ] Authentication and authorisation in place
- [ ] Input validation on all endpoints
- [ ] OpenAPI/Swagger documentation maintained
- [ ] CORS configured correctly
- [ ] HTTPS enforced in production
- [ ] Idempotency keys for POST operations where needed
