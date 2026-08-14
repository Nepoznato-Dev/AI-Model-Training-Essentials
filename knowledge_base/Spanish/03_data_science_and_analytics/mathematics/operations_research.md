---
# Metadata
title: "Operations Research"
description: "Linear programming formulations, transportation and assignment problems, network flow optimization, integer programming, dynamic programming, queueing theory, inventory models, and scheduling"
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
    changes: "Initial deep-dive into operations research"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [operations-research, linear-programming, transportation-problem, dynamic-programming, queueing-theory, inventory-models, scheduling, network-flow]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "graph_theory.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Investigación de operaciones
La investigación de operaciones (IO) es la aplicación de métodos matemáticos a la toma de decisiones. Nacido durante la Segunda Guerra Mundial para la logística militar, ahora optimiza las cadenas de suministro, programa aerolíneas, enruta flotas de entrega, gestiona inventarios y asigna recursos en todas las industrias. OR proporciona el conjunto de herramientas matemáticas para tomar las mejores decisiones posibles bajo restricciones.
---

## Formulaciones de programación lineal
### Formulario estándar
Minimizar coᵀx
Sujeto a: Ax = b, x ≥ 0
### Formulaciones comunes de LP
**Mezcla de productos:**
- Variables de decisión: xⱼ = cantidad de producto j a producir
- Objetivo: maximizar el beneficio Σ pⱼxⱼ
- Restricciones: límites de recursos Σ aᵢⱼxⱼ ≤ bᵢ
**Problema de dieta:**
- Variables de decisión: xⱼ = cantidad de alimento j a comprar
- Objetivo: minimizar el coste Σ cⱼxⱼ
- Restricciones: requerimientos nutricionales Σ nᵢⱼxⱼ ≥ rᵢ
**Problema de mezcla:**
- Variables de decisión: xⱼ = proporción del ingrediente j en la mezcla
- Objetivo: minimizar costes
- Restricciones: requisitos de calidad (octanaje, resistencia, etc.)
### Ejemplo resuelto: planificación de la producción
Una fábrica fabrica los productos A y B.
- A requiere 2 horas de mano de obra, 1 kg de material; ganancia $30
- B requiere 1 hora de mano de obra, 3 kg de material; ganancia $40
- Disponible: 40 horas de mano de obra, 30 kg de material
**Formulación:**
- Maximizar: 30x_A + 40x_B
- Sujeto a: 2x_A + x_B ≤ 40 (mano de obra)
- x_A + 3x_B ≤ 30 (material)
- x_A, x_B ≥ 0
**Solución:** Vértices de región factible: (0,0), (20,0), (18,4), (0,10)
- (0,0): beneficio = 0
- (20,0): beneficio = 600
- (18,4): beneficio = 700 ← óptimo
- (0,10): beneficio = 400
---

## Problema de transporte
Mover bienes desde m fuentes a n destinos con un costo mínimo.
### Formulación
- Variables de decisión: xᵢⱼ = cantidad enviada desde el origen i al destino j
- Objetivo: minimizar Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Sujeto a: Σⱼ xᵢⱼ = sᵢ (restricciones de oferta)
- Σᵢ xᵢⱼ = dⱼ (restricciones de demanda)
- xᵢⱼ ≥ 0
### Métodos de solución
| Método | Descripción | Calidad de la solución inicial |
|--------|-------------|---------------------|
| **Esquina noroeste** | Comience arriba a la izquierda, asigne con avidez | Factible pero a menudo pobre |
| **Aproximación de Vogel** | Considere los costos de penalización | Mejor solución inicial |
| **MODI / Trampolín** | Mejorar la solución inicial de forma iterativa | Encuentra óptimo |
### Ejemplo resuelto
| | D1 | D2 | D3 | Suministro |
|---|----|----|----|--------|
| T1 | 2 | 3 | 1 | 50 |
| T2 | 4 | 1 | 5 | 30 |
| T3 | 3 | 2 | 4 | 20 |
| Demanda | 40 | 30 | 30 | 100 |
---

## Problema de asignación
Asignar n trabajadores a n trabajos (uno a uno) para minimizar el costo total.
### Formulación
- Variables de decisión: xᵢⱼ ∈ {0, 1} (1 si el trabajador i asignado al trabajo j)
- Minimizar: Σᵢ Σⱼ cᵢⱼxᵢⱼ
- Sujeto a: Σⱼ xᵢⱼ = 1 (cada trabajador obtiene un trabajo)
- Σᵢ xᵢⱼ = 1 (cada trabajo recibe un trabajador)
### Algoritmo húngaro
| Propiedad | Valor |
|----------|-------|
| Complejidad del tiempo | O(n³) |
| ¿Óptimo? | Sí |
| Enfoque | Reducción de matriz + cobertura mínima |
**Pasos:**
1. Reste los mínimos de fila de cada fila
2. Reste los mínimos de columna de cada columna
3. Cubra todos los ceros con un número mínimo de líneas.
4. Si líneas = n, asignación óptima encontrada entre ceros
5. De lo contrario, ajuste la matriz y repita
---

