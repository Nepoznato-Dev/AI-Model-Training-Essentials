---
# Metadata
title: "Mathematics"
description: "Number systems, algebra, geometry, calculus, set theory, linear algebra, and binary — the mathematical foundations for data science and ML"
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
    changes: "Split from math_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [mathematics, algebra, calculus, geometry, linear-algebra, number-theory, set-theory]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Matemáticas
Las matemáticas no son sólo una materia que se estudia en la escuela: sustentan casi todos los campos técnicos. La física lo utiliza para describir el universo. La informática lo utiliza para diseñar algoritmos. El aprendizaje automático lo utiliza para optimizar los pesos. Las finanzas lo utilizan para valorar el riesgo. No es necesario dominar cada rama, pero comprender el panorama (y saber dónde se aplica cada rama) hace que otros temas sean más fáciles de comprender.
---

## Sistemas numéricos
Antes que nada, es útil comprender los tipos de números con los que está trabajando. Cada capa extiende la anterior para resolver un problema que la capa anterior no pudo.
| Tipo de número | Qué incluye | Por qué se inventó | Ejemplo |
|---|---|---|---|
| Números naturales | 1, 2, 3, 4, ... | Contando cosas | 5 manzanas |
| Números enteros | 0, 1, 2, 3, ... | Representando "nada" | 0 grados |
| Enteros | ..., −2, −1, 0, 1, 2, ... | Deuda, temperatura bajo cero | −15°C |
| Números racionales | pag/q donde q ≠ 0 | Dividiendo las cosas de manera desigual | 1/3, 0,75 |
| Números irracionales | No se puede expresar como fracciones | Diagonales, círculos, crecimiento | √2, π, mi |
| Números reales | Todo racional + irracional | La recta numérica completa | 3.14159... |
| Números imaginarios | Múltiplos de i = √(−1) | Resolviendo x² + 1 = 0 | 3i |
| Números complejos | a + bi (real + imaginario) | Ingeniería eléctrica, mecánica cuántica | 2+3i |
---

## Aritmética y teoría de números
Lo básico: suma, resta, multiplicación, división y las reglas que rigen su orden.
**Orden de operaciones** (PEMDAS/BODMAS): Paréntesis → Exponentes → Multiplicación/División (de izquierda a derecha) → Suma/Resta (de izquierda a derecha).
**Los números primos** (números enteros mayores que 1 sin más divisores que 1 y ellos mismos) son los átomos de la teoría de números. Los primeros: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Por qué los números primos son importantes más allá de la clase de matemáticas: el cifrado moderno (RSA) se basa en el hecho de que multiplicar dos números primos grandes es fácil, pero factorizar el resultado es computacionalmente brutal.
**Operaciones útiles:**
- Factorización prima: 84 = 2² × 3 × 7
- Máximo común divisor (MCD) de 24 y 36: 12
- Mínimo Común Múltiplo (MCM) de 4 y 6: 12
---

## Álgebra
Álgebra es donde dejas de trabajar con números específicos y comienzas a trabajar con *relaciones*. Una variable como`x`no tiene un valor fijo: representa lo que hace que la ecuación sea verdadera.
**La fórmula cuadrática** resuelve ax² + bx + c = 0:
x = (−b ± √(b² − 4ac)) / 2a
**Tipos de funciones comunes y dónde aparecen:**
| Función | Fórmula | Forma | Ejemplo del mundo real |
|---|---|---|---|
| Lineal | y = mx + b | Línea recta | Costo unitario a tanto alzado |
| Cuadrático | y = ax² + bx + c | Parábola | Movimiento de proyectil, distancia de frenado |
| Exponencial | y = a × b² | Rápido crecimiento/decadencia | Interés compuesto, crecimiento demográfico, propagación viral |
| Logarítmico | y = log_b(x) | Crecimiento lento, inverso al exponencial | Escala de decibeles, escala de pH, complejidad del algoritmo |
**Vocabulario clave:**
- **Dominio**: todas las entradas válidas (por ejemplo, no se puede dividir por cero, no se puede tomar √ de un negativo en reales)
- **Rango**: todas las salidas posibles
- **Pendiente** (m): tasa de cambio — "por cada unidad de x, y cambia en m"
- **Intersección**: donde la función cruza un eje
---

