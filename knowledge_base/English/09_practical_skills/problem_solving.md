---
title: Problem Solving
description: Systematic approaches to problem-solving for technical professionals
topics: [problem solving, debugging, analysis, decision making]
difficulty: intermediate
prerequisites: []
last_updated: 2025-01-15
---

# Problem Solving

## Introduction

Effective problem-solving is a critical skill for technology professionals. This guide presents systematic approaches to identify, analyze, and solve complex technical problems.

## Table of Contents

- Problem-Solving Frameworks
- Root Cause Analysis
- Debugging Strategies
- Decision Making Under Uncertainty
- Creative Problem Solving
- Collaborative Problem Solving

## Problem-Solving Frameworks

### Polya's Four-Step Method

1. **Understand the Problem**
   - What is unknown? What are the data? What is the condition?
   - Can you restate the problem in your own words?
   - Draw a figure or diagram if helpful

2. **Devise a Plan**
   - Have you seen a similar problem before?
   - Can you solve a simpler version first?
   - Break into smaller sub-problems

3. **Carry Out the Plan**
   - Execute each step carefully
   - Check each step as you go
   - Be patient and persistent

4. **Look Back**
   - Can you verify the result?
   - Is there another way to solve it?
   - Can you generalize the solution?

### IDEAL Model

**I**dentify the problem
- Recognize that a problem exists
- Define it clearly
- Gather relevant information

**D**efine goals
- What does success look like?
- What constraints exist?
- Prioritize objectives

**E**xplore possible strategies
- Brainstorm multiple approaches
- Consider pros and cons
- Select best option

**A**nticipate and act
- Plan implementation steps
- Execute the solution
- Monitor progress

**L**ook back and learn
- Evaluate outcomes
- Document learnings
- Identify improvements

### OODA Loop for Problem Solving

**O**bserve - Gather information about the problem
**O**rient - Analyze and synthesize information
**D**ecide - Choose a course of action
**A**ct - Implement and observe results

Repeat until problem is resolved.

## Root Cause Analysis

### Five Whys Technique

Ask "why" iteratively to drill down to root cause:

```
Problem: Website is slow

1. Why? Server response time is high
2. Why? Database queries are slow
3. Why? Missing indexes on key tables
4. Why? Schema changes weren't accompanied by index updates
5. Why? No process for reviewing indexing needs during deployments

Root Cause: Missing deployment checklist item for database review
```

### Fishbone Diagram (Ishikawa)

Categories to explore:
- **People**: Skills, training, communication
- **Process**: Procedures, policies, workflows
- **Technology**: Tools, systems, infrastructure
- **Environment**: Physical, organizational culture
- **Materials**: Data, inputs, resources
- **Measurement**: Metrics, monitoring, feedback

### Fault Tree Analysis

Top-down approach using boolean logic:
```
System Failure
├── Component A fails OR
├── Component B fails AND
│   ├── Backup fails OR
│   └── Recovery procedure fails
└── External factor
```

## Debugging Strategies

### Scientific Method for Debugging

1. **Observe** the symptom
2. **Form hypothesis** about cause
3. **Predict** what else should be true
4. **Test** the prediction
5. **Analyze** results
6. **Refine** hypothesis or fix

### Divide and Conquer

Binary search approach:
- Split system in half
- Determine which half contains the bug
- Repeat until isolated

Example for code:
```python
# Instead of checking line by line
# Add checkpoints at key divisions
print("Checkpoint 1: Before processing")
# ... first half of code ...
print("Checkpoint 2: After first half")
# ... second half of code ...
print("Checkpoint 3: After processing")
```

### Rubber Duck Debugging

Explain the problem aloud, step by step:
- Forces clear thinking
- Reveals assumptions
- Often leads to self-discovery of solution

### Change One Thing at a Time

- Make single, isolated changes
- Test after each change
- Revert if no improvement
- Document what you tried

## Decision Making Under Uncertainty

### Expected Value Analysis

Calculate expected value for each option:
```
EV = (Probability of Success × Value of Success) 
   - (Probability of Failure × Cost of Failure)
```

Choose option with highest expected value.

### Decision Trees

Map out decisions and outcomes:
```
Option A
├── Success (60%) → Value: +100
└── Failure (40%) → Cost: -50
EV = 0.6×100 - 0.4×50 = 40

Option B
├── Success (80%) → Value: +50
└── Failure (20%) → Cost: -20
EV = 0.8×50 - 0.2×20 = 36
```

### Satisficing vs. Maximizing

**Maximizing**: Find the absolute best solution
- Pros: Optimal outcome
- Cons: Time-consuming, analysis paralysis

**Satisficing**: Find good enough solution
- Pros: Faster, reduces stress
- Cons: May miss better options

Use satisficing for low-stakes decisions, maximizing for critical ones.

## Creative Problem Solving

### Brainstorming Rules

- Defer judgment
- Aim for quantity
- Welcome wild ideas
- Combine and improve ideas

### SCAMPER Technique

**S**ubstitute - What can you replace?
**C**ombine - What can you merge?
**A**dapt - What can you adjust?
**M**odify - What can you change?
**P**ut to other uses - How else can it be used?
**E**liminate - What can you remove?
**R**everse - What can you rearrange or reverse?

### Lateral Thinking

Challenge assumptions:
- What if the opposite were true?
- How would someone from a different field approach this?
- What would we do if we had unlimited resources?
- What would we do if we had no resources?

### Analogical Thinking

Find solutions in unrelated domains:
- How does nature solve this? (biomimicry)
- How do other industries handle this?
- What historical problems are similar?

## Collaborative Problem Solving

### Pair Problem Solving

Two people working together:
- One drives (implements)
- One navigates (thinks strategically)
- Switch roles regularly
- Discuss openly

### Mob Programming

Whole team works on same problem:
- One person types
- Others provide input
- Rotate frequently
- Collective ownership

### Design Thinking Process

1. **Empathize** - Understand user needs
2. **Define** - Frame the problem
3. **Ideate** - Generate solutions
4. **Prototype** - Build to think
5. **Test** - Get feedback

### Retrospectives for Learning

After solving a problem, discuss:
- What went well?
- What could be improved?
- What did we learn?
- What will we do differently next time?

## Common Problem-Solving Pitfalls

### Cognitive Biases

**Confirmation Bias**: Seeking evidence that supports your hypothesis
- Mitigation: Actively look for disconfirming evidence

**Anchoring**: Over-relying on first piece of information
- Mitigation: Consider multiple starting points

**Availability Heuristic**: Overweighting recent or memorable examples
- Mitigation: Seek statistical data

**Sunk Cost Fallacy**: Continuing because of past investment
- Mitigation: Ask "Would I start this today?"

### Process Mistakes

**Jumping to Solutions**: Implementing before understanding
- Fix: Spend more time on problem definition

**Solving Wrong Problem**: Addressing symptoms not causes
- Fix: Verify you're solving the right problem

**Not Documenting**: Losing institutional knowledge
- Fix: Write down what you learned

## Summary

Effective problem-solving requires:
- Systematic frameworks and approaches
- Root cause analysis techniques
- Structured debugging strategies
- Sound decision-making under uncertainty
- Creative thinking methods
- Collaborative practices
- Awareness of common pitfalls

## Further Reading

- How to Solve It by George Polya
- Think Like a Programmer by V. Anton Spraul
- The Art of Problem Solving by Russell Ackoff

## See Also

- Critical Thinking (./critical_thinking.md)
- Research Methods (./research_methods.md)

## References

- MIT OpenCourseWare Problem Solving materials
- IEEE Software debugging research
