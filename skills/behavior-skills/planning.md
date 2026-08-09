---
# Metadata
title: "Planning"
description: "Break down complex tasks into manageable, actionable steps"
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
  - planning
  - project-management
  - strategy
  - organization
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "15 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Planning Skill

## Overview

Break down complex tasks into manageable, actionable steps. This skill helps you create clear plans that guide execution from start to finish.

## Core Competencies

- **SMART Goal Definition**: Set Specific, Measurable, Achievable, Relevant, and Time-bound objectives
- **Task Decomposition**: Break complex projects into actionable items using WBS and user story mapping
- **Prioritization**: Apply MoSCoW and value-vs-effort frameworks to focus on what matters most
- **Estimation**: Use three-point estimation and planning poker for realistic timelines
- **Progress Tracking**: Monitor execution with Kanban boards, burn-down charts, and adaptation triggers

## When to Use

- Starting a new project or feature
- Facing a large, ambiguous task
- Needing to estimate time or resources
- Coordinating work with others
- Tracking progress on complex initiatives

## The Planning Framework

### Step 1: Define the Goal

**Goal:** Clearly articulate what success looks like.

**SMART Criteria:**
- **S**pecific: Clear and unambiguous
- **M**easurable: Quantifiable outcomes
- **A**chievable: Realistic given constraints
- **R**elevant: Aligned with broader objectives
- **T**ime-bound: Has a deadline

**Example:**
```
❌ Vague: "Improve the website"
✅ SMART: "Reduce homepage load time from 3s to 1s by end of Q2"
```

**Questions to Answer:**
- What exactly needs to be accomplished?
- How will we know it's done?
- Who is this for?
- Why does this matter?
- When does it need to be complete?

### Step 2: Gather Requirements

**Goal:** Understand all constraints and dependencies.

**Types of Requirements:**

| Type | Questions | Examples |
|------|-----------|----------|
| **Functional** | What should it do? | User can log in, System generates reports |
| **Non-functional** | How should it perform? | Load in <2s, 99.9% uptime |
| **Technical** | What tech constraints exist? | Must use PostgreSQL, Compatible with IE11 |
| **Business** | What business rules apply? | GDPR compliance, Budget limit $50k |
| **User** | What do users need? | Mobile-friendly, Accessible (WCAG AA) |

**Dependencies to Identify:**
- Other teams or people
- External services or APIs
- Infrastructure or resources
- Predecessor tasks
- Approvals or sign-offs

### Step 3: Break Down Tasks

**Goal:** Decompose the goal into small, actionable items.

**Decomposition Techniques:**

#### Work Breakdown Structure (WBS)
Hierarchical decomposition of work:

```
Project: Launch E-commerce Site
├── 1. Backend Development
│   ├── 1.1 Database Schema
│   ├── 1.2 API Endpoints
│   └── 1.3 Payment Integration
├── 2. Frontend Development
│   ├── 2.1 Homepage
│   ├── 2.2 Product Pages
│   └── 2.3 Checkout Flow
├── 3. Testing
│   ├── 3.1 Unit Tests
│   ├── 3.2 Integration Tests
│   └── 3.3 User Acceptance Testing
└── 4. Deployment
    ├── 4.1 CI/CD Setup
    ├── 4.2 Production Environment
    └── 4.3 Monitoring
```

#### User Story Mapping
Break down from user perspective:

```
User Journey: Purchase a Product
├── Browse Products
│   → View category listing
│   → Search for products
│   → Filter results
├── View Product Details
│   → See product images
│   → Read description
│   → Check availability
├── Add to Cart
│   → Select quantity
│   → View cart summary
└── Checkout
    → Enter shipping info
    → Choose payment method
    → Confirm order
```

**Task Sizing Guidelines:**
- Each task should be completable in 1-3 days
- If larger, break it down further
- Tasks should be independently testable
- Clear acceptance criteria for each task

### Step 4: Sequence and Prioritize

**Goal:** Determine the optimal order of execution.

**Dependency Types:**
- **Finish-to-Start (FS):** Task B can't start until Task A finishes
- **Start-to-Start (SS):** Task B can't start until Task A starts
- **Finish-to-Finish (FF):** Task B can't finish until Task A finishes
- **Start-to-Finish (SF):** Task B can't finish until Task A starts (rare)

**Prioritization Methods:**

#### MoSCoW Method
- **M**ust have: Critical for launch
- **S**hould have: Important but not critical
- **C**ould have: Nice to have if time permits
- **W**on't have: Agreed to exclude for now

#### Value vs Effort Matrix
```
                High Value
                    │
        ┌───────────┼───────────┐
        │   DO      │  PLAN     │
        │   FIRST   │  LATER    │
Low ────┼───────────┼───────────┼──── Low Effort
Effort  │           │           │  Effort
        │   FILL    │  SKIP     │
        │   TIME    │  (LOW     │
        │           │  VALUE)   │
        └───────────┼───────────┘
                    │
                Low Value
```

### Step 5: Estimate and Schedule

**Goal:** Create realistic timelines.

