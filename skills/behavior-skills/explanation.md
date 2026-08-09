---
# Metadata
title: "Explanation"
description: "Communicate complex technical concepts clearly and effectively"
category: "Behavior Skills"
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
reviewed_by: "Behavior Skills Team"
next_review: "2027-01-15"

# Classification
tags:
  - explanation
  - communication
  - clarity
  - teaching
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Explanation Skill

## Overview

Communicate complex technical concepts clearly and effectively. This skill helps you break down complicated ideas into understandable pieces for different audiences.

## Core Competencies

- **Audience Analysis**: Assess technical background and tailor explanations to the listener's level
- **Structured Communication**: Use pyramid principle, problem-solution-benefit, and what-why-how frameworks
- **Analogy Construction**: Connect abstract concepts to familiar real-world examples
- **Visual Aiding**: Create diagrams, code annotations, and tables to clarify complex ideas
- **Comprehension Checking**: Verify understanding through open-ended questions and observational cues

## When to Use

- Teaching someone a new concept
- Documenting code or systems
- Presenting technical decisions to stakeholders
- Writing commit messages or pull request descriptions
- Answering questions in code reviews
- Creating onboarding materials

## The Explanation Framework

### Step 1: Know Your Audience

**Assess their background:**
- What do they already know?
- What terminology is familiar to them?
- What's their goal in understanding this?

**Audience Types:**

| Audience | Focus On | Avoid |
|----------|----------|-------|
| **Executives** | Business impact, ROI, risks | Technical jargon, implementation details |
| **Product Managers** | User value, trade-offs, timelines | Deep code details, algorithmic complexity |
| **Developers** | Implementation, patterns, edge cases | Oversimplification, hand-waving |
| **New Team Members** | Context, conventions, gotchas | Assumptions about prior knowledge |
| **Non-technical Stakeholders** | Analogies, outcomes, visual aids | Any jargon without explanation |

### Step 2: Structure Your Explanation

**The Pyramid Principle:**
Start with the main point, then support it with details.

```
Main Point (Conclusion First)
├── Supporting Argument 1
│   └── Evidence/Example
├── Supporting Argument 2
│   └── Evidence/Example
└── Supporting Argument 3
    └── Evidence/Example
```

**Alternative Structures:**

#### Problem → Solution → Benefit
1. What problem are we solving?
2. How does this solution work?
3. What benefits does it provide?

#### What → Why → How
1. **What** is it?
2. **Why** does it matter?
3. **How** does it work?

#### Context → Action → Result
1. **Context:** Situation before
2. **Action:** What was done
3. **Result:** Outcome after

### Step 3: Use Clear Language

**Principles:**

1. **Simple over complex:** Use simpler words when possible
   - ❌ "Utilize" → ✅ "Use"
   - ❌ "Facilitate" → ✅ "Help"
   - ❌ "Implement" → ✅ "Build"

2. **Active voice:** Make sentences direct and clear
   - ❌ "The code was written by the team" → ✅ "The team wrote the code"

3. **Concrete over abstract:** Use specific examples
   - ❌ "Improved performance" → ✅ "Reduced load time from 3s to 200ms"

4. **Define jargon:** Explain technical terms on first use
   - "We use caching (storing frequently-used data for quick access) to..."

### Step 4: Add Examples and Analogies

**Examples make abstract concepts concrete:**

```python
# Abstract: "We implement lazy loading"
# Concrete: "Images only load when they scroll into view, 
#            like how a vending machine only dispenses 
#            the item you select, not everything inside"
```

**Good analogies:**
- Connect to something familiar
- Highlight the key mechanism
- Acknowledge where the analogy breaks down

**Example:**
```
"A database index is like a book's index:
- Without it: You read every page to find a topic (full table scan)
- With it: You look up the page number directly (indexed lookup)
- Limitation: Indexes speed up reads but slow down writes 
  (like how adding entries to a book's index takes extra work)"
```

### Step 5: Visual Aids

**When to use visuals:**
- Showing relationships between components
- Explaining flows or processes
- Comparing before/after states
- Illustrating data structures

**Types of visuals:**
- Diagrams (architecture, flow charts)
- Code snippets with annotations
- Tables comparing options
- ASCII art for quick illustrations

```
Request Flow:

User → Load Balancer → API Server → Database
         │                │
         │                └→ Cache Layer
         │
         └→ CDN (static assets)
```

## Explanation Patterns

### The Feynman Technique

1. Choose a concept
2. Explain it as if teaching a beginner
3. Identify gaps in your explanation
4. Review and simplify

### ELI5 (Explain Like I'm 5)

Break down to fundamental concepts:
- What problem does this solve?
- How would you explain it without any technical terms?
- What real-world thing is it most like?

### Compare and Contrast

When explaining something new, compare it to something similar:

