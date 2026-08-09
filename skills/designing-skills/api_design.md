---
# Metadata
title: "API Design Skill"
description: "Design intuitive, consistent, and scalable APIs for seamless system integration"
category: "Designing Skills"
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
    date: "2026-01-15"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-01-15"
last_modified: "2026-01-15"
review_date: "2026-07-15"
reviewed_by: "Designing Skills Team"
next_review: "2027-01-15"

# Classification
tags: [api-design, rest, graphql, microservices, documentation]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# API Design Skill

## Overview
The ability to design intuitive, consistent, and scalable APIs that enable seamless integration between systems and provide excellent developer experiences.

## Core Competencies

### 1. RESTful Design
- **Resource-Oriented**: Nouns as endpoints, not verbs
- **HTTP Methods**: Proper use of GET, POST, PUT, PATCH, DELETE
- **Status Codes**: Meaningful response codes (200, 201, 400, 404, 500, etc.)
- **Versioning**: URL path, header, or query parameter strategies
- **HATEOAS**: Hypermedia as the Engine of Application State
- **Statelessness**: Each request contains all necessary information

### 2. GraphQL Design
- **Schema Definition**: Types, queries, mutations, subscriptions
- **Resolver Implementation**: Data fetching logic
- **Query Optimization**: Avoiding N+1 problems
- **Fragment Usage**: Reusable field selections
- **Error Handling**: Structured error responses

### 3. gRPC Design
- **Protocol Buffers**: Efficient serialization format
- **Service Definitions**: RPC methods and message types
- **Streaming**: Unary, server, client, bidirectional streaming
- **Interceptors**: Cross-cutting concerns (auth, logging)

### 4. Security Best Practices
- **Authentication**: OAuth2, JWT, API keys
- **Authorization**: Role-based, attribute-based access control
- **Rate Limiting**: Prevent abuse and ensure fair usage
- **Input Validation**: Sanitize all inputs
- **HTTPS**: Encrypt all communications
- **CORS**: Controlled cross-origin resource sharing

## Frameworks & Methods

### API Design-First Approach
1. **Define Requirements**: Understand use cases and consumer needs
2. **Design Contract**: Create OpenAPI/Swagger specification
3. **Review & Iterate**: Get stakeholder feedback
4. **Mock Server**: Enable parallel development
5. **Implement**: Build according to contract
6. **Test**: Validate against specification
7. **Document**: Generate comprehensive docs
8. **Version**: Plan for evolution

### Richardson Maturity Model
- **Level 0**: Single endpoint, HTTP as transport
- **Level 1**: Multiple endpoints (resources)
- **Level 2**: HTTP verbs and status codes
- **Level 3**: HATEOAS, hypermedia controls

## Practical Templates

### OpenAPI Specification Template
```yaml
openapi: 3.0.0
info:
  title: API Name
  version: 1.0.0
  description: API description

servers:
  - url: https://api.example.com/v1

paths:
  /resources:
    get:
      summary: List resources
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      $ref: '#/components/schemas/Resource'
                  meta:
                    $ref: '#/components/schemas/Pagination'

components:
  schemas:
    Resource:
      type: object
      properties:
        id:
          type: string
        name:
          type: string
```

### API Changelog Template
```markdown
## Version 2.0.0 - YYYY-MM-DD

### Breaking Changes
- [Description of breaking change]
- Migration guide: [Link]

### New Features
- [Feature description]
- [Feature description]

### Improvements
- [Improvement description]

### Bug Fixes
- [Fix description]

### Deprecations
- [Deprecated feature] - Will be removed in v3.0.0
```

### Error Response Format
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input provided",
    "details": [
      {
        "field": "email",
        "message": "Must be a valid email address"
      }
    ],
    "request_id": "req_abc123",
    "documentation_url": "https://docs.example.com/errors#VALIDATION_ERROR"
  }
}
```

## Common Pitfalls

### ❌ What to Avoid
- Inconsistent naming conventions
- Leaking internal implementation details
- Over-fetching or under-fetching data
- Poor error messages
- No versioning strategy
- Ignoring pagination for large datasets
- Mixing authentication methods inconsistently
- Not documenting rate limits
- Verb-based endpoints (e.g., `/getUser`, `/createUser`)

### ✅ Best Practices
- Use nouns for resources (`/users`, not `/getUsers`)
- Implement consistent pagination (cursor or offset-based)
- Provide filtering, sorting, and field selection
- Use standard HTTP status codes correctly
- Include request IDs for debugging
- Document all endpoints thoroughly
- Design for backward compatibility
- Implement proper caching headers
- Use plural nouns for collections
- Return appropriate Content-Type headers

## Tools & Resources

### Design & Documentation
- **Swagger/OpenAPI**: API specification standard
- **Stoplight**: Visual API design
- **Postman**: API development and testing
- **Insomnia**: API client and documentation
- **Redoc**: Beautiful API documentation

### Testing & Monitoring
- **Newman**: CLI collection runner for Postman
- **Dredd**: API blueprint testing
- **Schemathesis**: Property-based API testing
- **Datadog/New Relic**: API performance monitoring

## Example Application

### Scenario: Designing a Blog Platform API

**RESTful Endpoints:**
```
GET    /articles           # List articles
POST   /articles           # Create article
GET    /articles/{id}      # Get article
PATCH  /articles/{id}      # Update article
DELETE /articles/{id}      # Delete article
GET    /articles/{id}/comments  # List comments
POST   /articles/{id}/comments  # Add comment
```

**Query Parameters:**
```
GET /articles?author=john&tag=tech&sort=-created_at&limit=10&fields=id,title,excerpt
```

**Response Example:**
```json
{
  "data": [
    {
      "id": "art_123",
      "type": "article",
      "attributes": {
        "title": "API Design Best Practices",
        "excerpt": "Learn how to design great APIs...",
        "created_at": "2026-01-15T10:30:00Z"
      },
      "relationships": {
        "author": {
          "data": { "type": "user", "id": "usr_456" }
        },
        "comments": {
          "links": {
            "related": "/articles/art_123/comments"
          }
        }
      }
    }
  ],
  "meta": {
    "page": {
      "total": 150,
      "limit": 10,
      "next": "/articles?page=2"
    }
  },
  "links": {
    "self": "/articles",
    "next": "/articles?page=2"
  }
}
```

## Related Skills

- [System Architecture](system_architecture.md) - High-level system design
- [GUI Design](gui_design.md) - User-facing interface design
- [Database Design](../data-skills/database_design.md) - Data access layer design

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Designing Skills Team
next_review: 2026-07-15
---
