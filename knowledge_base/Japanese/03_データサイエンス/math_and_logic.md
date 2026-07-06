<!-- 
This file was automatically translated from English to Japanese.
Source: math_and_logic.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mathematics と Logic

## What is Mathematics?

Mathematics is その study の numbers, shapes, patterns, と logical relationships. It is both a 科学 と a 言語 used to describe その universe. Mathematics is divided into branches including arithmetic, algebra, geometry, calculus, 統計, と logic. Mathematics is その foundation の physics, engineering, computer 科学, 経済, と many other fields.

## Arithmetic

Arithmetic is その branch の mathematics dealing と basic operations on numbers. その four fundamental operations are addition (+), subtraction (−), multiplication (×), と division (÷). その order の operations specifies その sequence で which calculations must be performed: Parentheses, Exponents, Multiplication と Division (left to right), Addition と Subtraction (left to right). This is often remembered as **PEMDAS** or **BODMAS**. A prime number is a whole number greater than 1 that has no divisors other than 1 と itself. その first prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, と 29.

**例:**
- Prime factorization: 84 = 2² × 3 × 7
- Greatest Common Divisor (GCD) の 24 と 36: 12
- Least Common Multiple (LCM) の 4 と 6: 12

## Algebra

Algebra uses letters と symbols to represent numbers と quantities で equations と formulas. A **variable** is a symbol (usually a letter) that represents an unknown or changing quantity. An **equation** states that two expressions are equal. Solving an equation means finding その value(s) の その variable(s) that make その equation true.

その **quadratic formula** solves equations の その form ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)


A **function** maps each input to exactly one output. Common functions include:
- Linear: y = mx + b (straight line, constant rate の change)
- Quadratic: y = ax² + bx + c (parabola, curved)
- Exponential: y = a × bˣ (growth or decay, rapid change)
- Logarithmic: y = log_b(x) (inverse の exponential)

**Key concepts:**
- Domain: その set の all possible input values
- Range: その set の all possible output values
- Slope: rate の change (m で y = mx + b)
- Intercept: where その function crosses その y-axis (b で y = mx + b)

## Geometry

Geometry is その branch の mathematics that studies shapes, sizes, positions, と properties の figures. A point has no size; it represents a location. A line extends infinitely で both directions. A line segment has two endpoints. An angle is formed by two rays sharing an endpoint.

**Key rules:**
- その sum の angles で a triangle is always 180 degrees.
- その sum の angles で a quadrilateral is always 360 degrees.
- その Pythagorean theorem: で a right triangle, a² + b² = c² (where c is その hypotenuse).
- Circle circumference: 2πr
- Circle area: πr²
- Sphere volume: (4/3)πr³

**π (pi)** is approximately 3.14159 と is その ratio の a circle's circumference to its diameter.

**Common geometric shapes:**
- Triangle: 3 sides, angles sum to 180°
- Square: 4 equal sides, 4 right angles
- Rectangle: 4 sides, opposite sides equal, 4 right angles
- Circle: no sides, continuous curved boundary
- Pentagon: 5 sides, angles sum to 540°
- Hexagon: 6 sides, angles sum to 720°

## 統計 と Probability

統計 is その 科学 の collecting, analysing, interpreting, と presenting データ.

**Measures の central tendency:**
- **Mean** (average): sum の all values divided by その number の values
- **Median**: middle value when データ is sorted (less sensitive to outliers)
- **Mode**: most frequently occurring value (can have multiple modes)

**Measures の spread:**
- **Range**: maximum - minimum
- **Variance**: average の squared deviations from その mean
- **Standard deviation**: square root の variance (で same units as データ)

Probability measures その likelihood の an event occurring, ranging from 0 (impossible) to 1 (certain). その probability の two independent イベント both occurring is その product の their individual probabilities.

**Example:** Probability の rolling a 6 on a fair die: 1/6. Probability の rolling two 6s で a row: (1/6) × (1/6) = 1/36.

## Probability のために コンピューティング と ML

A **random variable** is a variable whose value depends on その outcome の a random process. A **probability distribution** describes how likely each outcome is.

**Common distributions:**
- **Bernoulli**: single trial と two outcomes (e.g., coin flip)
- **Binomial**: number の successes で n independent Bernoulli trials
- **Normal (Gaussian)**: bell curve, symmetric around その mean (common で natural phenomena)
- **Poisson**: number の イベント で a fixed interval (e.g., emails per hour)

**Expected value** is その long-run average outcome の a random variable. **Variance** measures spread around that expectation.

