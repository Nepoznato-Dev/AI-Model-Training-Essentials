<!--
---
# Metadata
title: "Discrete Mathematics"
description: "Sets in depth, relations, functions, combinatorics, pigeonhole principle, recurrence relations, and generating functions"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into discrete mathematics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [discrete-mathematics, set-theory, relations, combinatorics, pigeonhole-principle, recurrence-relations, generating-functions]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "../logic_and_critical_thinking.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Discrete Mathematics

Discrete mathematics is the study of mathematical structures that are fundamentally countable or separated — as opposed to continuous mathematics (calculus, real analysis), which deals with smooth, unbroken quantities. Discrete math underpins computer science, cryptography, algorithm design, and data structures. If continuous math describes the physical world, discrete math describes the computational world.

---

## Set Theory in Depth

Sets are the foundation on which nearly all of modern mathematics is built. A **set** is an unordered collection of distinct objects, called **elements** or **members**.

### Axiomatic Foundations (ZFC)

Modern set theory rests on the **Zermelo-Fraenkel axioms with the Axiom of Choice (ZFC)**. These axioms resolve paradoxes like Russell's Paradox ("the set of all sets that do not contain themselves") by restricting how sets can be formed.

| Axiom | Informal Statement |
|-------|--------------------|
| Extensionality | Two sets are equal iff they have the same elements |
| Empty Set | There exists a set with no elements: ∅ |
| Pairing | For any a, b, there exists {a, b} |
| Union | For any family of sets, their union exists |
| Power Set | For any set S, the set of all subsets of S exists: P(S) |
| Infinity | There exists an infinite set |
| Specification | For any set A and property P, {x ∈ A : P(x)} exists |
| Replacement | The image of a set under a definable function is a set |
| Regularity | Every non-empty set contains an element disjoint from it (prevents self-membership) |
| Choice | For any family of non-empty pairwise disjoint sets, a choice function exists |

### Cardinality and Size of Sets

The **cardinality** of a set, denoted |S|, measures its "size."

| Concept | Definition | Example |
|---------|------------|---------|
| Finite set | Has a natural number as cardinality | |{a, b, c}| = 3 |
| Countably infinite | Same cardinality as ℕ | ℤ, ℚ are countably infinite |
| Uncountable | Larger than ℕ | ℝ, P(ℕ), the set of all functions ℕ → {0,1} |
| Cantor's Theorem | For any set S, |P(S)| > |S| | |P(ℕ)| > |ℕ| |

**Cantor's diagonal argument** proves that ℝ is uncountable: assume you can list all reals in [0,1], then construct a new real that differs from the nth listed real in the nth decimal place — contradiction.

### Operations on Sets

| Operation | Notation | Definition | Property |
|-----------|----------|------------|----------|
| Union | A ∪ B | {x : x ∈ A or x ∈ B} | Commutative, associative |
| Intersection | A ∩ B | {x : x ∈ A and x ∈ B} | Commutative, associative |
| Difference | A \ B | {x : x ∈ A and x ∉ B} | Not commutative |
| Symmetric Difference | A △ B | (A \ B) ∪ (B \ A) | Commutative, associative |
| Complement | Aᶜ | U \ A (where U is universal set) | (Aᶜ)ᶜ = A |
| Cartesian Product | A × B | {(a,b) : a ∈ A, b ∈ B} | |A × B| = |A| · |B| |

**De Morgan's Laws:**
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ

