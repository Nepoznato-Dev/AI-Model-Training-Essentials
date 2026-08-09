---
# Metadata
title: "Mathematics and Logic"
description: "Mathematics, logic, proofs"
category: "Data Science and Analytics"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [math, logic, data-science-and-analytics]
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

# Mathematics and Logic

Mathematics isn't just a subject you study in school — it's the operating system underlying nearly every technical field. Physics uses it to describe the universe. Computer science uses it to design algorithms. Machine learning uses it to optimise weights. Finance uses it to price risk. You don't need to master every branch, but understanding the landscape — and knowing where each branch shows up — makes everything else click faster.

---

## Number Systems

Before anything else, it helps to understand the kinds of numbers you're working with. Each layer extends the previous one to solve a problem the old layer couldn't.

| Number Type | What It Includes | Why It Was Invented | Example |
|---|---|---|---|
| Natural numbers | 1, 2, 3, 4, ... | Counting things | 5 apples |
| Whole numbers | 0, 1, 2, 3, ... | Representing "nothing" | 0 degrees |
| Integers | ..., −2, −1, 0, 1, 2, ... | Debt, temperature below zero | −15°C |
| Rational numbers | p/q where q ≠ 0 | Dividing things unevenly | 1/3, 0.75 |
| Irrational numbers | Can't be expressed as fractions | Diagonals, circles, growth | √2, π, e |
| Real numbers | All rational + irrational | The complete number line | 3.14159... |
| Imaginary numbers | Multiples of i = √(−1) | Solving x² + 1 = 0 | 3i |
| Complex numbers | a + bi (real + imaginary) | Electrical engineering, quantum mechanics | 2 + 3i |

---

## Arithmetic and Number Theory

The basics: addition, subtraction, multiplication, division, and the rules governing their order.

**Order of operations** (PEMDAS/BODMAS): Parentheses → Exponents → Multiplication/Division (left to right) → Addition/Subtraction (left to right).

**Prime numbers** — whole numbers greater than 1 with no divisors other than 1 and themselves — are the atoms of number theory. The first few: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.

Why primes matter beyond math class: modern encryption (RSA) relies on the fact that multiplying two large primes is easy, but factoring the result back is computationally brutal.

**Useful operations:**
- Prime factorization: 84 = 2² × 3 × 7
- Greatest Common Divisor (GCD) of 24 and 36: 12
- Least Common Multiple (LCM) of 4 and 6: 12

---

## Algebra

Algebra is where you stop working with specific numbers and start working with *relationships*. A variable like `x` doesn't have a fixed value — it represents whatever makes the equation true.

**The quadratic formula** solves ax² + bx + c = 0:

x = (−b ± √(b² − 4ac)) / 2a

**Common function types and where they appear:**

| Function | Formula | Shape | Real-World Example |
|---|---|---|---|
| Linear | y = mx + b | Straight line | Cost per unit at a flat rate |
| Quadratic | y = ax² + bx + c | Parabola | Projectile motion, braking distance |
| Exponential | y = a × b² | Rapid growth/decay | Compound interest, population growth, viral spread |
| Logarithmic | y = log_b(x) | Slow growth, inverse of exponential | Decibel scale, pH scale, algorithm complexity |

**Key vocabulary:**
- **Domain**: all valid inputs (e.g., can't divide by zero, can't take √ of a negative in reals)
- **Range**: all possible outputs
- **Slope** (m): rate of change — "for every 1 unit of x, y changes by m"
- **Intercept**: where the function crosses an axis

---

## Geometry

Geometry studies shapes, sizes, and spatial relationships. It shows up everywhere: game engines use it for rendering, robotics uses it for path planning, architecture uses it for structural design.

**Essential formulas:**

| Shape | Property | Formula |
|---|---|---|
| Triangle | Angle sum | 180° |
| Quadrilateral | Angle sum | 360° |
| Circle | Circumference | 2πr |
| Circle | Area | πr² |
| Sphere | Volume | (4/3)πr³ |
| Right triangle | Pythagorean theorem | a² + b² = c² |

**π (pi)** ≈ 3.14159 — the ratio of any circle's circumference to its diameter. It shows up in places you wouldn't expect: probability (normal distribution), engineering (signal processing), even the equation for Heisenberg's uncertainty principle.

---

## Statistics and Probability

Statistics is how you make sense of data. It's the difference between "I think this works" and "I have evidence this works."

**Measures of central tendency — what's "typical":**

| Measure | How It's Calculated | When to Use It |
|---|---|---|
| Mean (average) | Sum ÷ count | Default choice; sensitive to outliers |
| Median | Middle value when sorted | Skewed data (e.g., house prices, salaries) |
| Mode | Most frequent value | Categorical data (e.g., most popular colour) |

**Measures of spread — how "varied" the data is:**

| Measure | Formula Idea | What It Tells You |
|---|---|---|
| Range | max − min | Total spread, but outlier-sensitive |
| Variance | Average squared deviation from mean | In squared units (hard to interpret directly) |
| Standard deviation | √variance | Same units as data — the go-to spread measure |

**Probability basics:**
- Ranges from 0 (impossible) to 1 (certain)
- Independent events: P(A and B) = P(A) × P(B)
- Example: rolling two 6s in a row = (1/6) × (1/6) = 1/36

**Probability distributions you'll encounter in ML:**

| Distribution | What It Models | Example |
|---|---|---|
| Bernoulli | Single trial, two outcomes | One coin flip |
| Binomial | Successes in n trials | Correct answers on a 10-question MCQ |
| Normal (Gaussian) | Bell curve, natural phenomena | Heights, test scores, measurement noise |
| Poisson | Events in a fixed interval | Emails per hour, defects per batch |

**Bayes' theorem** — updating beliefs with evidence:

