<!--
---
# Metadata
title: "Optimization"
description: "Linear programming, convex optimization, gradient descent variants, Lagrange multipliers, KKT conditions, duality, integer programming, and heuristic methods"
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
    changes: "Initial deep-dive into optimization"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [optimization, linear-programming, convex-optimization, gradient-descent, lagrange-multipliers, kkt, duality, integer-programming]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "real_analysis.md"
estimated_reading_time: "30 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Optimización
La optimización es la matemática para encontrar la mejor solución a partir de un conjunto de soluciones factibles. Pregunta: dadas una función y restricciones, ¿qué entrada minimiza (o maximiza) la salida? La optimización es el motor del aprendizaje automático: entrenar un modelo significa minimizar una función de pérdida. Aparece en la investigación de operaciones, la economía, el diseño de ingeniería y prácticamente en todos los campos cuantitativos.
---

## Formulación del problema
Un **problema de optimización** general tiene la forma:
Minimizar f(x)
Sujeto a: gᵢ(x) ≤ 0 (restricciones de desigualdad), hⱼ(x) = 0 (restricciones de igualdad)
| Término | Significado |
|------|---------|
| **Función objetivo** f(x) | La cantidad a minimizar (o maximizar) |
| **Variables de decisión** x | Los valores que podemos controlar |
| **Región factible** | Conjunto de todos los x que satisfacen todas las restricciones |
| **Mínimo global** | X* factible con f(x*) ≤ f(x) para todo x factible |
| **Mínimo local** | X* factible con f(x*) ≤ f(x) para todo x factible en alguna vecindad |
| **Problema convexo** | f es convexa, la región factible es un conjunto convexo (mínimo local = mínimo global) |
---

## Programación lineal (LP)
Cuando tanto el objetivo como todas las restricciones son **lineales**, el problema es un programa lineal.
### Formulario estándar
Minimizar coᵀx
Sujeto a: Ax ≤ b, x ≥ 0
donde c, x ∈ ℝⁿ, A ∈ ℝᵐˣⁿ, b ∈ ℝᵐ.
### Propiedades
| Propiedad | Declaración |
|----------|-----------|
| Convexidad | LP es siempre un problema convexo |
| Solución óptima | Siempre en un vértice (punto de esquina) del politopo factible |
| Existencia | Si la región factible está acotada y no vacía, existe una solución óptima |
| Múltiples óptimos | Si dos vértices son óptimos, cada punto en el borde entre ellos también es óptimo |
### El método símplex
El **método simplex** (Dantzig, 1947) se mueve a lo largo de las aristas del politopo factible de vértice a vértice, mejorando siempre el objetivo, hasta alcanzar el óptimo.
| Propiedad | Valor |
|----------|-------|
| El peor momento | O(2ⁿ) (exponencial, poco frecuente en la práctica) |
| Tiempo promedio de caso | Polinomio para la mayoría de los problemas prácticos |
| Idea clave | Mover al vértice adyacente con mejor valor objetivo |
**Algoritmo (descripción general):**
1. Comience en una solución básica factible (vértice del politopo)
2. Elige una variable entrante (una que mejore el objetivo)
3. Elija una variable saliente (mantenga la viabilidad)
4. Pivotar: pasar al nuevo vértice
5. Repita hasta que no exista una dirección de mejora.
### Métodos de puntos interiores
Alternativa al simplex: acercarse al óptimo desde el interior de la región factible.
| Propiedad | Valor |
|----------|-------|
| El peor momento | Polinomio (O(n³·⁵) para algunas variantes) |
| Rendimiento práctico | Competitivo con simplex en grandes problemas |
| Idea clave | Sigue un "camino central" por el interior |
### Ejemplo de LP trabajado
**Problema:** Una fábrica produce sillas (x₁) y mesas (x₂).
- Ganancia: $30 por silla, $50 por mesa
- Madera: 2x₁ + 4x₂ ≤ 100 (pies tablares disponibles)
- Mano de obra: x₁ + 3x₂ ≤ 60 (horas disponibles)
- Maximizar: 30x₁ + 50x₂
**Solución (método gráfico para 2 variables):**
- Vértices de región factible: (0,0), (30,0), (40,10), (0,20)
- Evaluar objetivo en cada vértice:
  - (0,0): beneficio = 0
  - (30,0): beneficio = 900
  - (40,10): beneficio = 1700 ← óptimo
  - (0,20): beneficio = 1000