## Optimización del flujo de red
### Flujo de costo mínimo
Dada una red con capacidades y costos en los bordes, encuentre el flujo que satisfaga las demandas al mínimo costo.
**Formulación:**
- Minimizar: Σ cᵢⱼxᵢⱼ
- Sujeto a: conservación del flujo en cada nodo
- Restricciones de capacidad: 0 ≤ xᵢⱼ ≤ uᵢⱼ
### Ruta más corta como flujo de red
El problema del camino más corto es un caso especial de flujo de costo mínimo (enviar 1 unidad de s a t).
### Aplicaciones
| Solicitud | Modelo de red |
|-------------|--------------|
| Cadena de suministro | Nodos = almacenes, bordes = rutas de envío |
| Comunicación | Nodos = enrutadores, bordes = enlaces con ancho de banda |
| Tráfico | Nodos = intersecciones, bordes = caminos con capacidad |
| Gestión de proyectos | Redes CPM/PERT |
---

## Programación dinámica
**La programación dinámica (DP)** resuelve problemas complejos dividiéndolos en subproblemas superpuestos.
### Principio de optimización de Bellman
Una política óptima tiene la propiedad de que cualquiera que sea el estado y la decisión iniciales, las decisiones restantes deben constituir una política óptima para el estado resultante.
### Elementos clave
| Elemento | Descripción |
|---------|-------------|
| **Escenario** | Punto de decisión (paso de tiempo, índice de artículos) |
| **Estado** | Información necesaria para tomar una decisión |
| **Decisión** | Elección realizada en cada etapa |
| **Recurrencia** | Valor óptimo en la etapa n en términos de la etapa n−1 |
### Problemas clásicos de DP
| Problema | Recurrencia | Complejidad |
|---------|-----------|------------|
| **Fibonacci** | F(n) = F(n−1) + F(n−2) | O(n) con memorización |
| **Mochila** | V(i,w) = máx(V(i−1,w), vᵢ + V(i−1,w−wᵢ)) | O(nW) |
| **Camino más corto** | d(i) = min_j(d(j) + cⱼᵢ) | O(V²) u O(E log V) |
| **Editar distancia** | D(i,j) = min(D(i−1,j)+1, D(i,j−1)+1, D(i−1,j−1)+costo) | O(min) |
| **Subsecuencia común más larga** | L(i,j) = L(i−1,j−1)+1 si coincide, de lo contrario max(L(i−1,j), L(i,j−1)) | O(min) |
| **Multiplicación de cadenas de matrices** | M(i,j) = min_k(M(i,k) + M(k+1,j) + pᵢ₋₁pₖpⱼ) | O(n³) |
### Ejemplo resuelto: 0/1 Mochila
Ítems: {peso: valor} = {(2, 12), (3, 10), (4, 8), (5, 11)}. Capacidad W = 7.
V(i, w) = valor máximo usando los primeros i elementos con capacidad w
| yo\w | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 12 | 12 | 12 | 12 | 12 | 12 |
| 2 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 3 | 0 | 0 | 12 | 12 | 12 | 22 | 22 | 22 |
| 4 | 0 | 0 | 12 | 12 | 12 | 22 | 23 | 23 |
Óptimo: V(4, 7) = 23 (ítems 1 y 4: peso 2+5=7, valor 12+11=23).
---

## Teoría de colas
La teoría de las colas estudia las colas de espera: cuánto duran, cuánto tiempo se espera y cómo reducir ambas.
### Notación de Kendall
A/B/c/K/N/D donde:
- A = proceso de llegada (M = Markoviano/Poisson, D = determinista, G = general)
- B = proceso de servicio (mismas opciones)
- c = número de servidores
- K = capacidad (por defecto ∞)
- N = población (por defecto ∞)
- D = disciplina (FIFO, LIFO, Prioridad)
### Cola M/M/1 (servidor único)
| Métrica | Fórmula |
|--------|---------|
| Utilización | ρ = λ/μ |
| Número medio en el sistema | L = ρ/(1−ρ) |
| Tiempo medio en el sistema | W = 1/(μ−λ) |
| Número medio en cola | L_q = ρ²/(1−ρ) |
| Tiempo medio de espera | W_q = ρ/(μ−λ) |
donde λ = tasa de llegada, μ = tasa de servicio, ρ = utilización.
### Cola M/M/c (múltiples servidores)
| Métrica | Fórmula |
|--------|---------|
| Utilización | ρ = λ/(cμ) |
| Probabilidad de espera (Erlang C) | P_w = fórmula compleja que involucra ρ y c |
| Longitud media de la cola | L_q = P_w · ρ/(1−ρ) |
### Ley de Little
L = λW (número promedio en el sistema = tasa de llegada × tiempo promedio)
Esto es válido para CUALQUIER sistema de colas, independientemente de la distribución de llegadas/servicios.
### Ejemplos de aplicación
| Escenario | Modelo de cola |
|----------|-------------|
| Centro de llamadas | M/M/c (agentes c) |
| Solicitudes de servidor web | M/M/1 o M/G/1 |
| Emergencia hospitalaria | M/G/c con prioridades |
| Línea de fabricación | Red de colas |
| Programación de CPU de computadora | Compartir procesador M/M/1 |
---

