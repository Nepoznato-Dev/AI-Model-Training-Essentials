---
# Metadata
title: "Stochastic Processes"
description: "Random variables review, Markov chains, random walks, Brownian motion, Poisson processes, martingales, Monte Carlo methods, and MCMC"
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
    changes: "Initial deep-dive into stochastic processes"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [stochastic-processes, markov-chains, random-walks, brownian-motion, poisson-processes, martingales, monte-carlo, mcmc]
difficulty_level: "advanced"
prerequisites:
  - "statistics_and_probability.md"
  - "real_analysis.md"
estimated_reading_time: "28 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Procesos estocásticos
Un **proceso estocástico** es una colección de variables aleatorias indexadas por el tiempo (o el espacio). Mientras que la teoría de la probabilidad estudia eventos aleatorios individuales, los procesos estocásticos estudian cómo evoluciona la aleatoriedad con el tiempo. Modelan los precios de las acciones, la duración de las colas, la propagación de enfermedades, la generación de lenguaje y la dinámica de entrenamiento de los modelos de aprendizaje automático.
---

## Fundaciones
### Definición
Un proceso estocástico {X_t : t ∈ T} es una familia de variables aleatorias definidas en un espacio de probabilidad común. T es el **conjunto de índices** (tiempo):
- **Tiempo discreto:** T = {0, 1, 2, ...}
- **Tiempo continuo:** T = [0, ∞)
El **espacio de estados** S es el conjunto de posibles valores que X_t puede tomar.
### Propiedades clave
| Propiedad | Definición |
|----------|------------|
| **Estacionariedad** | Distribución conjunta de (X_{t₁}, ..., X_{tₖ}) igual que (X_{t₁+τ}, ..., X_{tₖ+τ}) |
| **Independencia** | X_t independiente de X_s para t ≠ s |
| **Ergodicidad** | Los promedios de tiempo convergen a los promedios de conjuntos |
| **Propiedad de Markov** | El futuro depende sólo del presente, no del pasado |
| **Martingala** | El valor futuro esperado es igual al valor actual |
---

## Cadenas de Markov
Una **cadena de Markov** es un proceso estocástico en el que el estado futuro depende únicamente del estado actual (propiedad sin memoria).
### Cadenas de Markov de tiempo discreto (DTMC)
P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, ...) = P(X_{n+1} = j | X_n = i) = p_{ij}
La **matriz de transición** P tiene entradas p_{ij} = P(ir a j | actualmente en i).
| Propiedad | Declaración |
|----------|-----------|
| Sumas de filas | Cada fila suma 1: Σⱼ p_{ij} = 1 |
| transición de n pasos | P(X_{n+m} = j | X_m = i) = (Pⁿ)_{ij} |
| Distribución estacionaria | πP = π (vector propio izquierdo con valor propio 1) |
### Clasificación de estados
| Término | Definición |
|------|------------|
| **Recurrente** | La cadena vuelve al estado i con probabilidad 1 |
| **Transitorio** | Probabilidad distinta de cero de no regresar nunca |
| **Absorbente** | p_{ii} = 1 (una vez ingresado, nunca abandonado) |
| **Periodo** | MCD de tiempos de retorno; período 1 = aperiódico |
| **Comunicándose** | Los estados i y j pueden comunicarse entre sí |
### Distribución estacionaria
Para una cadena de Markov recurrente positiva e irreducible, la distribución estacionaria π existe, es única y satisface:
πP = π, Σᵢ πᵢ = 1
**Interpretación:** πᵢ = proporción de largo plazo del tiempo pasado en el estado i.
**Ejemplo resuelto:** Modelo meteorológico con estados {Soleado, Lluvioso}.
P = [[0.9, 0.1], [0.5, 0.5]] (filas: de Soleado, de Lluvioso)
Distribución estacionaria: πP = π
- π₁ = 0,9π₁ + 0,5π₂
- π₂ = 0,1π₁ + 0,5π₂
- π₁ + π₂ = 1
- Resolviendo: π₁ = 5/6 ≈ 0,833, π₂ = 1/6 ≈ 0,167
### Convergencia a la estacionariedad
Para una cadena recurrente positiva, aperiódica e irreducible:
- Pⁿ → Π (matriz con todas las filas iguales a π) como n → ∞
- **Tiempo de mezcla:** Número de pasos hasta que la distribución se acerque a π
- **Brecha espectral:** 1 − |λ₂| (donde λ₂ es el segundo valor propio más grande) determina la velocidad de mezcla
### Cadenas de Markov de tiempo continuo (CTMC)
Las transiciones ocurren en momentos aleatorios regidos por distribuciones exponenciales.
| Concepto | Descripción |
|---------|-------------|
| **Matriz de tarifas Q** | q_{ij} ≥ 0 para i ≠ j; q_{ii} = −Σ_{j≠i} q_{ij} |
| **Probabilidades de transición** | P(t) = e^{Qt} (matriz exponencial) |
| **Distribución estacionaria** | πQ = 0 |
| **Tiempo de espera** | El tiempo en el estado i es Exp(−q_{ii}) |
---

