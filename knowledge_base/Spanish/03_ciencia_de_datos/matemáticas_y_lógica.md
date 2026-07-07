<!-- 
This file was automatically translated from English to Spanish.
Source: math_and_logic.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mathematics y Logic

## What is Mathematics?

Mathematics is el study de numbers, shapes, patterns, y logical relationships. It is both a Ciencia y a Idioma used to describe el universe. Mathematics is divided into branches including arithmetic, algebra, geometry, calculus, Estadísticas, y logic. Mathematics is el foundation de physics, ingeniería, computer Ciencia, Economía, y many other fields.

## Arithmetic

Arithmetic is el branch de matemáticas dealing con basic operations on numbers. el four fundamental operations are addition (+), subtraction (−), multiplication (×), y division (÷). el order de operations specifies el sequence en which calculations must be performed: Parentheses, Exponents, Multiplication y Division (left to right), Addition y Subtraction (left to right). This is often remembered as **PEMDAS** or **BODMAS**. A prime number is a whole number greater than 1 that has no divisors other than 1 y itself. el first prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, y 29.

**Ejemplos:**
- Prime factorization: 84 = 2² × 3 × 7
- Greatest Common Divisor (GCD) de 24 y 36: 12
- Least Common Multiple (LCM) de 4 y 6: 12

## Algebra

Algebra uses letters y symbols to represent numbers y quantities en equations y formulas. A **variable** is a symbol (usually a letter) that represents an unknown or changing quantity. An **equation** states that two expressions are equal. Solving an equation means finding el value(s) del variable(s) that make el equation true.

el **quadratic formula** solves equations del form ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)


A **function** mapears each input to exactly one output. Common functions incluyen:
- Linear: y = mx + b (straight line, constant rate de change)
- Quadratic: y = ax² + bx + c (parabola, curved)
- Exponential: y = a × bˣ (growth or decay, rapid change)
- Logarithmic: y = log_b(x) (inverse de exponential)

**Key concepts:**
- Domain: el set de all possible input values
- Range: el set de all possible output values
- Slope: rate de change (m en y = mx + b)
- Intercept: where el function crosses el y-axis (b en y = mx + b)

## Geometry

Geometry is el branch de matemáticas that studies shapes, sizes, positions, y properties de figures. A point has no size; it represents a location. A line extends infinitely en both directions. A line segment has two endpoints. An angle is formed by two rays sharing an endpoint.

**Key rules:**
- el sum de angles en a triangle is always 180 degrees.
- el sum de angles en a quadrilateral is always 360 degrees.
- el Pythagorean theorem: en a right triangle, a² + b² = c² (where c is el hypotenuse).
- Circle circumference: 2πr
- Circle area: πr²
- Sphere volume: (4/3)πr³

**π (pi)** is approximately 3.14159 y is el ratio de a circle's circumference to its diameter.

**Common geometric shapes:**
- Triangle: 3 sides, angles sum to 180°
- Square: 4 equal sides, 4 right angles
- Rectangle: 4 sides, opposite sides equal, 4 right angles
- Circle: no sides, continuous curved boundary
- Pentagon: 5 sides, angles sum to 540°
- Hexagon: 6 sides, angles sum to 720°

## Estadísticas y Probability

Estadísticas is el Ciencia de collecting, analysing, interpreting, y presenting Datos.

**Measures de central tendency:**
- **Mean** (average): sum de all values divided by el number de values
- **Median**: middle value when Datos is sorted (less sensitive to outliers)
- **Mode**: most frequently occurring value (can have multiple modes)

**Measures de spread:**
- **Range**: maximum - minimum
- **Variance**: average de squared deviations from el mean
- **Standard deviation**: square root de variance (en same units as Datos)

Probability measures el likelihood de an event occurring, ranging from 0 (impossible) to 1 (certain). el probability de two independent Eventos both occurring is el product de their individual probabilities.

**Example:** Probability de rolling a 6 on a fair die: 1/6. Probability de rolling two 6s en a row: (1/6) × (1/6) = 1/36.

## Probability para Informática y ML

A **random variable** is a variable whose value depends on el outcome de a random process. A **probability distribution** describes how likely each outcome is.

**Common distributions:**
- **Bernoulli**: single trial con two outcomes (e.g., coin flip)
- **Binomial**: number de successes en n independent Bernoulli trials
- **Normal (Gaussian)**: bell curve, symmetric alrededor de el mean (common en natural phenomena)
- **Poisson**: number de Eventos en a fixed interval (e.g., emails per hour)

