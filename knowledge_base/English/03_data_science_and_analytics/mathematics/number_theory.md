<!--
---
# Metadata
title: "Number Theory"
description: "Divisibility, primes, modular arithmetic, Euler's theorem, Fermat's little theorem, Chinese Remainder Theorem, and applications to cryptography"
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
    changes: "Initial deep-dive into number theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [number-theory, primes, divisibility, modular-arithmetic, cryptography, euler-theorem, fermat, chinese-remainder-theorem]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Number Theory

Number theory is the study of the integers — whole numbers and their properties. Gauss called it "the queen of mathematics." Despite studying the simplest objects (1, 2, 3, ...), number theory produces some of the deepest and hardest problems in all of mathematics. Today, it underpins modern cryptography, hashing algorithms, error-correcting codes, and random number generation.

---

## Divisibility and the Division Algorithm

### Core Definitions

| Term | Definition | Example |
|------|------------|---------|
| **Divides** | a \| b means ∃k ∈ ℤ: b = ak | 3 \| 12 (since 12 = 3 × 4) |
| **Divisor** | A number that divides another | Divisors of 12: 1, 2, 3, 4, 6, 12 |
| **Multiple** | b is a multiple of a if a \| b | 15 is a multiple of 5 |
| **Quotient** | The result of division | 17 ÷ 5 = quotient 3 |
| **Remainder** | What's left after division | 17 ÷ 5 = remainder 2 |

### The Division Algorithm

For any integers a and b with b > 0, there exist unique integers q (quotient) and r (remainder) such that:

a = bq + r, where 0 ≤ r < b

**Example:** 23 = 5 × 4 + 3. Quotient q = 4, remainder r = 3.

### Properties of Divisibility

| Property | Statement |
|----------|-----------|
| Transitivity | If a \| b and b \| c, then a \| c |
| Linearity | If a \| b and a \| c, then a \| (bx + cy) for all integers x, y |
| Comparison | If a \| b and b > 0, then a ≤ b |
| Trivial | a \| 0 for all a; 1 \| a for all a; a \| a for all a ≠ 0 |

---

## Greatest Common Divisor (GCD)

The **greatest common divisor** of a and b, denoted gcd(a, b), is the largest positive integer dividing both a and b.

### The Euclidean Algorithm

The most efficient classical algorithm for computing the GCD.

**Key insight:** gcd(a, b) = gcd(b, a mod b)

