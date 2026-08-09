---
# Metadata
title: "Teaching"
description: "Guide others in acquiring new knowledge and skills effectively"
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
  - teaching
  - mentoring
  - education
  - knowledge-transfer
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
# Teaching Skill

## Overview

Guide others in acquiring new knowledge and skills effectively. This skill helps you structure learning experiences, explain concepts clearly, and support skill development in others.

## Core Competencies

- **Learner Assessment**: Evaluate a learner's current level, goals, and preferred learning style
- **Objective Setting**: Define clear, measurable learning objectives using Bloom's Taxonomy
- **Content Structuring**: Organize material from simple to complex, concrete to abstract, known to unknown
- **Adaptive Delivery**: Use "I Do, We Do, You Do" scaffolding and adjust pace based on comprehension cues
- **Constructive Feedback**: Provide specific, timely feedback that focuses on the work, not the person

## When to Use

- Onboarding new team members
- Mentoring junior developers
- Leading training sessions or workshops
- Creating educational content
- Pair programming
- Code review as a teaching opportunity

## The Teaching Framework

### Step 1: Assess the Learner

**Goal:** Understand where the learner is starting from.

**Questions to Ask:**
- What's your current experience level with this topic?
- Have you worked with similar technologies before?
- What are your learning goals?
- How do you prefer to learn (visual, hands-on, reading)?
- What's your timeline for learning this?

**Assessment Methods:**
- **Skill inventory:** List related skills they already have
- **Pre-test:** Simple questions to gauge baseline knowledge
- **Discussion:** Talk about their experience and goals
- **Observation:** Watch them attempt a simple task

### Step 2: Set Clear Objectives

**Goal:** Define what success looks like for the learning session.

**Learning Objective Formula:**
```
By the end of this [session/course], you will be able to [action verb] [content] [condition/criteria]
```

**Examples:**
- "By the end of this session, you will be able to write basic SQL queries using SELECT, WHERE, and JOIN"
- "After this workshop, you will be able to create a React component with props and state"
- "By tomorrow, you'll be able to navigate the codebase and find relevant files independently"

**Bloom's Taxonomy Levels:**
| Level | Verbs | Example |
|-------|-------|---------|
| Remember | Define, list, recall | List the Git commands |
| Understand | Explain, describe, summarize | Explain how closures work |
| Apply | Use, implement, solve | Use async/await to handle promises |
| Analyze | Compare, contrast, differentiate | Compare REST vs GraphQL |
| Evaluate | Judge, critique, recommend | Critique this code architecture |
| Create | Build, design, develop | Build a complete API endpoint |

### Step 3: Structure the Content

**Goal:** Organize material in a logical, digestible sequence.

**Effective Sequences:**

#### Simple to Complex
```
Variables → Data Types → Operators → Functions → Objects → Classes
```

#### Concrete to Abstract
```
Specific example → Pattern recognition → General principle → Application
```

#### Known to Unknown
```
Connect new concepts to what they already understand
```

#### Problem-Centered
```
Present a problem → Teach concepts needed to solve it → Practice
```

**Chunking Guidelines:**
- Break content into 5-10 minute segments
- One concept per chunk
- Build on previous chunks
- Include practice between chunks

### Step 4: Deliver Instruction

**Goal:** Present material in an engaging, understandable way.

**Teaching Techniques:**

#### I Do, We Do, You Do
1. **I Do:** Demonstrate while explaining your thinking
2. **We Do:** Solve a problem together with guidance
3. **You Do:** Learner solves independently

#### Think Aloud
Verbalize your thought process:
```
"I'm looking at this error message... it says 'undefined is not a function'...
that usually means I'm calling something that doesn't exist...
let me check where this variable is defined..."
```

#### Scaffolding
Provide temporary support that's gradually removed:
- Start with templates and examples
- Provide hints before full answers
- Reduce help as competence grows

#### Analogies and Metaphors
Connect abstract concepts to familiar things:
```
"A Promise is like ordering food at a restaurant:
- You place the order (initiate the async operation)
- You get a ticket/pager (the Promise object)
- Sometimes your food is ready (resolved)
- Sometimes there's a problem (rejected)"
```

### Step 5: Check Understanding

**Goal:** Verify the learner has grasped the concepts.

**Formative Assessment Methods:**

#### Questions to Ask
- "Can you explain this back to me in your own words?"
- "What would happen if we changed X to Y?"
- "How is this different from [related concept]?"
- "When would you use this approach vs [alternative]?"

#### Practical Checks
- Have them solve a similar problem
- Ask them to debug intentionally broken code
- Request they teach the concept back to you
- Give a short coding exercise

#### Observational Cues
Watch for:
- ✅ Confident body language
- ✅ Asking insightful questions
- ✅ Making connections to prior knowledge
- ❌ Furrowed brow, confused expression
- ❌ Silent when you expect questions
- ❌ Copying without understanding

### Step 6: Provide Feedback

**Goal:** Help the learner improve through constructive feedback.

**Feedback Principles:**

#### Be Specific
```
❌ "Good job"
✅ "Your function naming is clear and consistent, which makes the code easy to follow"
```

#### Focus on the Work, Not the Person
```
❌ "You're not getting this"
✅ "This approach has a issue with edge cases"
```

#### Balance Positive and Constructive
```
"What's working well: [specific strengths]
What to improve: [specific areas]
How to improve: [actionable suggestions]"
```

