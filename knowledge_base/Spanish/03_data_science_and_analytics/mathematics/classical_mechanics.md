---
# Metadata
title: "Classical Mechanics"
description: "Newton's laws, free-body diagrams, work-energy theorem, conservation laws, Lagrangian mechanics, Hamiltonian mechanics, rigid body dynamics, and orbital mechanics"
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
    changes: "Initial deep-dive into classical mechanics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [classical-mechanics, newton, lagrangian, hamiltonian, conservation-laws, orbital-mechanics, rigid-body]
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
# Mecánica clásica
La mecánica clásica describe el movimiento de objetos bajo la influencia de fuerzas. Desde manzanas que caen hasta planetas en órbita, desde cuerdas vibrantes hasta partículas en colisión, sus principios gobiernan el mundo macroscópico. Más allá de sus aplicaciones físicas, la mecánica clásica dio origen al cálculo de variaciones, la geometría simpléctica y el marco hamiltoniano que sustenta la mecánica cuántica y la optimización moderna.
---

## Mecánica Newtoniana
### Las tres leyes de Newton
| Ley | Declaración | Forma matemática |
|-----|-----------|-------------------|
| **Primero (Inercia)** | Un objeto permanece en reposo o en movimiento uniforme a menos que actúe sobre él una fuerza. Si F_net = 0, entonces v = constante |
| **Segundo (F = ma)** | La fuerza es igual a la masa por la aceleración | **F** = m**a** = m(d²**x**/dt²) |
| **Tercero (Acción-Reacción)** | Cada acción tiene una reacción igual y opuesta | **F**₁₂ = −**F**₂₁ |
### Diagramas de cuerpo libre
Un **diagrama de cuerpo libre** aísla un objeto y muestra todas las fuerzas que actúan sobre él.
**Fuerzas comunes:**
| Fuerza | Fórmula | Dirección |
|-------|---------|-----------|
| Gravedad (cerca de la Tierra) | F = mg | Hacia abajo |
| Fuerza normal | norte | Perpendicular a la superficie |
| Fricción (estática) | f_s ≤ μ_s norte | Se opone a una moción inminente |
| Fricción (cinética) | f_k = μ_k norte | Se opone a la moción |
| Primavera (ley de Hooke) | F = −kx | Restauración (hacia el equilibrio) |
| Tensión | T | A lo largo de la cuerda/cuerda |
| Arrastrar | F_d = ½C_d ρAv² | Se opone a la velocidad |
### Ejemplo resuelto: bloque en pendiente
Un bloque de masa m sobre un plano inclinado sin fricción formando un ángulo θ.
- Fuerzas: gravedad (mg hacia abajo), fuerza normal (N perpendicular a la superficie)
- Descomponer la gravedad: mg sin θ (a lo largo de una pendiente), mg cos θ (en la superficie)
- N = mg cos θ (sin movimiento perpendicular a la superficie)
- Aceleración en pendiente: a = g sen θ
---

## Métodos energéticos
### Trabajo y energía cinética
**Trabajo** realizado por una fuerza: W = ∫ **F** · d**r**
**Teorema trabajo-energía:** W_net = ΔKE = ½mv₂² − ½mv₁²
### Energía potencial
| Fuerza | Energía potencial | Notas |
|-------|-----------------|-------|
| Gravedad (cerca de la superficie) | U = mgh | h = altura sobre la referencia |
| Gravedad (general) | U = −GMm/r | Cero en el infinito |
| Primavera | U = ½kx² | x = desplazamiento del equilibrio |
| Electrostático | U = kq₁q₂/r | Cargas similares: U positiva |
### Conservación de energía
Si sólo actúan fuerzas conservativas: E = KE + PE = constante
½mv₁² + U₁ = ½mv₂² + U₂
**Ejemplo resuelto:** Una pelota que se deja caer desde una altura h.
- Inicial: KE = 0, PE = mgh
- Justo antes de tocar el suelo: KE = ½mv², PE = 0
- Conservación: mgh = ½mv² → v = √(2gh)
### Fuerza
P = dW/dt = **F** · **v** (tasa de realización del trabajo)
---