## Modelos de inventario
### Cantidad de pedido económico (EOQ)
La cantidad óptima de pedido que minimiza los costos totales de inventario.
Q* = √(2DS/H)
| Variables | Significado |
|----------|---------|
| D | Demanda anual |
| S | Costo de pedido por pedido |
| H | Costo de tenencia por unidad por año |
| Q* | Cantidad de pedido óptima |
**Costo total en Q*:** TC = √(2DSH)
### Extensiones
| Modelo | Ampliación |
|-------|-----------|
| **EOQ con descuentos** | Los descuentos por cantidad cambian la función de costos |
| **Cantidad de pedido de producción** | Artículos producidos gradualmente, no entregados todos a la vez |
| **(s, Q) modelo** | Reordenar Q unidades cuando el inventario baje al nivel s |
| **(s, S) modelo** | Ordene hasta S cuando el inventario baje a s |
| **Modelo de vendedor de noticias** | Demanda incierta de un solo período |
### Modelo de vendedor de noticias
Cantidad de pedido óptima para inventario de perecederos de un solo período:
P(D ≤ Q*) = c_u / (c_u + c_o)
donde c_u = costo insuficiente (lucro cesante) y c_o = costo excedente (desperdicio).
---

## Programación
### Programación de taller de trabajo
| Notación | Significado |
|----------|---------|
| n/m/J/C_máx | n trabajos, m máquinas, taller de trabajo, minimizar el espacio de trabajo |
| Tienda de flujo | Todos los trabajos visitan las máquinas en el mismo orden |
| Tienda de empleo | Cada trabajo tiene su propia secuencia de máquina |
| Tienda abierta | Sin restricciones de pedido |
### Reglas de prioridad
| Regla | Descripción | Efecto |
|------|-------------|--------|
| FCFS | Primero en llegar, primero en ser atendido | Justo, pero no óptimo |
| SPT | El tiempo de procesamiento más corto primero | Minimiza la finalización promedio |
| EDD | Fecha de vencimiento más temprana primero | Minimiza la tardanza máxima |
| RC | Ratio crítico (fecha de vencimiento restante / tiempo de procesamiento) | Equilibrado |
| LPT | El tiempo de procesamiento más largo primero | Bueno para makepan en máquinas paralelas |
### Algoritmo de Johnson (taller de flujo de 2 máquinas)
Para n trabajos en 2 máquinas, minimizando el espacio de trabajo:
1. Encuentre el trabajo con el menor tiempo de procesamiento
2. Si está en la máquina 1, prográmelo primero; si está en la máquina 2, prográmelo al final
3. Elimina ese trabajo y repite
Óptimo para 2 máquinas; NP-duro para más de 3 máquinas.
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| O Concepto | Solicitud |
|-----------|-------------|
| Programación lineal | Asignación de recursos, optimización de cartera, asignación de presupuesto publicitario |
| Transporte/asignación | Logística, emparejamiento de viajes compartidos, asignación de tareas |
| Flujo de red | Optimización de la cadena de suministro, enrutamiento del tráfico del centro de datos |
| Programación dinámica | Alineación de secuencias (bioinformática), algoritmo de Viterbi (HMM), RL (ecuación de Bellman) |
| Teoría de colas | Planificación de la capacidad del servidor, modelado de latencia, asignación de recursos en la nube |
| Modelos de inventario | Integración de previsión de demanda, cadena de suministro ML |
| Programación | Orquestación de canalizaciones de aprendizaje automático, programación de trabajos de GPU, programación de búsqueda de hiperparámetros |
| Programación entera | Selección de características (binaria), selección de modelo, diseño de red |
---

## Resumen
| Tema | Problema central | Método clave |
|-------|-------------|------------|
| Formulaciones LP | Optimizar objetivo lineal con restricciones | Simplex, punto interior |
| Transporte | Enviar mercancías al mínimo coste | MODI, trampolín |
| Tarea | Emparejar trabajadores con puestos de trabajo | Algoritmo húngaro |
| Flujo de red | Flujo de rutas a través de una red | Algoritmos de flujo de costo mínimo |
| Programación dinámica | Subproblemas superpuestos | Principio de Bellman, memorización |
| Teoría de las colas | Análisis de líneas de espera | M/M/1, ley de Little |
| Inventario | Cuándo y cuánto pedir | EOQ, vendedor de periódicos |
| Programación | Trabajos de secuencia en máquinas | Reglas de prioridad, algoritmo de Johnson |
La investigación operativa transforma la toma de decisiones del arte a la ciencia. Al formular matemáticamente problemas del mundo real, OR proporciona soluciones demostrablemente óptimas (o casi óptimas) a problemas de logística, programación, asignación de recursos y planificación que afectan a todas las industrias. Para los científicos de datos, los métodos de OR complementan el aprendizaje automático: mientras que el ML predice, el OR prescribe, y juntos forman la base de los sistemas de decisión inteligentes.