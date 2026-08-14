---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
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
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Teoría de juegos
La teoría de juegos es la matemática de la interacción estratégica: situaciones en las que el resultado depende no sólo de tus propias decisiones, sino también de las decisiones de los demás. Desde guerras de precios entre empresas hasta carreras de armamentos nucleares, desde subastas en línea hasta biología evolutiva, la teoría de juegos proporciona las herramientas para analizar el conflicto y la cooperación. Se ha vuelto cada vez más relevante para el aprendizaje automático a través del aprendizaje por refuerzo de múltiples agentes, redes generativas adversarias (GAN) y diseño de mecanismos para plataformas en línea.
---

## Juegos de forma estratégica
### Definición
Un **juego en forma estratégica (forma normal)** consta de:
- Un conjunto de jugadores N = {1, 2, ..., n}
- La estrategia establece S₁, S₂, ..., Sₙ para cada jugador
- Funciones de pago u₁, u₂, ..., uₙ que asignan perfiles de estrategia a números reales
### Ejemplo: el dilema del prisionero
| | Cooperar (C) | Defecto (D) |
|---|---------------|------------|
| **Cooperar (C)** | (-1, -1) | (-3, 0) |
| **Defecto (D)** | (0, −3) | (-2, -2) |
| Análisis | Resultado |
|----------|--------|
| Estrategia dominante | Defecto (D domina a C para ambos jugadores) |
| Equilibrio de Nash | (D, D) con pago (−2, −2) |
| Óptimo social | (C, C) con pago (−1, −1) |
| Dilema | La racionalidad individual conduce a la irracionalidad colectiva |
### Más juegos clásicos
**Batalla de los sexos:**
| | Ópera | Fútbol |
|---|-------|----------|
| Ópera | (2, 1) | (0, 0) |
| Fútbol | (0, 0) | (1, 2) |
Dos equilibrios de Nash: (Ópera, Ópera) y (Fútbol, ​​Fútbol).
**Pollo (halcón-paloma):**
| | Halcón | Paloma |
|---|------|------|
| Halcón | (-10, -10) | (5, 0) |
| Paloma | (0, 5) | (1, 1) |
Dos equilibrios de Nash: (Halcón, Paloma) y (Paloma, Halcón).
---

## Estrategias dominantes
| Concepto | Definición |
|---------|------------|
| **Estrictamente dominante** | La estrategia sᵢ ofrece mayores beneficios que cualquier otra estrategia, independientemente de las elecciones de los oponentes |
| **Débilmente dominante** | La estrategia sᵢ ofrece al menos una recompensa tan alta como cualquier otra, y estrictamente mayor para algunos perfiles de oponentes |
| **Estrategia dominada** | Una estrategia que nunca es la mejor respuesta |
**Eliminación iterada de estrategias dominadas:**
1. Elimine cualquier estrategia estrictamente dominada.
2. Repita hasta que no se puedan eliminar más.
3. Si queda un perfil de estrategia, es el equilibrio único de Nash.
---

## Equilibrio de Nash
Un **equilibrio de Nash** es un perfil de estrategia en el que ningún jugador puede mejorar su rentabilidad cambiando unilateralmente su estrategia.
### Definición
(s₁*, s₂*, ..., sₙ*) es un equilibrio de Nash si para cada jugador i:
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) para todos los sᵢ ∈ Sᵢ
### Encontrar equilibrios de Nash (juegos 2×2)
**Mejor método de respuesta:**
1. Para cada columna, subraya la mejor respuesta del jugador 1.
2. Para cada fila, subraya la mejor respuesta del jugador 2.
3. Las celdas donde ambos están subrayados son equilibrios de Nash.
### Existencia (teorema de Nash)
Todo juego finito tiene al menos un equilibrio de Nash (posiblemente en estrategias mixtas).
### Estrategias mixtas
Una **estrategia mixta** es una distribución de probabilidad sobre estrategias puras.
| Concepto | Definición |
|---------|------------|
| Estrategia mixta σᵢ | Distribución de probabilidad sobre Sᵢ |
| Estrategia mixta NE | Ningún jugador puede mejorar el resultado esperado cambiando su combinación |
| Soporte | Conjunto de estrategias puras jugadas con probabilidad positiva |
**Ejemplo resuelto: emparejar centavos**
| | Cabezas | Colas |
|---|-------|-------|
| Cabezas | (1, −1) | (-1, 1) |
| Colas | (-1, 1) | (1, −1) |
No hay estrategia pura NE. NE mixto: ambos juegan H y T con probabilidad ½ cada uno.
---