```
"GraphQL vs REST:
- REST: Like ordering from a fixed menu (pre-defined endpoints)
- GraphQL: Like ordering from a buffet (request exactly what you want)
- REST may over-fetch or under-fetch data
- GraphQL lets you specify exact data needs"
```

## Common Explanation Scenarios

### Explaining Code Changes

```markdown
## What Changed
Refactored user authentication to use JWT tokens instead of sessions.

## Why
- Sessions required server-side storage, limiting horizontal scaling
- JWT tokens are stateless, enabling easier scaling
- Better support for mobile and third-party clients

## How It Works
1. User logs in with credentials
2. Server validates and returns a signed JWT
3. Client includes JWT in Authorization header
4. Server verifies token signature on each request

## Migration
Existing sessions remain valid for 24 hours. No user action required.
```

### Explaining Technical Debt

```markdown
## Current Situation
Our payment processing code has grown to 800 lines in a single function.

## The Problem
- Hard to test individual scenarios
- Any change risks breaking unrelated payment methods
- New team members take weeks to understand the flow

## Proposed Solution
Break into smaller functions organized by payment method:
- `processCreditCard()`
- `processPayPal()`
- `processBankTransfer()`

## Trade-offs
- Takes 2-3 days to refactor
- Requires careful testing to avoid regressions
- Long-term: faster development, fewer bugs
```

### Explaining Architecture Decisions

```markdown
## Decision: Use PostgreSQL over MongoDB

## Context
We need a database for our e-commerce platform with:
- Complex transactions (orders, inventory, payments)
- Relational data (users, orders, products)
- Strong consistency requirements

## Options Considered

### PostgreSQL (Chosen)
✅ ACID transactions
✅ Complex joins
✅ Mature ecosystem
❌ Less flexible schema

### MongoDB
✅ Flexible schema
✅ Easy horizontal scaling
❌ Multi-document transactions are newer
❌ Joins require application-level handling

## Conclusion
PostgreSQL's strong consistency and transaction support 
better match our requirements for financial data.
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Curse of knowledge | Listeners can't follow your explanation | Assume less context, ask about their level |
| Jargon dumping | Audience feels lost or excluded | Define technical terms on first use |
| Wall of text | Key points get buried in prose | Use headers, bullets, and visual breaks |
| Solution before why | Audience doesn't understand the motivation | Always explain WHY before HOW |
| No examples | Abstract explanation fails to land | Include at least one concrete example |

## Best Practices

1. **Start with the main point**: Use the pyramid principle — conclusion first, then supporting details
2. **Use the Feynman Technique**: Explain as if teaching a beginner; gaps reveal your own blind spots
3. **One idea per paragraph**: Avoid nesting multiple concepts in a single explanation
4. **Concrete over abstract**: "Reduced load time from 3s to 200ms" beats "improved performance"
5. **Check understanding early**: Ask "Does this make sense?" and watch for confused signals
6. **Adapt to your audience**: Use the audience table to calibrate detail level and terminology

## Tools & Resources

- **Excalidraw/diagrams.net** - Create clear architecture and flow diagrams
- **The Pyramid Principle** by Barbara Minto - Structured communication framework
- **Markdown** - Write well-structured documentation with headers, lists, and code blocks
- **Loom/Screen recording** - Create video explanations with visual walkthroughs
- **Mermaid.js** - Generate diagrams from text descriptions in documentation

## Example Application

**Scenario:** Explaining a database migration decision to mixed audience (executives + engineers)

**Application:**
1. **Audience Analysis**: Executives need business impact; engineers need technical rationale
2. **Structure**: Pyramid principle — conclusion first ("We chose PostgreSQL over MongoDB")
3. **For Executives**: "PostgreSQL's ACID transactions protect financial data, reducing risk of data corruption"
4. **For Engineers**: Comparison table with join support, consistency guarantees, and ecosystem maturity
5. **Visual Aid**: Architecture diagram showing data flow with PostgreSQL at the center

**Outcome**: Both audiences understood the decision. Executives approved the budget; engineers had clear implementation guidance. No follow-up meetings needed.

## Success Indicators

You've mastered explanation when you can:

- ✅ Explain any technical concept to a non-technical audience in under 2 minutes
- ✅ Write documentation that reduces onboarding time for new team members
- ✅ Adapt the same explanation for different audience levels on the fly
- ✅ Use effective analogies that make abstract concepts click
- ✅ Receive feedback like "that's the clearest explanation I've heard"

## Related Skills

- [Teaching](teaching.md) - Guided instruction and skill development
- [Summarization](summarization.md) - Condensing information to key points
- [Pair Programming](../collaboration-skills/pair_programming.md) - Real-time code explanation

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Behavior Skills Team
next_review: 2026-07-15
---
