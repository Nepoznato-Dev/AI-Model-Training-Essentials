---
# Metadata
title: "Brainstorming"
description: "Generate diverse ideas and explore multiple possibilities before converging on solutions"
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
  - brainstorming
  - ideation
  - creativity
  - problem-solving
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Brainstorming Skill

## Overview

Generate diverse ideas and explore multiple possibilities before converging on solutions. This skill helps you think broadly, challenge assumptions, and discover creative approaches to problems.

## Core Competencies

- **Divergent Thinking**: Generate a high volume of diverse ideas using techniques like mind mapping, SCAMPER, and free writing
- **Convergent Evaluation**: Assess and prioritize ideas using feasibility, impact, and effort criteria
- **Session Facilitation**: Guide group brainstorming to ensure inclusive participation and productive outcomes
- **Creative Constraint**: Use limitations and prompts to spark innovation rather than stifle it
- **Idea Refinement**: Transform raw ideas into actionable concepts with clear value propositions

## When to Use

- Starting a new project or feature
- Solving a complex problem with no obvious solution
- Exploring multiple approaches before committing to one
- Breaking out of conventional thinking patterns
- Generating options for decision-making

## The Brainstorming Process

### Phase 1: Divergent Thinking (Expand)

**Goal:** Generate as many ideas as possible without judgment.

**Rules:**
1. Defer judgment - no idea is too wild
2. Go for quantity over quality initially
3. Build on others' ideas (or your own previous ideas)
4. Welcome unconventional approaches

**Techniques:**

#### 1. Free Writing
Set a timer for 5-10 minutes and write continuously about the problem without stopping or editing.

#### 2. Mind Mapping
Start with the central problem and branch out with related concepts, connections, and associations.

```
Central Problem
├── Aspect A
│   ├── Idea A1
│   └── Idea A2
├── Aspect B
│   ├── Idea B1
│   └── Idea B2
└── Aspect C
    ├── Idea C1
    └── Idea C2
```

#### 3. SCAMPER Method
Ask questions using these prompts:
- **S**ubstitute: What can be replaced?
- **C**ombine: What can be merged?
- **A**dapt: What can be adjusted for this purpose?
- **M**odify: What can be changed?
- **P**ut to other uses: How else can this be used?
- **E**liminate: What can be removed?
- **R**everse: What can be rearranged or reversed?

#### 4. Worst Possible Idea
Intentionally think of terrible solutions. This reduces pressure and often reveals insights when you reverse them.

### Phase 2: Convergent Thinking (Narrow Down)

**Goal:** Evaluate and select the most promising ideas.

**Evaluation Criteria:**
1. **Feasibility:** Can we actually build this?
2. **Impact:** How much value does this create?
3. **Effort:** What resources are required?
4. **Risk:** What could go wrong?
5. **Alignment:** Does this fit our goals?

**Prioritization Matrix:**

```
                High Impact
                    │
        ┌───────────┼───────────┐
        │           │           │
        │  Quick    │  Major    │
        │  Wins     │  Projects │
Low ────┼───────────┼───────────┼──── Low Effort
Effort  │           │           │  Effort
        │  Fill-ins │  Time     │
        │           │  Sinks    │
        └───────────┼───────────┘
                    │
                Low Impact
```

### Phase 3: Refinement

**Goal:** Develop selected ideas into actionable concepts.

For each chosen idea:
1. Define the core value proposition
2. Identify key requirements
3. Spot potential obstacles
4. Outline next steps

## Example Session

**Problem:** "How might we improve code review quality?"

**Divergent Ideas:**
- Automated AI pre-review before human review
- Rotating review assignments across teams
- Review checklist templates for different change types
- Gamification with review quality scores
- Pair programming instead of async reviews
- Review timeboxed to 30 minutes max
- Require reviewers to run the code locally
- Video walkthroughs from authors
- Focus reviews on architecture, let CI handle style
- Random reviewer assignment to prevent bias

**Convergent Selection:**
After evaluation, top 3 ideas:
1. Automated AI pre-review (high impact, medium effort)
2. Review checklist templates (quick win)
3. Require running code locally (medium impact, low effort)

## Tips for Better Brainstorming

- **Change context:** Move to a different environment or use a whiteboard
- **Time box:** Set clear time limits to maintain focus
- **Mix perspectives:** Consider how different stakeholders would approach this
- **Use constraints:** Artificial limitations can spark creativity
- **Take breaks:** Step away to let subconscious processing work
- **Document everything:** Capture all ideas, even rejected ones

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Judging ideas too early | Kills creativity, reduces idea volume | Defer judgment during divergent phase |
| Letting one voice dominate | Biases outcomes, loses diverse perspectives | Use round-robin or silent brainstorming |
| No clear problem statement | Ideas lack focus, waste time | Define the problem before generating ideas |
| Skipping convergent phase | Ideas never become actionable | Always allocate time for evaluation |
| Comfort zone thinking | Produces incremental, unoriginal ideas | Use provocations and constraints |

## Best Practices

1. **Time-box divergent thinking**: Set a timer (5-15 min) to maintain energy and focus
2. **Aim for quantity first**: More ideas increase the chance of breakthrough solutions
3. **Build on ideas**: Use "Yes, and..." instead of "No, but..."
4. **Use varied techniques**: Mix mind mapping, SCAMPER, and worst-possible-idea to stay fresh
5. **Document everything**: Capture all ideas, even rejected ones, for future reference
6. **Change context**: Move to a whiteboard or different environment to stimulate thinking

## Tools & Resources

- **Miro/Mural** - Digital whiteboards for collaborative brainstorming
- **MindMeister** - Mind mapping tool for visual idea organization
- **SCAMPER Checklist** - [mindtools.com/scamper](https://www.mindtools.com/scamper)
- **Edward de Bono's Six Thinking Hats** - Structured perspective-shifting technique
- **Timer/Timeboxing apps** - Keep divergent and convergent phases distinct

## Example Application

**Scenario:** "How might we improve code review quality on our team?"

**Application:**
1. **Divergent Phase** (10 min): Generated 15+ ideas including AI pre-review, rotating assignments, checklists, gamification, pair reviews, video walkthroughs
2. **Convergent Phase** (5 min): Evaluated on impact/effort matrix — selected top 3: AI pre-review (high impact), review checklists (quick win), require running code locally (low effort)
3. **Refinement**: Defined implementation plan for each selected idea with owners and timelines

**Outcome:** Team adopted review checklists within one sprint, AI pre-review prototype within a month. Code review turnaround improved by 40%.

## Success Indicators

You've mastered brainstorming when you can:

- ✅ Generate 15+ diverse ideas in under 10 minutes
- ✅ Facilitate sessions where all participants contribute equally
- ✅ Effectively evaluate and prioritize ideas using structured criteria
- ✅ Transform top ideas into actionable plans with clear next steps
- ✅ Use at least 3 different ideation techniques flexibly
- ✅ Recognize and avoid groupthink and premature convergence

## Related Skills

- [Planning](planning.md) - Turning brainstormed ideas into structured plans
- [Explanation](explanation.md) - Communicating ideas clearly to stakeholders
- [Team Collaboration](../collaboration-skills/team_collaboration.md) - Facilitating group brainstorming

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Behavior Skills Team
next_review: 2026-07-15
---