## Momento y colisiones
### Momento lineal
**p** = m**v**
Segunda ley de Newton (forma alternativa): **F** = d**p**/dt
### Conservación del impulso
Si no hay fuerzas externas: se conserva el impulso total.
| Tipo de colisión | KE ¿Conservado? | ¿Impulso conservado? |
|---------------|---------------|---------------------|
| **Elástico** | Sí | Sí |
| **Inelástico** | No | Sí |
| **Perfectamente inelástico** | No (pérdida máxima) | Sí (los objetos se pegan) |
**Colisión elástica 1D:** Dos masas m₁, m₂ con velocidades iniciales u₁, u₂:
- v₁ = ((m₁−m₂)u₁ + 2m₂u₂) / (m₁+m₂)
- v₂ = ((m₂−m₁)u₂ + 2m₁u₁) / (m₁+m₂)
### Momento angular
**L** = **r** × **p** = m(**r** × **v**)
Par: **τ** = d**L**/dt = **r** × **F**
**Conservación:** Si no hay torsión externa, se conserva el momento angular.
---

## Mecánica Lagrangiana
La formulación **Lagrangiana** reemplaza las fuerzas con energía, proporcionando un marco más elegante y general.
### El lagrangiano
L = T − V (energía cinética menos energía potencial)
### Principio de acción mínima (principio de Hamilton)
El camino real tomado por un sistema entre los tiempos t₁ y t₂ minimiza (más precisamente, lo vuelve estacionario) la **acción**:
S = ∫_{t₁}^{t₂} L(q, q̇, t) dt
### Ecuaciones de Euler-Lagrange
La condición δS = 0 produce:
d/dt(∂L/∂q̇) − ∂L/∂q = 0
para cada coordenada generalizada q.
**Ejemplo resuelto:** Péndulo simple (longitud l, masa m, ángulo θ con respecto a la vertical).
- T = ½ml²θ̇²
- V = −mgl porque θ
- L = ½ml²θ̇² + mgl cos θ
- ∂L/∂θ = −mgl sen θ
- ∂L/∂θ̇ = ml²θ̇ → d/dt(∂L/∂θ̇) = ml²θ̈
- Euler-Lagrange: ml²θ̈ + mgl sen θ = 0 → θ̈ + (g/l) sen θ = 0
### Ventajas de la mecánica lagrangiana
| Ventaja | Explicación |
|-----------|-------------|
| Independiente de coordenadas | Funciona en cualquier sistema de coordenadas |
| Maneja las limitaciones de forma natural | No es necesario calcular las fuerzas restrictivas |
| Simetría → conservación | El teorema de Noether conecta simetrías con cantidades conservadas |
| Generaliza fácilmente | A campos, relatividad, mecánica cuántica |
---

## Mecánica hamiltoniana
La formulación **hamiltoniana** es una reformulación de la mecánica lagrangiana que utiliza posiciones y momentos (en lugar de posiciones y velocidades).
### El hamiltoniano
H = Σᵢ pᵢq̇ᵢ − L = T + V (para la mayoría de los sistemas mecánicos)
donde pᵢ = ∂L/∂q̇ᵢ son los **momentos generalizados**.
### Ecuaciones de Hamilton
q̇ᵢ = ∂H/∂pᵢ
ṗᵢ = −∂H/∂qᵢ
Estas son 2n EDO de primer orden (frente a n ecuaciones de Euler-Lagrange de segundo orden).
**Ejemplo resuelto:** Oscilador armónico (masa m, constante del resorte k).
- H = p²/(2m) + ½kx²
- ẋ = ∂H/∂p = p/m → p = mẋ (como se esperaba)
- ṗ = −∂H/∂x = −kx → mẍ = −kx (ley de Hooke)
### Soportes de Poisson
Para funciones f(q, p) y g(q, p):
{f, g} = Σᵢ (∂f/∂qᵢ · ∂g/∂pᵢ − ∂f/∂pᵢ · ∂g/∂qᵢ)
| Propiedad | Declaración |
|----------|-----------|
| Evolución del tiempo | df/dt = {f, H} + ∂f/∂t |
| Conservación | f se conserva si y sólo si {f, H} = 0 (y ∂f/∂t = 0) |
| Soportes fundamentales | {qᵢ, pⱼ} = δᵢⱼ, {qᵢ, qⱼ} = 0, {pᵢ, pⱼ} = 0 |
**Conexión con la mecánica cuántica:** Los corchetes de Poisson se convierten en conmutadores: {f, g} → (1/iℏ)[f̂, ĝ]
---

