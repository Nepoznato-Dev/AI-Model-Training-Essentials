---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
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
tags: [devops, cicd, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# DevOps and CI/CD

DevOps is the combination of cultural philosophy, practices, and tools that enables teams to deliver software faster and more reliably. It breaks down the wall between developers (who want to ship changes) and operations (who want stability). CI/CD — Continuous Integration and Continuous Delivery — is the automation backbone that makes it possible.

---

## CI/CD Pipelines

### What CI/CD Actually Means

| Term | What It Does |
|------|-------------|
| **Continuous Integration (CI)** | Developers merge code frequently; each merge triggers automated builds and tests |
| **Continuous Delivery (CD)** | Code is always in a deployable state; releasing to production is a manual decision |
| **Continuous Deployment** | Every change that passes tests goes to production automatically — no manual gate |

### Typical Pipeline Stages

| Stage | What Happens | Tools |
|-------|-------------|-------|
| **Source** | Developer pushes code to Git | GitHub, GitLab, Bitbucket |
| **Build** | Compile code, install dependencies | Maven, Gradle, npm, pip |
| **Test** | Run unit, integration, lint checks | Jest, pytest, JUnit |
| **Package** | Build Docker image or artifact | Docker, Buildpacks |
| **Deploy (staging)** | Deploy to staging environment | Kubernetes, ECS, VM |
| **Test (staging)** | Integration tests, smoke tests | Selenium, Postman |
| **Deploy (production)** | Release to production | Blue-green, canary, rolling |
| **Monitor** | Observe health, errors, performance | Prometheus, Grafana, Datadog |

### CI/CD Tools Compared

| Tool | Type | Strength |
|------|------|----------|
| **GitHub Actions** | Cloud CI/CD | Deeply integrated with GitHub; YAML workflows |
| **GitLab CI** | Built-in CI/CD | Single platform for repo + pipeline |
| **Jenkins** | Self-hosted CI/CD | Highly configurable; massive plugin ecosystem |
| **CircleCI** | Cloud CI/CD | Fast; good for containerised workflows |
| **ArgoCD** | GitOps for Kubernetes | Declarative, Git-driven deployments |

---

## Docker and Containers

### Why Containers?

Before containers, the classic problem was "it works on my machine." Containers solve this by packaging an application with all its dependencies — libraries, runtime, config — into a single, portable unit that runs identically anywhere.

### Docker Essentials

| Concept | Description |
|---------|-------------|
| **Image** | Read-only template with app + dependencies |
| **Container** | Running instance of an image |
| **Dockerfile** | Recipe for building an image |
| **Registry** | Storage for images (Docker Hub, ECR, GCR) |
| **Volume** | Persistent storage that survives container restarts |
| **Network** | Isolated networking layer for containers |

### Dockerfile Best Practices

```dockerfile
# Use specific base image tags, not 'latest'
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run as non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 8000
CMD ["python", "main.py"]
```

Key practices: use slim/alpine base images, run as non-root, leverage layer caching, use `.dockerignore`, scan images for vulnerabilities (`trivy`, `docker scan`), and set resource limits.

### Docker Compose

For running multiple containers together (app + database + cache):

```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db, redis]
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

---

## Kubernetes (K8s)

Kubernetes is the industry-standard container orchestrator. It manages the deployment, scaling, and operation of containerised applications.

### Core Architecture

| Component | Role |
|-----------|------|
| **Control Plane** | Manages the cluster (API server, scheduler, etcd, controller manager) |
| **Node** | Worker machine (VM or physical) that runs containers |
| **Pod** | Smallest deployable unit; one or more containers that share networking |
| **Service** | Stable network endpoint that routes traffic to pods |
| **Deployment** | Declarative definition of desired pod state (replicas, image, etc.) |
| **Ingress** | HTTP routing rules for external traffic |
| **ConfigMap / Secret** | Configuration and sensitive data injected into pods |

### Essential kubectl Commands

```bash
kubectl get pods                    # List pods
kubectl get services                # List services
kubectl describe pod <name>         # Detailed pod info
kubectl logs <pod-name>             # View pod logs
kubectl exec -it <pod> -- /bin/sh   # Shell into a pod
kubectl apply -f deployment.yaml    # Apply a manifest
kubectl rollout status deploy/myapp # Check rollout progress
kubectl scale deploy/myapp --replicas=5  # Scale to 5 replicas
```

### Helm

Helm is the package manager for Kubernetes. A **chart** is a bundle of pre-configured Kubernetes resources. Think of it as `apt` or `brew` for K8s.

```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Infrastructure as Code (IaC)

IaC treats infrastructure configuration the same way you treat application code: version-controlled, tested, and deployed through pipelines.

### Terraform vs Ansible

| Tool | Type | Approach | Best For |
|------|------|----------|----------|
| **Terraform** | Provisioning | Declarative (HCL); state-based | Creating cloud resources (VPCs, VMs, databases) |
| **Ansible** | Configuration | Declarative (YAML); agentless | Configuring servers, installing software |
| **Pulumi** | Provisioning | Imperative (Python, Go, TS) | Teams that prefer real programming languages |
| **CloudFormation** | Provisioning | Declarative (YAML/JSON); AWS-native | AWS-only infrastructure |

### Terraform Example

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

Best practices: use modules for reusability, store state remotely (S3 + DynamoDB for locking), never hardcode secrets, and version-control everything.

---

## Monitoring and Observability

### The Three Pillars

| Pillar | What It Tells You | Tools |
|--------|------------------|-------|
| **Metrics** | Numerical measurements over time (CPU, request rate, error rate) | Prometheus, CloudWatch, Datadog |
| **Logs** | Discrete events with context (errors, requests, state changes) | ELK Stack, Loki, CloudWatch Logs |
| **Traces** | End-to-end request journey across services | Jaeger, X-Ray, Zipkin |

### Prometheus + Grafana Stack

The standard open-source monitoring stack:

| Component | Role |
|-----------|------|
| **Prometheus** | Time-series database; pulls metrics from services |
| **Grafana** | Visualisation and dashboards |
| **Alertmanager** | Routes alerts to Slack, PagerDuty, email |
| **Node Exporter** | Exposes system-level metrics (CPU, RAM, disk) |
| **Blackbox Exporter** | Probes endpoints (HTTP, TCP, ICMP) |

### Key Metrics to Track

| Category | Metrics |
|----------|---------|
| **Infrastructure** | CPU, RAM, disk usage, network I/O |
| **Application** | Request rate, latency (p50, p95, p99), error rate |
| **Database** | Query count, slow queries, connection pool usage |
| **Business** | Signups, conversions, revenue |

---

## Deployment Strategies

| Strategy | How It Works | Risk | Rollback |
|----------|-------------|------|----------|
| **Rolling Update** | Replace old instances with new ones gradually | Some users on old, some on new version | Revert to previous image |
| **Blue-Green** | Run two identical environments; switch traffic | Double infrastructure cost during transition | Instant switch back |
| **Canary** | Route small % of traffic to new version; increase gradually | Complex traffic management | Route traffic back to stable |
| **Feature Flags** | Deploy code but hide features behind toggles | Code complexity from conditional logic | Toggle off |

---

## GitOps

GitOps takes IaC to its logical conclusion: the Git repository is the single source of truth for the desired state of your infrastructure and applications.

| Principle | Description |
|-----------|-------------|
| **Declarative** | Everything described as code (YAML, HCL) |
| **Versioned** | Git is the source of truth |
| **Automated** | Tools continuously reconcile desired state with actual state |
| **Auditable** | Every change is a Git commit |

**ArgoCD** and **Flux** are the leading GitOps tools for Kubernetes. You push a change to your Git repo, and the tool automatically deploys it to the cluster.

---

## Incident Response

When something breaks at 3 AM:

1. **Acknowledge** the alert.
2. **Assess scope**: which services, users, and data are affected?
3. **Identify** the root cause — check logs, metrics, recent deployments.
4. **Contain** if possible — circuit breakers, feature flags, traffic shifting.
5. **Fix** — rollback or patch forward.
6. **Communicate** — update stakeholders and users (status page).
7. **Post-mortem** — within 24–48 hours, document root cause and action items.

The objective is not only to resolve the incident but to ensure the same incident cannot recur.
