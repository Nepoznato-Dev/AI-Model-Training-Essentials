<!-- 
Этот файл был автоматически переведён с английского на русский.
Источник: math_and_logic.md
Примечание: технические термины, примеры кода и имена собственные могут оставаться на английском.
Чтобы улучшить точность, присылайте правки через pull request.
-->

# Mathematics и Logic

## What is Mathematics?

Mathematics is the study из numbers, shapes, patterns, и logical relationships. It is both a Наука и a Язык used to describe the universe. Mathematics is divided into branches including arithmetic, algebra, geometry, calculus, Статистика, и logic. Mathematics is the foundation из physics, engineering, computer Наука, Экономика, и many other fields.

## Arithmetic

Arithmetic is the branch из mathematics dealing с basic operations on numbers. the four fundamental operations are addition (+), subtraction (−), multiplication (×), и division (÷). the order из operations specifies the sequence в which calculations must be performed: Parentheses, Exponents, Multiplication и Division (left to right), Addition и Subtraction (left to right). This is often remembered as **PEMDAS** or **BODMAS**. A prime number is a whole number greater than 1 that has no divisors other than 1 и itself. the first prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23, и 29.

**Примеры:**
- Prime factorization: 84 = 2² × 3 × 7
- Greatest Common Divisor (GCD) из 24 и 36: 12
- Least Common Multiple (LCM) из 4 и 6: 12

## Algebra

Algebra uses letters и symbols to represent numbers и quantities в equations и formulas. A **variable** is a symbol (usually a letter) that represents an unknown or changing quantity. An **equation** states that two expressions are equal. Solving an equation means finding the value(s) из the variable(s) that make the equation true.

the **quadratic formula** solves equations из the form ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)


A **function** maps each input to exactly one output. Common functions include:
- Linear: y = mx + b (straight line, constant rate из change)
- Quadratic: y = ax² + bx + c (parabola, curved)
- Exponential: y = a × bˣ (growth or decay, rapid change)
- Logarithmic: y = log_b(x) (inverse из exponential)

**Key concepts:**
- Domain: the set из all possible input values
- Range: the set из all possible output values
- Slope: rate из change (m в y = mx + b)
- Intercept: where the function crosses the y-axis (b в y = mx + b)

## Geometry

Geometry is the branch из mathematics that studies shapes, sizes, positions, и properties из figures. A point has no size; it represents a location. A line extends infinitely в both directions. A line segment has two endpoints. An angle is formed by two rays sharing an endpoint.

**Key rules:**
- the sum из angles в a triangle is always 180 degrees.
- the sum из angles в a quadrilateral is always 360 degrees.
- the Pythagorean theorem: в a right triangle, a² + b² = c² (where c is the hypotenuse).
- Circle circumference: 2πr
- Circle area: πr²
- Sphere volume: (4/3)πr³

**π (pi)** is approximately 3.14159 и is the ratio из a circle's circumference to its diameter.

**Common geometric shapes:**
- Triangle: 3 sides, angles sum to 180°
- Square: 4 equal sides, 4 right angles
- Rectangle: 4 sides, opposite sides equal, 4 right angles
- Circle: no sides, continuous curved boundary
- Pentagon: 5 sides, angles sum to 540°
- Hexagon: 6 sides, angles sum to 720°

## Статистика и Probability

Статистика is the Наука из collecting, analysing, interpreting, и presenting Данные.

**Measures из central tendency:**
- **Mean** (average): sum из all values divided by the number из values
- **Median**: middle value when Данные is sorted (less sensitive to outliers)
- **Mode**: most frequently occurring value (can have multiple modes)

**Measures из spread:**
- **Range**: maximum - minimum
- **Дисперсия**: среднее квадратичное отклонение от среднего
- **Стандартное отклонение**: квадратный корень из дисперсии (в тех же единицах, что и данные)

Вероятность измеряет, насколько вероятно наступление события, и принимает значения от 0 (невозможно) до 1 (достоверно). Вероятность того, что два независимых события произойдут одновременно, равна произведению их отдельных вероятностей.

**Пример:** Вероятность выбросить 6 на честном кубике: 1/6. Вероятность выбросить две 6 подряд: (1/6) × (1/6) = 1/36.

## Вероятность в вычислениях и ML

**Случайная величина** — это переменная, значение которой зависит от результата случайного процесса. **Распределение вероятностей** описывает, насколько вероятен каждый исход.

**Распространённые распределения:**
- **Распределение Бернулли**: одно испытание с двумя исходами (например, подбрасывание монеты)
- **Биномиальное распределение**: число успехов в n независимых испытаниях Бернулли
- **Нормальное (гауссово) распределение**: колоколообразная кривая, симметричная относительно среднего (часто встречается в природных явлениях)
- **Распределение Пуассона**: число событий за фиксированный интервал (например, количество писем в час)