**Inclusion-Exclusion Principle** (for finite sets):
|A₁ ∪ A₂ ∪ ... ∪ Aₙ| = Σ|Aᵢ| − Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| − ... + (−1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|

---

## Relations

A **relation** R on sets A and B is a subset of A × B. When (a, b) ∈ R, we write aRb.

### Types of Relations

A relation R on a set A can have these properties:

| Property | Definition | Example |
|----------|------------|---------|
| Reflexive | ∀a ∈ A: aRa | ≤ on ℤ |
| Irreflexive | ∀a ∈ A: ¬(aRa) | < on ℤ |
| Symmetric | ∀a,b: aRb → bRa | = on any set |
| Antisymmetric | ∀a,b: aRb ∧ bRa → a = b | ≤ on ℤ |
| Transitive | ∀a,b,c: aRb ∧ bRc → aRc | <, ≤, = on ℤ |

### Equivalence Relations

An **equivalence relation** is reflexive, symmetric, and transitive. It partitions a set into disjoint **equivalence classes**.

**Example:** Modular arithmetic. Define a ~ b iff a ≡ b (mod n). The equivalence classes are [0], [1], ..., [n−1], which partition ℤ into n classes.

**Worked Example:** On ℤ × ℤ, define (a,b) ~ (c,d) iff a + d = b + c. This is an equivalence relation. The class [(0,0)] = {(n,n) : n ∈ ℤ}. The class [(1,0)] = {(n+1,n) : n ∈ ℤ}. This construction actually defines the integers from the natural numbers.

### Partial Orders

A **partial order** is reflexive, antisymmetric, and transitive. A set with a partial order is called a **partially ordered set (poset)**.

| Concept | Definition | Example |
|---------|------------|---------|
| Poset | (S, ≤) with ≤ a partial order | (P(A), ⊆) — subsets ordered by inclusion |
| Chain | A totally ordered subset | {∅, {a}, {a,b}} in P({a,b,c}) |
| Antichain | A subset where no two elements are comparable | {{a}, {b}} in P({a,b}) |
| Hasse Diagram | Visual representation of a poset | Draw edges only for covering relations |
| Upper Bound | An element ≥ every element in a subset | sup({2,3}) = 6 in (ℤ, \|) (divisibility) |
| Least Upper Bound (sup) | Smallest upper bound | sup({2,3}) in (ℕ, ≤) is 3 |
| Greatest Lower Bound (inf) | Largest lower bound | inf({4,6}) in (ℕ, \|) is 2 |

---

## Functions

A **function** f: A → B assigns to each element of A exactly one element of B.

### Classification of Functions

| Type | Definition | Example |
|------|------------|---------|
| Injective (one-to-one) | f(a) = f(b) → a = b | f(x) = 2x from ℤ → ℤ |
| Surjective (onto) | ∀b ∈ B, ∃a ∈ A: f(a) = b | f(x) = x mod 2 from ℤ → {0,1} |
| Bijective | Both injective and surjective | f(x) = x + 1 from ℤ → ℤ |

### Important Function Concepts

| Concept | Definition | Use Case |
|---------|------------|----------|
| Inverse function | f⁻¹ exists iff f is bijective | Decrypting encrypted data |
| Composition | (g ∘ f)(x) = g(f(x)) | Chaining transformations |
| Identity function | id(x) = x | Neutral element for composition |
| Fixed point | f(x) = x | Recursive definitions, semantics |
| Permutation | A bijection from a set to itself | Rearranging data, shuffling |

### Counting Functions

Given finite sets |A| = m and |B| = n:

| Type | Count |
|------|-------|
| All functions A → B | nᵐ |
| Injective functions | n! / (n−m)! (if n ≥ m, else 0) |
| Surjective functions | Σₖ₌₀ⁿ (−1)ᵏ · C(n,k) · (n−k)ᵐ (by inclusion-exclusion) |
| Bijective functions | n! (when m = n) |

---

## Combinatorics

Combinatorics is the mathematics of counting, arranging, and selecting.

### Fundamental Counting Principles

| Principle | Statement | Example |
|-----------|-----------|---------|
| Rule of Sum | If A and B are disjoint, |A ∪ B| = |A| + |B| | Choosing a fruit: 3 apples + 4 oranges = 7 options |
| Rule of Product | |A × B| = |A| · |B| | Outfit: 3 shirts × 4 pants = 12 outfits |
| Bijection Rule | If f: A → B is a bijection, |A| = |B| | Count subsets by counting binary strings |
| Complement | |A| = |U| − |Aᶜ| | Count "at least one" as total minus "none" |

### Permutations and Combinations

| Notation | Name | Formula | Meaning |
|----------|------|---------|---------|
| C(n, k) or (n k) | Binomial coefficient | n! / (k!(n−k)!) | Ways to choose k items from n (order doesn't matter) |
| P(n, k) | k-permutations of n | n! / (n−k)! | Ways to arrange k items from n (order matters) |
| n! | Factorial | n × (n−1) × ... × 1 | Ways to arrange all n items |
| (n k) with repetition | Multichoose | C(n+k−1, k) | Choose k from n with repetition allowed |

**Binomial Theorem:**
(x + y)ⁿ = Σₖ₌₀ⁿ C(n,k) · xᵏ · yⁿ⁻ᵏ

**Pascal's Identity:** C(n,k) = C(n−1,k−1) + C(n−1,k)

### The Pigeonhole Principle

**Basic form:** If n+1 objects are placed into n boxes, at least one box contains ≥ 2 objects.

**General form:** If N objects are placed into k boxes, at least one box contains ≥ ⌈N/k⌉ objects.

**Worked Examples:**

1. Among any 13 people, at least 2 share a birth month. (13 people, 12 months → pigeonhole.)

2. Show that among any 5 integers, there exist 3 whose sum is divisible by 3.
   - Consider residues mod 3: {0, 1, 2}. With 5 integers and 3 residue classes, by generalized pigeonhole, at least ⌈5/3⌉ = 2 share a residue.
   - If 3 share a residue r: their sum ≡ 3r ≡ 0 (mod 3).
   - If 2 share residue 0 and 2 share residue 1: pick one from each pair plus a residue-0 element → sum ≡ 0 (mod 3).

3. **Application in CS:** Any lossless compression algorithm must expand some inputs. (If every n-bit string compressed to < n bits, you'd map 2ⁿ strings into fewer than 2ⁿ compressed strings — violating injectivity.)

### Catalan Numbers

The nth **Catalan number** Cₙ = C(2n, n) / (n+1) counts:

| Structure | Example |
|-----------|---------|
| Valid parenthesis sequences | ()(), (()) for n = 2 |
| Binary trees with n internal nodes | 2 trees for n = 2 |
| Paths not crossing the diagonal | Grid paths from (0,0) to (n,n) staying below y = x |
| Triangulations of a polygon | Ways to divide an (n+2)-gon into triangles |

First few: C₀ = 1, C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42.

Recurrence: Cₙ₊₁ = Σᵢ₌₀ⁿ Cᵢ · Cₙ₋ᵢ

---

## Recurrence Relations

A **recurrence relation** defines each term of a sequence as a function of preceding terms.

### Types and Solutions

| Type | Form | Solution Method |
|------|------|-----------------|
| Linear homogeneous (constant coeff.) | aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ | Characteristic equation |
| Linear non-homogeneous | aₙ = c₁aₙ₋₁ + ... + f(n) | Particular solution + homogeneous solution |
| Divide and conquer | T(n) = aT(n/b) + f(n) | Master theorem |

### Characteristic Equation Method

For aₙ = c₁aₙ₋₁ + c₂aₙ₋₂, form the characteristic equation:
r² − c₁r − c₂ = 0

| Case | Roots | General Solution |
|------|-------|------------------|
| Two distinct real roots r₁, r₂ | r₁ ≠ r₂ | aₙ = A·r₁ⁿ + B·r₂ⁿ |
| Repeated root r | r₁ = r₂ = r | aₙ = (A + Bn)·rⁿ |
| Complex roots α ± βi | Convert to polar: r·e^(±iθ) | aₙ = rⁿ(A cos(nθ) + B sin(nθ)) |

**Worked Example:** Fibonacci sequence Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1.
- Characteristic equation: r² − r − 1 = 0
- Roots: r = (1 ± √5) / 2 → φ = (1+√5)/2 ≈ 1.618, ψ = (1−√5)/2 ≈ −0.618
- General solution: Fₙ = A·φⁿ + B·ψⁿ
- From initial conditions: A = 1/√5, B = −1/√5
- **Closed form:** Fₙ = (φⁿ − ψⁿ) / √5 (Binet's formula)

### The Master Theorem

For recurrences of the form T(n) = aT(n/b) + f(n) where a ≥ 1, b > 1:

Let c = log_b(a).

| Case | Condition | Solution |
|------|-----------|----------|
| 1 | f(n) = O(nᵈ) where d < c | T(n) = Θ(nᶜ) |
| 2 | f(n) = Θ(nᶜ) | T(n) = Θ(nᶜ log n) |
| 3 | f(n) = Θ(nᵈ) where d > c, and af(n/b) ≤ kf(n) for some k < 1 | T(n) = Θ(nᵈ) |

**Examples:**
- Merge sort: T(n) = 2T(n/2) + O(n). Here a=2, b=2, c=1, f(n)=n=Θ(n¹). Case 2: T(n) = Θ(n log n).
- Binary search: T(n) = T(n/2) + O(1). Here a=1, b=2, c=0, f(n)=1=Θ(n⁰). Case 2: T(n) = Θ(log n).

---

## Generating Functions

A **generating function** encodes a sequence (aₙ) as coefficients of a formal power series.

### Types

| Type | Form | Use Case |
|------|------|----------|
| Ordinary (OGF) | G(x) = Σₙ₌₀^∞ aₙxⁿ | Unlabelled structures, compositions |
| Exponential (EGF) | E(x) = Σₙ₌₀^∞ aₙxⁿ/n! | Labelled structures, permutations |

### Common Generating Functions

| Sequence aₙ | OGF G(x) |
|-------------|-----------|
| 1, 1, 1, 1, ... | 1/(1−x) |
| 1, 2, 3, 4, ... | 1/(1−x)² |
| 1, r, r², r³, ... | 1/(1−rx) |
| C(n,k) for fixed k | xᵏ/(1−x)ᵏ⁺¹ |
| Fibonacci Fₙ | x/(1−x−x²) |
| Catalan Cₙ | (1 − √(1−4x)) / (2x) |

### Using Generating Functions to Solve Recurrences

**Worked Example:** Solve aₙ = 3aₙ₋₁ − 2aₙ₋₂, a₀ = 1, a₁ = 3.

1. Let G(x) = Σ aₙxⁿ.
2. From the recurrence: G(x) − a₀ − a₁x = 3x(G(x) − a₀) − 2x²G(x)
3. Substitute: G(x) − 1 − 3x = 3x(G(x) − 1) − 2x²G(x)
4. G(x)(1 − 3x + 2x²) = 1
5. G(x) = 1 / (1 − 3x + 2x²) = 1 / ((1−x)(1−2x))
6. Partial fractions: G(x) = 2/(1−2x) − 1/(1−x)
7. Extract coefficients: aₙ = 2·2ⁿ − 1 = 2ⁿ⁺¹ − 1

**Verification:** a₀ = 2−1 = 1, a₁ = 4−1 = 3, a₂ = 8−1 = 7. Check: 3(3) − 2(1) = 7.

---

## Boolean Algebra and Propositional Logic

Boolean algebra is the algebra of two truth values: **True (1)** and **False (0)**. It is the mathematical foundation of digital circuits, database queries, and programming conditionals.

### Operations and Laws

| Operation | Symbol | Meaning | Truth Table |
|-----------|--------|---------|-------------|
| AND | p ∧ q | True only when both are true | T∧T=T, T∧F=F, F∧T=F, F∧F=F |
| OR | p ∨ q | True when at least one is true | T∨T=T, T∨F=T, F∨T=T, F∨F=F |
| NOT | ¬p | Negation | ¬T=F, ¬F=T |
| XOR | p ⊕ q | True when exactly one is true | T⊕T=F, T⊕F=T, F⊕T=T, F⊕F=F |
| IMPLIES | p → q | False only when p=T and q=F | T→T=T, T→F=F, F→T=T, F→F=T |
| BICONDITIONAL | p ↔ q | True when both have same value | T↔T=T, T↔F=F, F↔T=F, F↔F=T |

### Key Boolean Identities

| Law | Formula |
|-----|--------|
| Commutativity | p ∧ q = q ∧ p; p ∨ q = q ∨ p |
| Associativity | (p ∧ q) ∧ r = p ∧ (q ∧ r) |
| Distributivity | p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) |
| De Morgan's Laws | ¬(p ∧ q) = ¬p ∨ ¬q; ¬(p ∨ q) = ¬p ∧ ¬q |
| Double Negation | ¬(¬p) = p |
| Idempotence | p ∧ p = p; p ∨ p = p |
| Absorption | p ∨ (p ∧ q) = p; p ∧ (p ∨ q) = p |
| Contrapositive | (p → q) ≡ (¬q → ¬p) |

### Normal Forms

| Form | Structure | Use Case |
|------|-----------|----------|
| Conjunctive Normal Form (CNF) | AND of ORs: (A∨B) ∧ (C∨D) | SAT solvers, resolution theorem proving |
| Disjunctive Normal Form (DNF) | OR of ANDs: (A∧B) ∨ (C∧D) | Circuit design, rule-based systems |

**Converting to CNF:** Apply De Morgan's laws, distribute OR over AND, eliminate double negations.

---

## Modular Arithmetic and Congruences

Modular arithmetic studies integers under the operation of "remainder after division." It is essential for cryptography, hashing, and number theory.

### Core Definitions

| Concept | Notation | Definition |
|---------|----------|------------|
| Congruence | a ≡ b (mod n) | n divides (a − b) |
| Residue class | [a]ₙ | The set {a + kn : k ∈ ℤ} |
| Modular inverse | a⁻¹ mod n | Value x such that ax ≡ 1 (mod n) |
| Euler's totient | φ(n) | Count of integers in {1,...,n} coprime to n |

### Key Properties

| Property | Statement |
|----------|----------|
| Addition | If a ≡ b and c ≡ d (mod n), then a+c ≡ b+d (mod n) |
| Multiplication | If a ≡ b and c ≡ d (mod n), then ac ≡ bd (mod n) |
| Fermat's Little Theorem | If p is prime and gcd(a,p) = 1, then aᵖ⁻¹ ≡ 1 (mod p) |
| Euler's Theorem | If gcd(a,n) = 1, then a^φ(n) ≡ 1 (mod n) |
| Chinese Remainder Theorem | If gcd(m,n) = 1, the system x ≡ a (mod m), x ≡ b (mod n) has a unique solution mod mn |

### Computing Euler's Totient

For n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ (prime factorization):
φ(n) = n · (1 − 1/p₁) · (1 − 1/p₂) · ... · (1 − 1/pₖ)

**Example:** φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. Indeed, {1, 5, 7, 11} are coprime to 12.

### Application: RSA Cryptography (Overview)

1. Choose large primes p, q. Compute n = pq, φ(n) = (p−1)(q−1).
2. Choose e such that gcd(e, φ(n)) = 1 (public exponent).
3. Compute d ≡ e⁻¹ (mod φ(n)) (private exponent).
4. Encrypt: c = mᵉ mod n. Decrypt: m = cᵈ mod n.
5. Security relies on the difficulty of factoring n to find p and q.

---

## Mathematical Induction

**Mathematical induction** is the primary proof technique for statements about all natural numbers.

### Structure of a Proof by Induction

1. **Base case:** Prove the statement for n = 0 (or n = 1).
2. **Inductive step:** Assume the statement holds for n = k (inductive hypothesis), then prove it for n = k + 1.

### Variants

| Variant | When to Use |
|---------|-------------|
| Simple induction | Prove P(k) → P(k+1) |
| Strong induction | Assume P(0), P(1), ..., P(k) to prove P(k+1) |
| Structural induction | Prove properties of recursively defined structures (trees, formulas) |
| Transfinite induction | Extend induction to well-ordered sets beyond ℕ |

**Worked Example (Strong Induction):** Prove every integer n ≥ 2 can be written as a product of primes.

- Base: n = 2 is prime, so it is a product of primes (itself).
- Inductive step: Assume true for all integers from 2 to k. Consider k+1.
  - If k+1 is prime, done.
  - If k+1 is composite, k+1 = ab where 2 ≤ a, b ≤ k. By the inductive hypothesis, both a and b are products of primes, so k+1 is a product of primes.

---

## Relevance to Machine Learning and Data Science

| Discrete Math Concept | Application in ML / Data Science |
|-----------------------|----------------------------------|
| Set theory | Database operations (SQL JOINs), feature set manipulation, probability events |
| Relations | Database schemas, entity-relationship modelling, knowledge graphs |
| Functions | Activation functions, feature transformations, mappings between spaces |
| Combinatorics | Feature selection (choosing k from n), hyperparameter grid search sizing |
| Pigeonhole principle | Hashing collisions, lower bounds on compression, information theory proofs |
| Recurrence relations | Dynamic programming, algorithm complexity analysis, time series models |
| Generating functions | Probability generating functions, solving combinatorial problems in feature engineering |
| Catalan numbers | Counting tree structures (decision trees), parsing expressions, stack operations |
| Graph theory (see next file) | Social network analysis, recommendation systems, knowledge representation |

---

## Summary

| Topic | Core Idea | Key Tool |
|-------|-----------|----------|
| Set Theory | Collections of distinct objects | ZFC axioms, cardinality, operations |
| Relations | Connections between elements | Equivalence relations, partial orders |
| Functions | Mappings between sets | Injectivity, surjectivity, bijection |
| Combinatorics | Counting arrangements | Binomial coefficients, pigeonhole principle |
| Recurrence Relations | Sequences defined recursively | Characteristic equations, Master theorem |
| Generating Functions | Sequences as power series | OGF/EGF, solving recurrences algebraically |

Discrete mathematics provides the language and tools for reasoning about finite or countable structures — which is precisely what computers manipulate. Every algorithm, data structure, database query, and cryptographic protocol rests on discrete foundations. Mastery of these topics sharpens problem-solving ability and provides the vocabulary for advanced study in algorithms, complexity theory, and machine learning.