## Paseos aleatorios
Un **camino aleatorio** es un camino formado por sucesivos pasos aleatorios.
### Paseo aleatorio simple
X_n = X_{n-1} + Z_n, donde Z_n ∈ {+1, −1} con probabilidades p, q = 1−p.
| Propiedad | p = 1/2 (simétrico) | p ≠ 1/2 (sesgado) |
|----------|---------------------|-------------------|
| E[X_n] | 0 | norte(2p−1) |
| Var[X_n] | norte | 4npq |
| ¿Regresos al origen? | Sí (con probabilidad 1) | No (se aleja) |
| ¿Recurrente? | Sí (en 1D y 2D) | No |
### Paseo aleatorio en dimensiones superiores
| Dimensión | ¿Recurrente? | Intuición |
|-----------|------------|-----------|
| 1D | Sí | "Un borracho siempre encuentra el camino a casa" |
| 2D | Sí | "Un pájaro borracho siempre encuentra el camino a casa" |
| 3D+ | No | "Un gorrión borracho nunca encuentra el camino a casa" |
### Conexión con el movimiento browniano
Escalar un paseo aleatorio: sea S_n = ΣZ_i. Luego como tamaño de paso → 0 y pasos → ∞:
S_{⌊nt⌋} / √n → B(t) (movimiento browniano, según el teorema de Donsker)
---

## Movimiento browniano
**Movimiento browniano** (proceso de Wiener) B(t) es el límite de tiempo continuo de una caminata aleatoria.
### Definición
B(t) satisface:
1.B(0) = 0
2. B(t) tiene caminos continuos
3. Incrementos independientes: B(t) − B(s) es independiente de B(s) − B(r) para r < s < t
4. B(t) − B(s) ~ N(0, t − s) (incrementos gaussianos)
### Propiedades clave
| Propiedad | Declaración |
|----------|-----------|
| E[B(t)] | = 0 |
| Var[B(t)] | = t |
| Cov[B(s), B(t)] | = mín(s, t) |
| En ninguna parte diferenciable | Los caminos son continuos pero no tienen derivada |
| Dimensión fractal | El gráfico tiene dimensión de Hausdorff 3/2 |
| Markov propiedad | El futuro depende sólo de la posición actual |
| Martingala | E[B(t) | F_s] = B(s) para s < t |
### Movimiento browniano geométrico
S(t) = S(0) exp((μ − σ²/2)t + σB(t))
Este es el modelo estándar para los precios de las acciones en el marco de Black-Scholes.
- μ: deriva (retorno esperado)
- σ: volatilidad
---