- **Óptimo:** x₁ = 40 sillas, x₂ = 10 mesas, ganancia = $1700
---

## Optimización convexa
Un problema es **convexo** si la función objetivo es convexa y la región factible es un conjunto convexo.
### Conjuntos y funciones convexos
| Concepto | Definición |
|---------|------------|
| **Conjunto convexo** | Para cualquier x, y en el conjunto y t ∈ [0,1]: tx + (1−t)y también está en el conjunto |
| **Función convexa** | f(tx + (1−t)y) ≤ tf(x) + (1−t)f(y) para todo t ∈ [0,1] |
| **Estrictamente convexo** | La desigualdad es estricta para t ∈ (0,1) y x ≠ y |
**Propiedad clave:** Para la optimización convexa, cada mínimo local es un mínimo global.
### Funciones convexas comunes
| Función | ¿Convexo? | Dónde |
|----------|---------|-------|
| hacha + b (lineal) | Sí (y cóncavo) | En todas partes |
| x² | Sí | ℝ |
| miˣ | Sí | ℝ |
| −log(x) | Sí | x > 0 |
| \|x\|ᵖ (p ≥ 1) | Sí | ℝⁿ |
| max(f₁, f₂) si f₁, f₂ convexo | Sí | Intersección de dominios |
### Descenso de gradiente
El algoritmo de optimización más fundamental en el aprendizaje automático.
**Regla de actualización:** x_{k+1} = x_k − α∇f(x_k)
donde α > 0 es la **tasa de aprendizaje** (tamaño del paso).
| Variante | Actualizar regla | Ventaja |
|---------|-------------|-----------|
| **GD por lotes** | x ← x − α∇f(x) | Convergencia estable |
| **GD estocástico (SGD)** | x ← x − α∇fᵢ(x) (una muestra) | Rápido por iteración, escapa a los mínimos locales |
| **Mini lote SGD** | x ← x − α(1/|B|)Σᵢ∈B ∇fᵢ(x) | Equilibrio entre lotes y estocástico |
| **Impulso** | v ← βv − α∇f(x); x ← x + v | Acelera a través de regiones planas |
| **Adán** | Tasas de aprendizaje adaptativo por parámetro | Funciona bien desde el primer momento para el aprendizaje profundo |
| **RMSprop** | Escalar la tasa de aprendizaje mediante el promedio móvil de la magnitud del gradiente | Bueno para los RNN |
### Tasas de convergencia
| Método | Convexo f | Fuertemente convexo f |
|--------|----------|-------------------|
| Descenso de gradiente | O(1/k) | O((1−μ/L)ᵏ) (lineal) |
| SGD | O(1/√k) | O(1/k) |
| GD acelerado (Nesterov) | O(1/k²) | O((1−√(μ/L))ᵏ) |
donde k = recuento de iteraciones, μ = parámetro de convexidad fuerte, L = constante de Lipschitz.
### Elegir la tasa de aprendizaje
| Estrategia | Descripción |
|----------|-------------|
| Fijo α | Simple pero puede divergir (demasiado grande) o converger lentamente (demasiado pequeño) |
| Búsqueda de líneas | Encuentre α que minimice f(x − α∇f(x)) a lo largo de la dirección del gradiente |
| Horarios de decadencia | α_t = α₀ / (1 + βt) o α_t = α₀ · βᵗ |
| Calentamiento | Comience poco a poco, aumente y luego disminuya (común en el entrenamiento de transformadores) |
| Adaptativo (Adán) | Tasas de aprendizaje por parámetro basadas en estadísticas de gradiente |
---

