# Quality & Reliability Agents

## Introduction

This document explains the quality and reliability assurance agents: Debug, Test, Review, Lint, and Performance. It describes their responsibilities, methodologies, tooling integration, and how they fit into automated quality workflows and CI/CD pipelines.

## Overview

The agents form a cohesive quality loop: Lint ensures style and static checks early; Test validates behavior; Review inspects design and code quality; Debug resolves issues; Performance optimizes runtime characteristics.

```mermaid
graph TB
A["agent_modes/Debug.md"] --> B["agent_modes/Test.md"]
A --> C["agent_modes/Review.md"]
D["agent_modes/Lint.md"] --> C
E["agent_modes/Performance.md"] --> C
B --> F["skills/testing-skills/"]
A --> G["skills/behavior-skills/debugging.md"]
C --> H["skills/collaboration-skills/code_review.md"]
D --> I["skills/devops-skills/ci_cd.md"]
E --> I
```

## Debug Agent

### Purpose
Diagnose errors, analyze stack traces and logs, identify root causes, propose evidence-based solutions, and coordinate follow-ups.

### Methodology
Observe → Orient → Hypothesize → Test → Conclude → Recommend → Confirm resolution.

### Tools
Read/search code, execute commands, get terminal output, analyze test failures, fetch GitHub issues/PRs.

### Workflow

```mermaid
flowchart TD
Start(["Receive Issue"]) --> Gather["Gather Evidence<br/>Errors, Logs, Terminal Output"]
Gather --> Reproduce{"Can Reproduce?"}
Reproduce --> |No| AskUser["Request Steps/Environment"]
Reproduce --> |Yes| Trace["Trace Execution Path"]
Trace --> Hypothesize["Form Hypotheses"]
Hypothesize --> TestHypo["Run Targeted Tests"]
TestHypo --> RootCause{"Root Cause Confirmed?"}
RootCause --> |No| Iterate["Refine Hypothesis"]
Iterate --> TestHypo
RootCause --> |Yes| Recommend["Propose Fix + Prevention"]
Recommend --> HandoffFix["Handoff to Agent"]
HandoffFix --> HandoffTest["Handoff to Test"]
HandoffTest --> Verify["Verify Resolution"]
Verify --> End(["Close"])
```

### Handoffs
- Fix bug → Agent
- Write regression tests → Test

## Test Agent

### Purpose
Ensure correctness through comprehensive, maintainable tests across the test pyramid.

### Framework Awareness
Adapts to project conventions (Jest, pytest, JUnit, etc.).

### Practices
Clear naming, focused assertions, deterministic tests, robust setup/teardown, coverage reporting, flaky test management.

### Workflow

```mermaid
sequenceDiagram
participant Dev as "Developer"
participant Test as "Test Agent"
participant Runner as "Test Runner"
participant CI as "CI/CD"
Dev->>Test : "Write tests for feature/module"
Test->>Runner : "Execute suite"
Runner-->>Test : "Results + Coverage"
alt Failures
Test->>Test : "Analyze failure"
Test-->>Dev : "Recommend fix or debug"
else Pass
Test-->>CI : "Report pass + coverage"
end
```

### Handoffs
- Fix failing tests → Agent
- Debug test failures → Debug

## Review Agent

### Purpose
Evaluate code/design/plans across multiple dimensions without making changes; classify findings by severity; provide actionable recommendations.

### Dimensions
Correctness, reliability, security, performance, maintainability, testability, architecture, extensibility.

### Workflow

```mermaid
flowchart TD
S["Start Review"] --> Scope["Clarify Scope & Focus"]
Scope --> Inspect["Read Code/Design/Tests"]
Inspect --> Analyze["Evaluate Across Dimensions"]
Analyze --> Classify["Classify Severity"]
Classify --> Report["Deliver Structured Report"]
Report --> Handoff{"Changes Needed?"}
Handoff --> |Yes| Fix["Handoff to Agent"]
Handoff --> |No| Approve["Approve"]
Fix --> ReReview["Optional Re-review"]
```

### Handoffs
- Fix issues → Agent
- Re-review → Review

## Lint Agent

