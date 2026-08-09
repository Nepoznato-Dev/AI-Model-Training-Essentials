---
# Metadata
title: "Low-Code and Platform Engineering"
description: "Low-code platforms, internal developer platforms, golden paths"
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
tags: [low, code, platform, engineering, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Low-Code and Platform Engineering

Low-code platforms let people build applications with minimal hand-written code — typically through drag-and-drop interfaces, visual workflows, and pre-built connectors. Platform engineering is the discipline of building internal developer platforms (IDPs) that make it easy for product teams to self-serve infrastructure, CI/CD, and operational tooling. Both trends are responses to the same problem: the gap between the demand for software and the supply of developers who can build it.

---

## Low-Code Platforms

### What Low-Code Actually Means

| Aspect | Description |
|--------|-------------|
| **Visual development** | Drag-and-drop UI builders; visual workflow editors; form designers |
| **Pre-built components** | Ready-made widgets, connectors, templates, and integrations |
| **Declarative logic** | Configure behaviour through rules and conditions rather than writing code |
| **Extensibility** | Ability to add custom code when the platform's built-in capabilities aren't enough |
| **Managed infrastructure** | Platform handles hosting, scaling, security patches |

### Popular Low-Code Platforms

| Platform | Strength | Typical Use Case |
|----------|----------|-----------------|
| **Microsoft Power Platform** | Deep Microsoft 365 / Azure integration; Power Apps, Power Automate, Power BI | Enterprise workflows; internal tools |
| **Salesforce Platform** | CRM-native; Apex for extensions; Flow Builder | Customer-facing apps; sales workflows |
| **ServiceNow** | IT service management; workflow automation | IT operations; HR; facilities |
| **Appian** | Process mining; case management | Complex business processes; compliance |
| **OutSystems** | Full-stack web and mobile; enterprise-grade | Customer portals; mobile apps |
| **Retool** | Internal tool builder; connects to databases and APIs | Admin panels; dashboards; ops tools |
| **Airtable** | Spreadsheet-database hybrid; automations | Project tracking; lightweight CRM |

### When Low-Code Works Well

| Scenario | Why Low-Code Fits |
|----------|-------------------|
| **Internal tools** | Fast to build; users are internal so UI flexibility matters less |
| **Forms and approvals** | Visual workflow builders excel at this |
| **CRUD applications** | Most low-code platforms are optimised for create-read-update-delete patterns |
| **Prototyping** | Validate an idea in hours instead of weeks |
| **Citizen development** | Business analysts can build their own solutions with IT governance |

### When Low-Code Falls Short

| Limitation | Impact |
|------------|--------|
| **Vendor lock-in** | Applications can't easily be migrated away from the platform |
| **Performance ceilings** | Not suitable for high-throughput or latency-sensitive applications |
| **UI constraints** | Custom designs are difficult; you're limited to what the platform supports |
| **Integration complexity** | Connecting to unusual APIs or legacy systems can require custom code anyway |
| **Cost at scale** | Per-user or per-app pricing can become expensive as usage grows |
| **Debugging difficulty** | Visual abstractions make it hard to diagnose complex issues |

---

## Platform Engineering

### The Problem Platform Engineering Solves

| Without Platform Engineering | With Platform Engineering |
|------------------------------|---------------------------|
| Each team manages their own infrastructure | Self-service platform abstracts infrastructure |
| Inconsistent tooling across teams | Standardised toolchain; golden paths |
| Developers wait for ops to provision resources | Developers provision resources on demand |
| Knowledge silos; tribal knowledge | Documented; automated; discoverable |
| Slow onboarding for new engineers | New engineers can deploy on day one |

### Core Components of an Internal Developer Platform

| Component | Purpose | Example Tools |
|-----------|---------|---------------|
| **Service catalog** | Central registry of all services and their owners | Backstage; Port; Cortex |
| **Templated scaffolding** | Generate new services from approved templates | Backstage software templates; Cookiecutter |
| **Self-service infrastructure** | Developers provision cloud resources without filing tickets | Terraform modules; Pulumi; Crossplane |
| **CI/CD pipelines** | Standardised build, test, deploy pipelines | GitHub Actions; GitLab CI; Argo CD |
| **Environment management** | Ephemeral dev/staging environments on demand | Vcluster; Namespace; Gitpod |
| **Observability** | Logging, metrics, tracing built into every service | Prometheus; Grafana; OpenTelemetry; Datadog |
| **Secret management** | Secure storage and rotation of credentials | Vault; AWS Secrets Manager; SOPS |
| **Identity and access** | SSO; role-based access; service-to-service auth | Okta; Keycloak; SPIFFE |

### Golden Paths

A golden path is the supported, opinionated way to do something. It's the path of least resistance — if you follow it, everything works. You can go off-path, but you're on your own.

| Golden Path | What It Provides |
|-------------|-----------------|
| **New service** | Template repo; CI/CD; monitoring; logging; deployment config |
| **New database** | Provisioned instance; connection strings in secrets; backup configured |
| **New frontend** | Build pipeline; CDN; preview environments; lighthouse checks |
| **Data pipeline** | Orchestration; schema validation; monitoring; alerting |

### Build vs Buy Decisions

| Factor | Build Custom | Use Existing Tool |
|--------|-------------|-------------------|
| **Core competency** | Unique to your business; competitive advantage | Commodity; every company needs it |
| **Maintenance burden** | You have capacity to maintain it | Tool is well-maintained by vendor/community |
| **Integration needs** | Deep integration with internal systems required | Standard APIs and connectors suffice |
| **Cost** | Cheaper to build than license | Cheaper to license than build |

---

## The Relationship Between Low-Code and Platform Engineering

| Dimension | Low-Code | Platform Engineering |
|-----------|----------|---------------------|
| **Target user** | Business users; citizen developers | Professional software engineers |
| **Goal** | Reduce code; increase speed | Reduce cognitive load; increase autonomy |
| **Abstraction level** | Very high; visual | Medium; code-based but simplified |
| **Flexibility** | Limited by platform capabilities | Full flexibility; you can write any code |
| **Governance** | Platform enforces rules | Platform provides golden paths |

They're complementary: platform engineering makes professional developers faster, while low-code enables non-developers to build simple applications. Together, they address the software delivery gap from different angles.

---

## Summary

Low-code platforms and internal developer platforms both aim to increase the number of people who can deliver software. Low-code does this by abstracting away code entirely — visual builders, pre-built connectors, declarative logic. Platform engineering does this for professional developers by providing self-service infrastructure, golden paths, and standardised tooling so they spend less time on ops work and more time on product features. Neither is a silver bullet: low-code has vendor lock-in and performance limitations, and platform engineering requires ongoing investment to maintain. But when applied to the right problems — internal tools, CRUD apps, standardised service delivery — both can dramatically reduce the time from idea to production.
