---
# Metadata
title: "Numerical Methods"
description: "Floating-point arithmetic, root finding, numerical integration, ODE solvers, interpolation, numerical stability, and conditioning"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into numerical methods"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [numerical-methods, floating-point, root-finding, numerical-integration, ode-solvers, interpolation, stability]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Métodos numéricos
Los métodos numéricos son el puente entre la teoría matemática y la computación práctica. Si bien las matemáticas puras demuestran que existen soluciones, los métodos numéricos en realidad calculan respuestas aproximadas con precisión finita. Cada modelo de aprendizaje automático, simulación física y proceso de análisis de datos se basa en última instancia en la computación numérica. Comprender estos métodos (su precisión, estabilidad y limitaciones) es esencial para crear software confiable.
---

## Aritmética de coma flotante
Las computadoras representan números reales con precisión finita. El **estándar IEEE 754** define cómo se almacenan y manipulan los números de punto flotante.
### Formatos IEEE 754
| Formato | Puntas | Exponente | Mantisa | Dígitos decimales aproximados | Gama |
|--------|------|----------|----------|---------------------|-------|
| Mitad (fp16) | 16 | 5 | 10 | 3.3 | ±6,5 × 10⁴ |
| Soltero (fp32) | 32 | 8 | 23 | 7.2 | ±3,4 × 10³⁸ |
| Doble (fp64) | 64 | 11 | 52 | 15.9 | ±1,8 × 10³⁰⁸ |
### Máquina Épsilon
**Máquina épsilon** (ε_mach) es el número más pequeño tal que 1 + ε_mach > 1 en punto flotante.
| Formato | ε_mach |
|--------|--------|
| fp16 | 2⁻¹⁰ ≈ 9,8 × 10⁻⁴ |
| fp32 | 2⁻²³ ≈ 1,2 × 10⁻⁷ |
| fp64 | 2⁻⁵² ≈ 2,2 × 10⁻¹⁶ |
### Errores comunes
| Escollo | Ejemplo | Consecuencia |
|---------|---------|-------------|
| **Cancelación catastrófica** | Calcular (1 + x) − 1 para x pequeña | Pérdida de dígitos significativos |
| **Absorción** | 10⁸ + 1 = 10⁸ en fp32 | Pequeños valores perdidos en grandes sumas |
| **No asociatividad** | (a + b) + c ≠ a + (b + c) | El orden de la suma importa |
| **División por casi cero** | 1/10⁻³⁰⁰ → desbordamiento | Infinito o NaN |
### Estrategias de mitigación
| Estrategia | Descripción |
|----------|-------------|
| **Resumen de Kahan** | Suma compensada para reducir el error de absorción |
| **Kahan-Babuska-Neumaier** | Versión mejorada de la suma de Kahan |
| **Suma ordenada** | Primero sume números pequeños para evitar la absorción |
| **Aritmética doble-doble** | Utilice pares de dobles para mayor precisión |
| **Análisis de condicionamiento** | Comprenda si el problema en sí amplifica los errores |
---