## Leyes de conservación y teorema de Noether
### Teorema de Noether
Cada simetría continua del Lagrangiano corresponde a una cantidad conservada.
| Simetría | Cantidad conservada |
|----------|-------------------|
| invariancia del tiempo traducción | Energía |
| invariancia espacial traducción | Momento lineal |
| Invariancia rotacional | Momento angular |
| Invariancia de calibre | Carga eléctrica |
Este es uno de los resultados más profundos de toda la física: conecta la geometría del espacio-tiempo con las leyes fundamentales de conservación.
---

## Dinámica del cuerpo rígido
Un **cuerpo rígido** es un objeto donde todas las distancias internas permanecen fijas.
### Conceptos clave
| Concepto | Fórmula | Descripción |
|---------|---------|-------------|
| **Momento de inercia** | I = Σmᵢrᵢ² o I = ∫r² dm | Resistencia a la aceleración rotacional |
| **KE rotacional** | KE = ½Iω² | Energía de rotación |
| **Momento angular** | L = Yoω | Análogo rotacional de p = mv |
| **Par de torsión** | τ = Iα | Análogo rotacional de F = ma |
### Momentos de inercia (formas comunes)
| Forma | Eje | Yo |
|-------|------|---|
| Esfera sólida | Por el centro | (2/5)MR² |
| Esfera hueca | Por el centro | (2/3)MR² |
| Cilindro macizo | A lo largo del eje | (1/2)MR² |
| Varilla delgada | Por el centro, perpendicular | (1/12)ML² |
| Varilla delgada | Extremo pasante, perpendicular | (1/3)ML² |
| Disco | Por el centro, perpendicular | (1/2)MR² |
---

## Mecánica orbital
### Leyes de Kepler
| Ley | Declaración |
|-----|-----------|
| **Primero (Elipses)** | Los planetas se mueven en elipses con el Sol en un foco |
| **Segundo (Áreas iguales)** | Una línea que va del Sol al planeta recorre áreas iguales en tiempos iguales |
| **Tercero (Armónico)** | T² ∝ a³ (período al cuadrado proporcional al semieje mayor al cubo) |
### Energía orbital
E = ½mv² − GMm/r
| mi | Tipo de órbita |
|---|-----------|
| E< 0 | Elliptical (bound) |
| E = 0 | Parabolic (escape trajectory) |
| E >0 | Hiperbólico (sin consolidar) |
### Velocidad de escape
v_escape = √(2GM/R)
Para la Tierra: v_escape ≈ 11,2 km/s
---

## Relevancia para el aprendizaje automático y la ciencia de datos
| Concepto de mecánica | Solicitud |
|------------------|-------------|
| Leyes de Newton | Motores de física en simulaciones, IA de juegos, robótica |
| Métodos energéticos | Modelos basados ​​en energía, redes Hopfield, máquinas Boltzmann |
| Mecánica lagrangiana | Redes neuronales basadas en la física, control óptimo, optimización de trayectorias |
| Mecánica hamiltoniana | Redes neuronales hamiltonianas (HNN), integradores simplécticos para simulación |
| Leyes de conservación | Sesgos inductivos en modelos ML, redes neuronales equivariantes |
| Teorema de Noether | Aprendizaje automático consciente de la simetría, aprendizaje profundo geométrico |
| Dinámica del cuerpo rígido | Simulación robótica, dinámica molecular, animación 3D |
| Mecánica orbital | Posicionamiento por satélite (GPS para ML basado en la ubicación), diseño de misiones espaciales |
| Espacio de fase (hamiltoniano) | Comprensión de los sistemas dinámicos, redes de atractores |
| Cálculo de variaciones | Transporte óptimo, modelado generativo (coincidencia de flujo) |
---

## Resumen
| Marco | Ecuación central | Fuerza |
|-----------|--------------|----------|
| Newtoniano | **F** = m**a** | Análisis de fuerza directo e intuitivo |
| Lagrangiano | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | Sin coordenadas, maneja restricciones |
| hamiltoniano | q̇ = ∂H/∂p, ṗ = −∂H/∂q | Estructura simpléctica, conectada con QM |
| Leyes de conservación | Teorema de Noether | Conexión profunda simetría-conservación |
La mecánica clásica no se trata sólo de bolas que caen y péndulos que se balancean. Sus marcos matemáticos (la mecánica lagrangiana y hamiltoniana) se encuentran entre las ideas más influyentes de toda la ciencia. Se generalizan a la mecánica cuántica, la teoría de campos e incluso el aprendizaje automático moderno, donde los modelos basados ​​en energía y las redes neuronales basadas en la física se basan directamente en estas formulaciones centenarias.