## Optimización restringida
### Multiplicadores de Lagrange
Para el problema: minimizar f(x) sujeto a h(x) = 0.
**Lagrangiano:** L(x, λ) = f(x) + λh(x)
En el óptimo: ∇ₓL = 0 y ∇_λL = 0 (lo que da h(x) = 0).
**Ejemplo resuelto:** Minimizar f(x,y) = x² + y² sujeto a x + y = 1.
- L = x² + y² + λ(x + y − 1)
- ∂L/∂x = 2x + λ = 0 → x = −λ/2
- ∂L/∂y = 2y + λ = 0 → y = −λ/2
- Restricción: x + y = 1 → −λ = 1 → λ = −1
- Solución: x = 1/2, y = 1/2, f = 1/2
### Condiciones KKT
Las **condiciones Karush-Kuhn-Tucker (KKT)** generalizan los multiplicadores de Lagrange a restricciones de desigualdad.
Para: minimizar f(x) sujeto a gᵢ(x) ≤ 0, hⱼ(x) = 0.
**Lagrangiano:** L(x, λ, ν) = f(x) + Σᵢ λᵢgᵢ(x) + Σⱼ νⱼhⱼ(x)
**Condiciones KKT** (necesarias para la optimización):
| Condición | Ecuación |
|-----------|----------|
| Estacionariedad | ∇ₓL = 0 |
| Viabilidad primaria | gᵢ(x) ≤ 0, hⱼ(x) = 0 |
| Doble viabilidad | λᵢ ≥ 0 |
| Laxitud complementaria | λᵢgᵢ(x) = 0 para todo i |
**Laxitud complementaria** significa: si la restricción gᵢ no está activa (gᵢ(x) < 0), entonces λᵢ = 0 (la restricción no afecta la solución).
Para problemas convexos que satisfacen la condición de Slater, las condiciones KKT son necesarias y suficientes.
---

## Dualidad
Cada problema de optimización (el **primal**) tiene un problema **dual** asociado.
### Dualidad débil y fuerte
| Concepto | Declaración |
|---------|-----------|
| **Doble función** | g(λ, ν) = infₓ L(x, λ, ν) |
| **Problema doble** | Maximizar g(λ, ν) sujeto a λ ≥ 0 |
| **Dualidad débil** | Óptimo dual ≤ Óptimo primario (siempre se cumple) |
| **Fuerte dualidad** | Óptimo dual = Óptimo primario (se cumple para problemas convexos con la condición de Slater) |
| **Brecha de dualidad** | Óptimo primario - Óptimo dual (cero bajo dualidad fuerte) |
### Por qué es importante la dualidad
| Solicitud | Cómo ayuda la dualidad |
|-------------|-------------------|
| Límites inferiores | Dual entrega certificado de lo buena que es la solución primal |
| SVM | El doble problema de SVM conduce al truco del kernel |
| Análisis de sensibilidad | Las variables duales miden cuánto cambia el óptimo si se relajan las restricciones |
| Descomposición | Los problemas grandes se pueden dividir en subproblemas más pequeños mediante el método dual |
---

## Programación entera
Cuando algunas o todas las variables deben ser **números enteros**, el problema se vuelve mucho más difícil (NP-difícil en general).
### Tipos
| Tipo | Descripción |
|------|-------------|
| Propiedad intelectual pura | Todas las variables deben ser números enteros |
| IP mixta (MIP) | Algunas variables enteras, algunas continuas |
| IP binaria | Variables restringidas a {0, 1} |
### Métodos de solución
| Método | Ideas |
|--------|------|
| **Rama y encuadernado** | Dividir en subproblemas, resolver relajaciones de LP, podar |
| **Planos de corte** | Añadir restricciones lineales para reforzar la relajación LP |
| **Rama y corte** | Combine ramificar y encuadernar con planos de corte |
| **Heurística** | Búsqueda codiciosa, local, recocido simulado para soluciones aproximadas |
---