## Búsqueda de raíces
Encontrar x tal que f(x) = 0.
### Método de bisección
| Propiedad | Valor |
|----------|-------|
| Requiere | f continua, f(a) y f(b) tienen signos opuestos |
| Convergencia | Lineal (el error se reduce a la mitad en cada paso) |
| ¿Garantizado? | Sí, siempre converge |
| Iteraciones para d dígitos | ≈ d / log₁₀(2) ≈ 3,32d |
**Algoritmo:**
1. Comience con el intervalo [a, b] donde f(a) · f(b) < 0
2. Calcular el punto medio c = (a + b) / 2
3. Si f(c) = 0 o |b − a| < tolerancia, parada
4. Si f(a) · f(c) < 0, establezca b = c; de lo contrario establezca a = c
5. Repetir
### Método Newton-Raphson
| Propiedad | Valor |
|----------|-------|
| Requiere | f diferenciable, f'(x) ≠ 0 en la raíz |
| Convergencia | Cuadrático (cerca de la raíz) |
| ¿Garantizado? | No: puede divergir o circular |
| Regla de actualización | x_{n+1} = x_n − f(x_n) / f'(x_n) |
**Ejemplo resuelto:** Encuentra √2 resolviendo f(x) = x² − 2 = 0.
-f'(x) = 2x
- x₀ = 1,5
- x₁ = 1,5 − (2,25 − 2) / 3 = 1,5 − 0,0833 = 1,4167
- x₂ = 1,4167 − (2,0069 − 2) / 2,8333 = 1,4142
- x₃ = 1,41421356... (correcto con 8 decimales)
### Método secante
Como el método de Newton pero se aproxima a la derivada:
x_{n+1} = x_n - f(x_n) · (x_n - x_{n-1}) / (f(x_n) - f(x_{n-1}))
| Propiedad | Valor |
|----------|-------|
| Convergencia | Superlineal (orden ≈ 1.618, la proporción áurea) |
| Requiere | Dos conjeturas iniciales (no se necesita derivada) |
### Comparación de métodos de búsqueda de raíces
| Método | Convergencia | ¿Se necesita un derivado? | ¿Garantizado? | Costo por paso |
|--------|-------------|-------------------|-------------|---------------|
| Bisección | Lineal (1) | No | Sí | 1 función de evaluación |
| Newton-Raphson | Cuadrática (2) | Sí | No | 2 evaluaciones de funciones |
| Secante | Superlineal (1.618) | No | No | 1 función de evaluación |
| El método de Brent | Superlineal | No | Sí | Varía |
**El método de Brent** combina la bisección (convergencia garantizada) con la interpolación cuadrática secante/inversa (convergencia rápida). Es el buscador de raíces predeterminado en la mayoría de las bibliotecas numéricas.
---

## Integración numérica (cuadratura)
Calculando ∫ₐᵇ f(x) dx aproximadamente.
### Métodos
| Método | Fórmula | Error | Orden |
|--------|---------|-------|-------|
| **Rectángulo (punto medio)** | (b−a) · f((a+b)/2) | O(h²) | 1 |
| **Trapezoide** | (b−a)/2 · [f(a) + f(b)] | O(h²) | 2 |
| **Los Simpson 1/3** | (b−a)/6 · [f(a) + 4f(m) + f(b)] | O(h⁴) | 3 |
| **Los Simpson 3/8** | Utiliza 4 puntos igualmente espaciados | O(h⁴) | 4 |
| **Cuadratura gaussiana** | Ubicación óptima de los nodos | O(h²ⁿ) | n puntos |
### Reglas compuestas
Para n subintervalos de ancho h = (b−a)/n:
| Regla | Fórmula compuesta | Error |
|------|-------------------|-------|
| Trapezoidal compuesto | h[f(a)/2 + Σf(xᵢ) + f(b)/2] | O(h²) |
| Simpson compuesto | h/3[f(a) + 4Σf(impar) + 2Σf(par) + f(b)] | O(h⁴) |
**Ejemplo resuelto:** Aproxima ∫₀¹ e^(−x²) dx usando trapezoidal compuesto con n = 4.
- h = 0,25, puntos: 0, 0,25, 0,5, 0,75, 1
- f(0) = 1, f(0,25) = 0,9394, f(0,5) = 0,7788, f(0,75) = 0,5698, f(1) = 0,3679
- T = 0,25[1/2 + 0,9394 + 0,7788 + 0,5698 + 0,3679/2] = 0,25[1/2 + 2,2880 + 0,1840] = 0,7430
- Valor verdadero: ≈ 0,7468 (error ≈ 0,5%)
### Cuadratura adaptativa
Subdivide automáticamente intervalos donde la función varía rápidamente, utilizando menos puntos donde es suave. Esto es lo que usa`scipy.integrate.quad`(basado en QUADPACK).
---

