# Planning Skill

## Overview

Break down complex tasks into manageable, actionable steps. This skill helps you create clear plans that guide execution from start to finish.

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

## Common Planning Pitfalls

❌ **Planning Fallacy:** Underestimating time required
   - **Fix:** Use historical data, add buffers

❌ **Gold Plating:** Adding unnecessary features
   - **Fix:** Stick to requirements, validate additions

❌ **Analysis Paralysis:** Over-planning without action
   - **Fix:** Time-box planning, iterate

❌ **Ignoring Dependencies:** Missing critical path items
   - **Fix:** Map dependencies explicitly

❌ **No Buffer:** Planning for best-case scenario
   - **Fix:** Add contingency for unknowns

❌ **Set and Forget:** Not updating the plan
   - **Fix:** Regular check-ins, adapt as needed

## Tips for Better Planning

✅ **Involve the team:** Those doing the work should help plan it
✅ **Start coarse, refine:** High-level first, details later
✅ **Document assumptions:** Make implicit assumptions explicit
✅ **Plan for learning:** Include research/spike tasks
✅ **Review past plans:** Learn from estimation accuracy
✅ **Communicate clearly:** Ensure everyone understands the plan
✅ **Stay flexible:** Plans are guides, not contracts