**Ожидаемое значение** — это средний результат случайной величины на длинной дистанции. **Дисперсия** измеряет разброс вокруг этого ожидания.

**Conditional probability** describes the probability из an event given another event has occurred: P(A|B) = P(A ∩ B) / P(B) [if P(B) > 0].

**Bayes' theorem** updates beliefs using evidence: P(A|B) = P(B|A) × P(A) / P(B).


в Машинное обучение, probability underpins classification confidence, uncertainty estimation, Bayesian methods, и many loss functions (such as cross-entropy).

## Calculus

Calculus is the branch из mathematics that studies continuous change.

**Differential calculus** deals с rates из change и slopes из curves, using **derivatives**. the derivative из a function f(x) represents the rate из change из f с respect to x at a point. Notation: f'(x) or df/dx.

**Common derivatives:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Integral calculus** deals с accumulation из quantities и areas under curves, using **integrals**. the integral represents the area under the curve between two points.

the **fundamental theorem из calculus** connects differentiation и integration: differentiation и integration are inverse operations.

Calculus was developed independently by Isaac Newton и Gottfried Wilhelm Leibniz в the 17th century.

## Number Системы

- **Natural numbers**: 1, 2, 3, 4, ... (counting numbers)
- **Whole numbers**: 0, 1, 2, 3, ... (natural numbers plus zero)
- **Integers**: ..., −2, −1, 0, 1, 2, ... (all whole numbers и their negatives)
- **Rational numbers**: numbers expressible as p/q where p и q are integers и q ≠ 0 (e.g., 1/2, 3/4, −5/3)
- **Irrational numbers**: cannot be expressed as a fraction (e.g., √2, π, e)
- **Real numbers**: all rational и irrational numbers (the number line)
- **Imaginary numbers**: involve the square root из negative numbers; i = √(−1)
- **Complex numbers**: combine real и imaginary parts (a + bi)

## Logic и Reasoning

Logic is the study из valid reasoning.

**Deductive reasoning** draws specific conclusions from general premises. If the premises are true и the argument is valid, the conclusion must be true.
- **Example:** All humans are mortal. Socrates is human. Therefore, Socrates is mortal.

**Inductive reasoning** draws general conclusions from specific observations. It does not guarantee the conclusion is true, but makes it probable.
- **Example:** Every swan I've seen is white. Therefore, all swans are white. (Note: this is false; black swans exist!)

**Common logical fallacies (errors в reasoning):**
- **Ad hominem**: attacking the person rather than the argument
- **Straw man**: misrepresenting an argument to make it easier to attack
- **False dichotomy**: presenting only two options when more exist
- **Circular reasoning**: using the conclusion as a premise
- **Appeal to authority**: claiming something is true because an authority says so
- **Ошибка post hoc**: предположение, что если A произошло раньше B, то A вызвало B

## Sets

A **set** is a collection из distinct objects.
- **Union** (A ∪ B): all elements from both sets
- **Intersection** (A ∩ B): only elements common to both
- **Empty set** (∅ or {}): contains no elements
- **Subset** (A ⊆ B): all elements из A are also в B
- **Venn diagrams**: visually represent relationships between sets

Set theory is the foundation из modern mathematics и logic.

## Binary и Number Bases

Computers represent Данные в **binary** (base 2), using only digits 0 и 1. Each binary digit is called a **bit**. Eight bits make one **byte**.

**Decimal** is the base-10 number system humans typically use.

**Hexadecimal** is base 16, using digits 0–9 и letters A–F, often used в Вычисления to represent binary Данные compactly.

**Conversions:**
- Binary 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

Converting between number bases is a fundamental concept в computer Наука.

## Linear Algebra для Developers и ML

Linear algebra studies vectors, matrices, и linear transformations.

A **vector** is an ordered list из numbers (e.g., features в an ML sample).
- Example: [23, 1.8, 175] represents a person's age, height, и weight

A **matrix** is a 2D array из numbers (e.g., model weights or dataset batches).
- Example: [[1, 2], [3, 4]] is a 2×2 matrix

**Matrix multiplication** combines linear transformations и is a core operation в graphics, simulation, и Нейронные сети.

**Dot product** measures similarity и projection between vectors:
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- Cosine similarity ranges from -1 (opposite) to 1 (same direction)

**Eigenvalues и eigenvectors** describe directions that are scaled (not rotated) by a matrix и are used в methods such as PCA (Principal Component Analysis).

**Rank** indicates how much independent information a matrix contains. Low-rank approximations are useful для compression и dimensionality reduction.

Most modern ML workloads rely heavily on optimized linear algebra libraries и hardware acceleration.