## Procesos de Poisson
Un **proceso de Poisson** N(t) cuenta el número de eventos que ocurren en [0, t].
### Definición
N(t) ~ Poisson(λt), donde λ es la tasa (eventos por unidad de tiempo).
| Propiedad | Declaración |
|----------|-----------|
| norte(0) = 0 | — |
| Incrementos independientes | Los eventos en intervalos disjuntos son independientes |
| Incrementos estacionarios | norte(t+s) − norte(s) ~ Poisson(λt) |
| E[NORTE(t)] | = λt |
| Var[N(t)] | = λt |
| Horarios entre llegadas | Distribuida exponencialmente: T_i ~ Exp(λ) |
### Generalizaciones
| Variante | Descripción |
|---------|-------------|
| **No homogéneo** | La tasa λ(t) varía con el tiempo |
| **Poisson compuesto** | Cada evento tiene un tamaño aleatorio: S(t) = Σᵢ₌₁^{N(t)} Yᵢ |
| **Medida aleatoria de Poisson** | Puntos en el espacio-tiempo, no sólo en el tiempo |
| **Multivariante** | Múltiples tipos de eventos con posibles interacciones |
---

## Martingalas
Una **martingala** es un juego limpio: el valor futuro esperado, dada toda la información actual, es igual al valor actual.
### Definición
{X_n} es una martingala con respecto a la filtración {F_n} si:
1. X_n es F_n medible (adaptado)
2. E[|X_n|] < ∞ (integrable)
3. E[X_{n+1} | F_n] = X_n (juego limpio)
| Variante | Condición | Interpretación |
|---------|-----------|----------------|
| **Martingala** | mi[X_{n+1} | F_n] = X_n | Juego limpio |
| **Submartingala** | mi[X_{n+1} | F_n] ≥ X_n | Juego favorable (tendencia alcista) |
| **Supermartingala** | mi[X_{n+1} | F_n] ≤ X_n | Partido desfavorable (tendencia a la baja) |
### Teoremas clave
| Teorema | Declaración |
|---------|-----------|
| **Parada opcional** | En condiciones, E[X_T] = E[X_0] para un tiempo de parada T |
| **Convergencia** | Una martingala acotada converge casi con seguridad |
| **Desigualdad máxima** | P(max_{k≤n} X_k ≥ λ) ≤ E[X_n] / λ (Doob) |
---

## Métodos Montecarlo
Los **métodos de Monte Carlo** utilizan muestreo aleatorio para estimar cantidades deterministas.
### Idea básica
Para estimar E[f(X)] donde X ~ P:
1. Extraiga N muestras: x₁, x₂, ..., x_N de P
2. Calcular: Î = (1/N) Σᵢ f(xᵢ)
3. Por la ley de los grandes números: Î → E[f(X)] como N → ∞
**Error:** Error estándar = σ_f / √N, donde σ_f² = Var[f(X)]
### Técnicas de reducción de varianza
| Técnica | Ideas | Aceleración |
|-----------|------|---------|
| **Muestreo de importancia** | Muestra de Q en lugar de P, peso por P/Q | Puede ser dramático |
| **Variaciones antitéticas** | Utilice pares (x, −x) para cancelar la varianza | ~2x |
| **El control varía** | Resta la función de expectativa conocida correlacionada con f | Varía |
| **Muestreo estratificado** | Dividir dominio, muestrear cada estrato | Reduce la variación |
| **Rao-Blackwell** | Condición de contar con estadísticas suficientes | Siempre ayuda |
---

