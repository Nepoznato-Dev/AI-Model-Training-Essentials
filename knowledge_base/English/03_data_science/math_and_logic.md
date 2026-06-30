# Mathematics and Logic

## What is Mathematics?

Mathematics is the study of numbers, shapes, patterns, and logical relationships. It is both a science and a language used to describe the universe. Mathematics is divided into branches including arithmetic, algebra, geometry, calculus, statistics, and logic. Mathematics is the foundation of physics, engineering, computer science, economics, and many other fields.

## Arithmetic

Arithmetic is the branch of mathematics dealing with basic operations on numbers. The four fundamental operations are addition (+), subtraction (−), multiplication (×), and division (÷). The order of operations specifies the sequence in which calculations must be performed: Parentheses, Exponents, Multiplication and Division (left to right), Addition and Subtraction (left to right). This is often remembered as **PEMDAS** or **BODMAS**. A prime number is a whole number greater than 1 that has no divisors other than 1 and itself. The first prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, and 29.

**Examples:**
- Prime factorization: 84 = 2² × 3 × 7
- Greatest Common Divisor (GCD) of 24 and 36: 12
- Least Common Multiple (LCM) of 4 and 6: 12

## Algebra

Algebra uses letters and symbols to represent numbers and quantities in equations and formulas. A **variable** is a symbol (usually a letter) that represents an unknown or changing quantity. An **equation** states that two expressions are equal. Solving an equation means finding the value(s) of the variable(s) that make the equation true.

The **quadratic formula** solves equations of the form ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)


A **function** maps each input to exactly one output. Common functions include:
- Linear: y = mx + b (straight line, constant rate of change)
- Quadratic: y = ax² + bx + c (parabola, curved)
- Exponential: y = a × bˣ (growth or decay, rapid change)
- Logarithmic: y = log_b(x) (inverse of exponential)

**Key concepts:**
- Domain: the set of all possible input values
- Range: the set of all possible output values
- Slope: rate of change (m in y = mx + b)
- Intercept: where the function crosses the y-axis (b in y = mx + b)

## Geometry

Geometry is the branch of mathematics that studies shapes, sizes, positions, and properties of figures. A point has no size; it represents a location. A line extends infinitely in both directions. A line segment has two endpoints. An angle is formed by two rays sharing an endpoint.

**Key rules:**
- The sum of angles in a triangle is always 180 degrees.
- The sum of angles in a quadrilateral is always 360 degrees.
- The Pythagorean theorem: in a right triangle, a² + b² = c² (where c is the hypotenuse).
- Circle circumference: 2πr
- Circle area: πr²
- Sphere volume: (4/3)πr³

**π (pi)** is approximately 3.14159 and is the ratio of a circle's circumference to its diameter.

**Common geometric shapes:**
- Triangle: 3 sides, angles sum to 180°
- Square: 4 equal sides, 4 right angles
- Rectangle: 4 sides, opposite sides equal, 4 right angles
- Circle: no sides, continuous curved boundary
- Pentagon: 5 sides, angles sum to 540°
- Hexagon: 6 sides, angles sum to 720°

## Statistics and Probability

Statistics is the science of collecting, analysing, interpreting, and presenting data.

**Measures of central tendency:**
- **Mean** (average): sum of all values divided by the number of values
- **Median**: middle value when data is sorted (less sensitive to outliers)
- **Mode**: most frequently occurring value (can have multiple modes)

**Measures of spread:**
- **Range**: maximum - minimum
- **Variance**: average of squared deviations from the mean
- **Standard deviation**: square root of variance (in same units as data)

Probability measures the likelihood of an event occurring, ranging from 0 (impossible) to 1 (certain). The probability of two independent events both occurring is the product of their individual probabilities.

**Example:** Probability of rolling a 6 on a fair die: 1/6. Probability of rolling two 6s in a row: (1/6) × (1/6) = 1/36.

## Probability for Computing and ML

A **random variable** is a variable whose value depends on the outcome of a random process. A **probability distribution** describes how likely each outcome is.

**Common distributions:**
- **Bernoulli**: single trial with two outcomes (e.g., coin flip)
- **Binomial**: number of successes in n independent Bernoulli trials
- **Normal (Gaussian)**: bell curve, symmetric around the mean (common in natural phenomena)
- **Poisson**: number of events in a fixed interval (e.g., emails per hour)

**Expected value** is the long-run average outcome of a random variable. **Variance** measures spread around that expectation.

