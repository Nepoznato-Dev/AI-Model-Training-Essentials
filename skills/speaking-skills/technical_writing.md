---
# Metadata
title: "Technical Writing"
description: "Communicating complex technical information clearly and precisely through structured written documents, guides, and documentation."
category: "Speaking Skills"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2026-08-10"
reviewed_by: "Speaking Skills Team"
next_review: "2027-02-10"

# Classification
tags: [technical-writing, documentation, api-docs, style-guide, readability, communication]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Technical Writing

The practice of communicating complex technical information clearly, precisely, and accessibly through structured written documents.

## Overview

Technical writing transforms expert knowledge into documentation that others can act on. Unlike general writing, technical writing is judged not by its eloquence but by whether the reader can accomplish a task, understand a system, or make a decision after reading it.

In software engineering, technical writing takes many forms: API documentation, architecture decision records, README files, runbooks, post-mortems, design documents, and user guides. Each form has different conventions, but all share the same goal: reduce the gap between what the writer knows and what the reader needs to do.

Poor technical writing costs real money. Developers spend an estimated 25% of their time looking for information or working around unclear documentation. A well-written document pays for itself within days by reducing questions, errors, and onboarding time.

This skill covers the principles, structures, and editing techniques that make technical writing effective — regardless of the specific document type or audience.

## Core Competencies

- Structuring technical documents so readers can find information quickly and understand it on first read
- Writing for different audiences (developers, managers, end users) without sacrificing accuracy
- Explaining complex systems using progressive disclosure — simple first, details on demand
- Creating effective code examples, diagrams, and tables that complement prose
- Editing ruthlessly for clarity, removing ambiguity and unnecessary words
- Maintaining consistent style, terminology, and formatting across documents
- Writing document types: READMEs, API docs, ADRs, runbooks, tutorials, and post-mortems

## When to Use

- Writing or updating README files, guides, or documentation for a project
- Documenting an API, library, or SDK for external or internal consumers
- Creating architecture decision records (ADRs) for team reference
- Writing runbooks or operational procedures for production systems
- Communicating technical findings in post-mortems or incident reports
- Onboarding new team members with setup guides or knowledge transfer docs
- Writing proposals, RFCs, or design documents for technical review

## Framework/Methodology

### Phase 1: Audience & Purpose

Before writing anything, answer two questions:

1. **Who will read this?** — Expert developer? New hire? Non-technical manager? Each audience needs different depth, terminology, and pacing.
2. **What should the reader be able to DO after reading?** — If you cannot state the purpose in one sentence, the document lacks focus.

| Audience | Needs | Avoid |
|----------|-------|-------|
| Expert developers | Precise technical detail, edge cases, performance notes | Over-explanation of basics |
| New team members | Context, rationale, step-by-step instructions | Jargon without definitions |
| Technical managers | Impact, trade-offs, timeline, risks | Implementation minutiae |
| End users | Task-oriented instructions, screenshots | Internal architecture details |

### Phase 2: Structure

Technical documents follow predictable structures. Use the right one:

**Task-oriented (tutorial, how-to guide):**
1. What you'll accomplish (one sentence)
2. Prerequisites
3. Step-by-step instructions (numbered)
4. Expected outcome
5. Troubleshooting (common issues)

**Reference (API docs, config reference):**
1. One-paragraph overview
2. Parameters / endpoints in a consistent table format
3. Examples for each parameter or endpoint
4. Error codes and their meanings

**Decision record (ADR, design doc):**
1. Context — what situation prompted this decision
2. Decision — what was decided (one paragraph)
3. Consequences — what becomes easier and harder as a result
4. Alternatives considered — why they were rejected

**Explanation (concept doc, architecture overview):**
1. What this is and why it exists
2. How it works (with diagram)
3. Key design decisions and trade-offs
4. Related concepts and systems

### Phase 3: Writing Principles

Apply these principles to every sentence:

1. **One idea per sentence.** If a sentence has two clauses joined by "and" or "which," split it.
2. **Use active voice.** "The function processes the input" not "The input is processed by the function."
3. **Be specific.** "The API returns a 404 error" not "The API may return an error."
4. **Define terms on first use.** If the reader needs to know what "idempotent" means, define it inline.
5. **Use concrete examples.** A single example is worth three paragraphs of abstract explanation.
6. **Front-load important information.** Put the conclusion or key fact first, supporting detail second.
7. **Use formatting as navigation.** Headers, bullet lists, tables, and code blocks let readers scan and find what they need.

