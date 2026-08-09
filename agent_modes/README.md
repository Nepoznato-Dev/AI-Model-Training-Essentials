# Agent Modes

Agent modes are focused configurations for common AI-assisted development workflows. Choose a mode based on the kind of help you need, then hand off to another mode when the task changes.

## Quick Reference

### Core Workflow

| Mode | Best for |
|------|----------|
| [Agent](Agent.md) | Implementing, testing, and improving changes |
| [Plan](Plan.md) | Designing an implementation plan |
| [Explore](Explore.md) | Read-only research and discovery |
| [Ask](Ask.md) | Answering focused questions |
| [Chat](Chat.md) | General conversation and brainstorming |

### Quality & Reliability

| Mode | Best for |
|------|----------|
| [Debug](Debug.md) | Diagnosing and fixing failures |
| [Test](Test.md) | Creating and validating tests |
| [Review](Review.md) | Reviewing code, plans, or architecture |
| [Lint](Lint.md) | Enforcing code formatting and style guides |
| [Performance](Performance.md) | Profiling code and optimizing bottlenecks |

### Security & Operations

| Mode | Best for |
|------|----------|
| [Secure](Secure.md) | Security analysis and secure coding |
| [DevOps](DevOps.md) | CI/CD pipelines, Docker, and deployment configs |
| [Database](Database.md) | Schema design, query optimization, and data integrity |

### Specialized

| Mode | Best for |
|------|----------|
| [Documentation](Documentation.md) | Generating and maintaining technical documentation |
| [Migration](Migration.md) | Code transformations, dependency upgrades, and API migrations |
| [Orchestrator](Orchestrator.md) | Coordinating complex multi-agent tasks |

## Suggested Workflows

- **New feature:** Explore → Plan → Agent → Test → Review
- **Bug report:** Debug → Agent → Test
- **Security concern:** Secure → Agent → Review
- **Performance issue:** Performance → Debug → Agent
- **Database design:** Database → Plan → Agent → Test
- **CI/CD setup:** DevOps → Agent → Test
- **Code quality cleanup:** Lint → Agent → Review
- **Dependency or framework upgrade:** Migration → Agent → Test → Review
- **Documentation sprint:** Documentation → Review
- **Complex multi-part task:** Orchestrator → (delegates to specialized modes)
- **Question or concept:** Ask or Chat

## Categories at a Glance

- **Core Workflow** — The everyday modes for planning, implementing, and exploring.
- **Quality & Reliability** — Modes that verify correctness, catch bugs, and enforce standards.
- **Security & Operations** — Modes focused on hardening, deploying, and managing data.
- **Specialized** — Modes for documentation, large-scale migrations, and multi-agent coordination.

Each mode's file contains its tools, behavioral rules, and available handoffs.
