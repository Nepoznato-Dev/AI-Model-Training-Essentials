<!--
---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [terraform, quick-reference]
difficulty_level: "beginner"
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
# Terraform and Infrastructure as Code

Terraform is the most widely used Infrastructure as Code (IaC) tool — it lets you define cloud infrastructure (servers, databases, networks, permissions) in declarative configuration files that can be versioned, reviewed, tested, and automated. Instead of clicking through a cloud console, you write code that describes the desired state of your infrastructure, and Terraform figures out what changes to make.

---

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Provider** | Plugin that manages a specific cloud platform (AWS, Azure, GCP, etc.) |
| **Resource** | An infrastructure object (server, database, network) |
| **State** | Terraform's record of what infrastructure exists; stored in a state file |
| **Plan** | Preview of what changes Terraform will make |
| **Apply** | Execute the plan; create/update/destroy infrastructure |
| **Module** | Reusable collection of resources |
| **Variable** | Input parameter for configurations |
| **Output** | Value exported from a module or configuration |
| **Data source** | Read information from existing infrastructure |

---

## Basic Workflow

| Step | Command | Description |
|------|---------|-------------|
| **1. Write configuration** | Create `.tf` files | Define providers, resources, variables |
| **2. Initialise** | `terraform init` | Download providers; set up backend |
| **3. Format** | `terraform fmt` | Standardise formatting |
| **4. Validate** | `terraform validate` | Check syntax and configuration |
| **5. Plan** | `terraform plan` | Preview changes (dry run) |
| **6. Apply** | `terraform apply` | Create or update infrastructure |
| **7. Destroy** | `terraform destroy` | Tear down all managed infrastructure |

---

## Common Commands

| Command | Description |
|---------|-------------|
| `terraform init` | Initialise working directory; download providers and modules |
| `terraform plan` | Show what changes will be made |
| `terraform apply` | Apply changes; add `-auto-approve` to skip confirmation |
| `terraform destroy` | Destroy all managed resources |
| `terraform fmt` | Format configuration files to standard style |
| `terraform validate` | Validate configuration syntax |
| `terraform output` | Show output values |
| `terraform state list` | List all resources in state |
| `terraform state show <resource>` | Show details of a specific resource |
| `terraform import <resource> <id>` | Import existing infrastructure into state |
| `terraform taint <resource>` | Mark a resource for recreation on next apply |
| `terraform refresh` | Update state to match real infrastructure |
| `terraform graph` | Generate a visual dependency graph (DOT format) |
| `terraform console` | Interactive console for testing expressions |

---

## State Management

| Best Practice | Description |
|--------------|-------------|
| **Remote state** | Store state in S3, GCS, Azure Blob, or Terraform Cloud — never locally |
| **State locking** | Use DynamoDB (S3 backend) or native locking to prevent concurrent modifications |
| **State encryption** | Enable encryption at rest for state files (they contain sensitive data) |
| **State separation** | Use separate state files for different environments or teams |
| **State backup** | Remote backends automatically version state; keep this enabled |
| **Never edit state manually** | Use `terraform state mv`, `rm`, `import` instead |

---

## Module Structure

```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## Variable Types

| Type | Example | Use Case |
|------|---------|----------|
| **string** | `variable "region" { type = string }` | Single text value |
| **number** | `variable "count" { type = number }` | Numeric value |
| **bool** | `variable "enable" { type = bool }` | True/false flag |
| **list** | `variable "zones" { type = list(string) }` | Ordered collection |
| **map** | `variable "tags" { type = map(string) }` | Key-value pairs |
| **object** | `variable "config" { type = object({...}) }` | Structured configuration |

---

## Common Patterns

| Pattern | Description |
|---------|-------------|
| **Count** | `count = 3` creates multiple instances of a resource |
| **For each** | `for_each = var.items` iterates over a map or set |
| **Dynamic blocks** | Generate repeated nested blocks (e.g., ingress rules) |
| **Local values** | `locals { ... }` for computed values and reducing repetition |
| **Data sources** | Read existing infrastructure (e.g., find an existing VPC) |
| **Provisioners** | Run scripts on resources after creation (use sparingly) |
| **Workspaces** | Separate state for different environments within same config |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **State drift** | Run `terraform plan` to see differences; `terraform apply` to reconcile |
| **Locked state** | Check who has the lock; use `terraform force-unlock` if safe |
| **Provider errors** | Check credentials; update provider version; check API limits |
| **Import conflicts** | Resource already in state; use `terraform state rm` first |
| **Circular dependencies** | Restructure resources; use `depends_on` carefully |
| **Large state** | Split into modules; use `-target` for partial operations |

---

## Summary

Terraform manages infrastructure through declarative configuration files. The workflow is: write configuration → init → plan → apply. State tracks what exists and must be stored remotely with locking. Modules enable reuse. Variables parameterise configurations. The key principles are: treat infrastructure as code (version control; review; test); never edit state manually; plan before apply; use remote state with locking; and structure configurations with modules for maintainability.