## Geometría
La geometría estudia formas, tamaños y relaciones espaciales. Aparece en todas partes: los motores de juegos lo usan para renderizar, la robótica lo usa para planificar rutas, la arquitectura lo usa para el diseño estructural.
**Fórmulas esenciales:**
| Forma | Propiedad | Fórmula |
|---|---|---|
| Triángulo | Suma de ángulos | 180° |
| Cuadrilátero | Suma de ángulos | 360° |
| Círculo | Circunferencia | 2πr |
| Círculo | Área | πr² |
| Esfera | Volumen | (4/3)πr³ |
| Triángulo rectángulo | Teorema de Pitágoras | a² + b² = c² |
**π (pi)** ≈ 3,14159 — la relación entre la circunferencia de cualquier círculo y su diámetro. Aparece en lugares que no se esperaría: probabilidad (distribución normal), ingeniería (procesamiento de señales), incluso la ecuación del principio de incertidumbre de Heisenberg.
---

## Cálculo
El cálculo estudia *cambio* y *acumulación*. Si el álgebra se ocupa de instantáneas, el cálculo se ocupa de imágenes en movimiento.
### Cálculo diferencial
Tasas de cambio. La derivada f'(x) indica qué tan rápido cambia f en cualquier punto.
| Función f(x) | Derivada f'(x) | Intuición |
|---|---|---|
| xⁿ | n·xⁿ⁻¹ | Regla de poder |
| miˣ | miˣ | La única función igual a su propia derivada |
| ln(x) | 1/x | La tasa de crecimiento se desacelera a medida que x aumenta |
| pecado(x) | porque(x) | Tasa de cambio de oscilación |
**Por qué las derivadas son importantes en ML:** el descenso de gradiente, el algoritmo que entrena la mayoría de las redes neuronales, funciona calculando las derivadas de la función de pérdida y avanzando en la dirección que reduce el error.
### Reglas clave de diferenciación
| Regla | Fórmula | Caso de uso |
|------|---------|----------|
| **Regla de la cadena** | (f∘g)' = f'(g(x)) · g'(x) | Funciones anidadas: retropropagación en redes neuronales |
| **Regla del producto** | (fg)' = f'g + fg' | Multiplicar dos funciones de x |
| **Regla del cociente** | (f/g)' = (f'g − fg') / g² | Dividiendo dos funciones de x |
### Cálculo integral
Acumulación. La integral representa el área bajo una curva. Si las derivadas responden "¿a qué velocidad está cambiando?", las integrales responden "¿cuánto se ha acumulado?"
El **teorema fundamental del cálculo** conecta ambos: la diferenciación y la integración son operaciones inversas.
| Integrales | Resultado | Caso de uso |
|----------|--------|----------|
| ∫xⁿdx | xⁿ⁺¹/(n+1) + C | Área bajo curvas polinomiales |
| ∫ eˣ dx | miˣ + C | Crecimiento total acumulado |
| ∫ 1/x dx | ln|x| + C | Acumulación logarítmica |
---