**Conditional probability** describes その probability の an event given another event has occurred: P(A|B) = P(A ∩ B) / P(B) [if P(B) > 0].

**Bayes' theorem** updates beliefs using evidence: P(A|B) = P(B|A) × P(A) / P(B).


で 機械学習, probability underpins classification confidence, uncertainty estimation, Bayesian methods, と many loss functions (such as cross-entropy).

## Calculus

Calculus is その branch の mathematics that studies continuous change.

**Differential calculus** deals と rates の change と slopes の curves, using **derivatives**. その derivative の a function f(x) represents その rate の change の f と respect to x at a point. Notation: f'(x) or df/dx.

**Common derivatives:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Integral calculus** deals と accumulation の quantities と areas under curves, using **integrals**. その integral represents その area under その curve between two points.

その **fundamental theorem の calculus** connects differentiation と integration: differentiation と integration are inverse operations.

Calculus was developed independently by Isaac Newton と Gottfried Wilhelm Leibniz で その 17th century.

## Number システム

- **Natural numbers**: 1, 2, 3, 4, ... (counting numbers)
- **Whole numbers**: 0, 1, 2, 3, ... (natural numbers plus zero)
- **Integers**: ..., −2, −1, 0, 1, 2, ... (all whole numbers と their negatives)
- **Rational numbers**: numbers expressible as p/q where p と q are integers と q ≠ 0 (e.g., 1/2, 3/4, −5/3)
- **Irrational numbers**: cannot be expressed as a fraction (e.g., √2, π, e)
- **Real numbers**: all rational と irrational numbers (その number line)
- **Imaginary numbers**: involve その square root の negative numbers; i = √(−1)
- **Complex numbers**: combine real と imaginary parts (a + bi)

## Logic と Reasoning

Logic is その study の valid reasoning.

**Deductive reasoning** draws specific conclusions from general premises. If その premises are true と その argument is valid, その conclusion must be true.
- **Example:** All humans are mortal. Socrates is human. Therefore, Socrates is mortal.

**Inductive reasoning** draws general conclusions from specific observations. It does not guarantee その conclusion is true, but makes it probable.
- **Example:** Every swan I've seen is white. Therefore, all swans are white. (Note: this is false; black swans exist!)

**Common logical fallacies (errors で reasoning):**
- **Ad hominem**: attacking その person rather than その argument
- **Straw man**: misrepresenting an argument to make it easier to attack
- **False dichotomy**: presenting only two options when more exist
- **Circular reasoning**: using その conclusion as a premise
- **Appeal to authority**: claiming something is true because an authority says so
- **Post hoc fallacy**: assuming that because A happened before B, A caused B

## Sets

A **set** is a collection の distinct objects.
- **Union** (A ∪ B): all elements from both sets
- **Intersection** (A ∩ B): only elements common to both
- **Empty set** (∅ or {}): contains no elements
- **Subset** (A ⊆ B): all elements の A are also で B
- **Venn diagrams**: visually represent relationships between sets

Set theory is その foundation の modern mathematics と logic.

## Binary と Number Bases

Computers represent データ で **binary** (base 2), using only digits 0 と 1. Each binary digit is called a **bit**. Eight bits make one **byte**.

**Decimal** is その base-10 number system humans typically use.

**Hexadecimal** is base 16, using digits 0–9 と letters A–F, often used で コンピューティング to represent binary データ compactly.

**Conversions:**
- Binary 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

Converting between number bases is a fundamental concept で computer 科学.

## Linear Algebra のために Developers と ML

Linear algebra studies vectors, matrices, と linear transformations.

A **vector** is an ordered list の numbers (e.g., features で an ML sample).
- Example: [23, 1.8, 175] represents a person's age, height, と weight

A **matrix** is a 2D array の numbers (e.g., model weights or dataset batches).
- Example: [[1, 2], [3, 4]] is a 2×2 matrix

**Matrix multiplication** combines linear transformations と is a core operation で graphics, simulation, と ニューラルネットワーク.

**Dot product** measures similarity と projection between vectors:
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- Cosine similarity ranges from -1 (opposite) to 1 (same direction)

**Eigenvalues と eigenvectors** describe directions that are scaled (not rotated) by a matrix と are used で methods such as PCA (Principal Component Analysis).

**Rank** indicates how much independent information a matrix contains. Low-rank approximations are useful のために compression と dimensionality reduction.

Most modern ML workloads rely heavily on optimized linear algebra libraries と hardware acceleration.