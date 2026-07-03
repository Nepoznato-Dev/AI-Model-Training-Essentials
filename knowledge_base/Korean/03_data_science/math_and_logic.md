<!-- 
This file was automatically translated from English to Korean.
Source: math_and_logic.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mathematics 와 Logic

## What is Mathematics?

Mathematics is 그 study 의 numbers, shapes, patterns, 와 logical relationships. It is both a 과학 와 a 언어 used to describe 그 universe. Mathematics is divided into branches including arithmetic, algebra, geometry, calculus, 통계, 와 logic. Mathematics is 그 foundation 의 physics, engineering, computer 과학, 경제, 와 many other fields.

## Arithmetic

Arithmetic is 그 branch 의 mathematics dealing 와 함께 basic operations on numbers. 그 four fundamental operations are addition (+), subtraction (−), multiplication (×), 와 division (÷). 그 order 의 operations specifies 그 sequence 에서 which calculations must be performed: Parentheses, Exponents, Multiplication 와 Division (left to right), Addition 와 Subtraction (left to right). This is often remembered as **PEMDAS** or **BODMAS**. A prime number is a whole number greater than 1 that has no divisors other than 1 와 itself. 그 first prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 와 29.

**예시:**
- Prime factorization: 84 = 2² × 3 × 7
- Greatest Common Divisor (GCD) 의 24 와 36: 12
- Least Common Multiple (LCM) 의 4 와 6: 12

## Algebra

Algebra uses letters 와 symbols to represent numbers 와 quantities 에서 equations 와 formulas. A **variable** is a symbol (usually a letter) that represents an unknown or changing quantity. An **equation** states that two expressions are equal. Solving an equation means finding 그 value(s) 의 그 variable(s) that make 그 equation true.

그 **quadratic formula** solves equations 의 그 form ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)


A **function** maps each input to exactly one output. Common functions include:
- Linear: y = mx + b (straight line, constant rate 의 change)
- Quadratic: y = ax² + bx + c (parabola, curved)
- Exponential: y = a × bˣ (growth or decay, rapid change)
- Logarithmic: y = log_b(x) (inverse 의 exponential)

**Key concepts:**
- Domain: 그 set 의 all possible input values
- Range: 그 set 의 all possible output values
- Slope: rate 의 change (m 에서 y = mx + b)
- Intercept: where 그 function crosses 그 y-axis (b 에서 y = mx + b)

## Geometry

Geometry is 그 branch 의 mathematics that studies shapes, sizes, positions, 와 properties 의 figures. A point has no size; it represents a location. A line extends infinitely 에서 both directions. A line segment has two endpoints. An angle is formed by two rays sharing an endpoint.

**Key rules:**
- 그 sum 의 angles 에서 a triangle is always 180 degrees.
- 그 sum 의 angles 에서 a quadrilateral is always 360 degrees.
- 그 Pythagorean theorem: 에서 a right triangle, a² + b² = c² (where c is 그 hypotenuse).
- Circle circumference: 2πr
- Circle area: πr²
- Sphere volume: (4/3)πr³

**π (pi)** is approximately 3.14159 와 is 그 ratio 의 a circle's circumference to its diameter.

**Common geometric shapes:**
- Triangle: 3 sides, angles sum to 180°
- Square: 4 equal sides, 4 right angles
- Rectangle: 4 sides, opposite sides equal, 4 right angles
- Circle: no sides, continuous curved boundary
- Pentagon: 5 sides, angles sum to 540°
- Hexagon: 6 sides, angles sum to 720°

## 통계 와 Probability

통계 is 그 과학 의 collecting, analysing, interpreting, 와 presenting 데이터.

**Measures 의 central tendency:**
- **Mean** (average): sum 의 all values divided by 그 number 의 values
- **Median**: middle value when 데이터 is sorted (less sensitive to outliers)
- **Mode**: most frequently occurring value (can have multiple modes)

**Measures 의 spread:**
- **Range**: maximum - minimum
- **Variance**: average 의 squared deviations from 그 mean
- **Standard deviation**: square root 의 variance (에서 same units as 데이터)

Probability measures 그 likelihood 의 an event occurring, ranging from 0 (impossible) to 1 (certain). 그 probability 의 two independent 이벤트 both occurring is 그 product 의 their individual probabilities.

**Example:** Probability 의 rolling a 6 on a fair die: 1/6. Probability 의 rolling two 6s 에서 a row: (1/6) × (1/6) = 1/36.

## Probability 위한 컴퓨팅 와 ML

A **random variable** is a variable whose value depends on 그 outcome 의 a random process. A **probability distribution** describes how likely each outcome is.

**Common distributions:**
- **Bernoulli**: single trial 와 함께 two outcomes (e.g., coin flip)
- **Binomial**: number 의 successes 에서 n independent Bernoulli trials
- **Normal (Gaussian)**: bell curve, symmetric around 그 mean (common 에서 natural phenomena)
- **Poisson**: number 의 이벤트 에서 a fixed interval (e.g., emails per hour)