**Expected value** is el long-run average outcome de a random variable. **Variance** measures spread alrededor de that expectation.

**Conditional probability** describes el probability de an event given another event has occurred: P(A|B) = P(A ∩ B) / P(B) [if P(B) > 0].

**Bayes' theorem** updates beliefs using evidence: P(A|B) = P(B|A) × P(A) / P(B).


en Aprendizaje automático, probability underpins classification confidence, uncertainty estimation, Bayesian methods, y many loss functions (such as cross-entropy).

## Calculus

Calculus is el branch de matemáticas that studies continuous change.

**Differential calculus** deals con rates de change y slopes de curves, using **derivatives**. el derivative de a function f(x) represents el rate de change de f con respect to x at a point. Notation: f'(x) or df/dx.

**Common derivatives:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Integral calculus** deals con accumulation de quantities y areas under curves, using **integrals**. el integral represents el area under el curve between two points.

el **fundamental theorem de calculus** connects differentiation y integration: differentiation y integration are inverse operations.

Calculus was desarrolló independently by Isaac Newton y Gottfried Wilhelm Leibniz en el 17th century.

## Number Sistemas

- **Natural numbers**: 1, 2, 3, 4, ... (counting numbers)
- **Whole numbers**: 0, 1, 2, 3, ... (natural numbers plus zero)
- **Integers**: ..., −2, −1, 0, 1, 2, ... (all whole numbers y their negatives)
- **Rational numbers**: numbers expressible as p/q where p y q are integers y q ≠ 0 (e.g., 1/2, 3/4, −5/3)
- **Irrational numbers**: cannot be expressed as a fraction (e.g., √2, π, e)
- **Real numbers**: all rational y irrational numbers (el number line)
- **Imaginary numbers**: involve el square root de negative numbers; i = √(−1)
- **Complex numbers**: combine real y imaginary parts (a + bi)

## Logic y Reasoning

Logic is el study de valid razóning.

**Deductive razóning** draws specific conclusions from general premises. If el premises are true y el argument is valid, el conclusion must be true.
- **Example:** All humans are mortal. Socrates is human. Therefore, Socrates is mortal.

**Inductive razóning** draws general conclusions from specific observations. It does not guarantee el conclusion is true, but makes it probable.
- **Example:** Every swan I've seen is white. Therefore, all swans are white. (Note: this is false; black swans exist!)

**Common logical fallacies (errors en razóning):**
- **Ad hominem**: attacking el person rather than el argument
- **Straw man**: misrepresenting an argument to make it easier to attack
- **False dichotomy**: presenting only two options when more exist
- **Circular razóning**: using el conclusion as a premise
- **Appeal to authority**: claiming something is true because an authority says so
- **Post hoc fallacy**: assuming that because A happened before B, A caused B

## Sets

A **set** is a collection de distinct objects.
- **Union** (A ∪ B): all elements from both sets
- **Intersection** (A ∩ B): only elements common to both
- **Empty set** (∅ or {}): contains no elements
- **Subset** (A ⊆ B): all elements de A are also en B
- **Venn diagrams**: visually represent relationships between sets

Set theory is el foundation de modern matemáticas y logic.

## Binary y Number Bases

Computers represent Datos en **binary** (base 2), using only digits 0 y 1. Each binary digit is llamado a **bit**. Eight bits make one **byte**.

**Decimal** is el base-10 number system humans typically use.

**Hexadecimal** is base 16, using digits 0–9 y letters A–F, often used en Informática to represent binary Datos compactly.

**Conversions:**
- Binary 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

Converting between number bases is a fundamental concept en computer Ciencia.

## Linear Algebra para Developers y ML

Linear algebra studies vectors, matrices, y linear transformations.

A **vector** is an ordered list de numbers (e.g., features en an ML sample).
- Example: [23, 1.8, 175] represents a person's age, height, y weight

A **matrix** is a 2D array de numbers (e.g., model weights or dataset batches).
- Example: [[1, 2], [3, 4]] is a 2×2 matrix

**Matrix multiplication** combines linear transformations y is a core operation en graphics, simulation, y Redes neuronales.

**Dot product** measures similarity y projection between vectors:
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- Cosine similarity ranges from -1 (opposite) to 1 (same direction)

**Eigenvalues y eigenvectors** describe directions that are scaled (not rotated) by a matrix y are used en methods such as PCA (Principal Component Analysis).

**Rank** indicates how much independent information a matrix contains. Low-rank approximations are useful para compression y dimensionality reduction.

Most modern ML workloads rely heavily on optimized linear algebra libraries y hardware acceleration.