**Algorithm:**
```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Worked Example:** gcd(252, 105)
- 252 = 105 × 2 + 42 → gcd(105, 42)
- 105 = 42 × 2 + 21 → gcd(42, 21)
- 42 = 21 × 2 + 0 → gcd(21, 0)
- Result: gcd(252, 105) = 21

| Property | Value |
|----------|-------|
| Time complexity | O(log(min(a, b))) |
| Space complexity | O(1) iterative |

### Bézout's Identity

For any integers a, b, there exist integers x, y such that:

ax + by = gcd(a, b)

**Extended Euclidean Algorithm** computes gcd(a, b) and the coefficients x, y simultaneously.

**Worked Example:** Find x, y such that 252x + 105y = 21.
- Back-substituting from the Euclidean algorithm:
  - 21 = 105 − 42 × 2
  - 42 = 252 − 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 − 252 × 2
- So x = −2, y = 5. Check: 252(−2) + 105(5) = −504 + 525 = 21.

### Key Properties of GCD

| Property | Statement |
|----------|-----------|
| gcd(a, 0) | = a |
| gcd(a, 1) | = 1 (a and 1 are always coprime) |
| gcd(a, b) = gcd(b, a) | Commutative |
| gcd(a, b) = gcd(a, b + ka) | Adding multiples doesn't change GCD |
| gcd(ca, cb) | = c · gcd(a, b) |
| Coprime | gcd(a, b) = 1 means a and b share no common factors |

---

## Prime Numbers

A **prime** is an integer greater than 1 whose only positive divisors are 1 and itself.

### Fundamental Properties

| Property | Statement |
|----------|-----------|
| **Fundamental Theorem of Arithmetic** | Every integer n > 1 has a unique prime factorization |
| **Infinitude of primes** | There are infinitely many primes (Euclid, ~300 BC) |
| **Prime Number Theorem** | The number of primes ≤ n is approximately n / ln(n) |
| **Bertrand's Postulate** | For every n > 1, there exists a prime p with n < p < 2n |

### The First Primes

2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Prime Factorization

Every integer n > 1 can be written uniquely as:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ

where p₁ < p₂ < ... < pₖ are primes and aᵢ ≥ 1.

**Examples:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7 × 11 × 13

**Using factorization to compute GCD and LCM:**
- gcd(a, b) = product of min powers of shared primes
- lcm(a, b) = product of max powers of all primes

**Example:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- gcd(12, 18) = 2¹ × 3¹ = 6
- lcm(12, 18) = 2² × 3² = 36

### Sieve of Eratosthenes

The classical algorithm for finding all primes up to a limit N.

| Property | Value |
|----------|-------|
| Time complexity | O(N log log N) |
| Space complexity | O(N) |

**Algorithm:**
1. List all integers from 2 to N.
2. Start with p = 2. Cross out all multiples of p (starting from p²).
3. Find the next uncrossed number > p. Set p to that number.
4. Repeat until p² > N. All uncrossed numbers are prime.

### Primality Testing

| Method | Type | Time | Use Case |
|--------|------|------|----------|
| Trial division | Deterministic | O(√n) | Small numbers |
| Fermat test | Probabilistic | O(k log² n) | Quick screening |
| Miller-Rabin | Probabilistic | O(k log² n) | General purpose |
| AKS | Deterministic | O(log⁶ n) | Theoretical importance |

**Fermat primality test:** If p is prime and gcd(a, p) = 1, then aᵖ⁻¹ ≡ 1 (mod p). If this fails for some a, then p is definitely composite. If it passes for many random a values, p is probably prime.

**Caveat:** Carmichael numbers (e.g., 561) pass the Fermat test for all coprime bases but are composite. Miller-Rabin avoids this issue.

---

## Modular Arithmetic

Modular arithmetic studies integers under "wraparound" — arithmetic on a clock face.

### Congruence Relations

a ≡ b (mod n) means n | (a − b), i.e., a and b leave the same remainder when divided by n.

### Arithmetic Properties

| Operation | Rule |
|-----------|------|
| Addition | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Multiplication | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| Exponentiation | aᵇ mod n can be computed efficiently by repeated squaring |
| Negation | (−a) mod n = n − (a mod n) |

### Modular Exponentiation

Computing aᵇ mod n efficiently using **repeated squaring**:

**Worked Example:** 3¹³ mod 7
- 13 in binary: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3

| Property | Value |
|----------|-------|
| Time complexity | O(log b · log² n) |
| Space complexity | O(1) |

### Euler's Totient Function

φ(n) counts the integers from 1 to n that are coprime to n.

| n | φ(n) | Coprime integers |
|---|------|------------------|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 is prime) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |

**Formulas:**
- If p is prime: φ(p) = p − 1
- If p is prime: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- If gcd(m, n) = 1: φ(mn) = φ(m) · φ(n) (multiplicativity)
- General: φ(n) = n · Π_{p|n} (1 − 1/p) where the product is over distinct prime factors of n

---

## Key Theorems

### Fermat's Little Theorem

If p is prime and gcd(a, p) = 1, then:
aᵖ⁻¹ ≡ 1 (mod p)

**Corollary (for all a):** aᵖ ≡ a (mod p)

**Use:** Fast modular inverse when modulus is prime: a⁻¹ ≡ aᵖ⁻² (mod p)

**Worked Example:** Find 3⁻¹ mod 7.
- By Fermat: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Check: 3 × 5 = 15 ≡ 1 (mod 7).

### Euler's Theorem (Generalisation of Fermat)

If gcd(a, n) = 1, then:
a^φ(n) ≡ 1 (mod n)

This generalises Fermat's Little Theorem from primes to any modulus.

### Chinese Remainder Theorem (CRT)

If m₁, m₂, ..., mₖ are pairwise coprime, the system:
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (mod mₖ)

has a unique solution modulo M = m₁ · m₂ · ... · mₖ.

**Worked Example:** Solve x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Find inverses: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
- x ≡ 233 mod 105 = 23
- Check: 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.

### Wilson's Theorem

(p − 1)! ≡ −1 (mod p) if and only if p is prime.

Mostly of theoretical interest — not practical for primality testing since computing factorials is expensive.

### Quadratic Residues

An integer a is a **quadratic residue mod n** if x² ≡ a (mod n) has a solution.

**Euler's criterion:** a is a quadratic residue mod prime p iff a^((p−1)/2) ≡ 1 (mod p).

**Legendre symbol:** (a/p) = a^((p−1)/2) mod p, giving +1, −1, or 0.

**Quadratic Reciprocity** (Gauss): For distinct odd primes p, q:
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)

This deep theorem connects quadratic residues across different primes and has eight supplementary laws handling the cases p = 2.

---

## Applications to Cryptography

### RSA Cryptosystem

The most widely deployed public-key cryptosystem, based on the difficulty of factoring large integers.

**Setup:**
1. Choose two large primes p, q (typically 1024+ bits each)
2. Compute n = pq and φ(n) = (p−1)(q−1)
3. Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1 (common: e = 65537)
4. Compute d ≡ e⁻¹ (mod φ(n)) using the Extended Euclidean Algorithm
5. **Public key:** (n, e). **Private key:** (n, d)

**Encryption:** c = mᵉ mod n (where m is the plaintext message)
**Decryption:** m = cᵈ mod n

**Why it works:** cᵈ = m^(ed) ≡ m (mod n) by Euler's theorem, since ed ≡ 1 (mod φ(n)).

**Security:** Factoring n into p and q is computationally infeasible for large n (2048+ bits). Without p and q, an attacker cannot compute φ(n) and thus cannot find d.

### Diffie-Hellman Key Exchange

Allows two parties to establish a shared secret over an insecure channel.

**Setup:** Agree on a large prime p and a generator g (mod p).

**Protocol:**
1. Alice chooses secret a, sends A = gᵃ mod p to Bob
2. Bob chooses secret b, sends B = gᵇ mod p to Alice
3. Alice computes s = Bᵃ mod p = gᵃᵇ mod p
4. Bob computes s = Aᵇ mod p = gᵃᵇ mod p
5. Both share the secret s = gᵃᵇ mod p

**Security:** Based on the difficulty of the **discrete logarithm problem** — finding a from gᵃ mod p.

### Hash Functions and Number Theory

Good hash functions use modular arithmetic to distribute keys uniformly:
- **Multiplicative hashing:** h(k) = (k · A) mod m, where A ≈ m · (√5 − 1) / 2 (golden ratio)
- **Universal hashing:** h(k) = ((ak + b) mod p) mod m, where p is prime, a, b are random

---

## Relevance to Machine Learning and Data Science

| Number Theory Concept | Application |
|----------------------|-------------|
| Modular arithmetic | Hashing (hash tables, hash maps), random number generation |
| Prime numbers | Hash table sizing (use prime table sizes to reduce collisions) |
| GCD / Euclidean algorithm | Rational arithmetic, simplifying fractions in probability |
| Modular exponentiation | Cryptographic security for ML model serving over HTTPS |
| Euler's totient | RSA key generation, understanding cryptographic guarantees |
| Chinese Remainder Theorem | Distributed computation, parallel modular arithmetic |
| Primality testing | Generating primes for cryptographic operations |
| Quadratic residues | Quadratic residuosity problem in advanced cryptography |
| Finite fields (GF(p), GF(2ᵏ)) | Error-correcting codes, Reed-Solomon codes, AES encryption |

---

## Summary

| Topic | Core Idea | Key Result |
|-------|-----------|------------|
| Divisibility | Division with remainder | Division algorithm: a = bq + r |
| GCD | Largest shared factor | Euclidean algorithm: O(log n) |
| Primes | Atoms of the integers | Fundamental Theorem of Arithmetic (unique factorization) |
| Modular Arithmetic | Wraparound arithmetic | Congruence classes, modular exponentiation |
| Euler's Totient | Counting coprime integers | φ(n) = n · Π(1 − 1/p) |
| Fermat's Little Theorem | Prime modulus shortcut | aᵖ⁻¹ ≡ 1 (mod p) |
| Euler's Theorem | Generalised Fermat | a^φ(n) ≡ 1 (mod n) |
| Chinese Remainder Theorem | Combining modular systems | Unique solution mod product of coprime moduli |
| Cryptography | Hard number-theoretic problems | RSA (factoring), Diffie-Hellman (discrete log) |

Number theory transforms simple questions about integers into deep mathematics with profound practical applications. Every secure web connection, encrypted message, and digital signature relies on number-theoretic results discovered centuries before computers existed. For data scientists and ML engineers, understanding number theory provides insight into hashing, random number generation, and the cryptographic infrastructure that protects data in transit and at rest.