P(A|B) = P(B|A) × P(A) / P(B)

This is the backbone of spam filters, medical diagnostics, and Bayesian ML models. It says: your updated belief = (how well the evidence fits your hypothesis × your prior belief) / how likely the evidence is overall.

---

## Calculus

Calculus studies *change* and *accumulation*. If algebra handles snapshots, calculus handles motion pictures.

**Differential calculus** — rates of change. The derivative f'(x) tells you how fast f is changing at any point.

| Function f(x) | Derivative f'(x) | Intuition |
|---|---|---|
| xⁿ | n·xⁿâ»¹ | Power rule |
| e² | e² | The only function equal to its own derivative |
| ln(x) | 1/x | Growth rate slows as x increases |
| sin(x) | cos(x) | Rate of change of oscillation |

Why derivatives matter in ML: gradient descent — the algorithm that trains most neural networks — works by computing derivatives of the loss function and stepping in the direction that reduces error.

**Integral calculus** — accumulation. The integral represents the area under a curve. If derivatives answer "how fast is it changing?", integrals answer "how much has accumulated?"

The **fundamental theorem of calculus** connects both: differentiation and integration are inverse operations.

---

## Logic and Reasoning

Logic is the study of *valid* reasoning — not whether a conclusion *feels* right, but whether it *follows* from the premises.

**Deductive reasoning** (guaranteed conclusion if premises are true):
- All humans are mortal. Socrates is human. → Socrates is mortal.

**Inductive reasoning** (probable conclusion, not guaranteed):
- Every swan I've seen is white. → All swans are probably white. (But black swans exist.)

**Common logical fallacies — errors that look like reasoning but aren't:**

| Fallacy | What It Is | Example |
|---|---|---|
| Ad hominem | Attacking the person, not the argument | "You can't trust her policy idea — she's young." |
| Straw man | Misrepresenting an argument to knock it down | "He wants to cut military spending? He wants to leave us defenceless!" |
| False dichotomy | Presenting two options when more exist | "You're either with us or against us." |
| Circular reasoning | Using the conclusion as its own premise | "This law is unjust because it's unfair." |
| Appeal to authority | "It's true because an expert said so" | "This stock will rise — a famous investor said so." |
| Post hoc | Assuming A caused B because A came first | "I took this supplement, then my cold went away. The supplement cured me." |

---

## Sets

A **set** is a collection of distinct objects — the foundation of modern mathematics.

| Operation | Symbol | Meaning | Example (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Union | A ∪ B | Elements in either set | {1, 2, 3, 4} |
| Intersection | A ∩ B | Elements in both sets | {2} |
| Difference | A \ B | Elements in A but not B | {1, 3} |
| Empty set | ∅ | Contains nothing | {} |
| Subset | A ⊂ B | All of A's elements are in B | {1,2} ⊂ {1,2,3} |

Set theory shows up in databases (SQL JOINs are essentially set operations), probability (events are sets of outcomes), and programming (sets, hash maps).

---

## Binary and Number Bases

Computers think in binary (base 2): only 0s and 1s. Humans think in decimal (base 10). Programmers often use hexadecimal (base 16) as a compact way to represent binary.

| Base | Digits Used | Example | Decimal Equivalent |
|---|---|---|---|
| Binary (base 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| Decimal (base 10) | 0–9 | 11 | 11 |
| Hexadecimal (base 16) | 0–9, A–F | B | 11 |
| Hexadecimal | 0–9, A–F | A3 | 160 + 3 = 163 |

**Why it matters:** every piece of data in a computer — text, images, audio, video — is ultimately just binary. A byte (8 bits) can represent 256 distinct values. Colours in CSS (#FF5733), memory addresses (0x7FFF), and IP addresses all use hex because it compresses long binary strings into something readable.

---

## Linear Algebra for ML and Graphics

Linear algebra — vectors, matrices, and transformations — is the mathematical engine behind machine learning, computer graphics, physics simulations, and search engines.

**Vectors** are ordered lists of numbers. In ML, each data point is a vector of features:
- [23, 1.8, 75] could represent a person's age, height in metres, and weight in kg.

**Matrices** are 2D arrays of numbers. A neural network's weights are stored as matrices. A batch of 100 images might be a matrix of shape (100, 784) — 100 rows, each with 784 pixel values.

**Key operations:**

| Operation | What It Does | Where It Shows Up |
|---|---|---|
| Dot product | Measures similarity between two vectors | Recommendation systems, cosine similarity |
| Matrix multiplication | Combines linear transformations | Every layer of a neural network |
| Eigenvalues/eigenvectors | Directions a matrix scales (not rotates) | PCA dimensionality reduction, PageRank |
| Matrix rank | Amount of independent information | Compression, low-rank approximation |

**Cosine similarity** = (a·b) / (||a|| × ||b||) — ranges from −1 (opposite) to 1 (same direction). This is how search engines measure whether two documents are "about the same thing" and how embedding models compare semantic similarity.

---

## Summary

| Branch | Core Question | Key Application |
|---|---|---|
| Arithmetic & Number Theory | How do numbers behave? | Cryptography, hashing |
| Algebra | How do unknowns relate? | Modelling, equations |
| Geometry | How do shapes and spaces work? | Graphics, robotics, architecture |
| Statistics & Probability | What does the data say? | ML, A/B testing, risk analysis |
| Calculus | How do things change? | Training neural networks, physics |
| Logic | Is this reasoning valid? | Programming, proofs, argument analysis |
| Set Theory | How do collections relate? | Databases, probability |
| Linear Algebra | How do transformations work? | ML, graphics, search engines |

You don't need all of this on day one. But as you go deeper in any technical field, you'll keep coming back to these foundations. The good news: each branch makes a lot more sense once you see *why* it was invented — what problem it was trying to solve.