### Phase 4: Code Examples

Good code examples are the backbone of technical writing:

- **Minimal** — Show only the relevant code. Omit boilerplate unless it's part of the lesson.
- **Runnable** — The reader should be able to copy, paste, and execute without modification.
- **Annotated** — Add comments only where the code is non-obvious. Don't comment the obvious.
- **Progressive** — Start with the simplest case, then add complexity in subsequent examples.
- **Tested** — Every code example should be verified working. Stale examples are worse than no examples.

### Phase 5: Editing

The first draft is never the final document. Edit in three passes:

1. **Structure pass** — Does the document flow logically? Can the reader find what they need? Move sections if needed.
2. **Clarity pass** — Read each sentence. Can it be misunderstood? Is any word unnecessary? Cut ruthlessly.
3. **Consistency pass** — Are terms used the same way throughout? Is formatting consistent? Do all links work?

## Practical Templates

### Template 1: README Structure

```markdown
# Project Name

One-sentence description of what this project does and why it exists.

## Quick Start

\`\`\`bash
# Install
pip install project-name

# Run
python -m project_name --input data.csv
\`\`\`

## Features

- Feature 1: what it does
- Feature 2: what it does

## Usage

### Basic Usage
[Short explanation + minimal code example]

### Advanced Usage
[Progressively more complex example]

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--input` | required | Path to input CSV file |
| `--output` | `./out` | Directory for output files |

## Architecture

[Brief explanation of how it works, with diagram if helpful]

## Contributing

[How to contribute, development setup]

## License

[License type]
```

### Template 2: Architecture Decision Record (ADR)

```markdown
# ADR-0042: Use PostgreSQL Instead of MongoDB for User Data

## Status
Accepted | Proposed | Deprecated | Superseded by ADR-XXX

## Context
We need to store user profiles with complex relational queries (team membership,
role hierarchies, audit logs). The team has SQL experience. The data has strong
consistency requirements for authentication flows.

## Decision
Use PostgreSQL 15 as the primary database for user data.

## Consequences

### Positive
- Strong consistency for auth flows (ACID transactions)
- Team already has SQL expertise
- Mature ecosystem (ORMs, migration tools, monitoring)
- Complex joins for team/role queries are natural in SQL

### Negative
- Less flexible schema if user profile fields change frequently
- Horizontal scaling requires more planning than MongoDB

## Alternatives Considered

### MongoDB
Rejected because: eventual consistency conflicts with auth requirements;
team would need to learn document modeling for relational data.

### DynamoDB
Rejected because: overkill for current scale; team has no DynamoDB experience;
cost model less predictable at our usage pattern.
```

### Template 3: Runbook Entry

```markdown
# Runbook: High CPU Alert on Inference Server

## Trigger
CloudWatch alarm: `inference-server-cpu > 85% for 5 minutes`

## Severity
P2 — Service degraded, not down