## Cadena Markov Montecarlo (MCMC)
MCMC construye una cadena de Markov cuya distribución estacionaria es la distribución objetivo. Después de un período de "quemado", las muestras se aproximan a las extracciones del objetivo.
### Algoritmo de Metrópolis-Hastings
| Paso | Acción |
|------|--------|
| 1 | Estado actual: x_t |
| 2 | Proponer: x* ~ q(x* \| x_t) (distribución de propuesta) |
| 3 | Relación de aceptación: α = min(1, [π(x*)q(x_t\|x*)] / [π(x_t)q(x*\|x_t)]) |
| 4 | Aceptar con probabilidad α: x_{t+1} = x* (aceptar) o x_t (rechazar) |
**Caso especial: algoritmo de Metropolis:** Propuesta simétrica q(x*|x) = q(x|x*), entonces α = min(1, π(x*)/π(x_t)).
### Muestreo de Gibbs
Un caso especial de Metropolis-Hastings donde cada variable se actualiza a partir de su distribución condicional completa.
Para el objetivo π(x₁, x₂, ..., xₖ):
1. Muestra x₁^{(t+1)} ~ π(x₁ | x₂^{(t)}, ..., xₖ^{(t)})
2. Muestra x₂^{(t+1)} ~ π(x₂ | x₁^{(t+1)}, x₃^{(t)}, ..., xₖ^{(t)})
3. Continuar para todas las variables.
4. Repetir
| Propiedad | Declaración |
|----------|-----------|
| Siempre acepta | α = 1 (sin paso de rechazo) |
| Requiere | Capacidad de tomar muestras de cada condicional completo |
| Convergencia | Garantizado para cadenas irreductibles y aperiódicas |
### Diagnóstico MCMC
| Diagnóstico | Propósito |
|-----------|------------------|
| **Trazado de trazado** | Control visual de mezcla y estacionariedad |
| **Autocorrelación** | Mide la dependencia de la muestra (quiere una autocorrelación baja) |
| **Gelman-Rubin (R̂)** | Compara múltiples cadenas; R̂ < 1,05 sugiere convergencia |
| **Tamaño de muestra efectivo** | N_eff = N / (1 + 2Σρₖ); cuentas para la autocorrelación |
| **Grabado** | Deseche las muestras iniciales antes de que la cadena alcance la estacionariedad |
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Proceso estocástico | Solicitud |
|-------------------|-------------|
| Cadenas de Markov | PageRank (recorrido aleatorio en gráfico web), generación de texto (modelos de n-gramas), MCMC |
| Paseos aleatorios | Node2Vec y DeepWalk (incrustaciones de gráficos), exploración en RL |
| Movimiento browniano | Modelización de precios de acciones, modelos de difusión en IA generativa |
| Procesos de Poisson | Modelado de llegadas de eventos (clics, fallos), teoría de colas |
| Martingalas | Matemáticas financieras, que demuestran la convergencia del SGD (aproximación estocástica) |
| Montecarlo | Estimación de valores esperados, inferencia bayesiana, aprendizaje por refuerzo (evaluación de políticas) |
| MCMC (Metrópoli-Hastings) | Muestreo posterior bayesiano, programación probabilística (Stan, PyMC) |
| Muestreo de Gibbs | Modelos temáticos (LDA), redes bayesianas, eliminación de ruido de imágenes |
| Diagnóstico MCMC | Garantizar una inferencia fiable a partir de modelos probabilísticos |
---

## Resumen
| Proceso | Espacio de estados | Hora | Propiedad clave |
|---------|-------------|------|--------------|
| Cadena de Markov | Discreto/continuo | Discreto/continuo | Sin memoria (propiedad de Markov) |
| Paseo aleatorio | ℤᵈ | Discreto | Suma de i.i.d. pasos |
| Movimiento browniano | ℝ | Continuo | Incrementos gaussianos, caminos continuos |
| Proceso de Poisson | ℕ | Continuo | Proceso de conteo con brechas exponenciales |
| Martingala | ℝ | Discreto/continuo | Juego limpio (E[X_{t+1}|F_t] = X_t) |
Los procesos estocásticos son las matemáticas de la aleatoriedad en el tiempo. Son la base de la inferencia bayesiana moderna (MCMC), el aprendizaje por refuerzo (procesos de decisión de Markov), el modelado generativo (modelos de difusión), las matemáticas financieras y la teoría de colas. Comprender estos procesos le brinda las herramientas para modelar la incertidumbre de manera dinámica, no solo como una instantánea, sino a medida que evoluciona.