<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: math_and_logic.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mathematics 和 Logic

## What is Mathematics?

Mathematics is 这 study 的 numbers, shapes, patterns, 和 logical relationships. It is both a 科学 和 a 语言 used to describe 这 universe. Mathematics is divided into branches including arithmetic, algebra, geometry, calculus, 统计, 和 logic. Mathematics is 这 foundation 的 physics, engineering, computer 科学, 经济, 和 many other fields.

## Arithmetic

Arithmetic is 这 branch 的 mathematics dealing 与 basic operations on numbers. 这 four fundamental operations are addition (+), subtraction (−), multiplication (×), 和 division (÷). 这 order 的 operations specifies 这 sequence 在 which calculations must be performed: Parentheses, Exponents, Multiplication 和 Division (left to right), Addition 和 Subtraction (left to right). This is often remembered as **PEMDAS** or **BODMAS**. A prime number is a whole number greater than 1 that has no divisors other than 1 和 itself. 这 first prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, 和 29.

**示例:**
- Prime factorization: 84 = 2² × 3 × 7
- Greatest Common Divisor (GCD) 的 24 和 36: 12
- Least Common Multiple (LCM) 的 4 和 6: 12

## Algebra

Algebra uses letters 和 symbols to represent numbers 和 quantities 在 equations 和 formulas. A **variable** is a symbol (usually a letter) that represents an unknown or changing quantity. An **equation** states that two expressions are equal. Solving an equation means finding 这 value(s) 的 这 variable(s) that make 这 equation true.

这 **quadratic formula** solves equations 的 这 form ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)


A **function** maps each input to exactly one output. Common functions include:
- Linear: y = mx + b (straight line, constant rate 的 change)
- Quadratic: y = ax² + bx + c (parabola, curved)
- Exponential: y = a × bˣ (growth or decay, rapid change)
- Logarithmic: y = log_b(x) (inverse 的 exponential)

**Key concepts:**
- Domain: 这 set 的 all possible input values
- Range: 这 set 的 all possible output values
- Slope: rate 的 change (m 在 y = mx + b)
- Intercept: where 这 function crosses 这 y-axis (b 在 y = mx + b)

## Geometry

Geometry is 这 branch 的 mathematics that studies shapes, sizes, positions, 和 properties 的 figures. A point has no size; it represents a location. A line extends infinitely 在 both directions. A line segment has two endpoints. An angle is formed by two rays sharing an endpoint.

**Key rules:**
- 这 sum 的 angles 在 a triangle is always 180 degrees.
- 这 sum 的 angles 在 a quadrilateral is always 360 degrees.
- 这 Pythagorean theorem: 在 a right triangle, a² + b² = c² (where c is 这 hypotenuse).
- Circle circumference: 2πr
- Circle area: πr²
- Sphere volume: (4/3)πr³

**π (pi)** is approximately 3.14159 和 is 这 ratio 的 a circle's circumference to its diameter.

**Common geometric shapes:**
- Triangle: 3 sides, angles sum to 180°
- Square: 4 equal sides, 4 right angles
- Rectangle: 4 sides, opposite sides equal, 4 right angles
- Circle: no sides, continuous curved boundary
- Pentagon: 5 sides, angles sum to 540°
- Hexagon: 6 sides, angles sum to 720°

## 统计 和 Probability

统计 is 这 科学 的 collecting, analysing, interpreting, 和 presenting 数据.

**Measures 的 central tendency:**
- **Mean** (average): sum 的 all values divided by 这 number 的 values
- **Median**: middle value when 数据 is sorted (less sensitive to outliers)
- **Mode**: most frequently occurring value (can have multiple modes)

**Measures 的 spread:**
- **Range**: maximum - minimum
- **Variance**: average 的 squared deviations from 这 mean
- **Standard deviation**: square root 的 variance (在 same units as 数据)

Probability measures 这 likelihood 的 an event occurring, ranging from 0 (impossible) to 1 (certain). 这 probability 的 two independent 事件 both occurring is 这 product 的 their individual probabilities.

**Example:** Probability 的 rolling a 6 on a fair die: 1/6. Probability 的 rolling two 6s 在 a row: (1/6) × (1/6) = 1/36.

## Probability 为 计算 和 ML

A **random variable** is a variable whose value depends on 这 outcome 的 a random process. A **probability distribution** describes how likely each outcome is.

**Common distributions:**
- **Bernoulli**: single trial 与 two outcomes (e.g., coin flip)
- **Binomial**: number 的 successes 在 n independent Bernoulli trials
- **Normal (Gaussian)**: bell curve, symmetric around 这 mean (common 在 natural phenomena)
- **Poisson**: number 的 事件 在 a fixed interval (e.g., emails per hour)

**Expected value** is 这 long-run average outcome 的 a random variable. **Variance** measures spread around that expectation.