## Interpolación
Estimación de valores entre puntos de datos conocidos.
### Métodos
| Método | Descripción | Suavidad | Oscilación |
|--------|-------------|------------|-------------|
| **Vecino más cercano** | Utilice el punto de datos más cercano | Discontinuo | Ninguno |
| **Lineal** | Conecta puntos con líneas rectas | C⁰ (continuo) | Ninguno |
| **Polinomio (Lagrange)** | Polinomio único que pasa por todos los puntos | C^∞ | Severo en muchos puntos (fenómeno de Runge) |
| **Spline cúbico** | Cúbico por trozos, liso en las uniones | C² | Mínimo |
| **Función de base radial** | Suma ponderada de núcleos radiales | Depende del núcleo | Bajo |
### Interpolación de Lagrange
Dados n+1 puntos (x₀, y₀), ..., (xₙ, yₙ), el único polinomio de grado ≤ n que pasa por todos los puntos:
P(x) = Σᵢ₌₀ⁿ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)
**Fenómeno de Runge:** La interpolación polinómica de alto grado en puntos igualmente espaciados puede oscilar violentamente cerca de los bordes. Mitigado mediante el uso de nodos o splines de Chebyshev.
### Splines cúbicos
Polinomios cúbicos por partes que son C² continuos (segunda derivada continua).
| Tipo | Condición de contorno |
|------|-------------------|
| Estrías naturales | S''(x₀) = S''(xₙ) = 0 |
| Estría sujeta | S'(x₀) y S'(xₙ) especificados |
| Sin nudo | Tercera derivada continua en x₁ y xₙ₋₁ |
---

## Solucionadores de ODA
Resolver ecuaciones diferenciales ordinarias dy/dt = f(t, y) numéricamente.
### Método de Euler
El solucionador de ODE más simple.
**Actualización:** y_{n+1} = y_n + h · f(t_n, y_n)
| Propiedad | Valor |
|----------|-------|
| Orden | 1 (error por paso: O(h²), global: O(h)) |
| Estabilidad | Condicionalmente estable (se requiere h pequeña) |
| Costo | 1 evaluación de función por paso |
### Métodos de Runge-Kutta
| Método | Orden | Etapas | Notas |
|--------|-------|--------|-------|
| **Euler** | 1 | 1 | Más simple |
| **Punto medio** | 2 | 2 | Mejor precisión |
| **Heun (RK2)** | 2 | 2 | Predictor-corrector |
| **RK4 clásico** | 4 | 4 | Caballo de batalla estándar |
| **Dormand-Prince (RK45)** | 4(5) | 6 | Tamaño de paso adaptable (utilizado en ode45) |
### Clásico RK4 (Runge-Kutta de cuarto orden)
k₁ = f(t_n, y_n)
k₂ = f(t_n + h/2, y_n + hk₁/2)
k₃ = f(t_n + h/2, y_n + hk₂/2)
k₄ = f(t_n + h, y_n + hk₃)
y_{n+1} = y_n + h(k₁ + 2k₂ + 2k₃ + k₄) / 6
| Propiedad | Valor |
|----------|-------|
| Orden | 4 (error global: O(h⁴)) |
| Costo | 4 evaluaciones de funciones por paso |
| Estabilidad | Mucho mejor que Euler |
| Uso | Valor predeterminado para EDO no rígidas |
### EDO rígidas
Una EDO **rígida** tiene componentes que varían en escalas de tiempo muy diferentes. Los métodos explícitos (Euler, RK4) requieren tamaños de paso pequeños que no son prácticos.
| Método | Tipo | Estabilidad |
|--------|------|-----------|
| Euler implícito | Implícito | A-estable (incondicionalmente estable) |
| Fórmula de diferenciación hacia atrás (BDF) | Implícito | A-estable (hasta el pedido 5) |
| Runge-Kutta implícito | Implícito | Existen variantes L-estables |
| LSODA | Automático | Cambia entre rígido/no rígido |
---