## Teorema minimax
### Juegos de suma cero
En un **juego de suma cero**, la ganancia de un jugador es exactamente la pérdida del otro: u₁ + u₂ = 0.
### Teorema Minimax de Von Neumann
Para cada juego finito de suma cero de dos jugadores:
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
El **maximin** (mejor peor caso para el jugador 1) es igual al **minimax** (mejor peor caso para el jugador 2). Este valor común es el **valor del juego**.
### Resolver juegos de suma cero
Para un juego de suma cero 2×2 con matriz:
| | L | R |
|---|---|---|
| T | un | segundo |
| B | c | re |
Estrategia mixta óptima del jugador 1: jugar T con probabilidad p = (d−c)/((a−b)+(d−c))
Valor del juego: v = (ad−bc)/((a−b)+(d−c))
---

## Juegos de formato extensivo
Los juegos con movimientos secuenciales se representan como **árboles de juegos**.
### Conceptos clave
| Concepto | Definición |
|---------|------------|
| **Árbol de juego** | Árbol que muestra todas las posibles secuencias de movimientos |
| **Conjunto de información** | Conjunto de nodos que un jugador no puede distinguir |
| **Información perfecta** | Cada conjunto de información es un singleton (todos los movimientos observables) |
| **Subjuego perfecto NE** | Equilibrio de Nash en cada subjuego |
| **Inducción hacia atrás** | Resuelve desde el final del árbol hacia atrás |
### Teorema de Zermelo
En juegos finitos, de información perfecta, de dos jugadores sin posibilidades: o un jugador tiene una estrategia ganadora o ambos pueden forzar un empate (por ejemplo, ajedrez).
---

## Juegos cooperativos
En **juegos cooperativos**, los jugadores pueden formar coaliciones y acuerdos vinculantes.
### Función característica
Un juego cooperativo se define mediante una **función característica** v: 2^N → ℝ, donde v(S) es el valor que la coalición S puede lograr.
| Propiedad | Definición |
|----------|------------|
| **Superaditivo** | v(S ∪ T) ≥ v(S) + v(T) para S, T disjunto |
| **Convexo** | v(S ∪ {i}) − v(S) ≤ v(T ∪ {i}) − v(T) para S ⊂ T |
### El núcleo
El **núcleo** es el conjunto de asignaciones que ninguna coalición puede mejorar si se separa:
Núcleo = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) para todo S ⊂ N}
El núcleo puede estar vacío, en cuyo caso no existe una asignación estable.
### Valor de Shapley
El **valor de Shapley** proporciona una asignación justa única basada en contribuciones marginales:
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]
| Propiedad | Declaración |
|----------|-----------|
| Eficiencia | Σ φᵢ = v(N) (todo el valor está distribuido) |
| Simetría | Los contribuyentes iguales obtienen pagos iguales |
| Jugador ficticio | Los no contribuyentes obtienen cero |
| Aditividad | φ(v + w) = φ(v) + φ(w) |
**Interpretación:** El valor de Shapley de cada jugador es su contribución marginal promedio en todos los ordenamientos posibles de formación de coaliciones.
### Ejemplo resuelto
Tres jugadores: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.
| Jugador | Contribuciones marginales (promediadas sobre los pedidos) | Valor de Shapley |
|--------|--------------------------------------------------|---------------|
| 1 | (100+50+70+70+50+0)/6 = 56,7 | 37,5 |
| 2 | (100+50+60+60+50+0)/6 | 27,5 |
| 3 | (100+70+60+70+60+0)/6 | 35,0 |
(Calculado con precisión utilizando la fórmula de Shapley para cada permutación).
---