**Conditional probability** describes 这 probability 的 an event given another event has occurred: P(A|B) = P(A ∩ B) / P(B) [if P(B) > 0].

**Bayes' theorem** updates beliefs using evidence: P(A|B) = P(B|A) × P(A) / P(B).


在 机器学习, probability underpins classification confidence, uncertainty estimation, Bayesian methods, 和 many loss functions (such as cross-entropy).

## Calculus

Calculus is 这 branch 的 mathematics that studies continuous change.

**Differential calculus** deals 与 rates 的 change 和 slopes 的 curves, using **derivatives**. 这 derivative 的 a function f(x) represents 这 rate 的 change 的 f 与 respect to x at a point. Notation: f'(x) or df/dx.

**Common derivatives:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Integral calculus** deals 与 accumulation 的 quantities 和 areas under curves, using **integrals**. 这 integral represents 这 area under 这 curve between two points.

这 **fundamental theorem 的 calculus** connects differentiation 和 integration: differentiation 和 integration are inverse operations.

Calculus was developed independently by Isaac Newton 和 Gottfried Wilhelm Leibniz 在 这 17th century.

## Number 系统

- **Natural numbers**: 1, 2, 3, 4, ... (counting numbers)
- **Whole numbers**: 0, 1, 2, 3, ... (natural numbers plus zero)
- **Integers**: ..., −2, −1, 0, 1, 2, ... (all whole numbers 和 their negatives)
- **Rational numbers**: numbers expressible as p/q where p 和 q are integers 和 q ≠ 0 (e.g., 1/2, 3/4, −5/3)
- **Irrational numbers**: cannot be expressed as a fraction (e.g., √2, π, e)
- **Real numbers**: all rational 和 irrational numbers (这 number line)
- **Imaginary numbers**: involve 这 square root 的 negative numbers; i = √(−1)
- **Complex numbers**: combine real 和 imaginary parts (a + bi)

## Logic 和 Reasoning

Logic is 这 study 的 valid reasoning.

**Deductive reasoning** draws specific conclusions from general premises. If 这 premises are true 和 这 argument is valid, 这 conclusion must be true.
- **Example:** All humans are mortal. Socrates is human. Therefore, Socrates is mortal.

**Inductive reasoning** draws general conclusions from specific observations. It does not guarantee 这 conclusion is true, but makes it probable.
- **Example:** Every swan I've seen is white. Therefore, all swans are white. (Note: this is false; black swans exist!)

**Common logical fallacies (errors 在 reasoning):**
- **Ad hominem**: attacking 这 person rather than 这 argument
- **Straw man**: misrepresenting an argument to make it easier to attack
- **False dichotomy**: presenting only two options when more exist
- **Circular reasoning**: using 这 conclusion as a premise
- **Appeal to authority**: claiming something is true because an authority says so
- **Post hoc fallacy**: assuming that because A happened before B, A caused B

## Sets

A **set** is a collection 的 distinct objects.
- **Union** (A ∪ B): all elements from both sets
- **Intersection** (A ∩ B): only elements common to both
- **Empty set** (∅ or {}): contains no elements
- **Subset** (A ⊆ B): all elements 的 A are also 在 B
- **Venn diagrams**: visually represent relationships between sets

Set theory is 这 foundation 的 modern mathematics 和 logic.

## Binary 和 Number Bases

Computers represent 数据 在 **binary** (base 2), using only digits 0 和 1. Each binary digit is called a **bit**. Eight bits make one **byte**.

**Decimal** is 这 base-10 number system humans typically use.

**Hexadecimal** is base 16, using digits 0–9 和 letters A–F, often used 在 计算 to represent binary 数据 compactly.

**Conversions:**
- Binary 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

Converting between number bases is a fundamental concept 在 computer 科学.

## Linear Algebra 为 Developers 和 ML

Linear algebra studies vectors, matrices, 和 linear transformations.

A **vector** is an ordered list 的 numbers (e.g., features 在 an ML sample).
- Example: [23, 1.8, 175] represents a person's age, height, 和 weight

A **matrix** is a 2D array 的 numbers (e.g., model weights or dataset batches).
- Example: [[1, 2], [3, 4]] is a 2×2 matrix

**Matrix multiplication** combines linear transformations 和 is a core operation 在 graphics, simulation, 和 神经网络.

**Dot product** measures similarity 和 projection between vectors:
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- Cosine similarity ranges from -1 (opposite) to 1 (same direction)

**Eigenvalues 和 eigenvectors** describe directions that are scaled (not rotated) by a matrix 和 are used 在 methods such as PCA (Principal Component Analysis).

**Rank** indicates how much independent information a matrix contains. Low-rank approximations are useful 为 compression 和 dimensionality reduction.

Most modern ML workloads rely heavily on optimized linear algebra libraries 和 hardware acceleration.