## Métodos heurísticos y metaheurísticos
Cuando la optimización exacta es intratable, la heurística encuentra buenas soluciones (no necesariamente óptimas).
| Método | Idea clave | Mejor para |
|--------|----------|----------|
| **Descenso de gradiente** | Sigue el descenso más empinado | Funciones suaves y diferenciables |
| **Método de Newton** | Utilice información de segundo orden (curvatura) | Problemas suaves y bien acondicionados |
| **Recocido simulado** | Aceptar peores soluciones con probabilidad decreciente | Optimización global, combinatoria |
| **Algoritmos genéticos** | Evolucionar una población mediante selección, cruce y mutación | Multiobjetivo, indiferenciable |
| **Enjambre de partículas** | Agentes exploran el espacio, influenciados por posiciones más conocidas | Continuo, no convexo |
| **Optimización bayesiana** | Construya un modelo sustituto y utilice la función de adquisición | Costosas funciones de caja negra (ajuste de hiperparámetros) |
### Método de optimización de Newton
**Regla de actualización:** x_{k+1} = x_k − [H(x_k)]⁻¹ ∇f(x_k)
donde H es la matriz de Hesse (matriz de segundas derivadas).
| Propiedad | Valor |
|----------|-------|
| Tasa de convergencia | Cuadrático (cerca del óptimo) |
| Costo por iteración | O(n³) para inversión de Hesse |
| Requiere | Hessiano definido positivo, dos veces diferenciable |
| Cuasi-Newton (BFGS) | Hessiano aproximado a partir de gradientes | O(n²) por iteración |
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto de optimización | Solicitud |
|---------------------|-------------|
| Descenso de gradiente | Entrenamiento de redes neuronales, regresión logística, cualquier modelo diferenciable |
| SGD y variantes | ML a gran escala (entrenamiento en mini lotes), aprendizaje en línea |
| Adán, RMSprop | Optimizadores predeterminados para aprendizaje profundo |
| Optimización convexa | SVM, regresión logística, LASSO, Ridge (óptimo global garantizado) |
| Multiplicadores de Lagrange | Aprendizaje restringido, aprendizaje automático justo, asignación de recursos |
| Condiciones KKT | Derivando SVM dual, entendiendo la actividad de restricción |
| Dualidad | Truco del kernel SVM, análisis de sensibilidad, métodos de descomposición |
| Programación lineal | Asignación de recursos, optimización de cartera, flujo de red |
| Programación entera | Selección de características (binaria), programación, problemas combinatorios |
| Optimización bayesiana | Ajuste de hiperparámetros (Optuna, Hyperopt) |
| Newton/cuasi-Newton | Métodos de segundo orden para problemas pequeños y medianos (L-BFGS) |
---

## Resumen
| Método | Tipo de problema | Garantías | Escala |
|--------|-------------|------------|-------|
| Simplex | Programación lineal | Óptimo exacto | Millones de variables |
| Punto interior | Convexo (LP, QP, SOCP) | Óptimo exacto | Gran escala |
| Descenso de gradiente | Suave y sin restricciones | Converge al mínimo local | Muy grande (aprendizaje profundo) |
| SGD | Riesgo empírico a gran escala | Converge (con decadencia) | Conjuntos de datos masivos |
| Newton/BFGS | Suave, dos veces diferenciable | Convergencia cuadrática | Pequeño a mediano |
| KKT/Lagrange | Restringido (convexo) | Exacto bajo condiciones | Medio |
| Rama y encuadernado | Programación entera | Óptimo exacto | Pequeño a mediano |
| Heurística | Cualquiera (no convexa, combinatoria) | Sin garantía | Varía |
Podría decirse que la optimización es la herramienta matemática más importante en el aprendizaje automático. Cada modelo que entrene (desde la regresión lineal hasta modelos de lenguaje grandes) implica resolver un problema de optimización. Comprender cuándo un problema es convexo (óptimo global garantizado), cuándo convergerá el descenso de gradiente y cómo manejar las restricciones le brinda la base teórica para diseñar, depurar y mejorar algoritmos de aprendizaje.