## Conjuntos
Un **conjunto** es una colección de objetos distintos: la base de las matemáticas modernas.
| Operación | Símbolo | Significado | Ejemplo (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Unión | A∪B | Elementos en cualquier conjunto | {1, 2, 3, 4} |
| Intersección | A∩B | Elementos en ambos conjuntos | {2} |
| Diferencia | A\B | Elementos en A pero no en B | {1, 3} |
| Conjunto vacío | ∅ | No contiene nada | {} |
| Subconjunto | A⊂B | Todos los elementos de A están en B | {1,2} ⊂ {1,2,3} |
La teoría de conjuntos aparece en las bases de datos (las JOIN SQL son esencialmente operaciones de conjuntos), la probabilidad (los eventos son conjuntos de resultados) y la programación (conjuntos, mapas hash).
---

## Bases binarias y numéricas
Las computadoras piensan en binario (base 2): solo 0 y 1. Los humanos piensan en decimal (base 10). Los programadores suelen utilizar hexadecimal (base 16) como una forma compacta de representar binario.
| Base | Dígitos utilizados | Ejemplo | Equivalente decimal |
|---|---|---|---|
| Binario (base 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| decimales (base 10) | 0–9 | 11 | 11 |
| Hexadecimal (base 16) | 0–9, A–F | B | 11 |
| Hexadecimal | 0–9, A–F | A3 | 160 + 3 = 163 |
**Por qué es importante:** cada dato en una computadora (texto, imágenes, audio, video) es, en última instancia, simplemente binario. Un byte (8 bits) puede representar 256 valores distintos. Los colores en CSS (#FF5733), las direcciones de memoria (0x7FFF) y las direcciones IP usan hexadecimal porque comprimen cadenas binarias largas en algo legible.
---

## Álgebra lineal para ML y gráficos
El álgebra lineal (vectores, matrices y transformaciones) es el motor matemático detrás del aprendizaje automático, los gráficos por computadora, las simulaciones físicas y los motores de búsqueda.
### Vectores
**Vectores** son listas ordenadas de números. En ML, cada punto de datos es un vector de características:
- [23, 1.8, 75] podría representar la edad de una persona, su altura en metros y su peso en kg.
| Operación vectorial | Fórmula | Caso de uso |
|-----------------|---------|----------|
| **Adición** | a + b = [a₁+b₁, a₂+b₂, ...] | Combinando vectores de características |
| **Multiplicación escalar** | c·a = [c·a₁, c·a₂, ...] | Funciones de escala |
| **Producto escalar** | a·b = Σaᵢbᵢ | Similitud, proyecciones |
| **Norma (magnitud)** | ||un|| = √(Σaᵢ²) | Longitud del vector |
| **Producto cruzado** | a × b (sólo 3D) | Vector perpendicular, área |
### Matrices
**Matrices** son matrices de números 2D. Los pesos de una red neuronal se almacenan como matrices. Un lote de 100 imágenes podría ser una matriz de forma (100, 784): 100 filas, cada una con valores de 784 píxeles.
**Operaciones clave:**
| Operación | Qué hace | Dónde aparece |
|---|---|---|
| Producto escalar | Mide la similitud entre dos vectores | Sistemas de recomendación, similitud coseno |
| Multiplicación de matrices | Combina transformaciones lineales | Cada capa de una red neuronal |
| Valores propios/vectores propios | Direcciones que una matriz escala (no gira) | Reducción de dimensionalidad PCA, PageRank |
| Rango de matriz | Cantidad de información independiente | Compresión, aproximación de rango bajo |
| Transponer | Voltea filas y columnas | Cálculo de gradiente |
| Inverso | A⁻¹ tal que A·A⁻¹ = I | Resolución de sistemas lineales |
**Similitud del coseno** = (a·b) / (||a|| × ||b||) — varía de −1 (opuesto) a 1 (misma dirección). Así es como los motores de búsqueda miden si dos documentos son "más o menos lo mismo" y cómo los modelos de incrustación comparan la similitud semántica.
---

## Resumen
| Sucursal | Pregunta central | Aplicación clave |
|---|---|---|
| Aritmética y teoría de números | ¿Cómo se comportan los números? | Criptografía, hash |
| Álgebra | ¿Cómo se relacionan las incógnitas? | Modelado, ecuaciones |
| Geometría | ¿Cómo funcionan las formas y los espacios? | Gráfica, robótica, arquitectura |
| Cálculo | ¿Cómo cambian las cosas? | Entrenamiento de redes neuronales, física |
| Teoría de conjuntos | ¿Cómo se relacionan las colecciones? | Bases de datos, probabilidad |
| Álgebra lineal | ¿Cómo funcionan las transformaciones? | ML, gráficos, motores de búsqueda |
No todos estos temas son necesarios de inmediato. Sin embargo, a medida que uno profundiza en cualquier campo técnico, estos fundamentos se vuelven cada vez más relevantes. Cada rama se vuelve más clara una vez que se comprende el problema para el que fue diseñada.