**Estimation Techniques:**

#### Three-Point Estimation
For each task, estimate:
- **Optimistic (O):** Best case scenario
- **Most Likely (M):** Realistic expectation
- **Pessimistic (P):** Worst case scenario

Calculate expected duration: `(O + 4M + P) / 6`

#### Planning Poker
Team-based estimation using story points:
- Each team member votes on complexity
- Discuss differences in estimates
- Re-vote until consensus

**Buffer Guidelines:**
- Add 10-20% buffer for known unknowns
- Reserve additional contingency for high-risk items
- Account for meetings, reviews, and interruptions

### Step 6: Track and Adapt

**Goal:** Monitor progress and adjust as needed.

**Tracking Methods:**

#### Kanban Board
```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│   TO DO     │  IN PROGRESS│   REVIEW    │    DONE     │
├─────────────┼─────────────┼─────────────┼─────────────┤
│ Task A      │ Task C      │ Task E      │ Task G      │
│ Task B      │ Task D      │             │ Task H      │
│ Task F      │             │             │             │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

#### Progress Metrics
- **Tasks completed / Total tasks**
- **Burn-down chart:** Remaining work over time
- **Cycle time:** How long tasks take to complete
- **Velocity:** Work completed per iteration

**Adaptation Triggers:**
- Scope changes
- Resource availability changes
- Technical blockers discovered
- Priority shifts
- Timeline adjustments

## Planning Templates

### Simple Project Plan

```markdown
# Project: [Name]

## Objective
[What we're building and why]

## Success Criteria
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Timeline
Start: [Date]
End: [Date]
Key Milestones:
- [Date]: Milestone 1
- [Date]: Milestone 2

## Tasks
| ID | Task | Owner | Estimate | Status | Dependencies |
|----|------|-------|----------|--------|--------------|
| 1  |      |       |          |        |              |

## Risks
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
|      |             |        |            |

## Resources Needed
- [Resource 1]
- [Resource 2]
```

### Sprint Planning Template

```markdown
# Sprint [Number] - [Dates]

## Sprint Goal
[Single sentence describing the focus]

## Committed Stories
| Story | Points | Assignee | Status |
|-------|--------|----------|--------|
|       |        |          |        |

## Capacity
Total Points Available: [X]
Team Availability: [Note any vacations, holidays]

## Blockers
- [Blocker 1]
- [Blocker 2]
```

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Planning fallacy | Consistently underestimate time required | Use historical data and add 20% buffer |
| Gold plating | Adds unnecessary features, delays delivery | Stick to requirements, validate additions |
| Analysis paralysis | Over-planning without action | Time-box planning phase, iterate |
| Ignoring dependencies | Miss critical path items, block execution | Map dependencies explicitly before scheduling |
| No buffer | Best-case-only planning fails | Add contingency for unknowns |

## Best Practices

1. **Involve the team**: Those doing the work should help plan it — improves estimates and buy-in
2. **Start coarse, refine later**: High-level plan first, detailed tasks after initial alignment
3. **Document assumptions**: Make implicit assumptions explicit to avoid surprises
4. **Plan for learning**: Include research/spike tasks for unknowns
5. **Review past plans**: Learn from estimation accuracy to improve future planning
6. **Stay flexible**: Plans are living guides, not contracts — adapt as you learn

## Tools & Resources

- **Jira/Linear** - Project tracking with Kanban boards and sprint planning
- **Notion/Confluence** - Collaborative planning documents and wikis
- **Miro** - Visual planning with user story mapping and value-vs-effort matrices
- **Planning Poker tools** - [planningpoker.com](https://www.planningpoker.com/) for team estimation
- **The Art of Project Management** by Russell Matthews - Comprehensive planning guide

## Example Application

**Scenario:** Planning a 3-month feature launch for a new payment integration

**Application:**
1. **Define Goal**: "Launch Stripe payment integration supporting credit cards and ACH by end of Q2"
2. **Decompose**: WBS with 4 epics → 12 user stories → 45 tasks, each 1-3 days
3. **Prioritize**: MoSCoW — Must have: credit card payments; Should have: ACH; Won't have: crypto
4. **Estimate**: Three-point estimation with 15% buffer → 11 weeks total
5. **Track**: Kanban board with weekly check-ins, adaptation triggers for scope changes

**Outcome:** Feature launched on schedule. Buffer absorbed 2 unexpected API changes. Team had clear visibility throughout.

## Success Indicators

You've mastered planning when you can:

- ✅ Break any complex project into tasks completable in 1-3 days each
- ✅ Produce estimates within 20% of actual delivery time
- ✅ Create plans that the whole team understands and commits to
- ✅ Identify dependencies and risks before they become blockers
- ✅ Adapt plans quickly when scope or resources change

## Related Skills

- [Brainstorming](brainstorming.md) - Generate options before committing to a plan
- [Team Collaboration](../collaboration-skills/team_collaboration.md) - Coordinate execution with others
- [Project Management](../management-skills/project_management.md) - Larger-scale project oversight

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Behavior Skills Team
next_review: 2026-07-15
---