## Estabilidad numérica y acondicionamiento
### Número de condición
El **número de condición** mide cuánto cambia el resultado de un problema en relación con pequeños cambios en la entrada.
Para un sistema lineal Ax = b: κ(A) = ||A|| · ||A⁻¹||
| k(A) | Interpretación |
|-------|---------------|
| ≈ 1 | Bien acondicionado |
| 10³ | Ligeramente sensible |
| 10⁸ | Mal acondicionado (pierde ~8 dígitos de precisión) |
| → ∞ | Singular (sin solución única) |
### Estabilidad de los algoritmos
Un algoritmo es **numéricamente estable** si pequeñas perturbaciones en la entrada conducen a pequeñas perturbaciones en la salida (en relación con el número de condición del problema).
| Algoritmo | ¿Estable? | Notas |
|-----------|---------|-------|
| Eliminación gaussiana con pivote parcial | Sí | Enfoque estándar |
| Calcular valores propios mediante QR | Sí | Estable hacia atrás |
| Suma ingenua (grande + pequeña primero) | No | Utilice la suma de Kahan |
| Calcular la varianza como E[X²] − (E[X])² | Potencialmente no | Utilice el algoritmo en línea de Welford |
### Algoritmo en línea de Welford
Cálculo numéricamente estable de la media móvil y la varianza:
```
mean_new = mean_old + (x − mean_old) / n
M2_new = M2_old + (x − mean_old)(x − mean_new)
variance = M2 / (n − 1)
```

Esto evita la cancelación catastrófica que se produce en la ingenua fórmula de dos pasos.
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Método numérico | Solicitud |
|-----------------|-------------|
| Punto flotante (fp16/fp32/bf16) | Entrenamiento de precisión mixta, cuantificación de modelos, eficiencia de la memoria |
| Búsqueda de raíces | Estimación de máxima verosimilitud (hallazgo donde gradiente = 0) |
| Integración numérica | Inferencia bayesiana (cálculo de probabilidades marginales), valores esperados |
| Interpolación | Suavizado, imputación, modelos sustitutos, funciones de activación |
| Solucionadores de ODA | EDO neuronales, RNN de tiempo continuo, dinámica de poblaciones, ML basado en la física |
| Número de condición | Comprensión de cuestiones numéricas en regresión lineal, ecuaciones normales |
| Suma estable | Cálculo de funciones de pérdida, estadísticas de normalización por lotes |
| RK4 / solucionadores adaptativos | Simulación de sistemas dinámicos, entrenamiento de redes de profundidad continua |
---

## Resumen
| Tema | Idea central | Método clave |
|-------|-----------|------------|
| Punto flotante | Representación de precisión finita | IEEE 754, suma de Kahan |
| Búsqueda de raíces | Resuelva f(x) = 0 | Bisección, Newton-Raphson, Brent's |
| Integración numérica | Aproximado ∫f(x)dx | Cuadratura trapezoidal, de Simpson y gaussiana |
| Interpolación | Estimación entre puntos de datos | Splines cúbicos, Lagrange, RBF |
| Solucionadores de ODA | Resuelva dy/dt = f(t,y) | Euler, RK4, métodos adaptativos |
| Estabilidad | Sensibilidad a errores de redondeo | Número de condición, algoritmos estables |
Los métodos numéricos son el lugar donde las matemáticas se encuentran con la realidad. Ninguna computadora puede representar exactamente la mayoría de los números reales, ninguna derivada se calcula simbólicamente en la práctica y ninguna integral se evalúa en forma cerrada para problemas del mundo real. Comprender los métodos numéricos le permite elegir el algoritmo correcto, predecir su precisión y evitar los errores sutiles que surgen de la aritmética de precisión finita.