## Immediate Actions
1. Check current load:
   \`\`\`bash
   kubectl top pods -n ml-serving -l app=inference-server
   \`\`\`
2. Check recent deployments (may have introduced a regression):
   \`\`\`bash
   kubectl rollout history deployment/inference-server -n ml-serving
   \`\`\`
3. If a recent deploy caused this, roll back:
   \`\`\`bash
   kubectl rollout undo deployment/inference-server -n ml-serving
   \`\`\`

## Investigation
- Check request rate: [Grafana dashboard link]
- Check model size (larger models use more CPU per request)
- Check for stuck requests in the queue

## Escalation
If CPU stays above 90% after rollback: page the ML Platform team.

## Post-Incident
File an incident report within 24 hours. Link to the post-mortem template.
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Writing for yourself, not the reader | Document assumes knowledge the reader doesn't have | State the audience and their prerequisites before writing |
| No clear purpose | Reader finishes the document without knowing what to do | Write the purpose as the first sentence; cut everything that doesn't serve it |
| Wall of text | Readers skip or skim, missing critical information | Use headers, lists, tables, and code blocks to break up prose |
| Untested code examples | Examples don't work, destroying trust | Test every example; add a "last verified" date |
| Inconsistent terminology | Reader wonders if "model endpoint" and "model server" are different things | Define terms once and use them consistently; create a glossary if needed |
| Skipping the editing pass | First drafts are always unclear in places | Schedule a dedicated editing pass; read the document aloud to catch awkward phrasing |

## Best Practices

1. **Start with the hardest question the reader will have** and answer it early. If you don't, they'll be distracted looking for the answer while reading everything else.
2. **Use diagrams for anything spatial or relational.** Architecture, data flow, and state machines are almost always clearer as diagrams than as prose.
3. **Write the title last.** The title should summarize the document's content, which you only fully understand after writing it.
4. **Link to sources of truth, don't duplicate.** If deployment instructions live in the deployment repo, link there. Duplicated docs drift and become wrong.
5. **Add a "last updated" date.** Readers need to know whether the document reflects the current state of the system.
6. **Test your document on a newcomer.** Hand it to someone unfamiliar with the topic. Where they get stuck is where you need to rewrite.
7. **Prefer short documents over long ones.** Two focused documents are better than one sprawling document. Readers prefer to search and find a precise answer.

## Tools & Resources

- [Diátaxis Framework](https://diataxis.fr/) - Systematic framework for technical documentation (tutorials, how-to, reference, explanation)
- [Google Developer Documentation Style Guide](https://developers.google.com/style) - Comprehensive style guide for technical writing
- [Write the Docs](https://www.writethedocs.org/) - Community and resources for documentation practitioners
- [Vale](https://vale-ls.github.io/vale-ls/) - Linter for prose style; enforces consistency in technical documents
- [Mermaid](https://mermaid.js.org/) - Diagram-as-code tool that renders in most Markdown viewers
- [The Documentation System](https://documentation.divio.com/) - Practical guide to documentation types and strategy

## Example Application

**Scenario**: A senior engineer writes a 3,000-word design document for a new caching layer. The team reads it and has 15 questions. The engineer is frustrated because "it's all in there."

**Application**:

1. *Diagnosis* — The document mixed three concerns: the problem statement, the technical design, and the implementation plan. Readers had to read all 3,000 words to find the specific part relevant to their question.

2. *Restructure* — The document is split into three:
   - A one-paragraph ADR stating the decision and rationale (for managers and architects)
   - A technical design doc with diagrams and API contracts (for engineers implementing it)
   - A rollout plan with timeline, migration steps, and rollback procedure (for the ops team)

3. *Add navigation* — Each document gets a clear table of contents, a "TL;DR" section at the top, and cross-links to the other two documents.

4. *Edit for clarity* — Sentences like "The caching layer, which leverages a distributed hash topology (see Appendix C for details), may in certain edge cases exhibit stale reads" become "The cache may return stale data for up to 30 seconds after a write. See [Consistency Model](#consistency-model) for details."

5. *Validate* — The restructured documents are reviewed by one person from each audience (manager, implementer, ops). Each confirms they can find what they need within two minutes.

**Outcome**: The 15 questions reduce to 3 (all about edge cases that were genuinely ambiguous). The team starts implementation two days earlier because everyone understands their part. The ADR is referenced in future decisions, demonstrating its long-term value.

## Success Indicators

You know you've mastered technical writing when:

- Readers can accomplish their goal after reading your document without asking follow-up questions
- Your documents are referenced by teammates months later as sources of truth
- You can write the same content appropriately for three different audiences (expert, newcomer, manager)
- Your code examples are tested and consistently working
- You edit your own first drafts ruthlessly, cutting 30%+ of the words without losing meaning
- Your documents have a clear "last updated" date and you maintain them as the system changes
- New team members onboard using your documentation and tell you it was genuinely helpful

## Related Skills

- [Writing](../behavior-skills/writing.md) - General writing fundamentals complement technical writing specifics
- [Explanation](../behavior-skills/explanation.md) - Explaining concepts clearly is the core of technical writing
- [Teaching](../behavior-skills/teaching.md) - Teaching principles apply directly to tutorial and guide writing
- [Technical Presentation](technical_presentation.md) - Same content, different medium; skills reinforce each other