**Expected value** is 그 long-run average outcome 의 a random variable. **Variance** measures spread around that expectation.

**Conditional probability** describes 그 probability 의 an event given another event has occurred: P(A|B) = P(A ∩ B) / P(B) [if P(B) > 0].

**Bayes' theorem** updates beliefs using evidence: P(A|B) = P(B|A) × P(A) / P(B).


에서 기계 학습, probability underpins classification confidence, uncertainty estimation, Bayesian methods, 와 many loss functions (such as cross-entropy).

## Calculus

Calculus is 그 branch 의 mathematics that studies continuous change.

**Differential calculus** deals 와 함께 rates 의 change 와 slopes 의 curves, using **derivatives**. 그 derivative 의 a function f(x) represents 그 rate 의 change 의 f 와 함께 respect to x at a point. Notation: f'(x) or df/dx.

**Common derivatives:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Integral calculus** deals 와 함께 accumulation 의 quantities 와 areas under curves, using **integrals**. 그 integral represents 그 area under 그 curve between two points.

그 **fundamental theorem 의 calculus** connects differentiation 와 integration: differentiation 와 integration are inverse operations.

Calculus was developed independently by Isaac Newton 와 Gottfried Wilhelm Leibniz 에서 그 17th century.

## Number 시스템

- **Natural numbers**: 1, 2, 3, 4, ... (counting numbers)
- **Whole numbers**: 0, 1, 2, 3, ... (natural numbers plus zero)
- **Integers**: ..., −2, −1, 0, 1, 2, ... (all whole numbers 와 their negatives)
- **Rational numbers**: numbers expressible as p/q where p 와 q are integers 와 q ≠ 0 (e.g., 1/2, 3/4, −5/3)
- **Irrational numbers**: cannot be expressed as a fraction (e.g., √2, π, e)
- **Real numbers**: all rational 와 irrational numbers (그 number line)
- **Imaginary numbers**: involve 그 square root 의 negative numbers; i = √(−1)
- **Complex numbers**: combine real 와 imaginary parts (a + bi)

## Logic 와 Reasoning

Logic is 그 study 의 valid reasoning.

**Deductive reasoning** draws specific conclusions from general premises. If 그 premises are true 와 그 argument is valid, 그 conclusion must be true.
- **Example:** All humans are mortal. Socrates is human. Therefore, Socrates is mortal.

**Inductive reasoning** draws general conclusions from specific observations. It does not guarantee 그 conclusion is true, but makes it probable.
- **Example:** Every swan I've seen is white. Therefore, all swans are white. (Note: this is false; black swans exist!)

**Common logical fallacies (errors 에서 reasoning):**
- **Ad hominem**: attacking 그 person rather than 그 argument
- **Straw man**: misrepresenting an argument to make it easier to attack
- **False dichotomy**: presenting only two options when more exist
- **Circular reasoning**: using 그 conclusion as a premise
- **Appeal to authority**: claiming something is true because an authority says so
- **Post hoc fallacy**: assuming that because A happened before B, A caused B

## Sets

A **set** is a collection 의 distinct objects.
- **Union** (A ∪ B): all elements from both sets
- **Intersection** (A ∩ B): only elements common to both
- **Empty set** (∅ or {}): contains no elements
- **Subset** (A ⊆ B): all elements 의 A are also 에서 B
- **Venn diagrams**: visually represent relationships between sets

Set theory is 그 foundation 의 modern mathematics 와 logic.

## Binary 와 Number Bases

Computers represent 데이터 에서 **binary** (base 2), using only digits 0 와 1. Each binary digit is called a **bit**. Eight bits make one **byte**.

**Decimal** is 그 base-10 number system humans typically use.

**Hexadecimal** is base 16, using digits 0–9 와 letters A–F, often used 에서 컴퓨팅 to represent binary 데이터 compactly.

**Conversions:**
- Binary 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

Converting between number bases is a fundamental concept 에서 computer 과학.

## Linear Algebra 위한 Developers 와 ML

Linear algebra studies vectors, matrices, 와 linear transformations.

A **vector** is an ordered list 의 numbers (e.g., features 에서 an ML sample).
- Example: [23, 1.8, 175] represents a person's age, height, 와 weight

A **matrix** is a 2D array 의 numbers (e.g., model weights or dataset batches).
- Example: [[1, 2], [3, 4]] is a 2×2 matrix

**Matrix multiplication** combines linear transformations 와 is a core operation 에서 graphics, simulation, 와 신경망.

**Dot product** measures similarity 와 projection between vectors:
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- Cosine similarity ranges from -1 (opposite) to 1 (same direction)

**Eigenvalues 와 eigenvectors** describe directions that are scaled (not rotated) by a matrix 와 are used 에서 methods such as PCA (Principal Component Analysis).

**Rank** indicates how much independent information a matrix contains. Low-rank approximations are useful 위한 compression 와 dimensionality reduction.

Most modern ML workloads rely heavily on optimized linear algebra libraries 와 hardware acceleration.