### Purpose
Enforce formatting, style guides, naming conventions, and manage linter configuration; automate safe fixes; integrate with pre-commit and CI.

### Capabilities
Configure ESLint/Pylint/Stylelint/etc., set formatters, define `.editorconfig`, run auto-fixes safely, enforce quality gates in PRs.

### Progressive Strategy
Start with basics → add core rules → introduce project-specific rules → continuously improve.

### Workflow

```mermaid
flowchart TD
Init["Assess Current State"] --> Configure["Configure Linters/Formatters"]
Configure --> AutoFix["Auto-Fix Safe Issues"]
AutoFix --> PreCommit["Set Up Pre-Commit Hooks"]
PreCommit --> CI["Integrate Linting in CI"]
CI --> Gate["Quality Gates on PRs"]
Gate --> Maintain["Maintain & Improve Rules"]
```

### Handoffs
- Review code quality → Review
- Test after linting → Test

## Performance Agent

### Purpose
Measure performance, identify bottlenecks, recommend targeted optimizations, establish baselines/budgets, and verify improvements.

### Profiling Areas
CPU hot paths, memory leaks, I/O latency, concurrency issues.

### Methodology
Define problem → measure baseline → identify bottleneck → recommend fixes → implement (via Agent) → verify with repeatable measurements.

### Workflow

```mermaid
sequenceDiagram
participant Dev as "Developer"
participant Perf as "Performance Agent"
participant Profiler as "Profiler"
participant Impl as "Agent"
Dev->>Perf : "Optimize performance"
Perf->>Profiler : "Profile CPU/Memory/I/O"
Profiler-->>Perf : "Metrics + Hotspots"
Perf->>Perf : "Analyze Bottlenecks"
Perf-->>Dev : "Recommendations + Baseline"
Dev->>Impl : "Implement optimizations"
Impl-->>Perf : "Re-profile to verify"
Perf-->>Dev : "Report improvements"
```

### Handoffs
- Optimize code → Agent
- Review optimizations → Review
- Write performance tests → Test

## CI/CD Integration

```mermaid
sequenceDiagram
participant Dev as "Developer"
participant Lint as "Lint Agent"
participant Test as "Test Agent"
participant Review as "Review Agent"
participant Debug as "Debug Agent"
participant CI as "CI/CD Pipeline"
Dev->>CI : Push/Pull Request
CI->>Lint : Run lint/format checks
Lint-->>CI : Pass/Fail
CI->>Test : Execute tests
Test-->>CI : Results + Coverage
CI->>Review : Trigger review
Review-->>CI : Findings by severity
alt Issues found
CI->>Debug : Investigate failures
Debug-->>CI : Root cause + fix
else No issues
CI-->>Dev : Approve/Merge
end
```

### Typical CI/CD Stages
1. Lint → Build → Unit Tests → Integration Tests → Security Scan → Package → Deploy Staging → E2E Tests → Deploy Production → Smoke Test

### Patterns
- Lint first for fast feedback
- Cache dependencies
- Parallelize tests
- Build once deploy many
- Gate checks before production

## Performance Considerations

- Keep test suites fast and deterministic; prefer unit tests for speed and reliability
- Cache dependencies in CI to reduce pipeline time
- Use parallel jobs where possible to shorten feedback loops
- Establish performance baselines and budgets; monitor regressions
- Avoid premature optimization; measure before changing code

## Troubleshooting

- **Debug Agent**: Use structured methodology to isolate symptoms vs. root causes; leverage terminal output and test failure analysis
- **Test Agent**: Manage flaky tests by isolating timing/order dependencies; quarantine unstable tests until fixed
- **Review Agent**: Provide severity-classified findings with specific locations and actionable recommendations
- **Lint Agent**: Start with essential rules; batch auto-fixes; enforce via pre-commit and CI
- **Performance Agent**: Compare before/after metrics; confirm no regressions; set up ongoing monitoring

## Related Resources

- [Agent Modes System](agent_modes_system.md) - Overview of all 16 agents
- [Core Workflow Agents](core_workflow_agents.md) - Agent, Plan, Explore, Ask, Chat
- [Skills Library](../skills/skills_library.md) - Reusable capabilities for agents