## Diseño de mecanismos
**El diseño de mecanismos** es una "teoría de juegos inversa": en lugar de analizar juegos determinados, diseñe juegos que produzcan los resultados deseados.
### El principio de la revelación
Cualquier mecanismo que logre un resultado deseado puede ser reemplazado por un **mecanismo de revelación directa** donde decir la verdad es un equilibrio de Nash.
### Teoría de la subasta
| Tipo de subasta | Reglas | Equivalencia de ingresos |
|-------------|-------|---------------------|
| **Primer precio en oferta cerrada** | El mejor postor gana y paga su oferta | Todas las subastas estándar generan los mismos ingresos esperados |
| **Segundo precio de oferta en sobre cerrado (Vickrey)** | El mejor postor gana y paga la segunda oferta más alta | (bajo valores privados independientes) |
| **Inglés (ascendente)** | El precio sube; primero en aceptar victorias | — |
| **Holandés (descendente)** | El precio cae; primero en aceptar victorias | — |
### Subasta de Vickrey (segundo precio)
**Estrategia dominante:** Ofrezca su verdadero valor.
| Propiedad | Declaración |
|----------|-----------|
| Oferta veraz | Estrategia débilmente dominante |
| Eficiencia | El artículo va al postor de mayor valor |
| Ingresos | Mismos ingresos esperados que el primer precio (Teorema de equivalencia de ingresos) |
### Diseño de subasta óptimo (Myerson)
La subasta que maximiza los ingresos:
- Se asigna al postor con mayor **valoración virtual**
- Establece un precio de reserva
- Valoración virtual: ψ(v) = v − (1−F(v))/f(v)
---

## Conexiones con el aprendizaje automático
### Redes generativas adversarias (GAN)
Las GAN son un juego de dos jugadores entre un generador G y un discriminador D:
min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]
| Concepto de teoría de juegos | Equivalente a GAN |
|--------------------|-----------------|
| Juego de suma cero para dos jugadores | Generador vs discriminador |
| Equilibrio de Nash | G genera datos reales, D genera ½ en todas partes |
| Minimáx | La función objetivo de GAN |
| Colapso de modo | No alcanzar el equilibrio |
### Aprendizaje por refuerzo multiagente (MARL)
| Concepto | Aplicación MARL |
|---------|-----------------|
| Equilibrio de Nash | Políticas estables en entornos multiagente |
| Minimáx | Políticas sólidas contra oponentes adversarios |
| Juegos cooperativos | Formación de coaliciones, asignación de tareas |
| Valor de Shapley | Cesión de crédito (¿qué agente aportó qué?) |
| Diseño de mecanismos | Diseño de incentivos en sistemas multiagente |
| Juego ficticio | Algoritmo de aprendizaje convergente al equilibrio de Nash |
### Otras conexiones de ML
| Solicitud | Herramienta de teoría de juegos |
|-------------|-----------------|
| Diseño de subasta de anuncios (Google, Facebook) | Diseño de mecanismos, teoría de subastas |
| Diseño de Marketplace (Uber, Airbnb) | Teoría del emparejamiento, diseño de mecanismos |
| Robustez adversaria | Juegos de suma cero entre atacante y defensor |
| División justa | Valor Shapley, asignación sin envidia |
| Aprendizaje federado | Teoría de juegos cooperativos para la medición de la contribución |
| Sistemas de recomendación | Diseño de mecanismos para la obtención veraz de preferencias |
---

## Resumen
| Concepto | Idea central | Resultado clave |
|---------|-----------|------------|
| Juegos de forma estratégica | Jugadores, estrategias, pagos | Representación de la matriz del juego |
| Estrategias dominantes | Mejor independientemente de los demás | Eliminación iterada |
| Equilibrio de Nash | Ninguna desviación unilateral rentable | Existe en todo juego finito |
| Estrategias mixtas | Aleatorizar las acciones | Teorema de existencia de Nash |
| Minimáx | Mejor peor de los casos (suma cero) | Teorema minimax de Von Neumann |
| Forma extensiva | Movimientos secuenciales | Inducción hacia atrás, perfección en subjuegos |
| Juegos cooperativos | Coaliciones vinculantes | Núcleo, valor de Shapley |
| Diseño de mecanismos | Diseñar juegos para obtener resultados | Principio de revelación, subastas óptimas |
| Teoría de la subasta | Vender a través de competencia | Equivalencia de ingresos, subasta de Vickrey |
La teoría de juegos es la matemática del pensamiento estratégico. En un mundo cada vez más poblado por agentes de IA que interactúan, mercados automatizados y sistemas adversarios, la teoría de juegos proporciona el conjunto de herramientas esencial para predecir comportamientos, diseñar mecanismos y construir sistemas robustos de múltiples agentes. Para los científicos de datos, explica cómo funcionan las GAN, cómo las subastas en línea generan miles de millones en ingresos y cómo construir sistemas de inteligencia artificial que funcionen bien en entornos competitivos.