**Conditional probability** describes the probability of an event given another event has occurred: P(A|B) = P(A ∩ B) / P(B) [if P(B) > 0].

**Bayes' theorem** updates beliefs using evidence: P(A|B) = P(B|A) × P(A) / P(B).


In machine learning, probability underpins classification confidence, uncertainty estimation, Bayesian methods, and many loss functions (such as cross-entropy).

## Calculus

Calculus is the branch of mathematics that studies continuous change.

**Differential calculus** deals with rates of change and slopes of curves, using **derivatives**. The derivative of a function f(x) represents the rate of change of f with respect to x at a point. Notation: f'(x) or df/dx.

**Common derivatives:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Integral calculus** deals with accumulation of quantities and areas under curves, using **integrals**. The integral represents the area under the curve between two points.

The **fundamental theorem of calculus** connects differentiation and integration: differentiation and integration are inverse operations.

Calculus was developed independently by Isaac Newton and Gottfried Wilhelm Leibniz in the 17th century.

## Number Systems

- **Natural numbers**: 1, 2, 3, 4, ... (counting numbers)
- **Whole numbers**: 0, 1, 2, 3, ... (natural numbers plus zero)
- **Integers**: ..., −2, −1, 0, 1, 2, ... (all whole numbers and their negatives)
- **Rational numbers**: numbers expressible as p/q where p and q are integers and q ≠ 0 (e.g., 1/2, 3/4, −5/3)
- **Irrational numbers**: cannot be expressed as a fraction (e.g., √2, π, e)
- **Real numbers**: all rational and irrational numbers (the number line)
- **Imaginary numbers**: involve the square root of negative numbers; i = √(−1)
- **Complex numbers**: combine real and imaginary parts (a + bi)

## Logic and Reasoning

Logic is the study of valid reasoning.

**Deductive reasoning** draws specific conclusions from general premises. If the premises are true and the argument is valid, the conclusion must be true.
- **Example:** All humans are mortal. Socrates is human. Therefore, Socrates is mortal.

**Inductive reasoning** draws general conclusions from specific observations. It does not guarantee the conclusion is true, but makes it probable.
- **Example:** Every swan I've seen is white. Therefore, all swans are white. (Note: this is false; black swans exist!)

**Common logical fallacies (errors in reasoning):**
- **Ad hominem**: attacking the person rather than the argument
- **Straw man**: misrepresenting an argument to make it easier to attack
- **False dichotomy**: presenting only two options when more exist
- **Circular reasoning**: using the conclusion as a premise
- **Appeal to authority**: claiming something is true because an authority says so
- **Post hoc fallacy**: assuming that because A happened before B, A caused B

## Sets

A **set** is a collection of distinct objects.
- **Union** (A ∪ B): all elements from both sets
- **Intersection** (A ∩ B): only elements common to both
- **Empty set** (∅ or {}): contains no elements
- **Subset** (A ⊆ B): all elements of A are also in B
- **Venn diagrams**: visually represent relationships between sets

Set theory is the foundation of modern mathematics and logic.

## Binary and Number Bases

Computers represent data in **binary** (base 2), using only digits 0 and 1. Each binary digit is called a **bit**. Eight bits make one **byte**.

**Decimal** is the base-10 number system humans typically use.

**Hexadecimal** is base 16, using digits 0–9 and letters A–F, often used in computing to represent binary data compactly.

**Conversions:**
- Binary 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

Converting between number bases is a fundamental concept in computer science.

## Linear Algebra for Developers and ML

Linear algebra studies vectors, matrices, and linear transformations.

A **vector** is an ordered list of numbers (e.g., features in an ML sample).
- Example: [23, 1.8, 175] represents a person's age, height, and weight

A **matrix** is a 2D array of numbers (e.g., model weights or dataset batches).
- Example: [[1, 2], [3, 4]] is a 2×2 matrix

**Matrix multiplication** combines linear transformations and is a core operation in graphics, simulation, and neural networks.

**Dot product** measures similarity and projection between vectors:
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- Cosine similarity ranges from -1 (opposite) to 1 (same direction)

**Eigenvalues and eigenvectors** describe directions that are scaled (not rotated) by a matrix and are used in methods such as PCA (Principal Component Analysis).

**Rank** indicates how much independent information a matrix contains. Low-rank approximations are useful for compression and dimensionality reduction.

Most modern ML workloads rely heavily on optimized linear algebra libraries and hardware acceleration.