#### Timely and Frequent
- Give feedback soon after the work
- Don't wait until the end to address issues
- Celebrate small wins along the way

## Teaching Patterns

### The Concept Attainment Model
1. Show examples that fit the concept
2. Show examples that don't fit
3. Learner identifies the pattern
4. Learner defines the concept
5. Test with new examples

### Guided Discovery
1. Present a problem or scenario
2. Let learner explore and experiment
3. Ask probing questions
4. Guide toward discovery
5. Formalize the learning

### Case-Based Learning
1. Present a real-world case
2. Analyze the situation together
3. Discuss possible approaches
4. Reveal what was actually done
5. Extract general principles

### Peer Teaching
1. Teach a concept to the learner
2. Have them teach it to someone else
3. Observe and provide feedback
4. Discuss what worked and what didn't

## Common Teaching Scenarios

### Explaining a New Concept

```markdown
## Teaching Plan: [Concept Name]

### Hook (Why should they care?)
[Real-world relevance or problem it solves]

### Prerequisites
[What they need to know first]

### Core Explanation
[Clear, concise definition]

### Example
[Concrete, relatable example]

### Non-Example
[What it's NOT, to clarify boundaries]

### Practice
[Hands-on exercise]

### Check Understanding
[Questions or tasks to verify learning]
```

### Debugging Session as Teaching

```markdown
## Approach

1. Let them share their screen
2. Ask them to explain what they're trying to do
3. Ask: "What have you tried so far?"
4. Guide them to observe the actual behavior
5. Ask: "What do you think is causing this?"
6. Help them form a hypothesis
7. Let them test their hypothesis
8. After fixing, ask: "What did you learn?"
```

### Code Review as Teaching

```markdown
## Teaching-Focused Review

### Start Positive
"This function handles the core logic well, especially..."

### Ask Questions Instead of Dictating
"What do you think about extracting this into a helper function?"

### Explain the Why
"We prefer immutability here because it prevents..."

### Prioritize
Focus on 2-3 most important points, not every nitpick

### Offer Resources
"Here's a great article on this pattern..."
```

## Adapting to Learning Styles

### Visual Learners
- Use diagrams and flowcharts
- Draw on whiteboard
- Show code examples
- Use color coding

### Auditory Learners
- Explain concepts verbally
- Encourage discussion
- Use mnemonics
- Have them explain back

### Kinesthetic Learners
- Hands-on coding exercises
- Build projects immediately
- Learn by debugging
- Physical analogies

### Reading/Writing Learners
- Provide documentation links
- Take notes together
- Write summaries
- Read code together

## Common Pitfalls

| Pitfall | Impact | Prevention |
|---------|--------|------------|
| Moving too fast | Learner can't keep up, disengages | Pause frequently, check understanding |
| Assuming knowledge | Learner lost on prerequisites | State assumptions, assess baseline first |
| Taking over | Learner doesn't develop independence | Guide with questions, let them struggle productively |
| No context | Facts feel disconnected, hard to retain | Connect to the bigger picture and real applications |
| One-size-fits-all | Doesn't match learner's style or pace | Adapt to individual needs and preferences |

## Best Practices

1. **Start with "why"**: Explain why the concept matters before diving into how it works
2. **Use "I Do, We Do, You Do"**: Demonstrate, practice together, then let them try independently
3. **Ask questions instead of telling**: "What do you think happens if...?" builds deeper understanding
4. **Chunk content**: Break material into 5-10 minute segments with practice between each
5. **Celebrate small wins**: Positive reinforcement maintains motivation through difficulty
6. **Normalize struggle**: "That's a common confusion — let's work through it together"

## Tools & Resources

- **Bloom's Taxonomy** - Framework for writing measurable learning objectives
- **Excalidraw/diagrams.net** - Create visual explanations and flowcharts
- **CodeSandbox/Replit** - Share runnable code examples for hands-on practice
- **Loom** - Record teaching sessions for async learning and review
- **The Art of Teaching** by G. Willoughby - Pedagogical techniques for technical instruction

## Example Application

**Scenario:** Onboarding a new developer to the team's React codebase

**Application:**
1. **Assess**: New dev knows Vue but not React — familiar with components, new to hooks
2. **Objectives**: "By end of week 1, you'll navigate the codebase and modify components independently"
3. **Structure**: Start with component basics (known) → hooks (new) → state management (complex)
4. **Deliver**: I Do (pair on a component), We Do (modify together), You Do (they build a feature)
5. **Check**: Ask them to explain the data flow back to you; debug a broken component together

**Outcome**: New dev was productive by week 2. Reported feeling confident and supported. Onboarding time reduced from 3 weeks to 2.

## Success Indicators

You've mastered teaching when you can:

- ✅ Assess a learner's level within the first 10 minutes of interaction
- ✅ Write clear learning objectives with measurable outcomes
- ✅ Adapt your teaching style to match visual, auditory, and kinesthetic learners
- ✅ Learners can independently solve problems they couldn't before the session
- ✅ Receive feedback like "you made this click for me" from learners

## Related Skills

- [Explanation](explanation.md) - Clear communication of complex concepts
- [Learning](learning.md) - Understanding how people learn improves how you teach
- [Pair Programming](../collaboration-skills/pair_programming.md) - Real-time teaching through code

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: Behavior Skills Team
next_review: 2026-07-15
---
