<!--
---
# Metadata
title: "Logic and Critical Thinking"
description: "Formal logic, logical fallacies, argument analysis, and critical thinking frameworks"
category: "Data Science and Analytics"
subcategory: "Mathematics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [logic, critical-thinking, fallacies, arguments, reasoning, boolean-algebra]
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

-->
# Logic and Critical Thinking

Logic is the study of valid reasoning — how to construct sound arguments and identify flawed ones. Critical thinking is the disciplined habit of questioning assumptions, evaluating evidence, and reasoning carefully. These skills are essential not just in mathematics and computer science, but in everyday decision-making, scientific research, and navigating an information-rich world.

---

## What Is an Argument?

In logic, an **argument** is a set of statements (premises) intended to support a conclusion.

| Component | Role | Example |
|-----------|------|---------|
| **Premise** | A statement offered as evidence | "All humans are mortal" |
| **Conclusion** | The claim the premises support | "Socrates is mortal" |
| **Inference** | The logical step from premises to conclusion | "Socrates is human, therefore..." |

### Valid vs. Sound

| Term | Meaning | Example |
|------|---------|---------|
| **Valid** | If premises are true, conclusion must be true | Structure is correct, even if premises are false |
| **Invalid** | Conclusion doesn't follow from premises | Logical structure is broken |
| **Sound** | Valid AND all premises are actually true | The gold standard of argument |
| **Unsound** | Either invalid or has false premises | Most flawed arguments |

---

## Types of Reasoning

| Type | Direction | Strength | Example |
|------|-----------|----------|---------|
| **Deductive** | General → specific | Certain (if valid) | "All mammals have lungs. A whale is a mammal. Therefore, a whale has lungs." |
| **Inductive** | Specific → general | Probable | "Every swan I've seen is white. Therefore, all swans are probably white." |
| **Abductive** | Observation → best explanation | Plausible | "The grass is wet. The best explanation is that it rained." |

---

## Propositional Logic

Propositional logic deals with simple propositions and how they combine:

### Logical Connectives

| Connective | Symbol | Meaning | Truth Condition |
|-----------|--------|---------|----------------|
| **AND** | ∧ (p ∧ q) | Conjunction | True only when both are true |
| **OR** | ∨ (p ∨ q) | Disjunction | True when at least one is true |
| **NOT** | ¬ (¬p) | Negation | Opposite truth value |
| **IF...THEN** | → (p → q) | Implication | False only when p is true and q is false |
| **IFF** | ↔ (p ↔ q) | Biconditional | True when both have the same truth value |

### Truth Table for Implication (p → q)

| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

Note: A false premise makes the implication vacuously true. "If the moon is cheese, then I'm the Pope" is logically true.

---

## Boolean Algebra

Boolean algebra is the mathematics of true/false values and is the foundation of digital circuit design and programming:

| Law | Expression | Meaning |
|-----|-----------|---------|
| **Commutative** | A ∧ B = B ∧ A | Order doesn't matter |
| **Associative** | (A ∧ B) ∧ C = A ∧ (B ∧ C) | Grouping doesn't matter |
| **Distributive** | A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C) | AND distributes over OR |
| **De Morgan's** | ¬(A ∧ B) = ¬A ∨ ¬B | Negation flips AND to OR |
| **De Morgan's** | ¬(A ∨ B) = ¬A ∧ ¬B | Negation flips OR to AND |
| **Double Negation** | ¬(¬A) = A | Two negations cancel |
| **Identity** | A ∧ T = A; A ∨ F = A | Identity elements |
| **Complement** | A ∧ ¬A = F; A ∨ ¬A = T | Contradiction and tautology |

---

## Common Logical Fallacies

Recognizing fallacies is essential for critical thinking:

### Formal Fallacies (Structural Errors)

| Fallacy | Structure | Example |
|---------|-----------|---------|
| **Affirming the Consequent** | If P then Q. Q. Therefore P. | "If it rains, the ground is wet. The ground is wet. Therefore it rained." (Could be a sprinkler.) |
| **Denying the Antecedent** | If P then Q. Not P. Therefore not Q. | "If it rains, the ground is wet. It didn't rain. Therefore the ground isn't wet." |

### Informal Fallacies (Content Errors)

| Fallacy | Description | Example |
|---------|-------------|---------|
| **Ad Hominem** | Attacking the person, not the argument | "You can't trust her economic plan — she's not even an economist." |
| **Straw Man** | Misrepresenting an argument to make it easier to attack | "You want to reduce military spending? So you want to leave the country defenseless!" |
| **Appeal to Authority** | Citing an authority who isn't an expert in the relevant field | "This celebrity says this diet works, so it must be effective." |
| **False Dilemma** | Presenting only two options when more exist | "You're either with us or against us." |
| **Slippery Slope** | Arguing that one event will inevitably lead to an extreme outcome | "If we allow this, next thing you know, total chaos." |
| **Circular Reasoning** | The conclusion is assumed in the premises | "The book is true because it says it's true." |
| **Hasty Generalization** | Drawing a broad conclusion from insufficient evidence | "I met two rude people from that city. Everyone there must be rude." |
| **Post Hoc Ergo Propter Hoc** | Assuming causation from temporal sequence | "I took this supplement and felt better, so it must work." |
| **Red Herring** | Introducing an irrelevant topic to distract | "You ask about my policy on education, but what really matters is the economy." |
| **Bandwagon** | Something is true because many people believe it | "Everyone is buying this product, so it must be the best." |

---

## Evaluating Arguments: A Checklist

| Step | Question |
|------|----------|
| 1. **Identify the conclusion** | What is the argument trying to prove? |
| 2. **Identify the premises** | What evidence is offered? |
| 3. **Check validity** | Does the conclusion follow from the premises? |
| 4. **Check soundness** | Are the premises actually true? |
| 5. **Look for fallacies** | Are there structural or content errors? |
| 6. **Consider counterarguments** | What objections might there be? |
| 7. **Assess evidence quality** | Is the evidence reliable, sufficient, and relevant? |

---

## Why This Matters

Logic and critical thinking are the foundation of mathematics, computer science, law, and scientific inquiry. In a world full of misinformation, advertising, and persuasive rhetoric, the ability to evaluate arguments rigorously is not just an academic skill — it's a survival skill. Whether you're debugging code, designing algorithms, or making life decisions, clear reasoning separates good judgments from bad ones.
